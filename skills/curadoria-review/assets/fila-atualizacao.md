# Fila de atualização — curadoriaprime.com

Inventário a partir do `post-sitemap.xml` em 12/08/2026.
Uma URL por vez. Sem fonte do dia, a URL fica em rascunho.

## Antes de qualquer texto

1. Confirmar intenção e se outra URL compete.
2. Preservar slug e canonical.
3. Diagnosticar: “testamos”, AggregateRating externo, imagem de IA,
   keyword stuffing, preço sem data.
4. Recapturar preço Amazon + ML + oficial.
5. Redigir no layout Apple TV 4K (`template-review.md` ou `template-guia.md`).
6. Checklist de bloqueio. Editor humano publica.

## P0 — canibalização e risco Google (fazer primeiro)

| URL | Ação |
| --- | --- |
| `/tablets-para-volta-as-aulas-2026/` | **No ar (12/08/2026).** Trio canônico. Depois do slug novo existir, acrescentar uma linha “alternativas”. |
| `/tablets-para-volta-as-aulas-2026-2/` → `/alternativas-galaxy-tab-s10-fe-ipad-estudar/` | **Retarget, não 301 para a canônica.** HTML em `articles/alternativas-galaxy-tab-s10-fe-ipad-estudar.html`. Criar post no slug novo → recapturar preço → publicar → 301 do `-2`. |
| `/lg-au801-50-review/` e `/lg-55au801-review-2026/` | Conferir se é o mesmo AU801. Se for, consolidar. |
| `/apple-tv-4k/` | Padrão de layout; limpar “testamos a fundo” e barra de estrelas como se fossem da casa. |

## P1 — home / recortes recentes

| URL | Tipo |
| --- | --- |
| `/presentes-dia-dos-pais-2026-tech-premium/` | guia |
| `/presentes-dia-dos-pais-tech-ate-300/` | guia |
| `/galaxy-watch7-44mm-vale-a-pena/` | review (wearable: disclaimer de saúde) |
| `/galaxy-s24-fe-em-2026/` | review |
| `/fire-tv-stick-4k-wifi-6/` | review |
| `/edifier-w820nb-review-2026-vale-a-pena/` | review |
| `/jbl-wave-buds-2-review-2026-vale-a-pena/` | review |
| `/lenovo-ideapad-1-i3-1215u-vale-a-pena-em-2026/` | review |
| `/lenovo-ideapad-slim-3-notebook-2026/` | review |
| `/redmi-note-15-pro-vale-a-pena/` | review (tom de vitrine) |
| `/moto-g56-5g-review/` | review |

## P2 — catálogo que ainda parece landing

| URL | Nota |
| --- | --- |
| `/soundcore-liberty-4-nc-vale-a-pena/` | “98,5%” só com atribuição da marca |
| `/samsung-galaxy-buds-core-vale-a-pena/` | |
| `/redmi-buds-6-play-review-2026-vale-a-pena/` | |
| `/qcy-t13-anc-review-2026-vale-a-pena/` | |
| `/melhor-fone-bluetooth-ate-500-reais-2026/` | guia; precisa se sustentar sozinho |
| `/iphone-16e-review-2026/` | |
| `/samsung-galaxy-s25-5g-review/` | |
| `/samsung-galaxy-a16-review/` | |
| `/xiaomi-redmi-note-14-pro-plus-review-2026/` | |
| `/samsung-galaxy-tab-s10-fe-5g-vale-a-pena/` | cruzar com os guias de tablet |
| `/samsung-galaxy-book4-review-2026/` | |
| `/xiaomi-smart-band-9-active-vale-a-pena/` | saúde |
| `/xiaomi-smart-band-10-vale-a-pena/` | saúde |
| `/samsung-galaxy-fit3-vale-a-pena/` | saúde |

## P3 — TV, som, casa

| URL | Nota |
| --- | --- |
| `/roku-vs-fire-tv-stick-4k/` | comparativo |
| `/samsung-s90f-qd-oled-review/` | |
| `/samsung-u8600f-review/` | |
| `/samsung-u8100f-smart-tv-4k-review/` | |
| `/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019/` | |
| `/lg-au801-50-review/` | ver P0 |
| `/lg-55au801-review-2026/` | ver P0 |
| `/philips-50pug7019-review/` | |
| `/tcl-c6k-review-2026/` | |
| `/samsung-hw-b400f-review/` | |
| `/jbl-cinema-sb180-review-vale-a-pena/` | |
| `/lg-sqc1-review-2026-vale-a-pena/` | |
| `/samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1/` | |
| `/purificador-de-agua-electrolux-pe12g-review/` | sem alegação médica |
| `/garrafa-termica-quick-flip-stanley-710ml/` | |
| `/kit-teclado-mouse-ultra-slim/` | risco de afiliado fino |
| `/camera-lampada-360-yoosee-lp8177-review-2026/` | privacidade / segurança |
| `/good-vision-kit-cameras-wifi-review/` | |
| `/melhores-cameras-de-seguranca-wi-fi-2026/` | guia |

## Páginas institucionais (não são review, mas entram no Who/How)

- `/sobre-a-curadoria-prime/` — alinhar o box de tipo de análise ao texto oficial.
- `/transparencia-curadoria-prime/`
- `/bio-do-cristian/` e `/nossa-prova/` — E-E-A-T; não inventar credencial de laboratório.
- `/sobre-nos-curadoria-prime/` — se duplicar o Sobre, consolidar.
- Termos, privacidade, cookies, isenção, contatos — só se o texto contradisser as regras.

## Como pedir cada URL à skill

> Atualiza `/slug/` no layout Apple TV 4K. Segue as regras editoriais e o Google. Aqui estão as fontes do dia: [colar URLs + preços + notas].

A skill devolve diagnóstico → alterações → artigo → registro → fontes → pendências → checklist. Sem isso, não cole no WordPress.
