#!/usr/bin/env python3
"""Patch tablet-infantil 25/08/2026 (parte 3) — captura Amazon do Positivo Vision Tab 7 Minions.

Dados reais: Amazon R$ 409,52 Pix/NuPay (de R$ 626,92) / R$ 455,04 em 9x R$ 50,56;
kit Amazon inclui SO CAPA (sem mochila); loja oficial Positivo; Escolha da Amazon;
4,1/5 · 38 classificacoes globais (19 BR visiveis). URL da captura: link.amazon/B0cJleAj2.
Regra da casa: 'Escolha da Amazon' nao e prova de qualidade — nao entra como selo.
"""

from pathlib import Path

P = Path(__file__).resolve().parent.parent / "articles/html_output" \
    / "tablet-infantil-dia-das-criancas-2026-3-melhores.html"

REPL = [
    # A1 — badge faixa de preco
    ('💰 De R$ 571 a R$ 1.124',
     '💰 De R$ 409 a R$ 1.124'),

    # A2 — hero: preco do Vision (Amazon e o menor preco; kit so capa)
    ('<strong style="color:#FFDAB9;">Positivo Vision Tab 7</strong> (7" Android 14 Go + capa e mochila, a partir de R$ 571,12 no Pix)',
     '<strong style="color:#FFDAB9;">Positivo Vision Tab 7</strong> (7" Android 14 Go com capa, a partir de R$ 409,52 na Amazon)'),

    # A3 — resposta rapida (card Vision): menor preco e na Amazon (kit so capa)
    ('<strong>Positivo Vision Tab 7 Minions</strong> (a partir de <strong>R$ 571,12</strong> no Pix, ML): 7" IPS, Android 14 Go, 3GB/64GB, controle parental, capa temática + mochila. Ressalva: relatos de bateria curta (~2–3h). Ideal para 3 a 6 anos como primeiro tablet.',
     '<strong>Positivo Vision Tab 7 Minions</strong> (a partir de <strong>R$ 409,52</strong> na Amazon): 7" IPS, Android 14 Go, 3GB/64GB, controle parental e capa inclusa — no Mercado Livre, capa + mochila por R$ 571,12. Ressalva: relatos de bateria curta (~2–3h) e tela frágil em quedas. Ideal para 3 a 6 anos como primeiro tablet.'),

    # A4 — tabela: preco Vision
    ('<td style="padding: 11px 14px; text-align: center;"><strong>R$ 571,12</strong> (Pix, ML)</td></tr>',
     '<td style="padding: 11px 14px; text-align: center;"><strong>R$ 409,52</strong> (Pix, Amz)</td></tr>'),

    # A5 — card avaliacao Vision: ML + Amazon reais
    ('<strong style="color: #3485DB;">Mercado Livre — Positivo Vision Tab 7 Minions</strong><br>⭐ <strong>4,7/5</strong> · <strong>~1.196 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO<br><span style="color:#475569;">Elogiado por custo-benefício, design e resistência; relatos de bateria curta (~2–3h), leve aquecimento e câmera fraca.</span>',
     '<strong style="color: #3485DB;">Positivo Vision Tab 7 Minions</strong><br>ML: ⭐ <strong>4,7/5</strong> · <strong>~1.196 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO<br>Amazon: ⭐ <strong>4,1/5</strong> · <strong>38 classificações globais</strong> (19 no Brasil)<br><span style="color:#475569;">Elogios: custo-benefício, design e resistência; críticas: bateria curta (~2–3h), leve aquecimento, câmera fraca e tela frágil em quedas.</span>'),

    # A6 — secao Vision: kit varia por loja
    ('Vem com <strong>capa temática dos Minions + mochila de proteção</strong> inclusas. Ressalvas dos compradores: bateria dura ~2–3h de uso contínuo, esquenta um pouco nas primeiras horas e o Android Go limita a instalação de alguns apps.',
     'O kit varia por loja: na Amazon vem com <strong>capa personalizada</strong>; no Mercado Livre, <strong>capa + mochila</strong>. Ressalvas dos compradores: bateria dura ~2–3h de uso contínuo, esquenta um pouco nas primeiras horas, câmera fraca e o Android Go limita a instalação de alguns apps.'),

    # A7 — card compra Vision: titulo/preco
    ('Positivo Vision Tab 7 Minions <span style="font-weight: 400; color: #888; font-size: 14px;">7" 3GB/64GB | R$ 571,12 (Pix) · R$ 581,12 outros</span>',
     'Positivo Vision Tab 7 Minions <span style="font-weight: 400; color: #888; font-size: 14px;">7" 3GB/64GB | R$ 409,52 (Amazon) · R$ 571,12 (Pix, ML)</span>'),

    # A8 — card compra Vision: nota
    ('<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. O mais barato do comparativo, com capa Minions + mochila inclusas. Ressalvas: bateria curta (~2–3h), câmera fraca e Android Go limita apps.</p>',
     '<p style="font-size: 14px; color: #666; margin: 0 0 14px 0;">Nota 8,5/10. O mais barato do comparativo. O kit varia por loja: na Amazon inclui só a capa (R$ 409,52); no Mercado Livre, capa + mochila (R$ 571,12). Ressalvas: bateria curta (~2–3h), câmera fraca e Android Go limita apps.</p>'),

    # A9 — card compra Vision: botao Amazon com URL real da captura
    ('<a style="background: linear-gradient(135deg, #ff9900 0%, #ff8500 100%); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://link.amazon/B033mQFUv" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver na Amazon</a>',
     '<a style="background: linear-gradient(135deg, #ff9900 0%, #ff8500 100%); color: white; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://link.amazon/B0cJleAj2" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver na Amazon · R$ 409,52</a>'),

    # A10 — card compra Vision: botao ML com preco
    ('<a style="background: linear-gradient(135deg, #9B2226 0%, #7a1a1e 100%); color: #fff; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://meli.la/2qiYYZt" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver no Mercado Livre</a>',
     '<a style="background: linear-gradient(135deg, #9B2226 0%, #7a1a1e 100%); color: #fff; text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;" href="https://meli.la/2qiYYZt" target="_blank" rel="sponsored noopener noreferrer">🛍️ Ver no Mercado Livre · capa + mochila</a>'),

    # A11 — resumo final: preco do Vision nas duas lojas
    ('<strong>Primeiro tablet barato</strong> → <strong>Positivo Vision Tab 7 Minions (R$ 571,12 no Pix, capa e mochila inclusas)</strong>, com bateria curta nos relatos. Nenhum é compra errada',
     '<strong>Primeiro tablet barato</strong> → <strong>Positivo Vision Tab 7 Minions — R$ 409,52 na Amazon (só capa) ou R$ 571,12 no ML (capa + mochila)</strong>, com bateria curta nos relatos. Nenhum é compra errada'),

    # A12 — fontes: precos do Vision nas duas lojas
    ('Vision Tab 7: ML R$ 571,12 no Pix).</li>',
     'Vision Tab 7: Amazon R$ 409,52 no Pix (só capa) · ML R$ 571,12 com capa e mochila).</li>'),

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