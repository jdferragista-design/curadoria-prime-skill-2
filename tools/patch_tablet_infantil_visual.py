#!/usr/bin/env python3
"""Patch 25/08/2026 — padronização visual completa do tablet-infantil (Parte 5).
1) Índice do conteúdo → padrão golden (2 colunas fixas, setas ▸).
2) 'O que dizem as avaliações' → 6 cards (1 por plataforma × 3 produtos), citações reais das capturas.
3) Resposta rápida → 3 blocos lado a lado fixos (cards brancos, borda superior colorida).
4) 'Qual tablet para cada idade?' → mesmo padrão lado a lado.
5) Régua ('Como chegamos às notas' + 'Notas por critério') → bloco de avaliação golden + caixa 🧮; elimina a 'Nota Geral 7,5' órfã.
6) Botões ML → cores oficiais (#2d3277→#1a1f5c, texto #ffe600); botões Amazon ganham sombra padrão."""
import io

F = "articles/html_output/tablet-infantil-dia-das-criancas-2026-3-melhores.html"
s = io.open(F, encoding="utf-8").read()
MARCA_FIM = "<!-- /wp:html -->"


def bloco_contemo(txt, marcador):
    """Retorna (inicio, fim) do bloco <!-- wp:html --> que contém o marcador."""
    i = txt.index(marcador)
    bs = txt.rindex("<!-- wp:html -->", 0, i)
    be = txt.index(MARCA_FIM, i) + len(MARCA_FIM)
    return bs, be


# ── 1) ÍNDICE no padrão golden ──
ITENS = [
    ("#resposta-rapida", "⚡ Resposta rápida"),
    ("#tabela", "📊 Tabela comparativa"),
    ("#multikid", "🟢 1. Multi Kid Pad NB425 (7,0/10)"),
    ("#taba9kids", "🛡️ 2. Galaxy Tab A9 + Kids (8,5/10)"),
    ("#vision7", "💸 3. Vision Tab 7 Minions (8,5/10)"),
    ("#controle", "🔒 Controle parental comparado"),
    ("#idade", "👶 Qual tablet para cada idade?"),
    ("#quando-comprar", "💰 Quando comprar barato"),
    ("#faq", "❓ Perguntas frequentes"),
    ("#veredito", "🏆 Veredito final"),
]


def li(href, rotulo):
    return ('<li><span style="color: #5a4fcf; font-weight: 800;">▸</span> '
            f'<a href="{href}" rel="noopener" style="color: #4a4a68; text-decoration: none;">{rotulo}</a></li>')


col1 = "\n".join(li(h, r) for h, r in ITENS[:5])
col2 = "\n".join(li(h, r) for h, r in ITENS[5:])
INDICE_NOVO = f'''<!-- wp:html -->
<div id="indice-conteudo" style="background: #fff; border: 1px solid #e2e2f0; border-radius: 12px; padding: 18px 22px; margin-bottom: 28px;">
<p style="font-size: 14px; font-weight: bold; color: #1a1a2e; margin: 0 0 12px; text-transform: uppercase; letter-spacing: .06em;">📑 Índice do conteúdo</p>
<div style="display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 0 32px;">
<ul style="margin: 0; padding-left: 8px; line-height: 2; list-style: none;">
{col1}
</ul>
<ul style="margin: 0; padding-left: 8px; line-height: 2; list-style: none;">
{col2}
</ul>
</div>
<style>
  @media (max-width: 782px) {{
    #indice-conteudo > div:nth-child(3) {{ grid-template-columns: 1fr !important; }}
    #indice-conteudo > div:nth-child(3) > ul + ul {{ margin-top: 8px; }}
  }}
</style>
</div>
<!-- /wp:html -->'''

bs, be = bloco_contemo(s, "📑 Índice do conteúdo:")
s = s[:bs] + INDICE_NOVO + s[be:]
print("1) índice golden ok")

