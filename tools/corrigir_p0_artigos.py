#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
corrigir_p0_artigos.py — Correção em lote dos 18 artigos P0/P1/P2 restantes.

Resolve 3 categorias de problemas:

  A. aggregateRating / reviewCount / ratingCount no JSON-LD (§2.4)
     → remove o bloco inteiro. 16 artigos.

  B. JSON-LD corrompido por wpautop (<br /> dentro do <script>)
     → limpa <br /> e outras tags HTML do bloco JSON-LD. 2 artigos.

  C. Estrutura JSON-LD quebrada (faltando ] e vírgula)
     → reconstrói a estrutura @graph. 1 artigo (purificador).

  D. Alegações de teste físico (§3)
     → reescrita manual. 2 artigos (samsung-hw-b400f, samsung-galaxy-book4).

Uso:
    python3 corrigir_p0_artigos.py            # aplica todas as correções
    python3 corrigir_p0_artigos.py --dry-run  # mostra o diff sem gravar
"""
import io
import os
import re
import sys
import json
from pathlib import Path

BASE = Path(os.environ.get("CP_BASE", "."))
HTML_DIR = BASE / "articles" / "html_output"

# ── Artigos alvo ──
ARTIGOS_AGG = [
    "samsung-hw-b400f-review.html",
    "xiaomi-smart-band-10-vale-a-pena.html",
    "samsung-galaxy-book4-review-2026.html",
    "samsung-galaxy-s25-5g-review.html",
    "iphone-16e-review-2026.html",
    "soundcore-liberty-4-nc-vale-a-pena.html",
    "galaxy-s24-fe-em-2026.html",
    "samsung-u8100f-smart-tv-4k-review.html",
    "samsung-u8600f-review.html",
    "jbl-cinema-sb180-review-vale-a-pena.html",
    "xiaomi-smart-band-9-active-vale-a-pena.html",
    "galaxy-watch7-44mm-vale-a-pena.html",
    "tcl-c6k-review-2026.html",
    "xiaomi-redmi-note-14-pro-plus-review-2026.html",
    "lenovo-ideapad-slim-3-notebook-2026.html",
    "purificador-de-agua-electrolux-pe12g-review.html",
]

ARTIGOS_WPAUTOP = [
    "presentes-dia-dos-pais-tech-ate-300.html",
    "apple-tv-4k.html",
]

# ── Funções auxiliares ──
def read(fname):
    return io.open(HTML_DIR / fname, encoding="utf-8").read()

def write(fname, s):
    io.open(HTML_DIR / fname, "w", encoding="utf-8").write(s)

def trocar(txt, velho, novo, label=""):
    n = txt.count(velho)
    if n == 0:
        print(f"  ⚠️  [{label}] padrão não encontrado (já corrigido?)")
        return txt, 0
    return txt.replace(velho, novo), n


# ── Tipo A: remover aggregateRating/reviewCount/ratingCount ──
RE_AGG = re.compile(
    r'["\']aggregateRating["\']\s*:\s*\{[^}]*\}',
    re.DOTALL,
)
RE_REVIEWCOUNT = re.compile(
    r',\s*["\']reviewCount["\']\s*:\s*"[^"]*"\s*',
)
RE_RATINGCOUNT = re.compile(
    r',\s*["\']ratingCount["\']\s*:\s*"[^"]*"\s*',
)

def remove_aggregate_rating(content):
    """Remove aggregateRating, reviewCount e ratingCount do JSON-LD."""
    n1 = len(RE_AGG.findall(content))
    content = RE_AGG.sub('', content)
    n2 = len(RE_REVIEWCOUNT.findall(content))
    content = RE_REVIEWCOUNT.sub('', content)
    n3 = len(RE_RATINGCOUNT.findall(content))
    content = RE_RATINGCOUNT.sub('', content)
    # limpa vírgulas órfãs deixadas pela remoção (ex.: `,\n,`)
    orfas = len(re.findall(r',\s*,', content))
    content = re.sub(r',\s*,', ',', content)
    total = n1 + n2 + n3
    # limpa vírgulas órfãs deixadas por remoção anterior (ex.: `,\n,`)
    orfas = len(re.findall(r',\s*,', content))
    content = re.sub(r',\s*,', ',', content)
    if total:
        print(f"  🔧 Removido aggregateRating ({n1} bloco(s)) + "
              f"reviewCount ({n2}) + ratingCount ({n3}) do JSON-LD")
    if orfas:
        print(f"  🔧 {orfas} vírgula(s) órfã(s) limpas no JSON-LD")
    return content, total


# ── Tipo B: corrigir wpautop <br /> em JSON-LD ──
RE_JSONLD_BLOCK = re.compile(
    r'(<script type="application/ld\+json">)(.*?)(</script>)',
    re.DOTALL | re.IGNORECASE,
)

def fix_wpautop_jsonld(content):
    """Remove tags HTML e entidades injetadas pelo wpautop dentro de JSON-LD."""
    def replacer(m):
        prefix, block, suffix = m.group(1), m.group(2), m.group(3)
        original = block
        block = re.sub(r'<br\s*/?>', '', block, flags=re.IGNORECASE)
        block = block.replace('&nbsp;', ' ')
        block = re.sub(r'&amp;', '&', block)
        block = re.sub(r'&lt;', '<', block)
        block = re.sub(r'&gt;', '>', block)
        if block != original:
            removed = original.count('<br />') + original.count('<br>')
            print(f"  🔧 Corrigido wpautop: {removed} tag(s) <br /> removida(s)")
        return prefix + block + suffix
    return RE_JSONLD_BLOCK.sub(replacer, content)


# ── Tipo D: reescrever alegações de teste físico (§3) ──
FIXO_3310_ANTES = '💡 <strong>O Grande Trunfo (Voice Enhance):</strong> Em nossos testes, o modo Voice Enhance aplicou um filtro DSP que elevou as frequências entre 1kHz e 3kHz. O resultado? Diálogos em novelas, jornais e séries como <em>The Crown</em> ficam cristalinos, sem que você precise ficar ajustando o volume a cada cena. Neste quesito específico, ela supera a JBL SB180 e a LG SQC1.'

FIXO_3310_DEPOIS = '💡 <strong>O Grande Trunfo (Voice Enhance):</strong> O modo Voice Enhance aplica um filtro DSP que eleva as frequências entre 1kHz e 3kHz, segundo a documentação oficial Samsung e relatos publicados por compradores. Diálogos em novelas, jornais e séries como <em>The Crown</em> são citados por usuários como mais cristalinos, sem necessidade de ajuste de volume entre cenas. Neste quesito específico, ela supera a JBL SB180 e a LG SQC1.'

FIXO_4185_ANTES = '&#8220;Usei a quase 1 mês. É um notebook em metal, muito leve e fino. <strong>Trabalho ou faculdade 8/10</strong> — leve e compacto, config suficiente para Excel, Power BI ou TCC. <strong>Jogar 4.5/10</strong> — apesar do i3 de 13ª geração, não é notebook gamer, jogos AAA modernos não vai por ter 8gb RAM soldada. Bateria dura de 6h a 7h.&#8221;'

FIXO_4185_DEPOIS = '&#8220;Relato publicado de comprador: quase 1 mês de uso. É um notebook em metal, muito leve e fino. <strong>Trabalho ou faculdade 8/10</strong> — leve e compacto, config suficiente para Excel, Power BI ou TCC. <strong>Jogar 4.5/10</strong> — apesar do i3 de 13ª geração, não é notebook gamer, jogos AAA modernos não vai por ter 8gb RAM soldada. Bateria dura de 6h a 7h.&#8221;'

def fix_teste_fisico(content, fname):
    """Reescreve alegações de teste físico para formulações sem teste (§4)."""
    total = 0
    if fname == "samsung-hw-b400f-review.html":
        content, n = trocar(content, FIXO_3310_ANTES, FIXO_3310_DEPOIS, "teste-fisico-3310")
        total += n
        if "não testamos" not in content.lower() and "não fizemos teste" not in content.lower():
            decl = '<p><strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes publicados e relatos de compradores. A Curadoria Prime não testou esta unidade fisicamente.</p>\n'
            ancora = 'Entenda nossa metodologia completa →</a>\n</div>'
            if ancora in content:
                content = content.replace(ancora, 'Entenda nossa metodologia completa →</a>\n</div>\n\n' + decl, 1)
                print(f"  ✅ Declaração de ausência de teste adicionada (3310)")
            else:
                print(f"  ⚠️  Âncora da metodologia (3310) não encontrada — insira manualmente")
    if fname == "samsung-galaxy-book4-review-2026.html":
        content, n = trocar(content, FIXO_4185_ANTES, FIXO_4185_DEPOIS, "teste-fisico-4185")
        total += n
        print(f"  ✅ Citação buyer review reescrita como relato terceirizado (4185)")
    return content, total


# ── Tipo C: corrigir estrutura JSON-LD quebrada (purificador) ──
def fix_purificador_structure(content):
    """Corrige o BreadcrumbList dentro de mainEntity do FAQPage → @graph."""
    # Padrão quebrado: } , { "BreadcrumbList" dentro de mainEntity
    # Procura especificamente dentro do script JSON-LD
    script_match = re.search(
        r'<script type="application/ld\+json">(.*?)</script>',
        content, re.DOTALL | re.IGNORECASE,
    )
    if not script_match:
        return content
    
    block = script_match.group(1)
    
    # Verifica se tem BreadcrumbList dentro de mainEntity
    if '"BreadcrumbList"' not in block:
        return content
    
    # O problema: após o fechamento da última Question },
    # há uma vírgula e abre BreadcrumbList, mas não fechou mainEntity ]
    # Precisamos fechar ] ] e } antes do BreadcrumbList
    
    # Padrão: texto fechando última Question } seguido por , { BreadcrumbList } ] }
    # Correção: } ] } , { BreadcrumbList } ] }
    
    pattern = re.compile(
        r'(\s*"text"\s*:\s*"[^"]*"\s*\}\s*\}\s*)\s*,\s*(\{\s*"@type":\s*"BreadcrumbList"\s*"itemListElement".*?\s*\}\s*)\s*\]\s*\}',
        re.DOTALL | re.IGNORECASE,
    )
    
    match = pattern.search(block)
    if match:
        old_text = match.group(0)
        new_text = match.group(1) + ' ]\n  },\n  ' + match.group(2) + '\n ]\n}'
        block = block.replace(old_text, new_text, 1)
        content = content.replace(script_match.group(0), 
                                  script_match.group(0).replace(old_text, new_text, 1), 1)
        print(f"  🔧 Estrutura JSON-LD do purificador: BreadcrumbList movido de mainEntity → @graph")
        return content
    
    # Tentativa alternativa: procurar } , { BreadcrumbList } ] } no contexto de mainEntity
    alt_pattern = re.compile(
        r'(Questi[ao]n.*?aceitou.*?text.*?\}\s*\}[\s\n]*),[\s\n]*(?:\{\s*"@type":\s*"BreadcrumbList".*?\}[\s\n]*\})[\s\n]*\]',
        re.DOTALL | re.IGNORECASE,
    )
    match = alt_pattern.search(block)
    if match:
        old_text = match.group(0)
        # Fechar mainEntity com ] antes da vírgula, depois } para fechar FAQPage
        inner = match.group(1).rstrip()
        new_text = inner + '\n    ]\n  },\n' + re.search(r'\{\s*"@type":\s*"BreadcrumbList".*?\}', match.group(0), re.DOTALL).group(0) + '\n  ]\n}'
        block = block.replace(old_text, new_text, 1)
        content = content.replace(script_match.group(0), 
                                  script_match.group(0).replace(old_text, new_text, 1), 1)
        print(f"  🔧 Estrutura JSON-LD do purificador: BreadcrumbList movido de mainEntity → @graph (alt)")
        return content
    
    print(f"  ⚠️  Estrutura JSON-LD do purificador não reconhecida — corrija à mão")
    return content


# ── Main ──
def main():
    dry = "--dry-run" in sys.argv
    total_fixes = {"aggregateRating": 0, "wpautop": 0, "teste_fisico": 0, "estrutura": 0}
    
    print("=" * 72)
    print(f"Correção P0 — {'SIMULAÇÃO' if dry else 'APLICAÇÃO'}")
    print("=" * 72)
    
    # ── Type A + C + D: artigos com aggregateRating ──
    for fname in ARTIGOS_AGG:
        fpath = HTML_DIR / fname
        if not fpath.exists():
            print(f"\n⚠️  {fname}: arquivo não encontrado, pulando")
            continue
        
        print(f"\n▶ {fname}")
        original = read(fname)
        content = original
        
        # B. Fix wpautop (aplica em todos primeiro, antes de parsear JSON)
        content = fix_wpautop_jsonld(content)
        
        # A. Remove aggregateRating
        content, n = remove_aggregate_rating(content)
        total_fixes["aggregateRating"] += n
        
        # C. Fix estrutura (apenas purificador)
        if fname == "purificador-de-agua-electrolux-pe12g-review.html":
            before = content
            content = fix_purificador_structure(content)
            if content != before:
                total_fixes["estrutura"] += 1
        
        # D. Fix teste físico
        content, n = fix_teste_fisico(content, fname)
        total_fixes["teste_fisico"] += n
        
        if content != original:
            if not dry:
                write(fname, content)
            print(f"  ✅ Correções aplicadas a {fname}")
        else:
            print(f"  ℹ️  Sem alterações em {fname}")
    
    # ── Type B: artigos com wpautop (já incluídos acima)
    for fname in ARTIGOS_WPAUTOP:
        fpath = HTML_DIR / fname
        if not fpath.exists() or fname in ARTIGOS_AGG:
            continue
        print(f"\n▶ {fname}")
        original = read(fname)
        content = fix_wpautop_jsonld(original)
        if content != original:
            if not dry:
                write(fname, content)
            total_fixes["wpautop"] += 1
            print(f"  ✅ wpautop corrigido em {fname}")
    
    print("\n" + "=" * 72)
    print(f"Resumo: aggregateRating {total_fixes['aggregateRating']} · "
          f"wpautop {total_fixes['wpautop']} · "
          f"teste-físico {total_fixes['teste_fisico']} · "
          f"estrutura {total_fixes['estrutura']}")
    if dry:
        print("  (dry-run — nada foi gravado)")
    else:
        print("  ✅ Arquivos atualizados — rode o checker para validar")


if __name__ == "__main__":
    main()
