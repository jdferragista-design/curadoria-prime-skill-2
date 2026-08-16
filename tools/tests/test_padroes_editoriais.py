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
