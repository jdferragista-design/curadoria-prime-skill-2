#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corrigir_artigos.py — remediação em lote dos 48 artigos já publicados.

Corrige automaticamente o que é MECÂNICO e seguro:
  1. rel="sponsored" ausente em links de afiliado  → adiciona rel completo
  2. divulgação de afiliado ausente                → insere o bloco padrão no topo

NÃO corrige automaticamente (exige reescrita humana — muda o significado do texto):
  3. alegações falsas de teste físico ("testamos", "testei", "unboxing")
     → apenas lista os trechos para você reescrever.

────────────────────────────────────────────────────────────────────────────
v2 — CORREÇÕES CRÍTICAS (não use a v1 com --aplicar)

  A. LÊ O FONTE, NÃO O RENDERIZADO.
     A v1 lia content.rendered (HTML já processado pelo wpautop, com centenas
     de newlines) e gravava isso de volta em content. O WordPress então rodava
     wpautop DE NOVO sobre um HTML já processado. Medido em posts reais:
        post 2943  <br />  10 → 365
        post 3226  <br />  35 → 526
        post 3183  <br />   2 → 268
     Grids e flex quebram. Como ?context=edit exige auth, o fonte original
     seria perdido para sempre. Agora o GET é autenticado com context=edit e
     usa content.raw.

  B. RECUSA-SE A GRAVAR SE NÃO TIVER O FONTE.
     Sem raw disponível, --aplicar aborta. Nunca mais grava rendered.

  C. BACKUP ANTES DE ESCREVER.
     Cada post tem o raw original salvo em backups/ antes do POST.

  D. VERIFICAÇÃO PÓS-GRAVAÇÃO.
     Depois de gravar, relê o post e compara a contagem de <br>. Se cresceu
     além da tolerância, restaura o backup automaticamente e para o lote.

  E. TLS VOLTA A SER VERIFICADO.
     A v1 fazia check_hostname=False / CERT_NONE — enviava a senha de
     aplicação por Basic Auth sem validar o certificado. Agora verifica.
     Só desativa com --tls-inseguro, e nesse caso recusa --aplicar.

  F. PAGINAÇÃO CORRETA.
     A v1 pedia per_page=50 numa página só. Com 48 artigos isso estava a dois
     posts de truncar silenciosamente. Agora pagina até o fim.
────────────────────────────────────────────────────────────────────────────

Uso:
    export WP_USER="seu_usuario"
    export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"

    python3 corrigir_artigos.py --dry-run              # simula em todos (padrão)
    python3 corrigir_artigos.py --dry-run --id 3153    # simula em um artigo
    python3 corrigir_artigos.py --aplicar --id 3153    # aplica em um artigo
    python3 corrigir_artigos.py --aplicar              # aplica em todos
    python3 corrigir_artigos.py --relatorio-alegacoes  # só lista o que é manual

