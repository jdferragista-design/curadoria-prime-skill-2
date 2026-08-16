#!/usr/bin/env python3
"""
checar_conformidade.py — trava de conformidade com as políticas do Google.

Roda ANTES de publicar. Verifica um artigo HTML (ou um JSON de produto) contra
as regras que realmente derrubam sites de afiliado:

  - Afiliação sem valor agregado (thin affiliation)
  - Abuso de conteúdo em escala (scaled content abuse)
  - Links de afiliado sem rel="sponsored"
  - Ausência de divulgação de afiliado (também exigido pelo CDC/CONAR no Brasil)
  - E-E-A-T: autoria, metodologia, data, fontes
  - Alegações de teste físico que não fazemos (risco de engano ao consumidor)
  - Marcação Review sem base declarada

Uso:
    python3 checar_conformidade.py artigo.html
    python3 checar_conformidade.py artigo.html --json exemplo-produto.json
    python3 checar_conformidade.py *.html --resumo

Saída: relatório + exit code 1 se houver ERRO (bloqueia publicação automatizada).
"""

import argparse
import glob
import json
import os
import re
from html import unescape
import sys
from collections import Counter

# Fonte única dos padrões de teste físico e vocabulário genérico.
# Ver tools/padroes_editoriais.py — importado também por corrigir_artigos.py.
from padroes_editoriais import (
    PADROES_TESTE_FISICO,
    PADROES_ENCHIMENTO,
    PADROES_PROVA_SOCIAL_INDEVIDA,
)

# ---------------------------------------------------------------- utilidades

ERRO, ALERTA, OK = "ERRO", "ALERTA", "OK"

DOMINIOS_AFILIADO = ["link.amazon", "meli.la", "amzn.to", "mercadolivre.com", "amazon.com.br"]


def texto_visivel(html):
    """Remove script/style/tags e devolve só o texto que o leitor vê."""
    h = re.sub(r"<script.*?</script>", " ", html, flags=re.S | re.I)
    h = re.sub(r"<style.*?</style>", " ", h, flags=re.S | re.I)
    h = re.sub(r"<[^>]+>", " ", h)
    # Decodifica entidades (&#8220; etc.) — sem isso as aspas tipográficas de
    # depoimentos de compradores não são reconhecidas como citação.
    h = unescape(h)
    h = h.replace("\xa0", " ")
    return re.sub(r"\s+", " ", h).strip()


def achados(nivel, regra, msg, detalhe=""):
    return {"nivel": nivel, "regra": regra, "msg": msg, "detalhe": detalhe}


# ---------------------------------------------------------------- checagens

def checar_links_afiliado(html):
    out = []
    tags = re.findall(r"<a\b[^>]*>", html, flags=re.I)
    afil = []
    for t in tags:
        href = re.search(r'href="([^"]*)"', t, flags=re.I)
        if href and any(d in href.group(1) for d in DOMINIOS_AFILIADO):
            afil.append(t)

    if not afil:
        out.append(achados(ALERTA, "afiliado", "Nenhum link de afiliado encontrado."))
        return out, 0

    sem_sponsored = [t for t in afil if "sponsored" not in t.lower()]
    if sem_sponsored:
        out.append(achados(
            ERRO, "rel-sponsored",
            f"{len(sem_sponsored)} de {len(afil)} links de afiliado sem rel=\"sponsored\".",
            "O Google pode aplicar ação manual quando links de afiliado não são qualificados.",
        ))
    else:
        out.append(achados(OK, "rel-sponsored",
                           f"Todos os {len(afil)} links de afiliado têm rel=\"sponsored\"."))

    placeholders = [t for t in afil if "SEU-CODIGO-AQUI" in t]
    if placeholders:
        out.append(achados(
            ERRO, "placeholder",
            f"{len(placeholders)} link(s) ainda com 'SEU-CODIGO-AQUI'.",
            "Publicar assim gera link quebrado e zero comissão.",
        ))
    return out, len(afil)


