#!/usr/bin/env python3
"""Templates golden — parte B: box 🧮, escolha rápida 3 colunas e card de FAQ."""

BLOCO_COMO_CHEGAMOS = '''<!-- wp:html -->
<div style="background: #fffbeb; border: 1px solid #fde68a; border-radius: 10px; padding: 14px 18px; margin: 22px 0; font-size: 13px; color: #78350f; line-height: 1.6;">
  <strong>🧮 Como chegamos à nota 8,5</strong><br><br>
  A nota do kit não é impressão geral: sai de seis critérios com pesos fixos — <strong>Custo-benefício 30%, Satisfação verificada 25%, Ficha técnica 20%, Recursos e usabilidade 10%, Consenso técnico 10% e Confiança e suporte 5%</strong> — definidos antes de pontuar e aplicados igualmente a tudo o que analisamos. As notas medem a qualidade da proposta a partir de evidência documental: ficha oficial dos fabricantes, consenso técnico e avaliações verificadas de compradores. Não são medição de bancada — não testamos fisicamente os itens e, por isso, não pontuamos conforto de uso nem durabilidade. Régua Curadoria Prime v2.0 (agosto/2026). <a href="https://curadoriaprime.com/como-avaliamos/" style="color: #78350f; font-weight: 700; text-decoration: underline;">Como calculamos esta nota →</a>
</div>
<!-- /wp:html -->'''

ESCOLHA_RAPIDA = '''<!-- wp:html -->
<div id="escolha-rapida-guia" style="margin-bottom: 28px;">
<p style="margin: 0 0 12px; font-size: 16px; font-weight: 700; color: #1e293b;">⚡ Escolha Rápida</p>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 12px;">
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #22c55e; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #166534;">🎓 Orçamento apertado</strong>Comece com Mouse M185 (R$ 68,90) + JBL Wave Buds 2 (R$ 232) = <strong>R$ 300,90</strong></div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #3b82f6; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #1e40af;">💻 Estudo em casa</strong>Adicione Roteador AX12 (R$ 169,15) + Suporte giratório c/ ventoinha (R$ 157,93) = <strong>R$ 627,98</strong></div>
<div style="background: #fff; border: 1px solid #e2e8f0; border-top: 3px solid #f59e0b; border-radius: 10px; padding: 14px 16px; font-size: 13.5px; line-height: 1.65;"><strong style="display: block; margin-bottom: 6px; color: #92400e;">🚀 Kit completo</strong>Todos os 7 produtos = <strong>R$ 1.563,97</strong></div>
</div>
<style>
  @media (max-width: 782px) {
    #escolha-rapida-guia > div:nth-child(2) { grid-template-columns: 1fr !important; }
  }
</style>
</div>
<!-- /wp:html -->'''

FAQ_CARD = '''<!-- wp:html -->
<div style="background: #fff; border-radius: 12px; margin-bottom: 10px; border: 1px solid #e2e2f0; overflow: hidden; box-shadow: 0 2px 8px rgba(90,79,207,.07);">
<p style="padding: 16px 20px; font-size: 15px; font-weight: bold; color: #5a4fcf; margin: 0; border-bottom: 1px solid #e2e2f0;">{q}</p>
<p style="padding: 14px 20px; color: #4a4a68; font-size: 15px; margin: 0; line-height: 1.7;">{a}</p>
</div>
<!-- /wp:html -->'''
