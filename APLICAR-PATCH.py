#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# =============================================================================
#  APLICAR-PATCH.py - patch autoextraivel, arquivo UNICO, texto puro.
#
#  Texto puro de proposito: zip binario se corrompe no transporte entre chats.
#  Este arquivo le a si mesmo e escreve os 2 arquivos do patch.
#
#  USO - a partir da RAIZ do repo curadoria-prime-skill-2:
#
#      python3 APLICAR-PATCH.py
#      cd tools && python3 -m unittest discover tests -v
#
#  Nao altera regra editorial nenhuma. Nao precisa de rede, credencial,
#  WordPress nem dependencia externa. Faz backup .bak se o arquivo ja existir
#  com conteudo diferente.
#
#  Depois disso faca as edicoes manuais dos passos 2, 3a, 3b e 3c do
#  COMO-APLICAR.md. Sem elas, 2 dos 10 testes falham DE PROPOSITO: sao os
#  bugs reais de §16 (AUTOR_CANONICO) e §6 (BLOCO_DIVULGACAO) no codigo atual.
# =============================================================================
import sys
from pathlib import Path

MARCA_INI = "#>>>>>ARQUIVO:"
MARCA_FIM = "#<<<<<FIM"


def extrair():
    linhas = Path(__file__).read_text(encoding="utf-8").splitlines(keepends=True)
    arquivos, atual, buf = {}, None, []
    for ln in linhas:
        if ln.startswith(MARCA_INI):
            atual = ln[len(MARCA_INI):].strip()
            buf = []
        elif ln.startswith(MARCA_FIM):
            if atual:
                arquivos[atual] = "".join(buf)
            atual = None
        elif atual is not None:
            buf.append(ln)
    return arquivos


def main():
    raiz = Path(".").resolve()
    if not (raiz / "tools").is_dir():
        print("!! Rode a partir da RAIZ do repo (a pasta que contem tools/).")
        print("   Diretorio atual:", raiz)
        return 1

    arquivos = extrair()
    if len(arquivos) != 2:
        print(f"!! Esperava 2 arquivos embutidos, encontrei {len(arquivos)}.")
        print("   O arquivo pode ter se corrompido no transporte.")
        return 1

    for destino, conteudo in arquivos.items():
        alvo = raiz / destino
        alvo.parent.mkdir(parents=True, exist_ok=True)
        if alvo.exists():
            antigo = alvo.read_text(encoding="utf-8")
            if antigo == conteudo:
                print(f"  = {destino} (ja identico)")
                continue
            bkp = alvo.with_suffix(alvo.suffix + ".bak")
            bkp.write_text(antigo, encoding="utf-8")
            print(f"  backup -> {bkp.relative_to(raiz)}")
        alvo.write_text(conteudo, encoding="utf-8")
        print(f"  + {destino}  ({len(conteudo)} bytes)")

    print()
    print("Proximo passo:")
    print("    cd tools && python3 -m unittest discover tests -v")
    print()
    print("Esperado AGORA: 8 passam, 2 falham (§16 e §6).")
    print("Essas 2 falhas sao os bugs reais do repo, nao erro do patch.")
    print("Aplique os passos 2, 3a, 3b, 3c do COMO-APLICAR.md -> 10/10.")
    return 0


if __name__ == "__main__":
    sys.exit(main())

# =============================================================================
#  CONTEUDO EMBUTIDO - nao edite abaixo desta linha
# =============================================================================
#>>>>>ARQUIVO:tools/padroes_editoriais.py
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
#<<<<<FIM
#>>>>>ARQUIVO:tools/tests/test_padroes_editoriais.py
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
test_padroes_editoriais.py — trava de regressão da fonte única de padrões.

Roda com a stdlib, sem dependência externa, sem rede, sem WordPress:

    cd tools && python3 -m unittest discover tests -v

Dois compromissos que estes testes protegem:

  1. Toda frase vetada pela regra 1 do SKILL.md é PEGA pelo gate.
     (Antes do patch, 6 de 7 passavam.)
  2. Nenhum texto legítimo do site é pego.
     Em especial a RESSALVA correta ("não testamos") e o teste de TERCEIRO
     com atribuição, que §3.4 permite. Falso positivo aqui é pior que
     falso negativo: treina o editor a ignorar o gate.