def checar_divulgacao(html):
    txt = texto_visivel(html).lower()
    tem = any(k in txt for k in ["link de afiliado", "links de afiliado", "comissão", "comissao"])
    if not tem:
        return [achados(
            ERRO, "divulgacao",
            "Sem divulgação visível de afiliado.",
            "Exigido pelo Google e pelo CDC/CONAR. Deve ser legível e antes dos links.",
        )]
    # A divulgação precisa vir ANTES do primeiro link de afiliado.
    pos_div = min([txt.find(k) for k in ["link de afiliado", "links de afiliado", "comissão", "comissao"]
                   if txt.find(k) != -1] or [10 ** 9])
    corpo = texto_visivel(html)
    m = re.search(r"(link\.amazon|meli\.la|amzn\.to)", html, flags=re.I)
    if m:
        # posição aproximada do 1º link no texto visível
        frac_link = m.start() / max(len(html), 1)
        frac_div = pos_div / max(len(corpo), 1)
        if frac_div > frac_link + 0.05:
            return [achados(ALERTA, "divulgacao",
                            "A divulgação de afiliado parece vir depois do primeiro link.",
                            "Coloque o aviso acima do primeiro CTA.")]
    return [achados(OK, "divulgacao", "Divulgação de afiliado presente e antes dos links.")]


def checar_eeat(html):
    out = []
    txt = texto_visivel(html)
    low = txt.lower()

    if re.search(r"\bpor\s+equipe\b|\bpor\s+curadoria prime\b|\bpor\s+[A-ZÀ-Ú][a-zà-ú]+\s+[A-ZÀ-Ú]", txt, re.I):
        out.append(achados(OK, "autoria", "Assinatura de autoria presente."))
    else:
        out.append(achados(ERRO, "autoria", "Sem assinatura de autor visível.",
                           "O Google avalia 'Quem criou o conteúdo'."))

    if "metodologia" in low or "como avaliamos" in low or "baseada em especificações" in low:
        out.append(achados(OK, "metodologia", "Metodologia declarada."))
    else:
        out.append(achados(ERRO, "metodologia", "Metodologia não declarada.",
                           "O Google avalia 'Como o conteúdo foi criado'."))

    if re.search(
        r"n[ãa]o (?:realizamos|realizou|fizemos|fez|conduzimos|conduziu) (?:testes?|ensaios?)"
        r"|n[ãa]o (?:testamos|testei|testou|avaliamos|avaliou)\b[^.]{0,60}\bfisicamente"
        r"|n[ãa]o (?:testamos|testei|testou|avaliamos|avaliou) (?:esta|este|essa|esse|as|os|a|o) \w+"
        r"|n[ãa]o (?:recebemos|tivemos acesso a|tivemos em m[ãa]os)"
        r"|sem (?:teste|ensaio) (?:f[íi]sico|em bancada|hands-?on)"
        r"|an[áa]lise (?:baseada|feita) em (?:especifica[çc][õo]es|dados)",
        low):
        out.append(achados(OK, "honestidade", "Declara que não faz teste físico."))
    else:
        out.append(achados(ALERTA, "honestidade",
                           "Não declara ausência de teste físico.",
                           "Sem essa ressalva, o leitor pode presumir teste hands-on."))

    if re.search(r"fontes consultadas", low):
        n = len(re.findall(r"<li><a\b", html, flags=re.I))
        out.append(achados(OK, "fontes", f"Seção de fontes presente (~{n} itens)."))
    else:
        out.append(achados(ALERTA, "fontes",
                           "Sem seção 'Fontes consultadas'.",
                           "§3.4 exige fonte com link para dado de terceiro. "
                           "Se o artigo não usa dado externo, isto é esperado."))

    if re.search(r"\d{2}/\d{2}/\d{4}", txt):
        out.append(achados(OK, "data", "Data de verificação visível."))
    else:
        out.append(achados(ALERTA, "data", "Sem data de verificação visível."))
    return out