# ── 2) AVALIAÇÕES: 6 cards (1 por plataforma × produto), citações reais das capturas ──
CARD = ('<div style="background: #fff; border: 1px solid {bc}; border-left: 4px solid {bl}; '
        'border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;">\n'
        '<strong style="color: {cl};">{titulo}</strong><br>{corpo}\n</div>')
AZUL = dict(bc="#a9cdfa", bl="#3485DB", cl="#3485DB")
LARANJA = dict(bc="#ffd499", bl="#FF9900", cl="#FF9900")

cards_av = []
cards_av.append(CARD.format(**AZUL, titulo="Mercado Livre — Multi Kid Pad NB425 Laranja",
    corpo='<br>⭐ <strong>4,4/5</strong> · <strong>129 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · <strong>R$ 856,75</strong> no Pix<br>'
          '<em>&#8220;Sem travamentos nos jogos de criança e streamers de vídeo rodando liso… Pelo preço foi o melhor custo-benefício.&#8221;</em> '
          '<span style="color:#64748b;">— compra verificada</span><br>'
          '<span style="color:#475569;">Contra-peso nas mesmas opiniões: bateria que para de carregar, superaquecimento e travamentos.</span>'))
cards_av.append(CARD.format(**LARANJA, titulo="Amazon — Multi Kid Pad NB425 Laranja",
    corpo='<br>⭐ <strong>2,9/5</strong> · <strong>24 classificações globais</strong> · <strong>R$ 884,44</strong><br>'
          '<em>&#8220;A tela tem boa resolução e tamanho. A capa protetora é bem resistente. O ponto negativo é que demora muito para iniciar o sistema Android e trava bastante.&#8221;</em> '
          '<span style="color:#64748b;">— Priscila A., compra verificada (jun/2025)</span><br>'
          '<span style="color:#475569;">30% das notas são 1 estrela — maioria por carga/bateria.</span>'))
cards_av.append(CARD.format(**AZUL, titulo="Mercado Livre — Galaxy Tab A9 64GB (Loja oficial Samsung)",
    corpo='<br>⭐ <strong>4,9/5</strong> · <strong>1.345 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO · <strong>R$ 1.114</strong> no Pix<br>'
          '<em>&#8220;Tablet simples, bonita, rápida e com uma qualidade de tela decente. Perfeita para consumir conteúdo multimídia.&#8221;</em> '
          '<span style="color:#64748b;">— compra verificada (traduzido)</span><br>'
          '<span style="color:#475569;">A melhor avaliação do comparativo.</span>'))
cards_av.append(CARD.format(**LARANJA, titulo="Amazon — Galaxy Tab A9 8,7&#34;",
    corpo='<br>⚠️ <strong>Sem estoque em 25/08/2026</strong><br>'
          '<span style="color:#475569;">O anúncio atual da Amazon é o <strong>Tab A9+ 11&#34;</strong>, outro aparelho — não há avaliação própria deste SKU para citar. Verifique a oferta no Mercado Livre.</span>'))
cards_av.append(CARD.format(**AZUL, titulo="Mercado Livre — Positivo Vision Tab 7 Minions",
    corpo='<br>⭐ <strong>4,7/5</strong> · <strong>1.196 opiniões</strong> <span style="font-size:12px;">(inclui internacionais)</span> · 🏆 MAIS VENDIDO · <strong>R$ 571,12</strong> no Pix (capa + mochila)<br>'
          '<em>&#8220;Um tablet excelente! Roda jogos básicos e até Roblox. Funciona bem pra redes sociais e YouTube também.&#8221;</em> '
          '<span style="color:#64748b;">— compra verificada</span><br>'
          '<span style="color:#475569;">Crítica mais comum: bateria dura ~2–3h de uso contínuo.</span>'))
cards_av.append(CARD.format(**LARANJA, titulo="Amazon — Positivo Vision Tab 7 Minions",
    corpo='<br>⭐ <strong>4,1/5</strong> · <strong>38 classificações globais</strong> · <strong>R$ 409,52</strong> no Pix (só capa)<br>'
          '<em>&#8220;O único, até agora, que permitiu espelhamento de tela. Bateria duradoura.&#8221;</em> '
          '<span style="color:#64748b;">— José Antonio V., compra verificada (ago/2026)</span><br>'
          '<span style="color:#475569;">61% das notas são 5 estrelas; queixa recorrente: bateria curta.</span>'))

