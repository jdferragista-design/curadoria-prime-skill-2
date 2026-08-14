# Regras do Google aplicadas à Curadoria Prime

Fontes oficiais (consultar de novo se a data da página mudar):

- [Conteúdo útil, confiável e feito para pessoas](https://developers.google.com/search/docs/fundamentals/creating-helpful-content) (atualizado 2025-12-10)
- [Como escrever avaliações de alta qualidade](https://developers.google.com/search/docs/specialty/ecommerce/write-high-quality-reviews) (2025-12-10)
- [Políticas de spam](https://developers.google.com/search/docs/essentials/spam-policies) (2026-05-15) — afiliado fino, conteúdo em escala, scraping
- [Review snippet / AggregateRating](https://developers.google.com/search/docs/appearance/structured-data/review-snippet) (2026-07-24)
- [Links de saída: sponsored / nofollow](https://developers.google.com/search/docs/crawling-indexing/qualify-outbound-links)

As regras editoriais da casa (§2.4, §8, §9) já batem com o Google. Esta página traduz o que muda no texto e no schema.

## People-first, não search-first

Perguntas do Google que cada artigo precisa passar:

- Há informação, análise ou recorte **próprio** (não só reescrita de ficha)?
- O título descreve o conteúdo sem choque nem “teste” falso?
- Você indicaria a página a um amigo que vai gastar o dinheiro dele?
- A página vale mais do que as outras no resultado — ou é mais um “vale a pena 2026”?

**Who / How / Why** (obrigatório no layout):

| Pergunta | Como a Curadoria responde |
| --- | --- |
| **Who** | Bylines só depois da revisão humana. Bio do editor com o que ele realmente faz (uso diário de tech, não laboratório). |
| **How** | Box “Tipo de análise” + metodologia em 5 etapas. Sem teste físico, diga isso. IA é ferramenta de redação; o editor verifica fato. |
| **Why** | Ajudar a decidir a compra no Brasil. Se o porquê for “ranquear”, a página não sobe. |

Google **não** pune texto assistido por IA. Pune volume sem valor original ([scaled content abuse](https://developers.google.com/search/docs/essentials/spam-policies#scaled-content)). Atualizar 40 URLs no mesmo dia com o mesmo molde e zero fonte nova é o exemplo da política.

## Avaliação de produto (o que o Google pede)

Do guia oficial de reviews:

1. Avaliar do ponto de vista de quem compra.
2. Mostrar conhecimento do produto (variante, caixa, homologação, rivais).
3. Evidência do **trabalho feito** — na Curadoria isso é captura de preço, ficha oficial, divergência entre lojas, padrão de relatos. **Não** é inventar foto de bancada.
4. Medidas quantitativas quando existirem em fonte independente (atribuídas).
5. O que diferencia dos concorrentes.
6. Qual rival é melhor para qual uso.
7. Prós e contras com base em pesquisa própria (cruzamento), não em release.
8. O que mudou em relação à geração anterior.
9. Fatores que realmente decidem a compra.
10. Escolhas de design além do que a marca diz.
11. Links úteis (metodologia, comparativo, rival).
12. Mais de um vendedor.
13. “Melhor para X” só com critério e evidência.
14. Lista ranqueada precisa se sustentar sozinha.

Conflito aparente com “mostre experiência em primeira mão”:

- Google quer **prova de trabalho e honestidade**.
- Experiência inventada (“testamos a fundo”, foto gerada como se fosse a unidade) é pior do que pesquisa editorial declarada.
- A evidência legítima da casa: PDF/print de preço com data, URL oficial, teste de terceiro creditado, síntese de relatos com plataforma e data, alerta de versão BR.

## Afiliado fino (thin affiliation)

Página que só descreve o produto e empurra o link é spam. Defesa:

- veredito por perfil;
- quem **não** deve comprar;
- faixa de preço em que deixa de valer;
- armadilha de anúncio (internacional, CN, geração antiga);
- alternativa sem comissão quando for melhor;
- `rel="sponsored nofollow"` em todo link afiliado.

## Schema (o que o Google proíbe e o que a casa também proíbe)

- **Não** agregar nota/contagem da Amazon, Mercado Livre ou outro site em `AggregateRating` / `ratingCount` / `reviewCount`. Google: “Don't aggregate reviews or ratings from other websites.”
- **Não** marcar review que não está visível na página.
- **Não** inventar `priceValidUntil`.
- **Não** FAQPage schema só para ganhar rich result (elegibilidade já foi estreita).
- Review editorial próprio, **se** o editor humano assinou e a nota está visível: `Review.reviewRating` com autor real, escala visível, sem misturar N de loja.
- `Offer` só com preço verificado no dia da publicação.

Notas da Amazon/ML podem ficar **no texto**, com loja e data — nunca no JSON-LD como se fossem do site.

## SEO que o Google trata como spam se exagerar

- Keyword stuffing (nome do produto em toda frase).
- Ano no título só para parecer fresco.
- Duas URLs para a mesma intenção (os dois guias de tablets).
- Scraping de ficha do fabricante sem análise.
- Imagem de IA passando por teste próprio.

## O que NÃO fazer neste projeto

- Reescrever o site inteiro de uma vez com o mesmo template e preços velhos.
- Trocar slug ou criar `/produto-2027/` para “atualizar”.
- Mudar `dateModified` sem mudança editorial real.
- Declarar a leva “pronta para o ar” sem checklist humano por URL.