SEMPRE rode --dry-run primeiro e confira o diff.
As credenciais agora são necessárias TAMBÉM no dry-run (para ler o fonte).
"""

import argparse
import base64
import json
import os
import re
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime
from html import unescape
from pathlib import Path

SITE = "https://curadoriaprime.com"
API = f"{SITE}/wp-json/wp/v2"

DOMINIOS_AFILIADO = [
    "amazon.com.br", "amzn.to", "link.amazon", "mercadolivre.com",
    "meli.la", "mercadolivre.com.br",
]

REL_CORRETO = "sponsored noopener noreferrer nofollow"

# §2.6 — assinatura humana única. O schema trazia 5 variantes (Cristiano,
# Cristian, Cristiano Martins, Curadoria Prime, Equipe Curadoria Prime).
AUTOR_CANONICO = "Cristiano Martins"

# Tolerância de crescimento de <br> após gravar. Um bloco de divulgação novo
# não introduz <br> nenhum; qualquer crescimento real é sintoma de wpautop.
TOLERANCIA_BR = 2

DIR_BACKUP = Path(os.environ.get("WP_BACKUP_DIR", "backups"))

BLOCO_DIVULGACAO = (
    '<div style="background:#f8f8ff;border:1px solid #e2e2f0;border-radius:12px;'
    'padding:16px 20px;margin:24px 0;font-size:.92em;color:#7c7c9a;line-height:1.6">'
    '🔍 <strong>Transparência:</strong> este artigo contém links de afiliado. '
    'Se você comprar por eles, podemos receber uma comissão <strong>sem custo adicional '
    'para você</strong>. Isso não influencia nossa análise — nossa nota é baseada em '
    'pesquisa técnica e dados de compradores verificados. '
    '<a href="' + SITE + '/transparencia-curadoria-prime/">Entenda nossa metodologia</a>.'
    '</div>'
)

PADROES_TESTE = [
    r"\btestamos\b", r"\btestei\b", r"\bem nossos testes\b", r"\bnos nossos testes\b",
    r"\busei (?:o|a|por)\b", r"\busamos (?:o|a|por) \w+ (?:durante|por)\b",
    r"\bdepois de (?:usar|testar)\b", r"\bnossa unidade\b", r"\bunboxing\b",
    r"\bsentimos na m[ãa]o\b", r"\bna nossa bancada\b", r"\bmedimos\b",
]

PADROES_TESTE_SCHEMA = PADROES_TESTE + [
    r"\bteste de \w+", r"\btestado(?:s|a|as)? (?:por n[óo]s|em)\b",
    r"\bcolocamos [àa] prova\b", r"\bap[óo]s \d+ dias de uso\b",
]

NEGACOES = re.compile(r"\b(n[ãa]o|sem|nunca|jamais)\b[\s\w,]{0,25}$", re.I)
INDICE = re.compile(r"(índice|sumário|neste (?:review|guia|artigo))", re.I)

_TLS_INSEGURO = False


# ─────────────────────────── utilidades ───────────────────────────

def _ctx():
    """Contexto TLS. Verificação LIGADA por padrão (v1 mandava a senha às cegas)."""
    c = ssl.create_default_context()
    if _TLS_INSEGURO:
        c.check_hostname = False
        c.verify_mode = ssl.CERT_NONE
    return c


def _auth():
    u, p = os.environ.get("WP_USER"), os.environ.get("WP_APP_PASSWORD")
    if not u or not p:
        sys.exit(
            "❌ Defina WP_USER e WP_APP_PASSWORD no ambiente.\n"
            "   A v2 precisa de credencial MESMO no --dry-run: sem autenticação a API\n"
            "   devolve apenas content.rendered, e trabalhar em cima do rendered é\n"
            "   exatamente o bug que esta versão corrige."
        )
    return base64.b64encode(f"{u}:{p}".encode()).decode()


def _abrir(req, tentativas=3):
    """GET/POST com retry. Falha de rede não vira 'o site caiu'."""
    ultimo = None
    for i in range(tentativas):
        try:
            return urllib.request.urlopen(req, timeout=90, context=_ctx())
        except urllib.error.HTTPError:
            raise                      # erro da aplicação: sobe na hora
        except (urllib.error.URLError, ssl.SSLError, TimeoutError, OSError) as e:
            ultimo = e
            if i < tentativas - 1:
                espera = 2 ** i
                print(f"   ⚠️  falha de rede ({e}); nova tentativa em {espera}s…")
                time.sleep(espera)
    raise SystemExit(
        f"❌ Falha de rede após {tentativas} tentativas: {ultimo}\n"
        f"   Confirme antes de culpar o site:\n"
        f"     curl -sS -o /dev/null -w '%{{http_code}}\\n' {API}/posts/2943\n"
        f"   Se o curl responde 200, o problema é a rede/proxy DESTE ambiente,\n"
        f"   não a API. Não altere o script por causa disso."
    )


def texto_visivel(html):
    h = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<!--.*?-->", " ", h, flags=re.S)          # comentários de bloco Gutenberg
    h = re.sub(r"<[^>]+>", " ", h)
    h = unescape(h).replace("\xa0", " ")
    return re.sub(r"\s+", " ", h).strip()


def e_afiliado(tag):
    m = re.search(r'href="([^"]*)"', tag, re.I)
    if not m:
        return False
    return any(d in m.group(1) for d in DOMINIOS_AFILIADO)


def conta_br(html):
    return len(re.findall(r"<br\s*/?>", html, re.I))


# ─────────────────────────── leitura ───────────────────────────

def buscar_posts(post_id=None, auth=None):
    """
    Lê os posts com context=edit → content.raw (o FONTE, não o renderizado).

    Retorna (posts, origem) onde origem ∈ {"raw", "rendered"}.
    origem == "rendered" significa que a autenticação não funcionou; nesse caso
    o chamador DEVE recusar --aplicar.
    """
    headers = {"User-Agent": "curadoriaprime-remediacao/2.0"}
    if auth:
        headers["Authorization"] = f"Basic {auth}"

    campos = "id,slug,link,title,content,date,status"
    origem = "raw" if auth else "rendered"

    def _get(url):
        try:
            return _abrir(urllib.request.Request(url, headers=headers))
        except urllib.error.HTTPError as e:
            if e.code in (401, 403):
                sys.exit(
                    f"❌ HTTP {e.code} ao ler o post com context=edit.\n"
                    "   A credencial foi rejeitada ou o usuário não tem permissão de edição.\n"
                    "   • WP_APP_PASSWORD é a SENHA DE APLICAÇÃO (Usuários → Perfil →\n"
                    "     Senhas de aplicativo), não a senha de login. Os espaços fazem parte dela.\n"
                    "   • WP_USER é o login (user_login), não o e-mail nem o apelido.\n"
                    "   Sem context=edit não há content.raw, e sem raw este script não grava."
                )
            raise

    out = []
    if post_id:
        ctx = "&context=edit" if auth else ""
        r = _get(f"{API}/posts/{post_id}?_fields={campos}{ctx}")
        out = [json.loads(r.read())]
    else:
        pagina = 1
        while True:
            ctx = "&context=edit" if auth else ""
            url = f"{API}/posts?per_page=25&page={pagina}&_fields={campos}{ctx}"
            try:
                r = _get(url)
            except urllib.error.HTTPError as e:
                if e.code == 400 and pagina > 1:
                    break                      # passou da última página
                raise
            lote = json.loads(r.read())
            if not lote:
                break
            out += lote
            total_pag = int(r.headers.get("X-WP-TotalPages") or 0)
            if total_pag and pagina >= total_pag:
                break
            if len(lote) < 25:
                break
            pagina += 1

    # o context=edit realmente entregou raw?
    if auth:
        sem_raw = [p["id"] for p in out if "raw" not in (p.get("content") or {})]
        if sem_raw:
            origem = "rendered"
    return out, origem


def conteudo(p, origem):
    c = p.get("content") or {}
    return c["raw"] if origem == "raw" and "raw" in c else c.get("rendered", "")


# ─────────────────────────── correções ───────────────────────────

def corrigir_sponsored(html):
    """Adiciona rel completo em links de afiliado que não têm rel=sponsored."""
    n = [0]

    def repl(m):
        tag = m.group(0)
        if not e_afiliado(tag):
            return tag
        if "sponsored" in tag.lower():
            return tag
        n[0] += 1
        if re.search(r'\brel\s*=\s*"[^"]*"', tag, re.I):
            return re.sub(r'\brel\s*=\s*"[^"]*"', f'rel="{REL_CORRETO}"', tag, flags=re.I)
        return tag[:-1].rstrip() + f' rel="{REL_CORRETO}">'

    novo = re.sub(r"<a\b[^>]*>", repl, html, flags=re.I)
    return novo, n[0]


def _e_gutenberg(html):
    return bool(re.search(r"<!--\s*/?wp:", html))


def corrigir_divulgacao(html):
    """
    Insere o bloco de divulgação se ausente, antes do primeiro link de afiliado.

    v2: se o conteúdo é Gutenberg, o bloco vai embrulhado em <!-- wp:html -->
    e o ponto de inserção respeita a fronteira de bloco — inserir HTML solto no
    meio de um bloco corrompe o parser e o editor marca o post como "inválido".
    """
    txt = texto_visivel(html).lower()
    if any(k in txt for k in ["link de afiliado", "links de afiliado", "comissão"]):
        return html, 0

    bloco = BLOCO_DIVULGACAO
    guten = _e_gutenberg(html)
    if guten:
        bloco = f"<!-- wp:html -->\n{BLOCO_DIVULGACAO}\n<!-- /wp:html -->\n\n"

    for m in re.finditer(r"<a\b[^>]*>", html, re.I):
        if not e_afiliado(m.group(0)):
            continue
        if guten:
            # sobe até o início do bloco Gutenberg que contém o link
            ini = html.rfind("<!-- wp:", 0, m.start())
            corte = ini if ini != -1 else 0
        else:
            corte = html.rfind("<", 0, m.start())
            corte = html.rfind(">", 0, corte) + 1 if corte > 0 else m.start()
        return html[:corte] + bloco + html[corte:], 1

    return bloco + html, 1


def _blocos_jsonld(html):
    """Devolve [(match, texto_json)] dos <script type=application/ld+json> do conteúdo."""
    return [(m, m.group(1)) for m in
            re.finditer(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', html, re.S | re.I)]


def _limpar_rating(obj, contador):
    """
    Remove aggregateRating/reviewCount recursivamente e padroniza author.name.

    §2.4: publicar a nota agregada da Amazon/ML dentro do Product do nosso site,
    sem atribuição, afirma ao Google que a coleta é nossa. O bloco 'review' com a
    NOSSA nota /10 é legítimo e é preservado.
    """
    if isinstance(obj, list):
        for i in obj:
            _limpar_rating(i, contador)
        return obj
    if not isinstance(obj, dict):
        return obj

    for chave in ("aggregateRating", "reviewCount", "ratingCount"):
        if chave in obj:
            del obj[chave]
            contador["agg"] += 1

    # author.name inconsistente (Cristiano / Cristian / Equipe…) fragmenta o E-E-A-T
    if obj.get("@type") == "Person" and "name" in obj:
        if obj["name"] != AUTOR_CANONICO:
            obj["name"] = AUTOR_CANONICO
            contador["autor"] += 1

    for v in obj.values():
        _limpar_rating(v, contador)
    return obj


def corrigir_schema(html):
    """
    Remove aggregateRating do JSON-LD embutido no conteúdo e padroniza o autor.

    Só mexe em bloco que faz parse como JSON. Bloco malformado é deixado intacto
    e reportado — reescrever JSON quebrado por regex é como o wpautop entrou aqui.
    Retorna (novo_html, n_agg, n_autor, n_falhas).
    """
    n_agg = n_autor = n_falhas = 0
    for m, bruto in reversed(_blocos_jsonld(html)):
        if "aggregateRating" not in bruto and '"Person"' not in bruto:
            continue
        try:
            dados = json.loads(bruto.strip())
        except json.JSONDecodeError:
            if "aggregateRating" in bruto:
                n_falhas += 1
            continue
        c = {"agg": 0, "autor": 0}
        _limpar_rating(dados, c)
        if not (c["agg"] or c["autor"]):
            continue
        novo_json = json.dumps(dados, ensure_ascii=False, indent=1)
        html = html[:m.start(1)] + "\n" + novo_json + "\n" + html[m.end(1):]
        n_agg += c["agg"]
        n_autor += c["autor"]
    return html, n_agg, n_autor, n_falhas


def alegacoes_schema(html):
    """
    Alegações de teste dentro do JSON-LD (description/headline).

    O listar_alegacoes lê só o texto visível — e texto_visivel() apaga <script>.
    Alegação no schema é pior que no corpo: é o que vai para o snippet do Google.
    """
    achados = []
    for _, bruto in _blocos_jsonld(html):
        for campo in re.finditer(r'"(description|headline|name)"\s*:\s*"([^"]{0,500})"', bruto):
            valor = campo.group(2)
            for pad in PADROES_TESTE_SCHEMA:
                m = re.search(pad, valor, re.I)
                if not m:
                    continue
                antes = valor[max(0, m.start() - 45):m.start()]
                if NEGACOES.search(antes):
                    continue
                if re.search(r"(independente|de terceiros|especializad|do fabricante)",
                             valor[max(0, m.start() - 60):m.end() + 60], re.I):
                    continue
                achados.append((campo.group(1), m.group(0), valor[:160]))
                break
    return achados


def listar_alegacoes(html):
    """Lista alegações de teste físico que precisam de reescrita humana."""
    txt = texto_visivel(html)
    achados = []
    for pad in PADROES_TESTE:
        for m in re.finditer(pad, txt, re.I):
            antes = txt[max(0, m.start() - 40):m.start()]
            if NEGACOES.search(antes):
                continue
            jan = txt[max(0, m.start() - 120):m.start()]
            if jan.count("“") > jan.count("”"):
                continue
            if "unboxing" in m.group(0).lower() and INDICE.search(txt[max(0, m.start() - 160):m.start()]):
                continue
            achados.append((m.group(0), txt[max(0, m.start() - 80):m.end() + 80].strip()))
    return achados


SUGESTOES = {
    "testamos": "analisamos as especificações e cruzamos com relatos de compradores verificados",
    "testei": "analisei os dados técnicos e as avaliações de compradores",
    "em nossos testes": "segundo os dados técnicos do fabricante e relatos de compradores",
    "nos nossos testes": "segundo os dados técnicos e relatos de compradores",
    "depois de usar": "segundo relatos de quem usa",
    "nossa unidade": "as unidades relatadas por compradores",
    "unboxing": "o que vem na caixa",
    "medimos": "os dados oficiais indicam",
    "sentimos na mão": "compradores relatam",
}


# ─────────────────────────── escrita ───────────────────────────

def salvar_backup(post_id, slug, html):
    DIR_BACKUP.mkdir(parents=True, exist_ok=True)
    carimbo = datetime.now().strftime("%Y%m%d-%H%M%S")
    caminho = DIR_BACKUP / f"{post_id}-{slug}-{carimbo}.raw.html"
    caminho.write_text(html, encoding="utf-8")
    return caminho


def atualizar_post(post_id, html, auth):
    req = urllib.request.Request(
        f"{API}/posts/{post_id}",
        data=json.dumps({"content": html}).encode(),
        headers={"Authorization": f"Basic {auth}", "Content-Type": "application/json",
                 "User-Agent": "curadoriaprime-remediacao/2.0"},
        method="POST",
    )
    try:
        r = _abrir(req)
        return r.status in (200, 201)
    except urllib.error.HTTPError as e:
        print(f"   ❌ HTTP {e.code}: {e.read()[:200].decode(errors='replace')}")
        return False


def verificar_gravacao(post_id, br_esperado, auth):
    """
    Relê o post e confere se o WordPress não reprocessou o HTML.
    Retorna (ok, br_lido).
    """
    posts, origem = buscar_posts(post_id, auth)
    lido = conteudo(posts[0], origem)
    br = conta_br(lido)
    return (br <= br_esperado + TOLERANCIA_BR), br


# ─────────────────────────── main ───────────────────────────

def main():
    global _TLS_INSEGURO

    ap = argparse.ArgumentParser(description="Remediação em lote dos artigos publicados.")
    g = ap.add_mutually_exclusive_group()
    g.add_argument("--dry-run", action="store_true", help="simula (padrão)")
    g.add_argument("--aplicar", action="store_true", help="grava as alterações no WordPress")
    ap.add_argument("--id", type=int, help="corrigir apenas um post")
    ap.add_argument("--relatorio-alegacoes", action="store_true",
                    help="só lista alegações de teste físico para reescrita manual")
    ap.add_argument("--tls-inseguro", action="store_true",
                    help="desativa a verificação de certificado (DEBUG; incompatível com --aplicar)")
    ap.add_argument("--pular-schema", action="store_true",
                    help="não mexe no JSON-LD (só rel=sponsored e divulgação)")
    ap.add_argument("--sem-verificacao", action="store_true",
                    help="não relê o post após gravar (NÃO recomendado)")
    a = ap.parse_args()

    _TLS_INSEGURO = a.tls_inseguro
    aplicar = a.aplicar

    if a.tls_inseguro and aplicar:
        sys.exit("❌ --tls-inseguro não pode ser combinado com --aplicar: seria enviar a "
                 "senha de aplicação por um canal não verificado.")
    if a.tls_inseguro:
        print("⚠️  Verificação de certificado DESATIVADA (modo debug).\n")

    auth = _auth()                     # agora obrigatório também no dry-run

    posts, origem = buscar_posts(a.id, auth)
    print(f"📥 {len(posts)} artigo(s) carregado(s) — fonte: content.{origem}\n")

    if origem != "raw":
        print("🔴 A API não devolveu content.raw (context=edit falhou — credencial "
              "inválida ou usuário sem permissão de edição).")
        if aplicar:
            sys.exit("   Abortado. Gravar o content.rendered de volta faz o WordPress "
                     "reprocessar o HTML com wpautop e destrói grids e flex.\n"
                     "   Verifique WP_USER / WP_APP_PASSWORD e tente de novo.")
        print("   Seguindo em modo leitura sobre o rendered — as contagens abaixo "
              "servem de estimativa, mas NÃO grave nada assim.\n")

    if a.relatorio_alegacoes:
        total = 0
        for p in posts:
            ach = listar_alegacoes(conteudo(p, origem))
            if not ach:
                continue
            total += len(ach)
            print(f"\n{'='*72}\nID {p['id']} · /{p['slug']}\n{p['link']}")
            for termo, trecho in ach:
                sug = SUGESTOES.get(termo.lower(), "reescreva sem alegar experiência física")
                print(f"\n  ❌ \"{termo}\"\n     …{trecho}…\n     ✏️  trocar por: {sug}")
        print(f"\n{'='*72}\nTotal: {total} trecho(s) para reescrita manual.")
        return

    tot_sp = tot_div = tot_posts = tot_agg = tot_aut = 0
    pendentes = []
    pendentes_schema = []
    pendentes_bad = []
    falhas = []

    for p in posts:
        html = conteudo(p, origem)
        novo, n_sp = corrigir_sponsored(html)
        novo, n_div = corrigir_divulgacao(novo)
        n_agg = n_aut = n_bad = 0
        if not a.pular_schema:
            novo, n_agg, n_aut, n_bad = corrigir_schema(novo)
        ach = listar_alegacoes(novo)
        ach_schema = alegacoes_schema(novo)
        if ach_schema:
            pendentes_schema.append((p["id"], p["slug"], ach_schema))
        if ach:
            pendentes.append((p["id"], p["slug"], len(ach)))
        if n_bad:
            pendentes_bad.append((p["id"], p["slug"], n_bad))
        if not (n_sp or n_div or n_agg or n_aut):
            continue
        tot_posts += 1
        tot_sp += n_sp
        tot_div += n_div
        tot_agg += n_agg
        tot_aut += n_aut

        br_antes, br_depois = conta_br(html), conta_br(novo)
        print(f"ID {p['id']} · /{p['slug']}")
        if n_sp:
            print(f"   🔧 {n_sp} link(s) ganharam rel=\"sponsored\"")
        if n_div:
            print(f"   🔧 bloco de divulgação inserido"
                  f"{' (embrulhado em wp:html)' if _e_gutenberg(html) else ''}")
        if n_agg:
            print(f"   🔴 {n_agg} aggregateRating/reviewCount REMOVIDO do JSON-LD (§2.4)")
        if n_aut:
            print(f"   🔧 {n_aut} author.name → \"{AUTOR_CANONICO}\"")
        if n_bad:
            print(f"   ⚠️  {n_bad} bloco(s) JSON-LD com aggregateRating não fizeram parse — corrija à mão")
        print(f"   📏 {len(html)} → {len(novo)} chars · <br> {br_antes} → {br_depois}")

        if br_depois > br_antes + TOLERANCIA_BR:
            print(f"   🛑 crescimento anômalo de <br> ANTES de gravar — post pulado.")
            falhas.append((p["id"], "crescimento de <br> na transformação local"))
            continue

        if not aplicar:
            print("   (dry-run — nada gravado)")
            continue

        bkp = salvar_backup(p["id"], p["slug"], html)
        print(f"   💾 backup: {bkp}")

        if not atualizar_post(p["id"], novo, auth):
            falhas.append((p["id"], "POST falhou"))
            print("   ❌ falhou")
            continue
        print("   ✅ gravado")

        if a.sem_verificacao:
            continue
        ok, br_lido = verificar_gravacao(p["id"], br_depois, auth)
        if ok:
            print(f"   🔎 verificado: <br> = {br_lido}")
            continue

        print(f"   🛑 REPROCESSAMENTO DETECTADO: <br> esperado ≤{br_depois + TOLERANCIA_BR}, "
              f"lido {br_lido}. Restaurando o backup…")
        restaurado = atualizar_post(p["id"], html, auth)
        print(f"   {'↩️  restaurado' if restaurado else '❌ FALHA AO RESTAURAR — use ' + str(bkp)}")
        falhas.append((p["id"], f"wpautop reprocessou (<br> {br_lido})"))
        sys.exit("\n🛑 Lote interrompido para não propagar o dano. "
                 "Investigue antes de continuar.")

    print(f"\n{'='*72}")
    modo = "APLICADO" if aplicar else "SIMULAÇÃO (use --aplicar para gravar)"
    print(f"{modo}: {tot_posts} artigo(s) · {tot_sp} links · {tot_div} divulgações · "
          f"{tot_agg} aggregateRating · {tot_aut} autores")
    if falhas:
        print(f"\n❌ {len(falhas)} problema(s):")
        for i, m in falhas:
            print(f"     ID {i:>5} · {m}")
    if pendentes:
        print(f"\n⚠️  {len(pendentes)} artigo(s) ainda com alegação de teste físico (reescrita MANUAL):")
        for i, s, n in sorted(pendentes, key=lambda x: -x[2]):
            print(f"     ID {i:>5} · {n} trecho(s) · /{s}")
        print("\n   Rode: python3 corrigir_artigos.py --relatorio-alegacoes")

    if pendentes_schema:
        print(f"\n🔴 {len(pendentes_schema)} artigo(s) com ALEGAÇÃO DE TESTE no JSON-LD "
              "(vai para o snippet do Google — reescreva à mão):")
        for i, s_, ach in pendentes_schema:
            for campo, termo, val in ach:
                print(f"     ID {i:>5} · {campo}: \"{termo}\" → …{val[:90]}…")

    if pendentes_bad:
        print(f"\n🔴 {len(pendentes_bad)} artigo(s) com JSON-LD MALFORMADO contendo "
              "aggregateRating — NÃO tocados pelo script (corrija à mão):")
        for i, s_, n in pendentes_bad:
            print(f"     ID {i:>5} · {n} bloco(s) · /{s_}")
        print("   Schema quebrado não é lido pelo Google: o rating não aparece,\n"
              "   mas o texto continua no HTML. Reconstrua o bloco inteiro.")


if __name__ == "__main__":
    main()
