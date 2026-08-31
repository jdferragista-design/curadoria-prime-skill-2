#!/usr/bin/env python3
"""Reorganizacao estrutural do tablet-infantil para a ordem/visual canonicos.

Ordem alvo (= melhores-techs aprovado):
transparencia -> hero -> imagem -> prova social -> indice -> intro -> tipo de analise ->
metodologia -> resposta rapida -> tabela -> produtos (3) -> controle parental ->
idade -> para quem NAO -> quando comprar -> FAQ -> REGUA (movida p/ pos-FAQ) ->
veredito (+ box 💡) -> onde comprar -> fontes -> ultima atualizacao (novo) ->
byline (movida p/ o fim) -> aviso -> JSON-LD.

Visual: hero escurecido (#9B2226->#5C1013), indice padrao golden (setas roxas 2 col),
FAQ em cards roxos, resumo do veredito em box 💡 verde, remove box 'Tipo de analise'
duplicado do topo, adiciona fecho wp:html faltante da regua e box 'Ultima atualizacao'.
"""

from pathlib import Path

P = Path(__file__).resolve().parent.parent / "articles/html_output" \
    / "tablet-infantil-dia-das-criancas-2026-3-melhores.html"

lines = P.read_text(encoding="utf-8").split("\n")


def seg(a: int, b: int) -> str:
    chunk = "\n".join(lines[a - 1:b])
    assert chunk.strip(), f"segmento {a}-{b} vazio"
    return chunk


def expect(n: int, needle: str) -> None:
    assert needle in lines[n - 1], f"linha {n} nao contem {needle!r}"


# --- sanidade nos limites (1-based) ---
for n, needle in [
    (12, "<!-- wp:html -->"), (14, "Tipo de análise"), (25, "<!-- /wp:html -->"),
    (27, "<!-- wp:html -->"), (32, "<!-- /wp:html -->"),
    (34, "<!-- wp:html -->"), (38, "<!-- /wp:html -->"),
    (40, "<!-- wp:html -->"), (49, "<!-- /wp:html -->"),
    (51, "<!-- wp:html -->"), (55, "<!-- /wp:html -->"),
    (57, "<!-- wp:html -->"), (76, "<!-- /wp:html -->"),
    (78, "<!-- wp:html -->"), (94, "<!-- /wp:html -->"),
    (96, "<!-- wp:html -->"), (150, "</div>"),
    (152, "<!-- wp:paragraph -->"), (157, "<!-- wp:html -->"),
    (163, "<!-- wp:heading -->"), (167, "<!-- wp:html -->"),
    (184, "<!-- wp:heading -->"), (188, "<!-- wp:html -->"),
    (214, "<!-- wp:heading -->"), (222, "<!-- wp:html -->"),
    (244, "<!-- wp:heading -->"), (252, "<!-- wp:html -->"),
    (272, "<!-- wp:heading -->"), (280, "<!-- wp:heading -->"),
    (284, "<!-- wp:html -->"), (308, "<!-- wp:heading -->"),
    (312, "<!-- wp:html -->"), (326, "<!-- wp:heading -->"),
    (330, "<!-- wp:html -->"), (341, "<!-- wp:heading -->"),
    (349, "<!-- wp:heading -->"), (353, "<!-- wp:html -->"),
    (382, "<!-- wp:heading -->"), (386, "<!-- wp:html -->"),
    (406, "<!-- wp:paragraph -->"), (410, "<!-- wp:html -->"),
    (458, "<!-- /wp:html -->"), (460, "<!-- wp:html -->"),
    (472, "<!-- /wp:html -->"), (474, "<!-- wp:html -->"),
    (478, "<!-- /wp:html -->"), (480, "<!-- wp:html -->"),
    (638, "<!-- /wp:html -->"),
]:
    expect(n, needle)

head = seg(1, 11)

hero = seg(12, 25).replace(
    '<p style="background:#fffbeb;border:1px solid #fde68a;border-radius:10px;padding:16px 20px;margin:24px 0;font-size:13px;color:#78350f;line-height:1.7;"><strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou esta unidade fisicamente.</p>',
    "", 1,
)
assert "Tipo de análise" not in hero

heroimg = seg(26, 32)
metod = seg(33, 39)
byline = seg(40, 49)
tipo2 = seg(50, 55)
prova = seg(56, 76)
regua = seg(95, 150) + "\n<!-- /wp:html -->"
intro = seg(151, 155)
transp = seg(156, 161)
rr = seg(162, 182)
tab = seg(183, 212)
prod = seg(213, 278)
ctrl = seg(279, 306)
idade = seg(307, 324)
pqn = seg(325, 339)
qcompra = seg(340, 347)
faq = seg(348, 380)
veredito_h2_grid = seg(381, 404)
resumo = seg(405, 408)
onde_comprar = seg(409, 458)
fontes = seg(459, 472)
aviso = seg(473, 478)
jsonld = seg(479, len(lines))