# Negações: "não testamos", "sem testar" etc. NÃO são alegações — são a ressalva correta.
NEGACOES = re.compile(r"\b(n[ãa]o|sem|nunca|jamais)\b[\s\w,]{0,25}$", re.I)


def _e_negado(txt, ini):
    """Verifica se o trecho imediatamente antes do match é uma negação."""
    return bool(NEGACOES.search(txt[max(0, ini - 40):ini]))


def _em_citacao(txt, ini):
    """Depoimento de comprador entre aspas não é alegação nossa."""
    janela = txt[max(0, ini - 120):ini]
    return janela.count("“") > janela.count("”") or janela.count('"') % 2 == 1


def checar_teste_fisico(html):
    txt = texto_visivel(html)
    hits = []
    for pad in PADROES_TESTE_FISICO:
        for m in re.finditer(pad, txt, flags=re.I):
            if _e_negado(txt, m.start()) or _em_citacao(txt, m.start()):
                continue
            ini, fim = max(0, m.start() - 60), min(len(txt), m.end() + 60)
            hits.append(f"…{txt[ini:fim]}…")
    if hits:
        return [achados(
            ERRO, "teste-fisico",
            f"{len(hits)} alegação(ões) de experiência física direta.",
            " | ".join(hits[:4]),
        )]
    return [achados(OK, "teste-fisico", "Nenhuma alegação falsa de teste físico.")]


def checar_valor_agregado(html):
    """Thin affiliation: o artigo precisa ter mais que ficha técnica + botão."""
    out = []
    txt = texto_visivel(html)
    palavras = len(txt.split())

    if palavras < 1200:
        out.append(achados(ERRO, "profundidade",
                           f"Apenas {palavras} palavras.",
                           "Risco de afiliação sem valor agregado."))
    elif palavras < 1800:
        out.append(achados(ALERTA, "profundidade",
                           f"{palavras} palavras — abaixo do padrão do site (~3.000)."))
    else:
        out.append(achados(OK, "profundidade", f"{palavras} palavras."))

    # Sinais de valor agregado que o Google cita nominalmente.
    sinais = {
        "comparativo com concorrentes": bool(re.search(r"comparativo|vs\.?\s", txt, re.I)),
        "prós e contras": bool(re.search(r"contras|pontos negativos", txt, re.I)),
        "para quem NÃO é": bool(re.search(r"não é para|não vale a pena para|evite se|quem n[ãa]o é|pense duas vezes", txt, re.I)),
        "FAQ": bool(re.search(r"perguntas frequentes|faq", txt, re.I)),
        "veredito/nota": bool(re.search(r"veredito|nota final|\d[,.]\d\s*/\s*10", txt, re.I)),
    }
    faltando = [k for k, v in sinais.items() if not v]
    if faltando:
        out.append(achados(ALERTA, "valor-agregado",
                           f"Faltam sinais de valor: {', '.join(faltando)}."))
    else:
        out.append(achados(OK, "valor-agregado", "Todos os sinais de valor agregado presentes."))

    # Um review 100% positivo não é review — é anúncio.
    # Conta os <li> do bloco de contras no HTML (o texto visível perde as tags).
    m = re.search(
        r"(?:Pontos de Atenção|Contras|Pontos Negativos)\s*</h[1-6]>(.*?)</ul>",
        html, re.I | re.S,
    )
    if m:
        itens = len(re.findall(r"<li\b", m.group(1), re.I))
        if itens < 3:
            out.append(achados(ALERTA, "imparcialidade",
                               f"Apenas {itens} contra(s) — reviews sem contras reais parecem promocionais."))
        else:
            out.append(achados(OK, "imparcialidade", f"{itens} contras listados."))
    else:
        out.append(achados(ALERTA, "imparcialidade", "Bloco de contras não localizado."))
    return out


