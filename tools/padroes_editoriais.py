# -*- coding: utf-8 -*-
"""
padroes_editoriais.py — FONTE ÚNICA dos padrões de texto das regras editoriais.

Por que este arquivo existe
---------------------------
Até agora `checar_conformidade.py` e `corrigir_artigos.py` mantinham cada um a
sua lista de padrões de teste físico. As listas divergiram: o gate — justamente
o script que BLOQUEIA — era o mais fraco dos dois. Seis das frases vetadas pela
regra 1 do SKILL.md passavam pelo gate sem erro.

É o mesmo problema que as regras em markdown já tiveram (duas cópias de 728
linhas, resolvido com um ponteiro), agora em Python. A solução é a mesma:
uma fonte, importada pelos dois.

Ao adicionar padrão aqui, os dois scripts passam a enxergá-lo no mesmo commit.

Fonte canônica das REGRAS (não deste arquivo):
    skills/curadoria-review/references/regras-editoriais.md
Quando este arquivo divergir daquele documento, o documento está certo.
"""

# ---------------------------------------------------------------------------
# §1 / §2.2 — alegação de experiência física direta.
# União das duas listas que existiam + as frases da regra 1 do SKILL.md que
# não estavam em script nenhum ("comprovamos", "colocamos à prova",
# "na nossa bancada", "testado por nós", "em nosso teste" no singular).
# ---------------------------------------------------------------------------
PADROES_TESTE_FISICO = [
    # --- verbos de teste em 1ª pessoa do plural
    r"\btestamos\b",
    r"\btestei\b",
    # NÃO incluir r"\btestou\b" solto: pega teste de TERCEIRO ("o fabricante
    # testou", "a Rtings testou"), que §3.4 permite citar com atribuição.
    # A alegação indevida é sempre em 1ª pessoa — coberta pelos padrões acima.
    r"\bcomprovamos\b",                      # regra 1 — não estava em script algum
    r"\bmedimos\b",
    r"\bcronometramos\b",
    r"\bavaliamos (?:fisicamente|em m[ãa]os)\b",

    # --- "nosso teste" em todas as flexões (o gate só tinha o plural)
    r"\bem nossos? testes?\b",
    r"\bnos nossos testes\b",
    r"\bno nosso laborat[óo]rio\b",
    r"\bna nossa bancada\b",                 # só existia no corrigir_artigos
    r"\bnossa bancada\b",
    r"\bnossa unidade\b",
    r"\bo aparelho que recebemos\b",

    # --- voz passiva / perifrástica
    r"\btestado(?:s|a|as)? (?:por n[óo]s|em nossa|em nosso)\b",
    r"\bcolocamos [àa] prova\b",             # só existia no corrigir_artigos
    r"\bp[uô]semos [àa] prova\b",
    r"\bteste de \w+ (?:que fizemos|nosso)\b",

    # --- uso prolongado
    r"\busamos (?:o|a|por) \w+ (?:durante|por)\b",
    r"\busei (?:o|a|por)\b",
    r"\bdepois de (?:usar|testar)\b",
    r"\bap[óo]s (?:semanas|dias|meses) de uso\b",
    r"\bap[óo]s \d+ (?:dias|semanas|meses) de uso\b",

    # --- contato físico / sensorial
    r"\bdesempacotamos\b",
    r"\bunboxing\b",
    r"\bseguramos\b",
    r"\bsentimos na m[ãa]o\b",
    r"\bao pegar (?:o|a) \w+ (?:na m[ãa]o|em m[ãa]os)\b",
]

# ---------------------------------------------------------------------------
# §11 — enchimento e vocabulário genérico de IA.
#
# Os 14 primeiros são os que já existiam em checar_conformidade.py.
# Os demais são a adaptação PT-BR do ai-writing-detox
# (jamditis/claude-skills-journalism, CC BY 4.0) — a lista em inglês original
# não serve, "delve"/"realm"/"tapestry" não ocorrem em texto PT-BR.
#
# NÍVEL: sempre ALERTA, nunca ERRO. Estilo não bloqueia publicação — só
# veracidade e transparência bloqueiam (§15).
# ---------------------------------------------------------------------------
PADROES_ENCHIMENTO = [
    # --- originais
    r"\bno mundo de hoje\b",
    r"\bnos dias de hoje\b",
    r"\bna era digital\b",
    r"\bneste artigo\b",
    r"\bvamos explorar\b",
    r"\bsem d[úu]vida alguma\b",
    r"\bvale ressaltar que\b",
    r"\b[ée] importante lembrar que\b",
    r"\bquando se trata de\b",
    r"\bem resumo,\b",
    r"\bem suma,\b",
    r"\brevolucion[áa]rio\b",
    r"\bincr[íi]vel experi[êe]ncia\b",
    r"\bsimplesmente perfeito\b",

    # --- ai-writing-detox, adaptado para PT-BR
    r"\bmergulh(?:ar|e|ando) fundo\b",
    r"\bvamos (?:mergulhar|falar sobre)\b",
    r"\brobusto\b",
    r"\bintegra[çc][ãa]o perfeita\b",
    r"\bperfeita integra[çc][ãa]o\b",
    r"\becossistema\b",
    r"\bde ponta\b",
    r"\bdivisor de [áa]guas\b",
    r"\bpotencializ(?:a|ar|ando)\b",
    r"\balavanc(?:a|ar|ando)\b",
    r"\bno final das contas\b",
    r"\bem termos de\b",
    r"\bvale mencionar\b",
    r"\btransformador(?:a)?\b",
    r"\babrangente\b",
    r"\binovador(?:a)?\b",
    r"\bexperi[êe]ncia [úu]nica\b",
    r"\bsolu[çc][ãa]o completa\b",
    r"\bdito isso,\b",
    r"\bem [úu]ltima an[áa]lise\b",
]

# ---------------------------------------------------------------------------
# §6 — "compradores verificados" só com selo explícito da plataforma.
# Usado para impedir que o próprio texto de remediação introduza a violação.
# ---------------------------------------------------------------------------
PADROES_PROVA_SOCIAL_INDEVIDA = [
    r"\bcompradores verificados\b",
    r"\bcompras verificadas\b",
    r"\bavalia[çc][õo]es verificadas\b",
    r"\banalisamos milhares\b",
]
