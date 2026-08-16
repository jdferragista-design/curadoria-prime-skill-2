# ESTADO — 3183 (Philips 50PUG7019 review)

**Status:** ✅ PUBLICADO NO AR (conferido 16/08/2026)

- URL: https://curadoriaprime.com/philips-50pug7019-review/
- Título: Philips 50PUG7019 Vale a Pena em 2026? Review Google TV 4K
- Entregável: `articles/philips-50pug7019-review.html`
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **6 links de afiliado** com `rel="sponsored noopener noreferrer nofollow"` (3 Philips 7019 + Samsung + LG + ... no total o artigo ficou com 8 links sponsored, incluindo os 2 da sucessora 7300).
- **Shortlink Amazon da Samsung unificado** em `4biQQdq` (o publicado usava `461ctv6`; ambos resolvem para a U8600F ASIN B0F5X4LL89 — mesmo produto).
- **"dados de compradores verificados"** → "avaliações publicadas por compradores" + box de metodologia com "não testamos esta unidade fisicamente".
- **Superlativos suavizados**: "líder de vendas", "a mais inteligente", "melhor custo-benefício da categoria", "vale ouro", "a melhor decisão possível", "não trava", "funciona de verdade", "compradores batem na tecla".
- **Preços atualizados (16/08/2026)**: a 50PUG7019 (2024) está em fim de linha com preço volátil (R$ 1.894 fev → anúncios acima de R$ 3.000 ago); **sucessora 50PUG7300 entra como OPÇÃO** (R$ 1.935 ML Pix / R$ 2.199 Amazon) com links do cliente.
- **"Pontos de Atenção"** (h4 + `<ul>` 4 itens) + "Prós e Contras" + "para quem NÃO é" + FAQ (4 perguntas).
- **Links "Veja também" corrigidos** — os 3 slugs do publicado estavam quebrados:
  - `...50pug7019-qual-tv-4k-50-comprar/` → `samsung-u8600f-vs-lg-au801-vs-philips-50pug7019/`
  - `...samsung-u8600f-50-vale-a-pena-em-2025-.../` → `samsung-u8600f-review/`
  - `...lg-au801-50-o-melhor-processamento-.../` → `lg-au801-50-review/`
- **Duplicação de legenda removida** (o bloco de 3 imagens do comparativo repetia a mesma legenda 3×).
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + Product (reviewRating 8,7/10) + FAQPage + BreadcrumbList (`tv-e-home-theater`); autor "Cristiano Martins"; sem aggregateRating/offers.
- **Bloco de autor canônico** + "Fontes consultadas".

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 8/8 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.223 palavras · valor-agregado completo · imparcialidade 5 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 30/30 · ul 3/3 · p 55/55 · h2 12/12 · li 12/12 · a 26/26. Zero base64.
```

## Dados de mercado (16/08/2026, reuso do post 3153)

| TV | Situação | Preço hoje |
|---|---|---|
| Philips 50PUG7019 (2024) | fim de linha, estoque variável | volátil — R$ 1.894 (fev) → anúncios > R$ 3.000 (ago) |
| Philips 50PUG7300 (2025, sucessora) | venda ativa | R$ 1.935 ML Pix · R$ 2.199 Amazon |
| Samsung U8600F | venda ativa | R$ 2.399 Amazon |
| LG AU801 | venda ativa | R$ 2.242 ML Pix |

- Avaliações Amazon (fev/2026, do publicado): Philips ~9 mil (4,8/5) · LG 815 (4,6/5) · Samsung 194 (4,7/5).

## Aviso de estoque + gancho 50PUG7300 (adicionado 16/08/2026)

Adicionado aviso "estoque baixo ou zerado" no CTA (motivo: sucessora
50PUG7300 chegando) + linha "Em breve: review dedicado da Philips 50PUG7300"
no bloco da sucessora. Quando o post da 7300 for publicado, trocar o texto
pelo link real.

## Pendências FORA do arquivo (painel / cliente)

1. **Colar no WP** substituindo o conteúdo atual (Editor de Código).
2. **Confirmar shortlink Amazon da Samsung** (unificado em `4biQQdq`; o publicado tinha `461ctv6` — ambos a U8600F).
3. **Shortlinks 7300** (Amazon `B09uCSSBI` + ML `27D4FgZ`) já fornecidos pelo cliente no post 3153 — reutilizados aqui.
4. ⚠️ **50PUG7019 em fim de linha**: vale monitorar. Se o estoque zerar, considerar 301 para um review da 50PUG7300 ou consolidar no comparativo 3153 (gatilho §17.2 nível 1).