"""

import os
import re
import sys
import unittest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from padroes_editoriais import (  # noqa: E402
    PADROES_TESTE_FISICO,
    PADROES_ENCHIMENTO,
    PADROES_PROVA_SOCIAL_INDEVIDA,
)

try:
    import checar_conformidade as C
    TEM_GATE = True
except ImportError:  # permite rodar os testes de padrão isoladamente
    TEM_GATE = False


def casa(frase, padroes):
    return any(re.search(p, frase, re.I) for p in padroes)


# ---------------------------------------------------------------- §1 / §2.2

class TestTesteFisicoPega(unittest.TestCase):
    """Frases vetadas pela regra 1 — todas devem ser pegas."""

    VETADAS = [
        "Testamos a fundo este produto.",
        "Testei o aparelho por duas semanas.",
        "Comprovamos a autonomia anunciada.",
        "Medimos o brilho da tela.",
        "Cronometramos o tempo de carga.",
        "Em nosso teste, o brilho superou o rival.",
        "Em nossos testes, o som ficou limpo.",
        "Nos nossos testes a bateria durou mais.",
        "No nosso laboratório, o resultado foi outro.",
        "Na nossa bancada, o som encheu a sala.",
        "Nossa unidade veio com defeito.",
        "O aparelho que recebemos tinha risco na tela.",
        "O produto foi testado por nós durante uma semana.",
        "Colocamos à prova o cancelamento de ruído.",
        "Usamos o fone durante um mês inteiro.",
        "Usei o tablet por duas semanas.",
        "Depois de usar, notamos o aquecimento.",
        "Após semanas de uso, a bateria degradou.",
        "Após 3 dias de uso, a bateria caiu.",
        "Desempacotamos a caixa com cuidado.",
        "O unboxing revelou os acessórios.",
        "Seguramos o aparelho e pareceu leve.",
        "Sentimos na mão o acabamento premium.",
    ]

    def test_todas_vetadas_sao_pegas(self):
        for frase in self.VETADAS:
            with self.subTest(frase=frase):
                self.assertTrue(
                    casa(frase, PADROES_TESTE_FISICO),
                    f"regra 1 veta mas o padrão não pega: {frase!r}",
                )


class TestTesteFisicoNaoPega(unittest.TestCase):
    """Texto legítimo — nenhum pode ser pego (direto ou via lógica do gate)."""

    LEGITIMAS = [
        "A Curadoria Prime não testou esta unidade fisicamente.",
        "Não realizamos testes físicos deste aparelho.",
        "Não recebemos o produto do fabricante.",
        "Sem teste físico, avaliamos apenas a ficha técnica.",
        "Análise baseada em especificações oficiais e relatos publicados.",
        "Tipo de análise: pesquisa editorial baseada em especificações oficiais.",
        "Preço verificado na Amazon em 14/08/2026, sujeito a alteração.",
        "Este artigo contém links de afiliado.",
        "Veredito por perfil: quem não deve comprar.",
        "Fontes consultadas: ficha oficial do fabricante.",
    ]

    # §3.4 — teste de TERCEIRO com atribuição é permitido e deve passar.
    DE_TERCEIRO = [
        "O fabricante testou o produto em laboratório próprio.",
        "A Rtings testou o brilho e mediu 1.400 nits.",
        "Segundo a DxOMark, a câmera foi testada em condições controladas.",
    ]

    @unittest.skipUnless(TEM_GATE, "checar_conformidade.py não disponível")
    def test_ressalva_correta_nao_e_erro(self):
        C.PADROES_TESTE_FISICO = PADROES_TESTE_FISICO
        for frase in self.LEGITIMAS:
            with self.subTest(frase=frase):
                achados = C.checar_teste_fisico(f"<p>{frase}</p>")
                erros = [a for a in achados if a["nivel"] == "ERRO"]
                self.assertEqual(
                    erros, [], f"falso positivo em texto legítimo: {frase!r}"
                )

    @unittest.skipUnless(TEM_GATE, "checar_conformidade.py não disponível")
    def test_teste_de_terceiro_e_permitido(self):
        C.PADROES_TESTE_FISICO = PADROES_TESTE_FISICO
        for frase in self.DE_TERCEIRO:
            with self.subTest(frase=frase):
                achados = C.checar_teste_fisico(f"<p>{frase}</p>")
                erros = [a for a in achados if a["nivel"] == "ERRO"]
                self.assertEqual(
                    erros, [], f"§3.4 permite teste de terceiro: {frase!r}"
                )


class TestNaoRegredirParaListasDivergentes(unittest.TestCase):
    """
    Os padrões que existiam SÓ em corrigir_artigos.py precisam continuar aqui.
    Se alguém recriar a divergência, este teste quebra.
    """

    ORFAOS = [
        "Na nossa bancada, o som encheu a sala.",
        "Colocamos à prova o cancelamento de ruído.",
        "O produto foi testado por nós durante uma semana.",
        "Após 3 dias de uso, a bateria caiu.",
        "Nos nossos testes a bateria durou mais.",
    ]

    def test_padroes_orfaos_presentes(self):
        for frase in self.ORFAOS:
            with self.subTest(frase=frase):
                self.assertTrue(casa(frase, PADROES_TESTE_FISICO))


# ------------------------------------------------------------------- §11

class TestEnchimento(unittest.TestCase):
    """Vocabulário genérico de IA — ALERTA, nunca ERRO."""

    GENERICAS = [
        "Vamos mergulhar fundo nos detalhes.",
        "Um som robusto para a sala.",
        "Integração perfeita com o ecossistema.",
        "Tecnologia de ponta neste modelo.",
        "Este produto é um divisor de águas.",
        "Vai potencializar sua experiência.",
        "Você pode alavancar todo o potencial.",
        "No final das contas, vale o preço.",
        "Em termos de áudio, ele entrega.",
        "Vale mencionar que o controle é simples.",
        "Uma experiência transformadora de som.",
        "Uma análise abrangente do aparelho.",
        "Um design inovador e moderno.",
        "No mundo de hoje, som importa.",
        "Na era digital, todo mundo assiste em casa.",
    ]

    LEGITIMAS = [
        "A Curadoria Prime não testou esta unidade fisicamente.",
        "Preço verificado na Amazon em 14/08/2026.",
        "Análise baseada em especificações oficiais.",
        "Veredito por perfil: quem não deve comprar.",
    ]

    def test_genericas_sao_detectadas(self):
        for frase in self.GENERICAS:
            with self.subTest(frase=frase):
                self.assertTrue(casa(frase, PADROES_ENCHIMENTO), frase)

    def test_legitimas_nao_sao_detectadas(self):
        for frase in self.LEGITIMAS:
            with self.subTest(frase=frase):
                self.assertFalse(casa(frase, PADROES_ENCHIMENTO), frase)

    @unittest.skipUnless(TEM_GATE, "checar_conformidade.py não disponível")
    def test_enchimento_nunca_bloqueia(self):
        """Estilo é ALERTA. Só veracidade e transparência bloqueiam (§15)."""
        C.PADROES_ENCHIMENTO = PADROES_ENCHIMENTO
        html = "<p>" + " ".join(self.GENERICAS) + "</p>"
        achados = C.checar_enchimento(html)
        self.assertEqual([a for a in achados if a["nivel"] == "ERRO"], [])
        self.assertTrue(any(a["nivel"] == "ALERTA" for a in achados))


# -------------------------------------------------------------------- §6

class TestProvaSocialIndevida(unittest.TestCase):
    """§6 — 'compradores verificados' sem selo explícito da plataforma."""

    def test_pega_expressao_vetada(self):
        self.assertTrue(
            casa("dados de compradores verificados", PADROES_PROVA_SOCIAL_INDEVIDA)
        )
        self.assertTrue(
            casa("analisamos milhares de avaliações", PADROES_PROVA_SOCIAL_INDEVIDA)
        )

    def test_bloco_divulgacao_do_projeto_esta_limpo(self):
        """
        Trava o bug real: o BLOCO_DIVULGACAO de corrigir_artigos.py continha
        'compradores verificados', violando §6 nos 10 artigos onde seria
        injetado. Este teste falha se a expressão voltar.
        """
        try:
            import corrigir_artigos as R
        except (ImportError, SystemExit):
            self.skipTest("corrigir_artigos.py não importável neste ambiente")
        self.assertFalse(
            casa(R.BLOCO_DIVULGACAO, PADROES_PROVA_SOCIAL_INDEVIDA),
            "BLOCO_DIVULGACAO viola §6 — remova 'compradores verificados'",
        )

    def test_autor_canonico_nao_e_pessoa(self):
        """
        §16 — a assinatura é do humano que aprovou, definida no momento da
        aprovação. O script não pode carimbar um nome fixo.
        """
        try:
            import corrigir_artigos as R
        except (ImportError, SystemExit):
            self.skipTest("corrigir_artigos.py não importável neste ambiente")
        self.assertNotEqual(
            getattr(R, "AUTOR_CANONICO", None),
            "Cristiano Martins",
            "§16 proíbe atribuir o artigo a uma pessoa fixa",
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
#<<<<<FIM