# --- indice padrao golden (setas roxas, card branco, 2 colunas) ---
ITENS = [
    ("#resposta-rapida", "Resposta rápida"),
    ("#tabela", "Tabela comparativa"),
    ("#multikid", "Multi Kid Pad NB425 Laranja (7,0/10)"),
    ("#taba9kids", "Galaxy Tab A9 + Samsung Kids (8,5/10)"),
    ("#vision7", "Positivo Vision Tab 7 Minions (8,5/10)"),
    ("#controle", "Controle parental comparado"),
    ("#idade", "Qual tablet para cada idade?"),
    ("#quando-comprar", "Quando comprar barato"),
    ("#faq", "Perguntas frequentes"),
    ("#veredito", "Veredito final"),
]
lis = "\n".join(
    f'<li><span style="color: #5a4fcf; font-weight: 800;">▸</span> '
    f'<a href="{h}" rel="noopener" style="color: #4a4a68; text-decoration: none;">{t}</a></li>'
    for h, t in ITENS
)
indice_new = (
    '<!-- wp:html -->\n'
    '<div style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">\n'
    '<p style="font-size: 14px; font-weight: bold; color: #1a1a2e; margin: 0 0 12px; text-transform: uppercase; letter-spacing: .06em;">📑 Índice do conteúdo:</p>\n'
    '<ul style="margin: 0; padding-left: 20px; line-height: 2; columns: 2;">\n'
    f"{lis}\n"
    '</ul>\n'
    '</div>\n'
    '<!-- /wp:html -->'
)

# --- FAQ em cards roxos golden ---
faq_new = faq.replace(
    '<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px 20px; margin-bottom: 12px;">',
    '<div style="background: #fff; border-radius: 12px; margin-bottom: 10px; border: 1px solid #e2e2f0; overflow: hidden; box-shadow: 0 2px 8px rgba(90,79,207,.07);">',
).replace(
    '<p style="margin: 0 0 8px; font-weight: 700; font-size: 14.5px;">',
    '<p style="padding: 16px 20px; font-size: 15px; font-weight: bold; color: #5a4fcf; margin: 0; border-bottom: 1px solid #e2e2f0;">',
).replace(
    '<p style="margin: 0; font-size: 14px; line-height: 1.65;">',
    '<p style="padding: 14px 20px; color: #4a4a68; font-size: 15px; margin: 0; line-height: 1.7;">',
)

# --- resumo do veredito em box 💡 verde ---
m = resumo.replace("<!-- wp:paragraph -->", "").replace("<!-- /wp:paragraph -->", "").strip()
inner = m[len("<p>"):-len("</p>")] if m.startswith("<p>") and m.endswith("</p>") else m
veredito_box = (
    '<!-- wp:html -->\n'
    '<div style="background: #f0fdf4; border-left: 4px solid #22c55e; border-radius: 8px; padding: 16px 20px; margin-bottom: 24px;">\n'
    '<p style="font-size: 15px; font-weight: bold; color: #14532d; margin: 0 0 8px;">💡 Veredito:</p>\n'
    f'<p style="color: #166534; font-size: 14.5px; margin: 0; line-height: 1.7;">{inner}</p>\n'
    '</div>\n'
    '<!-- /wp:html -->'
)

ultima = (
    '<!-- wp:html -->\n'
    '<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 16px 20px; margin-bottom: 24px; font-size: 13px; color: #78350f; line-height: 1.7;">\n'
    '<strong>📌 Última atualização:</strong> 25/08/2026 | <strong>Produtos em análise:</strong> 3 tablets infantis para o Dia das Crianças<br>\n'
    '<strong>⚠️ Aviso:</strong> Os preços mencionados foram verificados em <strong>08/08/2026</strong> e re-verificados em <strong>25/08/2026</strong>. Sempre confirme os valores atualizados nas lojas antes de comprar.\n'
    '</div>\n'
    '<!-- /wp:html -->'
)

hero = hero.replace(
    'linear-gradient(135deg,#FF6B6B 0%,#9B2226 100%); color: #fff; padding: 28px 30px;',
    'linear-gradient(135deg,#9B2226 0%,#5C1013 100%); color: #fff; padding: 28px 30px;',
    1,
)
assert "#5C1013" in hero

body = "\n\n".join([
    transp, hero, heroimg, prova, indice_new, intro, tipo2, metod, rr, tab,
    prod, ctrl, idade, pqn, qcompra, faq_new, regua,
    veredito_h2_grid, veredito_box, onde_comprar, fontes, ultima, byline,
    aviso, jsonld,
])

out = head + "\n" + body + "\n" + lines[-2] + "\n" + lines[-1] + "\n"
P.write_text(out, encoding="utf-8")
print("OK: reorganizado — ordem canonica + visual golden aplicados")