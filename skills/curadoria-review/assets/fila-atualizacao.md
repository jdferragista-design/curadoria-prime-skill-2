# Fila de atualização — curadoriaprime.com

Versão operacional: 2.0
Revisado em: 19/08/2026

Inventário original baseado no sitemap.

Este arquivo organiza trabalho.

NÃO é fonte factual sobre os produtos.

Preços, ratings, estoque, concorrentes e especificações precisam ser
reconfirmados na execução.

---

# Workflow de cada URL

1. Classificar formato:
   - REVIEW
   - VS
   - LISTA/GUIA

2. Confirmar intenção.

3. Procurar URL concorrente.

4. Preservar:
   - URL;
   - slug;
   - canonical.

5. Diagnosticar:
   - teste físico falso;
   - AggregateRating externo;
   - reviewCount/ratingCount externo;
   - preço velho;
   - CTA quebrado;
   - SKU errado;
   - imagem IA enganosa;
   - keyword stuffing;
   - nota em Régua antiga;
   - layout fora do padrão.

6. Rodar `curadoria-mercado`.

7. Atualizar fontes técnicas necessárias.

8. Aplicar Régua v2.0 quando houver nota.

9. Usar:
   - REVIEW → `template-review.md`
   - VS → `template-vs.md`
   - LISTA/GUIA → `template-lista.md`

10. Produzir RELATÓRIO DE IMAGENS se necessário.

11. Rodar `checklist-bloqueio.md`.

12. Editor humano revisa.

Sem evidência atual suficiente:

a URL permanece em atualização.

---

# Estados

- `PENDENTE`
- `EM_PESQUISA`
- `AGUARDANDO_MERCADO`
- `AGUARDANDO_IMAGENS`
- `PRONTO_PARA_REVISAO`
- `CONCLUIDO`

Não utilizar automaticamente:

`PRONTO_PARA_PUBLICAR`

---

# Prioridades

## P0

- erro factual;
- teste falso;
- schema enganoso;
- canibalização relevante;
- risco de saúde/segurança;
- CTA apontando ao produto errado.

## P1

Página relevante ou recente que precisa alinhamento.

## P2

Catálogo com estrutura/metodologia antiga.

## P3

Manutenção e páginas de menor prioridade.

Os estados de frescor são política interna da Curadoria, não regra
universal do Google.

---

# P0 — canibalização e risco

**Conferido ao vivo em 29/08/2026** — os 4 clusters abaixo foram validados
no site e não apresentam canibalização, teste falso nem schema enganoso.
**Recaptura de preços 29/08 concluída** via curadoria-mercado/browser-harness
(9 capturas na Amazon gravadas no LEDGER; Apple TV 4K sem estoque; LGs novos
no LEDGER). Ver `skills/curadoria-mercado/assets/historico-precos/LEDGER.csv`.

| URL | Ação | Status ao vivo |
| --- | --- | --- |
| `/tablets-para-volta-as-aulas-2026/` | Auditar intenção, mercado e Régua. | ✅ h1 "Tablets para Volta às Aulas 2026" (26/08) · trio S10 FE/iPad 11/A11+ · sem nota única (decisão editorial por cenário) · declara sem teste · **complementar ao -2**, não duplicidade · preços 12/08 |
| `/tablets-para-volta-as-aulas-2026-2/` | Auditar duplicidade/retarget antes de qualquer decisão de redirect. | ✅ h1 "Alternativas ao Galaxy Tab S10 FE e ao iPad" (26/08) · intenção distinta, cruza com o canônico · **sem redirect necessário** · preços 12/08 |
| `/lg-au801-50-review/` e `/lg-55au801-review-2026/` | Confirmar produto/intenção e consolidar se equivalentes. | ✅ **Produtos distintos**: AU801 50″ (nota 8,4, sem teste, documental) vs 55AU801 55″ (nota 8,5 Régua v2, sem teste) · **sem canibalização** · preços 13/08 |
| `/apple-tv-4k/` | Golden visual; corrigir teste falso, prova social e migrar metodologia quando necessário. | ✅ Golden: 3ª geração 2022 64GB (A2737) · nota 8,5 Régua v2 · declara sem teste físico · JSON-LD **sem** aggregateRating/reviewCount · preços 10/08 |

---

# P1 — home / recortes recentes