AV_NOVO = ('<!-- wp:html -->\n'
 '<div style="background: #f8fafc; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px 24px; margin-bottom: 28px;">\n'
 '<p style="margin: 0 0 14px; font-size: 16px; font-weight: 700; color: #1e293b;">⭐ O que dizem as avaliações '
 '<span style="font-size: 12px; font-weight: 400; color: #64748b;">(capturas das plataformas em 25/08/2026 · citações de compras verificadas)</span></p>\n'
 '<div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 16px;">\n'
 + "\n".join(cards_av) +
 '\n<!-- NOTA AO EDITOR: citações extraídas literalmente das capturas de 25/08/2026 '
 '(ML: Kid Pad 4,4/5·129, A9 4,9/5·1.345, Vision 4,7/5·1.196 | Amazon: Kid Pad 2,9/5·24, Vision 4,1/5·38; A9 sem estoque). '
 'Nome semi-anonimizado + data + plataforma conforme regra anti-alucinação da casa. -->\n</div>\n</div>\n<!-- /wp:html -->')

bs, be = bloco_contemo(s, "O que dizem as avaliações")
s = s[:bs] + AV_NOVO + s[be:]
print("2) avaliações 6 cards ok")

# ── 3) RESPOSTA RÁPIDA: 3 blocos lado a lado fixos (padrão Escolha Rápida golden) ──
RESP_NOVO = '''<!-- wp:html -->
<div id="resposta-rapida-cards" style="margin-bottom: 28px;">
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #22c55e; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #166534;">🟢 Melhor custo-benefício (tela grande)</strong><strong>Multi Kid Pad NB425 Laranja</strong> — R$ 856,75 no Pix (ML): tela 10,1" IPS, 6GB/128GB, bateria 6.000 mAh e capa com alça. Ressalva: relatos de defeito de bateria e travamentos. Ideal de 4 a 10 anos.</div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #3b82f6; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #1e40af;">🛡️ Mais seguro</strong><strong>Galaxy Tab A9 (com Samsung Kids)</strong> — R$ 1.114 no Pix (ML): Samsung Kids + Google Family Link, capa infantil avulsa e atualizações longas — a melhor avaliação do comparativo. <span style="font-size:12px; color:#64748b;">Amazon sem estoque em 25/08.</span></div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #f59e0b; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #92400e;">💸 Mais barato</strong><strong>Positivo Vision Tab 7 Minions</strong> — R$ 409,52 na Amazon (só capa): 7" IPS, Android 14 Go, 3GB/64GB; no ML, capa + mochila por R$ 571,12. Ressalva: bateria curta (~2–3h). Primeiro tablet para 3–6 anos.</div>
</div>
<style>
  @media (max-width: 782px) {
    #resposta-rapida-cards > div:first-child { grid-template-columns: 1fr !important; }
  }
</style>
</div>
<!-- /wp:html -->'''

bs, be = bloco_contemo(s, "🟢 Melhor custo-benefício (tela grande)")
s = s[:bs] + RESP_NOVO + s[be:]
print("3) resposta rápida lado a lado ok")

# ── 4) IDADE: 3 blocos lado a lado fixos ──
IDADE_NOVO = '''<!-- wp:html -->
<div id="idade-cards" style="margin-bottom: 28px;">
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #f59e0b; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #92400e;">👶 3–5 anos → Positivo Vision Tab 7</strong>Leve, barato, tela pequena para mãos pequenas. Se quebrar, o prejuízo é menor. Ótimo para Galinha Pintadinha, YouTube Kids e apps de alfabetização.</div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #22c55e; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #166534;">👦 6–8 anos → Multi Kid Pad NB425 Laranja</strong>Tela grande para desenho e joguinhos, 128GB para baixar tudo offline. Capa com alça aguenta escola e viagem.</div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #3b82f6; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #1e40af;">🧑 9–12 anos → Galaxy Tab A9 com Samsung Kids</strong>Hardware Samsung + controle que acompanha o crescimento. Depois dos 10, dá para sair do modo Kids e usar como tablet &#8220;de gente grande&#8221;.</div>
</div>
<style>
  @media (max-width: 782px) {
    #idade-cards > div:first-child { grid-template-columns: 1fr !important; }
  }
</style>
</div>
<!-- /wp:html -->'''

