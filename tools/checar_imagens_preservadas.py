#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
checar_imagens_preservadas.py — TRAVA DE REGRESSÃO DE IMAGENS

REGRA PERMANENTE DO CLIENTE (17/08/2026):
    "Mantenha sempre as imagens ao atualizar os artigos.
     Nunca remova as imagens de artigos que forem atualizados.
     É obrigatório preservar as imagens originais durante a atualização."

Este script compara a versão ATUAL de cada artigo com a versão anterior
registrada no git e FALHA se qualquer imagem tiver desaparecido.

Contexto: as reescritas do cluster de áudio suprimiram silenciosamente as
imagens do corpo de 4 artigos (§20). O checker de conformidade passava 14/14
porque não havia teste de imagem. Esta trava fecha esse buraco.

Uso:
    # compara com o commit anterior (HEAD)
    python3 tools/checar_imagens_preservadas.py articles/<arquivo>.html

    # compara com um commit/branch específico
    python3 tools/checar_imagens_preservadas.py --ref <commit> articles/*.html

    # valida tudo que está modificado no working tree
    python3 tools/checar_imagens_preservadas.py --modificados

Saída: código 0 se nenhuma imagem foi perdida, 1 se houve remoção.
Remoção intencional exige --autorizado, que exige justificativa por escrito.
"""
import re
import os
import sys
import subprocess

RAIZ = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def git(*args):
    """Roda git na raiz do repositório e devolve stdout (ou None se falhar)."""
    try:
        r = subprocess.run(['git'] + list(args), cwd=RAIZ,
                           capture_output=True, text=True, timeout=30)
        return r.stdout if r.returncode == 0 else None
    except Exception:
        return None


def imagens_de(html):
    """Extrai o conjunto de nomes de arquivo de imagem referenciados no HTML."""
    if html is None:
        return None
    srcs = re.findall(r'<img[^>]*src="([^"]+)"', html)
    return [s.split('/')[-1] for s in srcs]


def versao_anterior(caminho, ref):
    rel = os.path.relpath(os.path.abspath(caminho), RAIZ)
    return git('show', f'{ref}:{rel}')


def checar(caminho, ref, autorizado=False):
    nome = os.path.basename(caminho)
    atual = imagens_de(open(caminho, encoding='utf-8').read())
    antigo_html = versao_anterior(caminho, ref)

    if antigo_html is None:
        print(f'  ⬜ {nome}: arquivo novo (sem versão em {ref}) — nada a comparar.')
        return 0

    antigo = imagens_de(antigo_html)
    perdidas = [i for i in antigo if i not in atual]
    ganhas = [i for i in atual if i not in antigo]

    if not perdidas:
        extra = f'  (+{len(ganhas)} nova(s))' if ganhas else ''
        print(f'  ✅ {nome}: {len(antigo)} → {len(atual)} imagens preservadas.{extra}')
        return 0

    marca = '🟡 AUTORIZADO' if autorizado else '❌ BLOQUEADO'
    print(f'  {marca} {nome}: {len(perdidas)} imagem(ns) REMOVIDA(S)')
    for p in perdidas:
        print(f'       - {p}')
    if ganhas:
        print(f'     (ganhou {len(ganhas)}: ' + ', '.join(g[:44] for g in ganhas) + ')')
    if not autorizado:
        print('     → Restaure as imagens ou rode com --autorizado se a remoção for intencional.')
    return 0 if autorizado else 1


def main():
    args = sys.argv[1:]
    ref = 'HEAD'
    autorizado = '--autorizado' in args
    args = [a for a in args if a != '--autorizado']

    if '--ref' in args:
        i = args.index('--ref')
        ref = args[i + 1]
        del args[i:i + 2]

    if '--modificados' in args:
        args.remove('--modificados')
        saida = git('diff', '--name-only', 'HEAD', '--', 'articles/') or ''
        args += [os.path.join(RAIZ, l) for l in saida.split('\n')
                 if l.strip().endswith('.html')]

    alvos = [a for a in args if a.endswith('.html')]
    if not alvos:
        print(__doc__)
        return 1

    print('=' * 70)
    print(f'🔒 TRAVA DE PRESERVAÇÃO DE IMAGENS  (comparando com {ref})')
    print('=' * 70)

    falhas = sum(checar(a, ref, autorizado) for a in alvos)

    print('=' * 70)
    if falhas:
        print(f'❌ {falhas} artigo(s) perderam imagens. '
              'Regra do cliente: nunca remover imagens ao atualizar.')
    else:
        print(f'✅ {len(alvos)} artigo(s) verificados — nenhuma imagem perdida.')
    return 1 if falhas else 0


if __name__ == '__main__':
    sys.exit(main())
