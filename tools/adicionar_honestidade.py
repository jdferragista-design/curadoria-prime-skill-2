#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""adicionar_honestidade.py — insere a declaração de ausência de teste físico
(§5 regras-editoriais) nos 7 artigos que ainda têm o alerta [honestidade].

A declaração canônica contém "análise baseada em especificações" e "não testou
... fisicamente", o que também limpa o alerta [honestidade] no checker.
"""
import io, os, re, sys

ARTIGOS = {
    "iphone-16e-review-2026.html": "Apple",
    "samsung-u8100f-smart-tv-4k-review.html": "Samsung",
    "samsung-u8600f-review.html": "Samsung",
    "jbl-cinema-sb180-review-vale-a-pena.html": "JBL",
    "tcl-c6k-review-2026.html": "TCL",
    "xiaomi-redmi-note-14-pro-plus-review-2026.html": "Xiaomi",
    "lenovo-ideapad-slim-3-notebook-2026.html": "Lenovo",
}

# Respeita CP_BASE para rodar sobre o espelho de raws do WordPress:
#   CP_BASE=articles/wp_raw_mirror python3 tools/adicionar_honestidade.py
BASE = os.environ.get("CP_BASE", ".")
D = os.path.join(BASE, "articles", "html_output") + "/"

def decl(marca):
    return (f'<br><br><strong>Tipo de análise:</strong> pesquisa editorial '
            f'baseada em especificações oficiais da {marca}, testes '
            f'independentes publicados e relatos de compradores. A Curadoria '
            f'Prime não testou esta unidade fisicamente.')

# Âncoras: o fim do link da metodologia (vai variar entre os artigos)
RE_LINK = re.compile(r'(Entenda nossa metodologia[^<]*</a>|Veja nossa prova real de uso[^<]*</a>)')

def main():
    dry = "--dry-run" in sys.argv
    for fname, marca in ARTIGOS.items():
        p = D + fname
        s = io.open(p, encoding="utf-8").read()
        orig = s
        if "não testou" in s or "não testamos" in s:
            print(f"  ⏭️  {fname}: declaração já presente — pulando")
            continue
        ins = decl(marca)
        s2, n = RE_LINK.subn(r'\1' + ins, s, count=1)
        if n == 0:
            print(f"  ⚠️  {fname}: âncora do link não encontrada — corrija manual")
            continue
        if not dry:
            io.open(p, "w", encoding="utf-8").write(s2)
        print(f"  ✅ {fname}: declaração inserida após o link da metodologia ({marca})")
    print("\n(dry-run — nada gravado)" if dry else "\n✅ arquivos atualizados")


if __name__ == "__main__":
    main()