| URL | Tipo |
| --- | --- |
| `/melhores-smartphones-custo-beneficio-2026/` | GUIA — **AGENDADO** 01/09/2026 08:00 (confirmado no WP) · novo artigo · re-angle de "até R$1500" para "custo-benefício por faixas" (maximiza links internos p/ 5 reviews) · arquivo em `articles/html_output/melhores-smartphones-custo-beneficio-2026.html` · preços/ratings reais capturados 29/08 na Amazon via browser-harness · 6 imagens reais do WP Media (hero + 5 produtos) · nota Régua 8,2/10 · aprovado no checker (0 erros) · prompts de imagem em `articles/html_output/PROMPTS-IMAGENS-*.md` |
| `/melhores-jogos-nintendo-switch-2026/` | GUIA/GAMES — **AGENDADO 04/09/2026 08:00 (confirmado no WP)** · **HUB do cluster Dia das Crianças 2026** (pivot do hub original para "jogos/games") · arquivo em `articles/html_output/melhores-jogos-nintendo-switch-2026.html` · 5 itens: Switch Lite (🥇) + Mario Kart 8 Deluxe + Super Mario Bros. Wonder + Mario Party Superstars + Retro Game Stick (com ressalva) · produtos verificados ao vivo em 31/08/2026 · 10 capturas no LEDGER (5 SKUs × Amazon+ML) · aprovado no checker (0 erros) · 12 links sponsored · JSON-LD @graph (Article+ItemList+FAQPage+Breadcrumb, datePublished 04/09) · snippet otimizado (título 51/60 · descrição 138/160) · **imagens 5+autor+logo enviadas no WP Media e confirmadas HTTP 200** + hero Gemini aplicada (2 pontos: img no topo + image do JSON-LD) · datePublished = 04/09/2026 no agendamento (dateModified = 31/08/2026, data de verificação) |
| `/power-bank-no-aviao-2026/` | GUIA — **CONCLUIDO** · agendado 25/08/2026 08:00 · novo artigo · arquivo em `articles/html_output/power-bank-no-aviao-regras-anac-2026.html` · aprovado no checker (0 erros) |
| `/melhores-techs-custo-beneficio-2026/` | GUIA — **AGENDADO** 27/08/2026 08:00 · REPOSICIONADO de "volta às aulas" para evergreen "melhores techs custo-benefício para trabalhar e estudar" · mercado re-verificado: 14 capturas no LEDGER, total R$ 1.563,97 · fontes reconstruídas c/ fichas oficiais + preço Xiaomi inventado removido · visual alinhado ao golden (veredito 💡, alternativas 3 col.) · aprovado no checker (0 erros) · conferir imagens no WP Media antes de publicar |
| `/tablet-infantil-dia-das-criancas-2026-3-melhores/` | LISTA — **AGENDADO** 29/08/2026 08:00 · novo artigo sazonal · arquivo em `articles/html_output/tablet-infantil-dia-das-criancas-2026-3-melhores.html` · preços/avaliações reais dos 3 SKUs (capturas 25/08 no LEDGER: Kid Pad R$ 856,75 ML/R$ 884,44 Amz · A9 R$ 1.114 ML sem estoque Amz · Vision R$ 409,52 Amz/R$ 571,12 ML) · notas unificadas 7,0/8,5/8,5 · padronização visual golden completa (índice 2 col., avaliações 6 cards 1/plataforma, grids lado a lado, bloco avaliação+🧮, botões cores oficiais ML/Amazon) · aprovado no checker (0 erros) · pendências p/ publicar: subir imagens no WP Media (`/2026/09/*.webp`) + URLs dos anúncios ML no LEDGER + re-verificar preços em 10/09/2026 |
| `/presentes-dia-dos-pais-2026-tech-premium/` | LISTA/GUIA |
| `/presentes-dia-dos-pais-tech-ate-300/` | LISTA/GUIA |
| `/guia-presentes-dia-das-criancas-2026/` | GUIA — **CANCELADO** (substituído pelo `/melhores-jogos-nintendo-switch-2026/` como hub do cluster) · arquivo em `articles/html_output/guia-presentes-dia-das-criancas-2026.html` · 6 produtos (Fisher-Price, Mega Bloks, LEGO Classic, Galaxy Tab Kids, Switch Lite, Arduino) · 14 seções · 2.771 palavras · aprovado no checker (0 erros, 0 alertas) · tags balanceadas · JSON-LD @graph completo |
| `/galaxy-watch7-44mm-vale-a-pena/` | REVIEW — saúde |
| `/nintendo-switch-lite-review-2026/` | REVIEW — **PRONTO_PARA_REVISAO** · novo review individual do produto-âncora do cluster (Switch Lite, hub do guia de games) · arquivo em `articles/html_output/nintendo-switch-lite-review-2026.html` · gerado com `gerar_artigo.py` v2.0 (--tipo review) · preço R$ 1.366,67 Amazon / R$ 1.366,64 ML · nota 8,5/10 Régua · 1.851 palavras · aprovado no checker (0 erros) · JSON-LD Review+FAQPage · links: link.amazon/B09BDLVLW5 + meli.la/2mReGbQ · pendência: conferir se o meli.la é o link correto |
| `/galaxy-s24-fe-em-2026/` | REVIEW |
| `/fire-tv-stick-4k-wifi-6/` | REVIEW — **CONCLUIDO** · publicado 22/08/2026 · patch original aplicado; versão canônica em `3858-fire-tv-stick-4k-wifi-6-reconstruido.html` (recomendada para segunda atualização) |
| `/edifier-w820nb-review-2026-vale-a-pena/` | REVIEW |
| `/jbl-wave-buds-2-review-2026-vale-a-pena/` | REVIEW |
| `/lenovo-ideapad-1-i3-1215u-vale-a-pena-em-2026/` | REVIEW |
| `/lenovo-ideapad-slim-3-notebook-2026/` | REVIEW |
| `/redmi-note-15-pro-vale-a-pena/` | REVIEW |
| `/moto-g56-5g-review/` | REVIEW — **CONCLUIDO** · publicado 22/08/2026 · patch de 20/08 aplicado: alegações de teste removidas + metodologia/divulgação corrigidas · arquivo em `articles/correcoes/4251-moto-g56-5g-review.html` |