bs, be = bloco_contemo(s, "3–5 anos → Positivo Vision Tab 7")
s = s[:bs] + IDADE_NOVO + s[be:]
print("4) idade lado a lado ok")

# ── 5) RÉGUA → BLOCO DE AVALIAÇÃO GOLDEN + caixa 🧮 ──
CRITERIO = ('    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">\n'
            '      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">{nome}</div>\n'
            '      <div style="font-size: 36px; font-weight: 800; color: {cor}; margin-bottom: 8px; line-height: 1;">{nota}</div>\n'
            '      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">{desc}</div>\n'
            '    </div>')
VERDE, AMBAR = "#22c55e", "#f59e0b"
crits = [
    dict(nome="💰 Custo-benefício · 30%", nota="7.0", cor=AMBAR,
         desc="Preços acessíveis na faixa infantil; opções com controle parental incluso"),
    dict(nome="⭐ Satisfação verificada · 25%", nota="8.0", cor=VERDE,
         desc="Avaliações divergentes entre os três: Kid Pad com queixas de bateria (Amazon 2,9/5); Tab A9 com 4,9/5 e volume alto"),
    dict(nome="📋 Ficha técnica · 20%", nota="7.5", cor=AMBAR,
         desc="Specs oficiais conferidas junto aos fabricantes; telas adequadas à faixa etária"),
    dict(nome="⚙️ Recursos e usabilidade · 10%", nota="8.0", cor=VERDE,
         desc="Controle parental presente em todos; Samsung Kids e Kids Space analisados"),
    dict(nome="📚 Consenso técnico · 10%", nota="7.5", cor=AMBAR,
         desc="Relatos de pais e análises convergem nos pontos fortes e fracos mapeados"),
    dict(nome="🤝 Confiança e suporte · 5%", nota="8.0", cor=VERDE,
         desc="Garantia oficial Multi, Samsung e Positivo no Brasil; suporte documentado"),
]
grid_crits = "\n".join(CRITERIO.format(**c) for c in crits)
BADGE = ('<div style="background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 10px 16px; '
         'border-radius: 10px; text-align: center; box-shadow: 0 4px 12px rgba(15,23,42,0.3);">\n'
         '<div style="font-size: 24px; font-weight: 800; color: #fff; line-height: 1;">{nota}</div>\n'
         '<div style="font-size: 10px; color: rgba(255,255,255,0.85); font-weight: 600; text-transform: uppercase;">{rotulo}</div>\n'
         '</div>')
badges = "\n".join(BADGE.format(nota=n, rotulo=r) for n, r in [("7.0", "Multi NB425"), ("8.5", "Galaxy Tab A9"), ("8.5", "Vision Tab 7")])

