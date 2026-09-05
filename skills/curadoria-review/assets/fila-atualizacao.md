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

**Auditado em 03/09/2026 (Lotes 6-8):**
- `/tablets-para-volta-as-aulas-2026-2/`: **ALERTA CRÍTICO** — Conteúdo idêntico ao `/alternativas-galaxy-tab-s10-fe-ipad-estudar/`. Risco de canibalização/duplicidade. Recomenda-se 301 redirect ou exclusão.
- `/moto-g56-5g-review/`: **ALERTA CRÍTICO** — CTA "Ver na Amazon" aponta para link do Mercado Livre (perda de comissão e erro de UX).

| URL | Ação | Status ao vivo |
| --- | --- | --- |
| `/tablets-para-volta-as-aulas-2026/` | Auditar intenção, mercado e Régua. | ✅ h1 "Tablets para Volta às Aulas 2026" (26/08) · trio S10 FE/iPad 11/A11+ · sem nota única (decisão editorial por cenário) · declara sem teste · **complementar ao -2**, não duplicidade · preços 12/08 |
| `/tablets-para-volta-as-aulas-2026-2/` | Auditar duplicidade/retarget antes de qualquer decisão de redirect. | ✅ **RESOLVIDO (03/09)** · Aplicado 301 redirect para `/alternativas-galaxy-tab-s10-fe-ipad-estudar/` |
| `/lg-au801-50-review/` e `/lg-55au801-review-2026/` | Confirmar produto/intenção e consolidar se equivalentes. | ✅ **Produtos distintos**: AU801 50″ (nota 8,4, sem teste, documental) vs 55AU801 55″ (nota 8,5 Régua v2, sem teste) · **sem canibalização** · preços 13/08 |
| `/apple-tv-4k/` | Golden visual; corrigir teste falso, prova social e migrar metodologia quando necessário. | 🚨 **URGENTE (03/09)** · Preço oficial subiu (Jun/26) + Nova Geração iminente (Set/Out 26). Necessita re-angle imediato. |

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
| `/nintendo-switch-lite-review-2026/` | REVIEW — **AGENDADO 07/09/2026 08:00 (confirmado no WP, post 5092)** · review individual do produto-âncora do cluster · reconstruído no golden de REVIEW completo (hero + imagem + metodologia âmbar + prova social 4 cards + índice + resposta rápida + 🧮 Régua v2.0 + scorecard 3×2 + escolha rápida dark final + fontes com links internos) · paleta corrigida para #2997ff · autor = fragmento canônico · seção "Dicas de jogabilidade" (6 tópicos) · 3.504 palavras · checker 0 erros · +3 imagens de gameplay/design da biblioteca WP inseridas · **thumb+hero golden geradas via Pillow (estilo raios+palco reflexivo, sem preço) — destaque id 5106** · JSON-LD datePublished 07/09 · links: link.amazon/B06MejMa2 + meli.la/2mReGbQ · backup do raw anterior em `articles/wp_raw_backups/` |
| `/mario-kart-8-deluxe-review-2026/` | REVIEW — **AGENDADO 09/09/2026 08:00 (confirmado no WP, post 5090)** · review individual do 2º item do hub · reconstruído no golden de REVIEW completo (mesmos blocos do Switch Lite) · seção "Dicas de corrida" (7 tópicos: drift boost, assistentes, itens, combo kart, 200cc, atalhos, battle) · 3.731 palavras · checker 0 erros · +3 imagens oficiais Nintendo inseridas · **thumb+hero golden geradas via Pillow — destaque id 5107** · JSON-LD Article+Review+FAQPage+Breadcrumb com datePublished 09/09 · links: link.amazon/B028hyTBk + meli.la/2PhrCHL · backup do raw anterior em `articles/wp_raw_backups/` |
| `/super-mario-bros-wonder-review-2026/` | REVIEW — **AGENDADO 11/09/2026 08:00 (confirmado no WP, post 5117)** · review individual do 3º item do hub (novo artigo criado direto como scheduled) · golden de REVIEW completo · seção "Dicas de jogabilidade" (7 tópicos: personagem certo, fruta de elefante, insígnias, jogar 2x, Terras dos Arbustos, Lite+controle extra, efeitos mudam controles) · 4.150 palavras · checker 0 erros · 3 screenshots oficiais Nintendo (assets.nintendo.com, validados por visão) + thumb/hero Pillow (destaque id 5112) · nota 9,2 (CB 9,5 · Sat 9,0 · Conteúdo 8,5 · Joga 9,5 · Consenso 9,5 · Multi 9,0) · preços 31/08 LEDGER: Amazon R$ 274,55 Pix (4,9★/1.487, Escolha da Amazon) · ML R$ 329,96 (5,0★/30) · links: link.amazon/B01TVzGDg + meli.la/2K7rg1c · hub atualizado com links dos 3 reviews |
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