def checar_enchimento(html):
    txt = texto_visivel(html)
    hits = []
    for pad in PADROES_ENCHIMENTO:
        for m in re.finditer(pad, txt, flags=re.I):
            hits.append(m.group(0))
    if len(hits) >= 4:
        c = Counter(h.lower() for h in hits)
        return [achados(ALERTA, "enchimento",
                        f"{len(hits)} expressões genéricas de IA.",
                        ", ".join(f"'{k}' ({v}×)" for k, v in c.most_common(5)))]
    return [achados(OK, "enchimento", "Pouco texto de enchimento.")]


def checar_keyword_stuffing(html):
    txt = texto_visivel(html).lower()
    palavras = re.findall(r"[a-zà-ú]{4,}", txt)
    if not palavras:
        return []
    total = len(palavras)
    stop = {"para", "como", "mais", "isso", "esse", "essa", "pode", "quando", "você", "seus",
            "sua", "com", "que", "uma", "não", "por", "dos", "das", "mas", "muito", "bem",
            "sobre", "entre", "onde", "toda", "todo", "está", "ser", "tem", "faz", "sem"}
    c = Counter(w for w in palavras if w not in stop)
    for termo, n in c.most_common(6):
        dens = n / total
        if dens > 0.035 and n > 18:
            return [achados(ALERTA, "keyword-stuffing",
                            f"'{termo}' aparece {n}× ({dens:.1%} do texto).")]
    return [achados(OK, "keyword-stuffing", "Densidade de palavras-chave normal.")]


def checar_schema(html):
    out = []
    blocos = re.findall(r'<script type="application/ld\+json">(.*?)</script>', html, re.S)
    if not blocos:
        # §7.3: schema é opt-in. Ausência é o padrão, não um defeito.
        return [achados(OK, "schema", "Sem JSON-LD (opt-in, §7.3).")]
    for b in blocos:
        try:
            data = json.loads(b)
        except json.JSONDecodeError as e:
            out.append(achados(ERRO, "schema", f"JSON-LD inválido: {e}"))
            continue
        nodes = data.get("@graph", [data])
        # §2.4: nota agregada de terceiros nunca pode ir para o schema.
        bruto = json.dumps(data, ensure_ascii=False)
        for proibido in ("aggregateRating", "ratingCount", "reviewCount"):
            if proibido in bruto:
                out.append(achados(
                    ERRO, "schema",
                    f"'{proibido}' no JSON-LD — §2.4 proíbe publicar nota "
                    "agregada de terceiros como se fosse nossa."))
        for n in nodes:
            if n.get("@type") == "Review":
                a = n.get("author")
                if not a:
                    out.append(achados(ERRO, "schema", "Review sem 'author'."))
                elif isinstance(a, dict) and a.get("@type") != "Person":
                    out.append(achados(
                        ERRO, "schema",
                        f"author é '{a.get('@type')}' — §2.6 exige Person, "
                        "o humano que revisou e aprovou."))
                if not n.get("datePublished"):
                    out.append(achados(ALERTA, "schema", "Review sem 'datePublished'."))
                # §7.1: nota é opcional. Só validamos a escala se ela existir.
                r = n.get("reviewRating")
                if r:
                    v = r.get("ratingValue")
                    if v is None:
                        out.append(achados(ERRO, "schema", "reviewRating sem 'ratingValue'."))
                    elif not (float(r.get("worstRating", 0)) <= float(v) <= float(r.get("bestRating", 10))):
                        out.append(achados(ERRO, "schema", f"ratingValue fora da escala: {v}."))
    if not any(a["nivel"] == ERRO for a in out):
        out.append(achados(OK, "schema", "JSON-LD válido e completo."))
    return out