---

# P2 — catálogo

| URL | Tipo / Atenção |
| --- | --- |
| `/soundcore-liberty-4-nc-vale-a-pena/` | REVIEW — alegações quantitativas |
| `/samsung-galaxy-buds-core-vale-a-pena/` | REVIEW |
| `/redmi-buds-6-play-review-2026-vale-a-pena/` | REVIEW |
| `/qcy-t13-anc-review-2026-vale-a-pena/` | REVIEW — migrar Régua quando necessário |
| `/melhor-fone-bluetooth-ate-500-reais-2026/` | LISTA/GUIA |
| `/iphone-16e-review-2026/` | REVIEW |
| `/samsung-galaxy-s25-5g-review/` | REVIEW |
| `/samsung-galaxy-a16-review/` | REVIEW — **CONCLUIDO** · publicado 22/08/2026 · patch original aplicado; versão canônica em `2982-samsung-galaxy-a16-review-reconstruido.html` (recomendada para segunda atualização) |
| `/xiaomi-redmi-note-14-pro-plus-review-2026/` | REVIEW |
| `/samsung-galaxy-tab-s10-fe-5g-vale-a-pena/` | REVIEW — verificar canibalização |
| `/samsung-galaxy-book4-review-2026/` | REVIEW |
| `/xiaomi-smart-band-9-active-vale-a-pena/` | REVIEW — saúde |
| `/xiaomi-smart-band-10-vale-a-pena/` | REVIEW — saúde |
| `/samsung-galaxy-fit3-vale-a-pena/` | REVIEW — saúde |

---

# P3 — TV, áudio e casa

| URL | Tipo / Atenção |
| --- | --- |
| `/roku-vs-fire-tv-stick-4k/` | VS — **CONCLUIDO** · publicado 22/08/2026 · patch original aplicado; versão canônica em `2892-roku-vs-fire-tv-stick-4k-reconstruido.html` (recomendada para segunda atualização) |
| `/samsung-s90f-qd-oled-review/` | REVIEW |
| `/samsung-u8600f-review/` | REVIEW |
| `/samsung-u8100f-smart-tv-4k-review/` | REVIEW |
| `/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019/` | VS — **EM_REVISAO 20/08** · HTML novo no modelo VS canônico · corrigido: 50PUG7300=Titan OS (não Google TV), 50PUG7019=HDR10/HLG (sem Dolby Vision), HDMI=VRR/ALLM (não 2.1), 8ms só na 7300 · Régua v2.0 aplicada (7.5/8.5/7.0) · aguardando recaptura de preços |
| `/lg-au801-50-review/` | REVIEW — ver P0 |
| `/lg-55au801-review-2026/` | REVIEW — ver P0 |
| `/philips-50pug7019-review/` | REVIEW |
| `/tcl-c6k-review-2026/` | REVIEW |
| `/samsung-hw-b400f-review/` | REVIEW |
| `/jbl-cinema-sb180-review-vale-a-pena/` | REVIEW |
| `/lg-sqc1-review-2026-vale-a-pena/` | REVIEW |
| `/samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1/` | VS |
| `/purificador-de-agua-electrolux-pe12g-review/` | REVIEW — alegações de saúde |
| `/garrafa-termica-quick-flip-stanley-710ml/` | REVIEW |
| `/kit-teclado-mouse-ultra-slim/` | REVIEW — risco de afiliado fino |
| `/camera-lampada-360-yoosee-lp8177-review-2026/` | REVIEW — privacidade/segurança |
| `/good-vision-kit-cameras-wifi-review/` | REVIEW |
| `/melhores-cameras-de-seguranca-wi-fi-2026/` | LISTA/GUIA — **CONCLUIDO** · publicado 22/08/2026 · patch original aplicado; versão canônica em `3052-melhores-cameras-de-seguranca-wi-fi-reconstruido.html` (recomendada para segunda atualização) |