---

# Pauta 21/09 · 23/09 · 25/09/2026 (rascunho — planejada em 03/09/2026)

Janela estratégica: entre a Primavera Hot Sale (meados/set) e o pico de
pesquisa de Dia das Crianças (12/10). Publicar nesta janela dá ~2,5 semanas
de indexação antes do pico de intenção de compra. Todos os slots às 08:00.

| Data | Artigo | Tipo | Racional | Dados necessários |
|---|---|---|---|---|
| **21/09 (seg)** | `/mario-party-superstars-review-2026/` — "Mario Party Superstars Vale a Pena em 2026?" | REVIEW — **AGENDADO 21/09/2026 08:00 (confirmado no WP, post 5127)** · 4.110 palavras · nota 8,8 · checker 0 erros · 3 screenshots oficiais Nintendo (store/software/switch/70010000042934, validados por visão; key art com logo rejeitada) · thumb/hero Pillow (destaque 5122) · dicas de jogabilidade 7 tópicos · hub atualizado com o link |
| **23/09 (qua)** | `/retro-game-stick-lite-4k-review-2026/` — "Retro Game Stick Lite 4K Vale a Pena? Review Honesto" | REVIEW — **AGENDADO 23/09/2026 08:00 (confirmado no WP, post 5131)** · 2.864+ palavras · nota 6,6 ("bom com ressalvas" — mais baixa do cluster, intencional) · checker 0 erros · imagens: arte do fabricante da biblioteca WP (id 5078) + thumb/hero Pillow com **cartão arredondado** (recorte impossível: curva neon entrelaçada no kit) · destaque 5128 · hub atualizado com o link |
| **25/09 (sex)** | `/apple-tv-4k/` — RE-ANGLE (atualização do post 4537, manter URL/canonical) | REVIEW — **APLICADO NO WP 04/09 (post 4537, publicado)** · título/hero/thumb/meta SEO atualizados · funil reforçado p/ Fire TV Stick 4K (5 links internos, decisão do editor: produto caro, artigo converte para os rivais) · arquivo `articles/html_output/apple-tv-4k-reangle-2026-09.html` · gerador reprodutível `tools/reangle_apple_tv.py` (44 subs + 12 anchors) · checker 0 erros · mercado 04/09 no LEDGER: Apple Store R$ 2.499 (única rota nacional segura), Amazon 64GB esgotada, catálogo ML intl R$ 1.475 INDISPONÍVEL, ML VYSEGLOBAL R$ 1.764,99 sem impostos (~R$ 3.000 real) · ângulo "comprar agora ou esperar?" com evento Apple 9/9 confirmado (fonte apple.com/apple-events) · thumb/hero Pillow (media 5132/5133, validados por visão) · nota mantida 8,5 (motivo CB atualizado) · headline novo no JSON-LD + breadcrumb · dateModified 25/09 · ordem corrigida vs golden (prós/contras após compra; autor após fontes) · pendência: aplicar no WP só após OK do editor |

Sequência de produção por artigo (padrão da casa): curadoria-mercado
(recaptura na véspera) → golden do tipo → dicas de jogabilidade (games) →
imagens validadas por visão → thumb/hero Pillow → checker 0 erros →
revisão bloco a bloco vs golden → rascunho WP + destaque → AGENDAR só
após OK do editor.

Alternativas na manga (se algum slot furar):
- `/melhor-fone-bluetooth-ate-500-reais-2026/` (P2, LISTA) — evergreen, pico em Dia das Crianças também.
- `/galaxy-watch7-44mm-vale-a-pena/` (P1, REVIEW saúde).
- `/guia-presentes-dia-das-criancas-2026/` está CANCELADO — não reativar (hub de jogos ocupa o espaço).

---

## Automação de divulgação X → Telegram (criada 03/09/2026)

- Cron `x-post-cluster-games` (id 430be0725f8b, a cada 30min): monitor `~/.hermes/scripts/detecta_publicacoes_cluster.py` detecta quando um post do cluster (lista em `~/.hermes/scripts/cluster-games-wp.json`) passa a `publish` no WP; a cada detecção, o agente gera o post do X (≤280 chars, PT-BR, sem dados inventados) e envia ao Telegram do editor — **o Cristiano publica no X manualmente**.
- Detector usa a coleção pública do REST (`include=`): posts `future` não aparecem; presença = publicado. Endpoint single-post retorna 401 (WAF) — não usar.
