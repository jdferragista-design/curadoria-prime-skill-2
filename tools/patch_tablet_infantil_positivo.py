#!/usr/bin/env python3
"""Patch tablet-infantil 25/08/2026 (parte 2) — captura real do editor p/ Positivo Vision Tab 7 Minions.

Dados reais: ML 4,7/5 · 1.196 opinioes · MAIS VENDIDO (9o Tablets Positivo);
R$ 571,12 Pix (de R$ 629, 9% OFF) / R$ 581,12 outros meios / 10x R$ 58,11.
Inclui capa + mochila. Resolve o conflito R$ 383 vs R$ 499 (ambos errados).
Remove o "+18 mil avaliacoes" do hero (real: ~2.700 somadas).
"""

from pathlib import Path

P = Path(__file__).resolve().parent.parent / "articles/html_output" \
    / "tablet-infantil-dia-das-criancas-2026-3-melhores.html"

REPL = [
    # V1 — hero: preco do Vision
    ('<strong style="color:#FFDAB9;">Positivo Vision Tab 7</strong> (7" Android 14 Go, a partir de R$ 383)',
     '<strong style="color:#FFDAB9;">Positivo Vision Tab 7</strong> (7" Android 14 Go + capa e mochila, a partir de R$ 571,12 no Pix)'),

    # V2 — hero: remove "+18 mil avaliacoes" (real: ~2.700 somadas)
    ('Analisamos <strong>especificações oficiais, controle parental (Samsung Kids vs Google Family Link) e +18 mil avaliações de pais</strong> para você presentear com segurança.',
     'Analisamos <strong>especificações oficiais, controle parental (Samsung Kids vs Google Family Link) e quase 2.700 avaliações somadas nas lojas</strong> para você presentear com segurança.'),

    # V3 — badge faixa de preco
    ('💰 De R$ 499 a R$ 1.124',
     '💰 De R$ 571 a R$ 1.124'),

    # V4 — badge verificado
    ('🕒 Verificado: 08/08/2026 · Kid Pad e Tab A9: 25/08',
     '🕒 Verificado: 08/08/2026 · re-verificado: 25/08'),

    # V5 — titulo do box de avaliacoes
    ('(dados coletados em 08/08/2026 · Kid Pad e Tab A9 reavaliados em 25/08/2026)</span></p>',
     '(dados coletados em 08/08/2026 · os 3 SKUs reavaliados em 25/08/2026)</span></p>'),

    # V6 — card de avaliacao do Positivo (dados reais ML)
    ('<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #3485DB;">Amazon — Positivo Vision Tab 7</strong><br>⭐ <strong>4,6/5</strong> · <strong>~640 avaliações</strong> · <strong>Android 14 Go</strong><br><span style="color:#475569;">Nota alta com a menor base de avaliações — leia os relatos recentes antes de decidir.</span>\n'
     '</div>',
     '<div style="background: #fff; border: 1px solid #a9cdfa; border-left: 4px solid #3485DB; border-radius: 10px; padding: 14px 16px; font-size: 13.5px;">\n'
     '<strong style="color: #3485DB;">Mercado Livre — Positivo Vision Tab 7 Minions</strong><br>⭐ <strong>4,7/5</strong> · <strong>~1.196 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO<br><span style="color:#475569;">Elogiado por custo-benefício, design e resistência; relatos de bateria curta (~2–3h), leve aquecimento e câmera fraca.</span>\n'
     '</div>'),

    # V7 — comentario ao editor (box avaliacoes)
    ('<!-- NOTA AO EDITOR: Multi Kid Pad (ML 4,4/5 · 129; Amazon 2,9/5 · 24) e Tab A9 (ML 4,9/5 · 1.345) reavaliados em 25/08/2026.\n'
     '     Positivo Vision Tab 7 aguarda recaptura para fechar o ranking. Citação textual só com avaliação real\n'
     '     (nome semi-anonimizado + data + plataforma) confirmada na página do varejo — regra anti-alucinação da casa. -->',
     '<!-- NOTA AO EDITOR: os 3 SKUs foram reavaliados em 25/08/2026 — Kid Pad (ML 4,4/5 · 129; Amazon 2,9/5 · 24),\n'
     '     Tab A9 (ML 4,9/5 · 1.345) e Vision Tab 7 (ML 4,7/5 · 1.196). Citação textual só com avaliação real\n'
     '     (nome semi-anonimizado + data + plataforma) confirmada na página do varejo — regra anti-alucinação da casa. -->'),

    # V8 — resposta rapida (card Vision)
    ('<strong>Positivo Vision Tab 7</strong> (a partir de <strong>R$ 499</strong>): 7" IPS, Android 14 Go, 3GB/64GB, controle parental e capa temática. Ideal para 3 a 6 anos como primeiro tablet.',
     '<strong>Positivo Vision Tab 7 Minions</strong> (a partir de <strong>R$ 571,12</strong> no Pix, ML): 7" IPS, Android 14 Go, 3GB/64GB, controle parental, capa temática + mochila. Ressalva: relatos de bateria curta (~2–3h). Ideal para 3 a 6 anos como primeiro tablet.'),

    # V9 — tabela: preco Vision
    ('<td style="padding: 11px 14px; text-align: center;"><strong>R$ 383</strong></td></tr>',
     '<td style="padding: 11px 14px; text-align: center;"><strong>R$ 571,12</strong> (Pix, ML)</td></tr>'),

    # V10 — paragrafo da secao Vision (frase truncada completada + dados reais)
    ('<p>O <strong>Vision Tab 7</strong> é o "primeiro tablet" ideal para 3 a 6 anos. Leve (241g), Android 14 Go (mais leve e atual que Android 11 dos concorrentes baratos), 3GB/64GB e bateria de 3.100 mAh para o dia. A capa protetora</p>',
     '<p>O <strong>Vision Tab 7</strong> é o "primeiro tablet" ideal para 3 a 6 anos. Leve (241g), Android 14 Go (mais leve e atual que Android 11 dos concorrentes baratos), 3GB/64GB e bateria de 3.100 mAh. Vem com <strong>capa temática dos Minions + mochila de proteção</strong> inclusas. Ressalvas dos compradores: bateria dura ~2–3h de uso contínuo, esquenta um pouco nas primeiras horas e o Android Go limita a instalação de alguns apps.</p>'),

    # V11 — card compra Vision: titulo/preco
    ('Positivo Vision Tab 7 <span style="font-weight: 400; color: #888; font-size: 14px;">7" 3GB/64GB | R$ 499</span>',
     'Positivo Vision Tab 7 Minions <span style="font-weight: 400; color: #888; font-size: 14px;">7" 3GB/64GB | R$ 571,12 (Pix) · R$ 581,12 outros</span>'),

    # V12 — card compra Vision: nota
    ('<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. O mais leve e barato com Android 14 Goideal como primeiro presente — capa Minions que a criança ama.</p>',
     '<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. O mais barato do comparativo, com capa Minions + mochila inclusas. Ressalvas: bateria curta (~2–3h), câmera fraca e Android Go limita apps.</p>'),

    # V13 — resumo final: preco do Vision
    ('<strong>Primeiro tablet barato</strong> → <strong>Positivo Vision Tab 7</strong>. Nenhum é compra errada',
     '<strong>Primeiro tablet barato</strong> → <strong>Positivo Vision Tab 7 Minions (R$ 571,12 no Pix, capa e mochila inclusas)</strong>, com bateria curta nos relatos. Nenhum é compra errada'),

    # V14 — fontes: os 3 SKUs reavaliados
    ('<li>Amazon e Mercado Livre — avaliações coletadas em 08/08/2026; Kid Pad NB425 e Galaxy Tab A9 reavaliados em 25/08/2026 (Kid Pad: ML R$ 856,75 · Amazon R$ 884,44 · Tab A9: ML R$ 1.114 no Pix, Amazon sem estoque do Tab A9).</li>',
     '<li>Amazon e Mercado Livre — avaliações coletadas em 08/08/2026; os 3 SKUs reavaliados em 25/08/2026 (Kid Pad: ML R$ 856,75 · Amazon R$ 884,44 · Tab A9: ML R$ 1.114 no Pix, sem estoque na Amazon · Vision Tab 7: ML R$ 571,12 no Pix).</li>'),

    # V15 — nota ao editor (fontes)
    ('<!-- NOTA AO EDITOR: re-verificar preços/estoque em 10/09/2026 antes de publicar (véspera da Semana da Criança). Kid Pad NB425 e Tab A9 recapturados em 25/08; falta recapturar o Positivo Vision Tab 7 para fechar o ranking final. -->',
     '<!-- NOTA AO EDITOR: re-verificar preços/estoque em 10/09/2026 antes de publicar (véspera da Semana da Criança). Os 3 SKUs foram recapturados em 25/08/2026. -->'),

    # FIM-MARKER
]


def main() -> None:
    text = P.read_text(encoding="utf-8")
    for i, (old, new) in enumerate(REPL, 1):
        n = text.count(old)
        if n != 1:
            raise SystemExit(f"[{i}] old com count={n} (esperado 1):\n{old[:120]!r}")
        text = text.replace(old, new)
    P.write_text(text, encoding="utf-8")
    print(f"OK: {len(REPL)} substituicoes aplicadas em {P.name}")


if __name__ == "__main__":
    main()