---

# Páginas institucionais

Auditar separadamente:

- `/sobre-a-curadoria-prime/`
- `/transparencia-curadoria-prime/`
- `/bio-do-cristian/`
- `/nossa-prova/`
- `/sobre-nos-curadoria-prime/`
- termos;
- privacidade;
- cookies;
- isenção;
- contatos.

Institucional não usa template de REVIEW.

---

# Comando recomendado

`Atualize /slug/ integralmente conforme curadoria-review. Preserve URL e
canonical. Refaça mercado, evidências, Régua quando aplicável, template
canônico e relatório de imagens. Não publique.`

A Skill deve entregar conforme o contrato do SKILL.md.

---

# Rodada 27/08/2026 — P0 estabilizado (18 artigos com 0 erros)

Correção em lote dos artigos de maior risco (alegações de teste físico, schema
`aggregateRating`/`reviewCount`, JSON-LD inválido). Todos com **0 erros** no
`checar_conformidade.py`. Arquivos em `articles/html_output/`.

Estado: **PRONTO_PARA_REVISAO** (pendente: aplicação no WP + data de captura).

| URL | Antes | Depois |
|---|---|---|
| `/samsung-hw-b400f-review/` | teste-físico + aggregateRating + sem honestidade | ✅ 0 erros (teste reescrito + Tipo de análise) |
| `/samsung-galaxy-book4-review-2026/` | teste-físico + aggregateRating | ✅ 0 erros (citação reescrita + honestidade) |
| 14 artigos com aggregateRating | aggregateRating/reviewCount no schema | ✅ 0 erros (removidos §2.4) |
| `/presentes-dia-dos-pais-tech-ate-300/` | JSON-LD inválido (66 `<br/>`) | ✅ 0 erros (schema válido) |
| `/apple-tv-4k/` | JSON-LD inválido (61 `<br/>`) | ✅ 0 erros (schema válido) |
| `/purificador-de-agua-electrolux-pe12g-review/` | JSON-LD structure quebrada | ✅ 0 erros |

Pendências editoriais (não bloqueiam): data de verificação em 14 artigos,
posição da divulgação em 11, ressalva de ausência de teste em 7, bloco de
contras em 9, densidade de keyword em 6. Detalhes: `articles/correcoes/RELATORIO-CORRECOES-P0-2026-08-27.md`.

Ver relatório completo das correções P0.

---

# Rodada 27/08/2026 (b) — Aplicação no WordPress concluída (18/18 gravados)

Os 18 artigos P0 da rodada (a) foram aplicados DIRETAMENTE no WordPress via
`tools/aplicar_wp_p0.py` (PUT no `content.raw` autenticado, com backup
prévio, verificação pós-gravação e auditoria do render público). O gate
`--pipeline-check` provou antes que o pipeline reproduz byte a byte os
arquivos corrigidos a partir do render.

Estado: **APLICADO_NO_WP** (aguarda conferência visual do editor + data de
captura de preços).

Pendências editoriais remanescentes (não bloqueiam): data de verificação
(14), posição da divulgação de afiliado (11), bloco de contras (9),
densidade de keyword (6), revisão visual das citações reescritas
(hw-b400f id 3310 e galaxy-book4 id 4185).

Backups dos raws originais: `articles/wp_raw_backups/`.
Espelho do raw corrigido: `articles/wp_raw_mirror/articles/html_output/`.
Detalhes: `articles/correcoes/RELATORIO-CORRECOES-P0-2026-08-27.md` (seção
"Aplicação no WordPress").
