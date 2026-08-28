#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
aplicar_wp_p0.py — aplica as correções P0 + declarações de honestidade
DIRETAMENTE no WordPress, sobre o content.raw (context=edit autenticado).

Protocolo herdado de corrigir_artigos.py v2 (lições 2943/3226/3183):
  • NUNCA gravar content.rendered — wpautop reprocessa e amplifica <br />.
  • Backup do raw antes de gravar (articles/wp_raw_backups/).
  • Verificação pós-gravação (relê o raw; divergiu → restaura e aborta).

Etapas (nesta ordem):
  --pipeline-check  GET render público dos 18 posts, roda o pipeline local e
                    confere que reproduz EXATAMENTE articles/html_output/*.html
                    (prova que o pipeline cobre 100% das correções feitas).
  --baixar          GET context=edit → backup do raw + espelho em
                    articles/wp_raw_mirror/articles/html_output/ (intocado).
  --processar       roda o pipeline (corrigir_p0_artigos + adicionar_honestidade)
                    sobre o espelho, deixando-o corrigido.
  --validar         checagens objetivas no espelho: JSON-LD parseável, sem
                    aggregateRating/reviewCount/ratingCount, declarações
                    presentes, alegações de teste ausentes.
  --gravar [--simular]  PUT do raw corrigido por post + verificação + rollback.

Uso:
  export WP_USER="..." WP_APP_PASSWORD="..."
  python3 tools/aplicar_wp_p0.py --pipeline-check
  python3 tools/aplicar_wp_p0.py --baixar
  python3 tools/aplicar_wp_p0.py --processar
  python3 tools/aplicar_wp_p0.py --validar
  python3 tools/aplicar_wp_p0.py --gravar --simular
  python3 tools/aplicar_wp_p0.py --gravar
"""
import base64
import contextlib
import difflib
import io
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import corrigir_p0_artigos as P0          # noqa: E402  (funções de correção P0)
import adicionar_honestidade as HON       # noqa: E402  (declarações de honestidade)

SITE = "https://curadoriaprime.com"
API = f"{SITE}/wp-json/wp/v2"

BACKUP_DIR = ROOT / "articles" / "wp_raw_backups"
MIRROR = ROOT / "articles" / "wp_raw_mirror" / "articles" / "html_output"
LOCAL = ROOT / "articles" / "html_output"

# Os 18 artigos P0 (mesma lista do RELATORIO-CORRECOES-P0-2026-08-27.md)
SLUGS = [
    "apple-tv-4k",
    "galaxy-s24-fe-em-2026",
    "galaxy-watch7-44mm-vale-a-pena",
    "iphone-16e-review-2026",
    "jbl-cinema-sb180-review-vale-a-pena",
    "lenovo-ideapad-slim-3-notebook-2026",
    "presentes-dia-dos-pais-tech-ate-300",
    "purificador-de-agua-electrolux-pe12g-review",
    "samsung-galaxy-book4-review-2026",
    "samsung-galaxy-s25-5g-review",
    "samsung-hw-b400f-review",
    "samsung-u8100f-smart-tv-4k-review",
    "samsung-u8600f-review",
    "soundcore-liberty-4-nc-vale-a-pena",
    "tcl-c6k-review-2026",
    "xiaomi-redmi-note-14-pro-plus-review-2026",
    "xiaomi-smart-band-10-vale-a-pena",
    "xiaomi-smart-band-9-active-vale-a-pena",
]

RE_JSONLD = re.compile(
    r'<script type="application/ld\+json">(.*?)</script>', re.S | re.I)


# ─────────────────────────── API WordPress ───────────────────────────
def auth_header():
    user = os.environ.get("WP_USER")
    pwd = os.environ.get("WP_APP_PASSWORD")
    if not user or not pwd:
        sys.exit("❌ Defina WP_USER e WP_APP_PASSWORD no ambiente.")
    token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def req(url, method="GET", data=None, auth=False):
    headers = {"Content-Type": "application/json",
               "User-Agent": "CuradoriaPrime-Agent/1.0"}
    if auth:
        headers.update(auth_header())
    body = json.dumps(data).encode() if data is not None else None
    ultimo_erro = None
    for tentativa in range(4):
        r = urllib.request.Request(url, data=body, headers=headers,
                                   method=method)
        try:
            with urllib.request.urlopen(r, timeout=60) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            detalhe = e.read().decode()[:300]
            if e.code in (429, 502, 503, 504) and tentativa < 3:
                espera = 20 * (tentativa + 1)
                print(f"  ⏳ HTTP {e.code} — aguardando {espera}s antes de "
                      f"tentar novamente ({tentativa + 1}/3)…")
                time.sleep(espera)
                ultimo_erro = RuntimeError(
                    f"HTTP {e.code} em {method} {url}\n{detalhe}")
                continue
            raise RuntimeError(f"HTTP {e.code} em {method} {url}\n{detalhe}")
    raise ultimo_erro


def get_post(slug, edit=False, fields="id,slug,modified,status,link,content"):
    q = f"{API}/posts?slug={slug}&_fields={fields}"
    if edit:
        q += "&context=edit"
    res = req(q, auth=edit)
    if not res:
        raise RuntimeError(f"slug não encontrado: {slug}")
    return res[0]


# ─────────────────────────── Pipeline local ───────────────────────────
def has_declaracao(content):
    return "não testou" in content.lower() or "não testamos" in content.lower()


def pipeline(content, fname, quiet=True):
    """Mesma ordem do main() de corrigir_p0_artigos + declarações."""
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        content = P0.fix_wpautop_jsonld(content)
        if fname in P0.ARTIGOS_AGG:
            content, _ = P0.remove_aggregate_rating(content)
            content = P0.limpar_virgulas_jsonld(content)
            content, _ = P0.fix_literals_jsonld(content, fname)
            if fname == "purificador-de-agua-electrolux-pe12g-review.html":
                content = P0.fix_purificador_structure(content)
            content, _ = P0.fix_teste_fisico(content, fname)
        if fname in HON.ARTIGOS and not has_declaracao(content):
            ins = HON.decl(HON.ARTIGOS[fname])
            content, n = HON.RE_LINK.subn(
                lambda m: m.group(1) + ins, content, count=1)
            if n == 0:
                print(f"  ⚠️  {fname}: âncora da metodologia não encontrada")
    return content


def jsonld_blocks(html):
    return RE_JSONLD.findall(html)


def jsonld_valido(html):
    """True se todo bloco JSON-LD parseia como JSON."""
    try:
        for b in jsonld_blocks(html):
            json.loads(b)
        return True
    except (json.JSONDecodeError, ValueError):
        return False


def br_em_jsonld(html):
    return sum(b.count("<br") for b in jsonld_blocks(html))


def aggregate_presente(html):
    return bool(re.search(
        r'["\'](?:aggregateRating|reviewCount|ratingCount)["\']', html))


# ─────────────────────── Etapa 1: pipeline-check ───────────────────────
def cmd_pipeline_check():
    print("=" * 76)
    print("PIPELINE-CHECK — o pipeline reproduz os 18 locais a partir do render WP?")
    print("=" * 76)
    falhas = []
    for fname in SLUGS:
        slug = fname[:-5] if fname.endswith(".html") else fname
        fhtml = fname if fname.endswith(".html") else fname + ".html"
        try:
            post = get_post(slug)
        except RuntimeError as e:
            falhas.append((slug, f"API: {e}"))
            continue
        wp_render = post["content"]["rendered"]
        local = (LOCAL / fhtml).read_text(encoding="utf-8")
        got = pipeline(wp_render, fhtml)
        if got == local:
            print(f"  ✅ {fhtml}: pipeline reproduz o local byte a byte")
        else:
            falhas.append((slug, "pipeline ≠ local"))
            print(f"\n  ❌ {fhtml}: DIVERGÊNCIA — diff (WP→pipeline vs local):")
            diff = list(difflib.unified_diff(
                got.splitlines(), local.splitlines(),
                "pipeline(render_wp)", "local.html", lineterm="", n=0))
            for linha in diff[:24]:
                print("     " + linha[:200])
        time.sleep(2.0)  # ritmo gentil para não disparar rate-limit/503
    print()
    if falhas:
        print(f"❌ {len(falhas)} divergência(s) — corrija o pipeline antes de baixar:")
        for s, m in falhas:
            print(f"     {s}: {m}")
        sys.exit(1)
    print("✅ Pipeline cobre 100% das correções locais.")


# ─────────────────────── Etapa 2: baixar raws ───────────────────────
def cmd_baixar():
    print("=" * 76)
    print("BAIXAR — content.raw autenticado dos 18 posts (backup + espelho)")
    print("=" * 76)
    BACKUP_DIR.mkdir(parents=True, exist_ok=True)
    MIRROR.mkdir(parents=True, exist_ok=True)
    pulados = []
    for fname in SLUGS:
        fhtml = fname if fname.endswith(".html") else fname + ".html"
        slug = fhtml[:-5]
        post = get_post(slug, edit=True)
        raw = post["content"]["raw"]
        modified = post["modified"].replace("T", " ").replace("Z", "")
        dt_wp = datetime.strptime(modified, "%Y-%m-%d %H:%M:%S") \
            .replace(tzinfo=timezone.utc)
        mtime = datetime.fromtimestamp(
            (LOCAL / fhtml).stat().st_mtime, tz=timezone.utc)
        if dt_wp > mtime + timedelta(minutes=15):
            print(f"  ⏭️  {slug}: modificado no WP em {modified} (depois da "
                  f"captura local) — PULADO, revise manualmente")
            pulados.append(slug)
            continue
        bkp = BACKUP_DIR / f"{post['id']}-{slug}-raw.html"
        bkp.write_text(raw, encoding="utf-8")
        (MIRROR / fhtml).write_text(raw, encoding="utf-8")
        status = post.get("status", "?")
        print(f"  💾 {slug} (id {post['id']}, {status}, mod {modified}) "
              f"→ backup + espelho ({len(raw)} chars)")
        time.sleep(1.5)  # ritmo gentil para não disparar rate-limit/503
    print()
    if pulados:
        print(f"⚠️  {len(pulados)} post(s) pulado(s): {', '.join(pulados)}")
    print("✅ Espelho pronto em articles/wp_raw_mirror/")


# ─────────────────────── Etapa 3: processar espelho ───────────────────────
def cmd_processar():
    print("=" * 76)
    print("PROCESSAR — pipeline sobre o espelho de raws")
    print("=" * 76)
    for fhtml in SLUGS:
        fhtml = fhtml if fhtml.endswith(".html") else fhtml + ".html"
        p = MIRROR / fhtml
        if not p.exists():
            print(f"  ⚠️  {fhtml}: ausente no espelho (baixar antes)")
            continue
        original = p.read_text(encoding="utf-8")
        corrigido = pipeline(original, fhtml)
        if corrigido != original:
            p.write_text(corrigido, encoding="utf-8")
            print(f"  ✅ {fhtml}: corrigido ({len(original)} → {len(corrigido)} chars)")
        else:
            print(f"  ℹ️  {fhtml}: sem alterações")
    print("\n✅ Espelho processado — rode --validar")


# ─────────────────────── Etapa 4: validar espelho ───────────────────────
EXIGE_DECLARACAO = set(HON.ARTIGOS) | {
    "samsung-hw-b400f-review.html", "samsung-galaxy-book4-review-2026.html"}
ALEGACOES_PROIBIDAS = {
    "samsung-hw-b400f-review.html": ["Em nossos testes"],
    "samsung-galaxy-book4-review-2026.html": ["&#8220;Usei a quase 1 mês",
                                              "Usei a quase 1 mês"],
}


def cmd_validar():
    print("=" * 76)
    print("VALIDAR — checagens objetivas no espelho corrigido")
    print("=" * 76)
    erros = 0
    for fname in SLUGS:
        fhtml = fname if fname.endswith(".html") else fname + ".html"
        p = MIRROR / fhtml
        if not p.exists():
            print(f"  ⚠️  {fhtml}: ausente no espelho")
            erros += 1
            continue
        html = p.read_text(encoding="utf-8")
        probs = []
        if not jsonld_blocks(html):
            probs.append("sem JSON-LD")
        elif not jsonld_valido(html):
            probs.append("JSON-LD não parseia")
        if aggregate_presente(html):
            probs.append("aggregateRating/reviewCount/ratingCount presente (§2.4)")
        if fhtml in EXIGE_DECLARACAO and "não testou" not in html.lower():
            probs.append("sem declaração de ausência de teste")
        for trecho in ALEGACOES_PROIBIDAS.get(fhtml, []):
            if trecho in html:
                probs.append(f'alegação de teste: "{trecho[:40]}"')
        if br_em_jsonld(html):
            probs.append("<br /> dentro do JSON-LD")
        if probs:
            erros += len(probs)
            print(f"  ❌ {fhtml}: " + " · ".join(probs))
        else:
            print(f"  ✅ {fhtml}")
    print()
    if erros:
        sys.exit(f"❌ {erros} problema(s) no espelho — NÃO gravar no WP.")
    print("✅ Espelho 100% válido para gravação.")


# ─────────────────────── Etapa 5: gravar no WP ───────────────────────
def cmd_gravar(simular=False, forcar=False):
    print("=" * 76)
    print(f"GRAVAR — {'SIMULAÇÃO' if simular else 'APLICAÇÃO REAL'} no WordPress")
    print("=" * 76)
    gravados, problemas = 0, []
    for fname in SLUGS:
        fhtml = fname if fname.endswith(".html") else fname + ".html"
        slug = fhtml[:-5]
        p = MIRROR / fhtml
        if not p.exists():
            print(f"  ⚠️  {slug}: sem raw corrigido no espelho — pulado")
            problemas.append((slug, "espelho ausente"))
            continue
        corrigido = p.read_text(encoding="utf-8")
        post = get_post(slug, edit=True)
        pid = post["id"]
        raw_atual = post["content"]["raw"]
        bkp = BACKUP_DIR / f"{pid}-{slug}-raw.html"
        if bkp.exists() and bkp.read_text(encoding="utf-8") != raw_atual \
                and not forcar:
            print(f"  ⏭️  {slug}: raw no WP mudou desde o backup — pulado "
                  f"(use --forcar para sobrescrever)")
            problemas.append((slug, "raw divergiu do backup"))
            continue
        if raw_atual == corrigido:
            print(f"  ✅ {slug}: já está corrigido no WP")
            continue
        if simular:
            delta = len(corrigido) - len(raw_atual)
            print(f"  🧪 {slug} (id {pid}): gravaria ({delta:+d} chars)")
            continue
        req(f"{API}/posts/{pid}", "POST", {"content": corrigido}, auth=True)
        gravados += 1
        # verificação pós-gravação
        post2 = get_post(slug, edit=True)
        if post2["content"]["raw"] != corrigido:
            print(f"  🛑 {slug}: raw gravado ≠ enviado — restaurando backup…")
            req(f"{API}/posts/{pid}", "POST",
                {"content": bkp.read_text(encoding="utf-8")}, auth=True)
            problemas.append((slug, "gravado ≠ enviado (rollback ok)"))
            sys.exit("\n🛑 Lote interrompido para não propagar dano.")
        print(f"  ✅ {slug} (id {pid}): gravado e conferido")
        # verificação do render público
        pub = get_post(slug)
        render = pub["content"]["rendered"]
        avisos = []
        if jsonld_blocks(render) and not jsonld_valido(render):
            avisos.append("JSON-LD do render não parseia")
        if aggregate_presente(render):
            avisos.append("aggregateRating visível no render")
        if fhtml in EXIGE_DECLARACAO and "não testou" not in render.lower():
            avisos.append("declaração não aparece no render")
        if avisos:
            print(f"     ⚠️  render: " + " · ".join(avisos))
            problemas.append((slug, " · ".join(avisos)))
        time.sleep(2.0)  # ritmo gentil para não disparar rate-limit/503
    print()
    print(f"{'SIMULADO' if simular else 'GRAVADOS'}: {gravados} post(s)")
    if problemas:
        print(f"\n⚠️  {len(problemas)} pendência(s):")
        for s, m in problemas:
            print(f"     {s}: {m}")


def main():
    global SLUGS
    import argparse
    ap = argparse.ArgumentParser(description="Aplica correções P0 no WP (raw)")
    ap.add_argument("--pipeline-check", action="store_true")
    ap.add_argument("--baixar", action="store_true")
    ap.add_argument("--processar", action="store_true")
    ap.add_argument("--validar", action="store_true")
    ap.add_argument("--gravar", action="store_true")
    ap.add_argument("--simular", action="store_true")
    ap.add_argument("--forcar", action="store_true")
    ap.add_argument("--apenas", type=str, default="",
                    help="filtra SLUGS por substrings separados por vírgula")
    a = ap.parse_args()
    if a.apenas:
        filtros = [s.strip() for s in a.apenas.split(",") if s.strip()]
        SLUGS = [s for s in SLUGS if any(f in s for f in filtros)]
    if a.pipeline_check:
        cmd_pipeline_check()
    elif a.baixar:
        cmd_baixar()
    elif a.processar:
        cmd_processar()
    elif a.validar:
        cmd_validar()
    elif a.gravar:
        cmd_gravar(simular=a.simular, forcar=a.forcar)
    else:
        ap.print_help()


if __name__ == "__main__":
    main()


