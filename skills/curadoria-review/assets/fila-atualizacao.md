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

| URL | Ação |
| --- | --- |
| `/tablets-para-volta-as-aulas-2026/` | Auditar intenção, mercado e Régua. |
| `/tablets-para-volta-as-aulas-2026-2/` | Auditar duplicidade/retarget antes de qualquer decisão de redirect. |
| `/lg-au801-50-review/` e `/lg-55au801-review-2026/` | Confirmar produto/intenção e consolidar se equivalentes. |
| `/apple-tv-4k/` | Golden visual; corrigir teste falso, prova social e migrar metodologia quando necessário. |

---

# P1 — home / recortes recentes

| URL | Tipo |
| --- | --- |
| `/power-bank-no-aviao-2026/` | GUIA — **CONCLUIDO** · agendado 25/08/2026 08:00 · novo artigo · arquivo em `articles/html_output/power-bank-no-aviao-regras-anac-2026.html` · aprovado no checker (0 erros) |
| `/melhores-techs-custo-beneficio-2026/` | GUIA — **PRONTO_PARA_REVISAO** 25/08 · REPOSICIONADO de "volta às aulas" (dessazonalizado no fim de agosto) para evergreen "melhores techs custo-benefício para trabalhar e estudar" — novo título/slug/canonical/arquivo (`articles/html_output/melhores-techs-custo-beneficio-2026.html`) · mercado re-verificado: 14 capturas no LEDGER, total R$ 1.563,97 · seção 7 reescrita (suporte giratório c/ ventoinha, não PRINCASE) · aviso Anker A1695 (Amazon) vs A1289 (ML exclusivo) · aprovado no checker (0 erros) · pendência p/ agendar: subir imagens no WP Media |
| `/presentes-dia-dos-pais-2026-tech-premium/` | LISTA/GUIA |
| `/presentes-dia-dos-pais-tech-ate-300/` | LISTA/GUIA |
| `/galaxy-watch7-44mm-vale-a-pena/` | REVIEW — saúde |
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
