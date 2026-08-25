#!/usr/bin/env python3
"""Templates golden — parte A: bloco de avaliação (grid 3×2 + badge de nota geral)."""

BLOCO_AVALIACAO = '''<!-- wp:html -->
<div id="avaliacao-kit-tech" style="background: #fff; border: 1px solid #e2e8f0; border-radius: 14px; padding: 26px; margin: 28px 0;">

  <!-- Cabeçalho com nota geral -->
  <div style="display: flex; align-items: center; justify-content: space-between; flex-wrap: wrap; gap: 16px; margin-bottom: 24px; padding-bottom: 20px; border-bottom: 2px solid #e2e8f0;">
    <div>
      <div style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 4px;">🎯 Kit completo — 7 techs para trabalhar e estudar</div>
      <div style="font-size: 13px; color: #64748b;">Avaliação baseada em 6 critérios da Régua v2.0</div>
    </div>
    <div style="display: flex; align-items: center; gap: 12px; background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 100%); padding: 14px 22px; border-radius: 12px; box-shadow: 0 4px 12px rgba(15, 23, 42, 0.3);">
      <div style="text-align: center;">
        <div style="font-size: 36px; font-weight: 800; color: #fff; line-height: 1;">8.5</div>
        <div style="font-size: 11px; color: rgba(255,255,255,0.9); font-weight: 600; text-transform: uppercase; letter-spacing: 0.05em;">/10</div>
      </div>
      <div style="height: 44px; width: 1px; background: rgba(255,255,255,0.3);"></div>
      <div style="font-size: 13px; font-weight: 700; color: #fff; line-height: 1.3;">⭐<br>Recomendado</div>
    </div>
  </div>

  <!-- Grid 3×2 de critérios -->
  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 16px;">
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">💰 Custo-benefício · 30%</div>
      <div style="font-size: 36px; font-weight: 800; color: #f59e0b; margin-bottom: 8px; line-height: 1;">7.0</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Preços competitivos na faixa; Anker 737 destaque em custo por mAh</div>
    </div>
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">⭐ Satisfação verificada · 25%</div>
      <div style="font-size: 36px; font-weight: 800; color: #22c55e; margin-bottom: 8px; line-height: 1;">8.0</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Amazon e ML consistentes, com volumes expressivos</div>
    </div>
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">📋 Ficha técnica · 20%</div>
      <div style="font-size: 36px; font-weight: 800; color: #22c55e; margin-bottom: 8px; line-height: 1;">8.0</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Specs oficiais conferidas junto aos fabricantes</div>
    </div>
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">⚙️ Recursos usabilidade · 10%</div>
      <div style="font-size: 36px; font-weight: 800; color: #f59e0b; margin-bottom: 8px; line-height: 1;">7.5</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">ANC, Wi-Fi 6, hub 100W e alturas ajustáveis</div>
    </div>
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">📚 Consenso técnico · 10%</div>
      <div style="font-size: 36px; font-weight: 800; color: #f59e0b; margin-bottom: 8px; line-height: 1;">7.5</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Múltiplas fontes confirmam as especificações</div>
    </div>
    <div style="background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 18px; text-align: center;">
      <div style="font-size: 11px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.05em; color: #64748b; margin-bottom: 10px;">🤝 Confiança e suporte · 5%</div>
      <div style="font-size: 36px; font-weight: 800; color: #22c55e; margin-bottom: 8px; line-height: 1;">8.0</div>
      <div style="font-size: 12.5px; color: #475569; line-height: 1.5;">Marcas com presença e garantia no Brasil</div>
    </div>
  </div>

  <style>
    @media (max-width: 782px) {
      #avaliacao-kit-tech > div:nth-child(2) { grid-template-columns: repeat(2, 1fr) !important; }
    }
    @media (max-width: 480px) {
      #avaliacao-kit-tech > div:nth-child(2) { grid-template-columns: 1fr !important; }
      #avaliacao-kit-tech { padding: 20px 16px !important; }
    }
  </style>
</div>
<!-- /wp:html -->'''
