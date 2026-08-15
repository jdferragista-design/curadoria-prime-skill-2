# ESTADO — 3181 (LG AU801 50″ · `lg-au801-50-review`)

**Status:** ✅ FECHADO (artigo corrigido entregue e validado)

- URL: https://curadoriaprime.com/lg-au801-50-review/
- Título: Review LG AU801 50″: A Melhor para TV Aberta e YouTube
- Entregável: `articles/3181-lg-au801-50-artigo-completo.html`
- Data da última reescrita: 14/08/2026

## O que foi corrigido

- Urgência fabricada removida do CTA (sem "estoque limitado" / "há X horas").
- Preço datado (13/08/2026) nos 6 pontos; diferença vs Philips recalculada (~R$ 79).
- Alegação de teste trocada por metodologia documental ("não testamos fisicamente").
- Contagem de avaliações corrigida (50 avaliações, 4,6/5 Amazon).
- Heading sensacionalista suavizado; superlativos reatribuídos; sem "imbatível".
- JSON-LD reescrito em `wp:html` SEM `<br />`: @graph (TechArticle, Product, FAQPage, BreadcrumbList); sem aggregateRating; reviewRating com worstRating; autor "Cristiano Martins"; fuso -03:00; sem aspa reta de polegada; sem availability inventado.
- BreadcrumbList: categoria `tv-e-home-theater` (não `tvs`).
- Seção de contras: heading exato "Pontos de Atenção" + `<ul>` 5 itens.
- "Veja também": 3 links internos corrigidos para slugs reais.
- Ressalva (a) resolvida: imagem `webOS-para-entretenimento-LG-BR-1.png` removida da seção Gaming.
- Ressalva (b) resolvida: link `/transparencia-curadoria-prime/` reintroduzido.
- Fontes: LG oficial com link; marketplaces citados com data.
- Bloco de autor canônico (Cristiano Martins) aplicado.

## Validação (checar_conformidade.py)

- 0 erros. JSON-LD parse OK, div balanceado, sponsored 100%, zero base64.
- Alerta remanescente (falso positivo): `[divulgacao]` — heurística compara fração texto/HTML; confirmado por offset que a divulgação vem antes do 1º link.

## Pendências FORA do arquivo (painel)

1. Rank Math > título SEO: aspa reta de polegada → "50 polegadas".
2. Perfil WP: nome de exibição → "Cristiano Martins".

## Pendências abertas (aguardando decisão)

1. Shortlink Amazon: unificado em `B03wia3Ue`; rascunho anterior tinha `B0bDYSbFl`. Confirmar.
2. Schema: confirmar `sku: "50AU801"` e logo `cropped-image-270x270.jpg`.
3. Imagem da seção Upscaling (`LG-Suporte-Interativo-AI-Chatbot-Interface...webp`): nome sugere "suporte/chatbot", não upscaling. Conferir na biblioteca de mídia.