def checar_json_produto(caminho):
    """Checagens que só o JSON de entrada permite (preço/specs inventados)."""
    out = []
    with open(caminho, encoding="utf-8") as f:
        p = json.load(f)
    if not p.get("fontes"):
        out.append(achados(ERRO, "fontes-json", "JSON sem fontes."))
    elif len(p["fontes"]) < 2:
        out.append(achados(ALERTA, "fontes-json", "Menos de 2 fontes."))
    if not p.get("data_verificacao"):
        out.append(achados(ERRO, "data-json", "Sem 'data_verificacao'."))
    if p.get("preco") and not p.get("data_verificacao"):
        out.append(achados(ERRO, "preco-json", "Preço sem data de verificação."))
    n = p.get("nota")
    if n is not None and float(n) >= 9.5:
        out.append(achados(ALERTA, "nota-json",
                           f"Nota {n} — notas quase perfeitas em série sinalizam viés."))
    if len(p.get("contras", [])) < 3:
        out.append(achados(ALERTA, "contras-json", "Menos de 3 contras."))
    links = p.get("links", {})
    if any("SEU-CODIGO-AQUI" in str(v) for v in links.values()):
        out.append(achados(ERRO, "links-json", "Links de afiliado ainda são placeholders."))
    if not out:
        out.append(achados(OK, "json", "JSON de produto sem problemas."))
    return out


# ---------------------------------------------------------------- relatório

ICONE = {ERRO: "❌", ALERTA: "⚠️ ", OK: "✅"}


def analisar(caminho_html, caminho_json=None):
    with open(caminho_html, encoding="utf-8") as f:
        html = f.read()
    res = []
    r, _ = checar_links_afiliado(html)
    res += r
    res += checar_divulgacao(html)
    res += checar_eeat(html)
    res += checar_teste_fisico(html)
    res += checar_valor_agregado(html)
    res += checar_enchimento(html)
    res += checar_keyword_stuffing(html)
    res += checar_schema(html)
    if caminho_json:
        res += checar_json_produto(caminho_json)
    return res


def main():
    ap = argparse.ArgumentParser(description="Trava de conformidade Google para artigos de afiliado.")
    ap.add_argument("arquivos", nargs="+", help="Arquivo(s) HTML")
    ap.add_argument("--json", help="JSON de produto correspondente")
    ap.add_argument("--resumo", action="store_true", help="Só o placar por arquivo")
    args = ap.parse_args()

    caminhos = []
    for a in args.arquivos:
        caminhos.extend(sorted(glob.glob(a)) if any(c in a for c in "*?[") else [a])

    total_erros = 0
    for c in caminhos:
        if not os.path.exists(c):
            print(f"❌ Não encontrado: {c}")
            total_erros += 1
            continue
        res = analisar(c, args.json)
        erros = [x for x in res if x["nivel"] == ERRO]
        alertas = [x for x in res if x["nivel"] == ALERTA]
        total_erros += len(erros)

        print(f"\n{'=' * 66}\n📋 {os.path.basename(c)}\n{'=' * 66}")
        if args.resumo:
            print(f"   {len(erros)} erro(s) · {len(alertas)} alerta(s)")
        else:
            for grupo, titulo in ((erros, "BLOQUEIA PUBLICAÇÃO"),
                                  (alertas, "REVISAR"),
                                  ([x for x in res if x["nivel"] == OK], "OK")):
                if not grupo:
                    continue
                print(f"\n── {titulo} ──")
                for a in grupo:
                    print(f" {ICONE[a['nivel']]} [{a['regra']}] {a['msg']}")
                    if a["detalhe"]:
                        print(f"      ↳ {a['detalhe']}")
        veredito = ("🚫 NÃO PUBLICAR — corrija os erros." if erros
                    else "⚠️  Publicável após revisar os alertas." if alertas
                    else "✅ Aprovado.")
        print(f"\n{veredito}")

    print(f"\n{'=' * 66}\nTotal: {total_erros} erro(s) em {len(caminhos)} arquivo(s).")
    sys.exit(1 if total_erros else 0)


if __name__ == "__main__":
    main()
