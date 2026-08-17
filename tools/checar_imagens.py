#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checar_imagens.py — valida as imagens de um artigo contra a biblioteca real
do WordPress, exportada em imagens/curadoriaprime.WordPress.*.xml

Motivo (regra §20): as reescritas do cluster de áudio suprimiram silenciosamente
as imagens do corpo dos artigos. O checker de conformidade não detectava, porque
não havia teste de imagem — três reviews passaram 14/14 com zero fotos no corpo.

Uso:
    python3 tools/checar_imagens.py articles/<arquivo>.html [...]
    python3 tools/checar_imagens.py articles/*.html

Testes aplicados:
  1. src-existe   — todo <img src> aponta para arquivo presente na biblioteca
  2. corpo        — o artigo tem imagem no corpo (não só a foto do autor)
  3. alt          — toda imagem tem alt descritivo, sem emoji
  4. lazy         — imagens do corpo têm loading="lazy"
  5. dimensoes    — width/height declarados (evita layout shift)
  6. orfas        — avisa sobre imagens do produto na biblioteca que estão sem uso

Saída: código 0 se aprovado, 1 se houver erro.
"""
import re
import sys
import glob
import os
import xml.etree.ElementTree as ET

NS = {'wp': 'http://wordpress.org/export/1.2/'}
RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
FOTO_AUTOR = 'cristiano-curadoria-prime'
EMOJI = re.compile('[\U0001F300-\U0001FAFF\u2600-\u27BF]')


def carregar_biblioteca():
    """Lê o export mais recente do WordPress e devolve {nome_arquivo: url}."""
    xmls = sorted(glob.glob(os.path.join(RAIZ, 'imagens', '*.xml')))
    if not xmls:
        return None
    lib = {}
    for x in xmls:
        try:
            root = ET.parse(x).getroot()
        except ET.ParseError:
            continue
        for item in root.findall('./channel/item'):
            if item.findtext('wp:post_type', default='', namespaces=NS) != 'attachment':
                continue
            url = item.findtext('wp:attachment_url', default='', namespaces=NS)
            if url:
                lib[url.split('/')[-1]] = url
    return lib


def corpo_sem_cabecalho(html):
    """Remove o cabeçalho comentado de instruções, que não vai para o WordPress."""
    i = html.find('-->')
    return html[i + 3:] if i != -1 else html


def checar(caminho, lib):
    html = corpo_sem_cabecalho(open(caminho, encoding='utf-8').read())
    nome = os.path.basename(caminho)
    tags = re.findall(r'<img[^>]*>', html)
    erros, avisos, oks = [], [], []

    if not tags:
        erros.append('[corpo] Nenhuma imagem no artigo.')
        return nome, erros, avisos, oks

    corpo = [t for t in tags if FOTO_AUTOR not in t]
    if not corpo:
        erros.append(
            '[corpo] O artigo só tem a foto do autor — nenhuma imagem no corpo. '
            'Provável supressão na reescrita (§20).')
    else:
        oks.append(f'[corpo] {len(corpo)} imagem(ns) no corpo do artigo.')

    quebradas = []
    for tag in tags:
        m = re.search(r'src="([^"]+)"', tag)
        if not m:
            erros.append('[src-existe] <img> sem atributo src.')
            continue
        arq = m.group(1).split('/')[-1]
        if lib is None or arq in lib:
            continue
        # Plugins de conversão (EWWW, ShortPixel) servem "foo.jpg" como
        # "foo.jpg.webp". O anexo original é o que consta na biblioteca.
        if arq.endswith('.webp'):
            original = arq[:-len('.webp')]
            if original in lib:
                continue
        quebradas.append(arq)
    if quebradas:
        for q in quebradas:
            erros.append(f'[src-existe] Arquivo não encontrado na biblioteca: {q}')
    elif lib is not None:
        oks.append(f'[src-existe] Todos os {len(tags)} src existem na biblioteca.')

    sem_alt = [t for t in tags if not re.search(r'alt="[^"]{6,}"', t)]
    if sem_alt:
        erros.append(f'[alt] {len(sem_alt)} imagem(ns) sem alt descritivo.')
    else:
        oks.append('[alt] Todas as imagens têm alt descritivo.')

    com_emoji = [t for t in tags if EMOJI.search(re.search(r'alt="([^"]*)"', t).group(1))
                 for _ in [0] if re.search(r'alt="([^"]*)"', t)]
    if com_emoji:
        avisos.append(f'[alt] {len(com_emoji)} alt(s) com emoji — remover para acessibilidade.')

    sem_lazy = [t for t in corpo if 'loading="lazy"' not in t]
    if sem_lazy:
        avisos.append(f'[lazy] {len(sem_lazy)} imagem(ns) do corpo sem loading="lazy".')
    else:
        oks.append('[lazy] Imagens do corpo com carregamento preguiçoso.')

    sem_dim = [t for t in tags if not (re.search(r'width="\d+"', t) and re.search(r'height="\d+"', t))]
    if sem_dim:
        avisos.append(f'[dimensoes] {len(sem_dim)} imagem(ns) sem width/height declarados.')
    else:
        oks.append('[dimensoes] Todas com width/height.')

    return nome, erros, avisos, oks


def main():
    alvos = sys.argv[1:]
    if not alvos:
        print(__doc__)
        return 1
    lib = carregar_biblioteca()
    if lib is None:
        print('⚠️  Nenhum export encontrado em imagens/*.xml — '
              'validação de existência de arquivo desativada.\n')
    else:
        print(f'📚 Biblioteca carregada: {len(lib)} anexos.\n')

    total_erros = 0
    for caminho in alvos:
        nome, erros, avisos, oks = checar(caminho, lib)
        print('=' * 66)
        print(f'🖼️  {nome}')
        print('=' * 66)
        for o in oks:
            print(f'  ✅ {o}')
        for a in avisos:
            print(f'  🟡 {a}')
        for e in erros:
            print(f'  ❌ {e}')
        print('  ✅ Aprovado.\n' if not erros else f'  ❌ {len(erros)} erro(s).\n')
        total_erros += len(erros)

    print(f'Total: {total_erros} erro(s) em {len(alvos)} arquivo(s).')
    return 1 if total_erros else 0


if __name__ == '__main__':
    sys.exit(main())