REGUA_NOVA = f'''<!-- wp:html -->
<div id="avaliacao-tablets-infantil" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px; margin: 28px 0;">

  <!-- Cabeçalho com as notas dos 3 produtos -->
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 2px solid #e2e8f0;">
    <div>
      <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">🎯 Comparativo — 3 tablets infantis Dia das Crianças 2026</div>
      <div style="font-size: 13px; color: #64748b;">Notas por critério da Régua Curadoria Prime v2.0</div>
    </div>
    <div style="display: flex; gap: 10px; flex-wrap: wrap;">
{badges}
    </div>
  </div>

  <!-- Grid 3×2 de critérios -->
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
{grid_crits}
  </div>

  <style>
    @media (max-width: 782px) {{
      #avaliacao-tablets-infantil > div:nth-child(2) {{ grid-template-columns: repeat(2, 1fr) !important; }}
    }}
    @media (max-width: 480px) {{
      #avaliacao-tablets-infantil > div:nth-child(2) {{ grid-template-columns: 1fr !important; }}
      #avaliacao-tablets-infantil {{ padding: 20px 16px !important; }}
    }}
  </style>
</div>
<!-- /wp:html -->

<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
  <strong>🧮 Como chegamos às notas</strong><br><br>
  A nota de cada tablet não é impressão geral: sai de seis critérios com pesos fixos — <strong>Custo-benefício 30%, Satisfação verificada 25%, Ficha técnica 20%, Recursos e usabilidade 10%, Consenso técnico 10% e Confiança e suporte 5%</strong> — definidos antes de pontuar e aplicados igualmente aos três comparados. As notas medem a qualidade da proposta a partir de evidência documental: fichas oficiais Multi, Samsung e Positivo, consenso técnico e avaliações verificadas de compradores (capturas de 25/08/2026). Não são medição de bancada — não testamos fisicamente os aparelhos e, por isso, não pontuamos conforto de uso nem durabilidade. Régua Curadoria Prime v2.0 (agosto/2026). <a href="https://curadoriaprime.com/como-avaliamos/" style="color: #78350f; font-weight: 700; text-decoration: underline;">Como calculamos estas notas →</a>
</div>
<!-- /wp:html -->'''

i = s.index("📊 Como chegamos às notas")
bs = s.rindex("<!-- wp:html -->", 0, i)
j = s.index("👍 Bom com ressalvas")
be = s.index(MARCA_FIM, j) + len(MARCA_FIM)
s = s[:bs] + REGUA_NOVA + s[be:]
print("5) régua → bloco avaliação golden + 🧮 ok")

# ── 6) BOTÕES em cores oficiais das plataformas ──
ML_PADRAO = ('background: linear-gradient(135deg, #2d3277 0%, #1a1f5c 100%); color: #ffe600; '
             'text-decoration: none; padding: 12px 20px; border-radius: 8px; font-weight: 800; '
             'font-size: 15px; flex: 1; min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(45,50,119,0.3);"')


def trocar(txt, velho, novo, esperado=1):
    n = txt.count(velho)
    assert n == esperado, f"esperado {esperado}, encontrado {n}: {velho[:90]!r}"
    return txt.replace(velho, novo)


# 6a) botões ML vermelhos do artigo (cards Multi e Positivo) — 2 ocorrências idênticas
s = trocar(s,
    'background: linear-gradient(135deg, #9B2226 0%, #7a1a1e 100%); color: #fff; text-decoration: none; '
    'padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;"',
    ML_PADRAO, esperado=2)
# 6b) botão ML do card Samsung (azul Samsung → padrão oficial ML)
s = trocar(s,
    'background: linear-gradient(135deg, #1428A0 0%, #0a1550 100%); color: #ffe600; text-decoration: none; '
    'padding: 12px 20px; border-radius: 8px; font-weight: 800; font-size: 15px; flex: 1; min-width: 150px; text-align: center;"',
    ML_PADRAO, esperado=1)
# 6c) botões Amazon ganham sombra padrão (cor laranja já é a oficial)
s = trocar(s,
    'min-width: 150px; text-align: center;" href="https://link.amazon/B0alnCFJU"',
    'min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(255,150,0,0.3);" href="https://link.amazon/B0alnCFJU"')
s = trocar(s,
    'min-width: 150px; text-align: center;" href="https://link.amazon/B0cJleAj2"',
    'min-width: 150px; text-align: center; box-shadow: 0 2px 8px rgba(255,150,0,0.3);" href="https://link.amazon/B0cJleAj2"')
print("6) botões ML/Amazon em cores oficiais ok")

io.open(F, "w", encoding="utf-8").write(s)
print("OK: patch visual completo gravado.")
