#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checar_estado.py — detecta dessincronização entre os arquivos de estado
(audit/estado-<ID>.md) e os artigos que eles descrevem.

Achado C1 da auditoria de 17/08/2026: `audit/estado-3548.md` declarava
"4.261 palavras · nota 8,2/10" quando o artigo real tinha 5.239 palavras e
nota 8,0. `audit/estado-3550.md` declarava "8,4 · 3.633 palavras" contra
8,5 e 4.646 reais. Os arquivos de estado são a fonte de verdade da skill —
quando ficam defasados, toda decisão tomada a partir deles fica contaminada.

Causa: os campos eram digitados à mão no encerramento de cada rodada e não
revisitados quando o artigo mudava depois.

Uso:
    python3 tools/checar_estado.py                 # todos os estados
    python3 tools/checar_estado.py audit/estado-3548.md

Saída: 0 se tudo sincronizado, 1 se houver divergência.
"""
import re
import os
import sys
import glob

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TOLERANCIA_PALAVRAS = 0.02  # 2% — absorve variação de contagem entre métodos

# Mapa ID do post -> arquivo do artigo. Os nomes não seguem convenção única,
# por isso o vínculo é explícito.
MAPA = {
    '3548': 'redmi-buds-6-play-review-2026-vale-a-pena.html',
    '3550': 'jbl-wave-buds-2-review-2026-vale-a-pena.html',
    '3523': 'qcy-t13-anc-review-2026-vale-a-pena.html',
    '3527': 'edifier-w820nb-review-2026-vale-a-pena.html',
    '3545': 'samsung-galaxy-buds-core-vale-a-pena.html',
    '3336': 'melhor-fone-bluetooth-ate-500-reais-2026-artigo-completo.html',
}


def corpo(html):
    i = html.find('-->')
    return html[i + 3:] if i != -1 else html


def medir(caminho):
    c = corpo(open(caminho, encoding='utf-8').read())
    nota = re.search(r'"ratingValue":\s*"([\d.]+)"', c)
    imgs = len(re.findall(r'<img', c))
    return {
        'nota': nota.group(1).replace('.', ',') if nota else None,
        'palavras': len(re.sub(r'<[^>]+>', ' ', c).split()),
        'imagens': imgs,
    }


def checar(estado):
    nome = os.path.basename(estado)
    m = re.search(r'estado-(\d+)\.md', nome)
    if not m or m.group(1) not in MAPA:
        return None
    pid = m.group(1)
    artigo = os.path.join(RAIZ, 'articles', MAPA[pid])
    if not os.path.exists(artigo):
        print(f'  ⬜ {nome}: artigo não encontrado ({MAPA[pid]}).')
        return 0

    real = medir(artigo)
    texto = open(estado, encoding='utf-8').read()
    problemas = []

    # nota declarada em qualquer forma "8,5/10" ou "nota 8,5"
    declaradas = set(re.findall(r'nota[:\s]+(\d,\d)/10', texto, re.I))
    declaradas |= set(re.findall(r'\*\*Nota editorial:\*\*\s*(\d,\d)', texto))
    if real['nota'] and declaradas and real['nota'] not in declaradas:
        problemas.append(
            f"nota: estado diz {sorted(declaradas)}, artigo tem {real['nota']}")

    mp = re.search(r'([\d.]{3,6})\s*palavras', texto)
    if mp:
        decl = int(mp.group(1).replace('.', ''))
        dif = abs(decl - real['palavras']) / max(real['palavras'], 1)
        if dif > TOLERANCIA_PALAVRAS:
            problemas.append(
                f"palavras: estado diz {decl}, artigo tem {real['palavras']} "
                f"({dif*100:.0f}% de diferença)")

    mi = re.search(r'(\d+)\s*imagens', texto)
    if mi and int(mi.group(1)) != real['imagens']:
        problemas.append(
            f"imagens: estado diz {mi.group(1)}, artigo tem {real['imagens']}")

    if problemas:
        print(f'  ❌ {nome}')
        for p in problemas:
            print(f'       - {p}')
        return 1

    print(f"  ✅ {nome}: nota {real['nota']} · {real['palavras']} palavras · "
          f"{real['imagens']} imagens")
    return 0


def main():
    alvos = sys.argv[1:] or sorted(glob.glob(os.path.join(RAIZ, 'audit', 'estado-*.md')))
    print('=' * 70)
    print('🔄 SINCRONIA ENTRE ARQUIVOS DE ESTADO E ARTIGOS')
    print('=' * 70)
    falhas = 0
    for a in alvos:
        r = checar(a)
        if r:
            falhas += r
    print('=' * 70)
    if falhas:
        print(f'❌ {falhas} arquivo(s) de estado dessincronizado(s). '
              'Regenerar os campos a partir do artigo (achado C1).')
    else:
        print('✅ Todos os estados conferem com os artigos.')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
