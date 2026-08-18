# Checklist de bloqueio de publicação

O artigo **não pode ser publicado** se qualquer item for “não”.
A IA preenche o checklist na entrega. O editor humano é quem libera.

> **Espelho parcial da seção 15** de
> [`../references/regras-editoriais.md`](../references/regras-editoriais.md), que é a
> fonte canônica. Este arquivo é o resumo operacional para uso durante a entrega;
> quando a seção 15 mudar, atualize-o junto.

## Transparência

- [ ] O tipo de análise está identificado?
- [ ] Toda linguagem de teste próprio é verdadeira e documentada?
- [ ] O aviso de afiliado está visível?
- [ ] O autor humano responsável revisou o conteúdo?

## Mercado (skill curadoria-mercado)

- [ ] Existe `RELATÓRIO DE MERCADO` desta URL, com data?
- [ ] Cada CTA aponta para um checkout identificado (não catálogo ML)?
- [ ] Internacional / 64 GB / Wi-Fi≠5G / usado estão explícitos ou o SKU saiu?
- [ ] Nenhum SKU indicado perde em preço **e** em ficha para outro já no site?
- [ ] Não há R$ no botão sem captura do dia?

## Fatos e fontes

- [ ] Modelo, variante, especificações e certificações foram conferidos?
- [ ] Preço, estoque e avaliações externas possuem fonte e data?
- [ ] As fontes estão listadas com links diretos?
- [ ] Divergências importantes foram explicadas?
- [ ] Não há URLs, citações ou números inventados?

## Qualidade

- [ ] A página responde rapidamente à intenção de busca?
- [ ] Há informação própria além de ficha técnica e resumo de terceiros?
- [ ] Está claro quem deve e quem não deve comprar?
- [ ] Cada produto recomendado tem `Pontos de Atenção` / `Contras` / `Pontos Negativos` com ≥3 itens verificáveis (§2.7)?
- [ ] Prós, contras, nota e veredito são coerentes?
- [ ] Não há introdução genérica, repetição ou superlativos vazios?

## Avaliações e schema

- [ ] Avaliações externas são apresentadas apenas como dados de terceiros?
- [ ] Paráfrases não aparecem como citações literais?
- [ ] Não existe `AggregateRating` externo?
- [ ] A nota editorial possui escala e critérios claros — ou foi omitida?
- [ ] Todo schema corresponde ao conteúdo visível?

## Atualização e SEO

- [ ] A URL e o canonical corretos foram preservados?
- [ ] A data foi alterada apenas após mudança substancial?
- [ ] Não existe outro artigo concorrendo pela mesma intenção?
- [ ] Links internos e externos são relevantes?
- [ ] Título e H1 não prometem teste que não ocorreu?

## Marcadores internos (remover antes do ar)

- [ ] Nenhum `[VERIFICAÇÃO HUMANA NECESSÁRIA]` restou no HTML final
- [ ] Links afiliados têm `rel="sponsored nofollow"`
- [ ] Imagem de IA, se houver, tem a legenda oficial

## Faixa de preço histórica (§18)

- [ ] O artigo traz a **faixa dos últimos 6 meses** do produto principal?
- [ ] Cada produto tem **piso já visto**, **faixa típica**, **preço de hoje com data** e **leitura**?
- [ ] O "piso já visto" está declarado como valor anunciado no período, **não** como preço de hoje?
- [ ] Toda loja citada foi **re-verificada na data da revisão**? (se não, remover a loja)
- [ ] A faixa histórica ficou **fora** do JSON-LD (sem `offers`, sem `priceValidUntil`)?
- [ ] As datas e lojas de cada valor estão anotadas no dossiê em `audit/`?

## §19 — Nota editorial (bloqueadores)

- [ ] A nota é **múltiplo de 0,5**? (8,2 / 8,4 / 8,8 = ❌ viola a política pública)
- [ ] Existe badge de nota no hero?
- [ ] Existe a seção "🧮 Como chegamos ao X" com a tabela dos 6 critérios e pesos?
- [ ] O link aponta para `/como-avaliamos/` (e **não** para `/como-avaliamos-e-pontuamos-produtos/`, que dá 404)?
- [ ] A soma das contribuições confere com o total exibido?
- [ ] Existe a caixa "O que essa nota não mede"?
- [ ] `ratingValue` do JSON-LD é igual à nota visível no texto?
- [ ] Nenhuma grade de características se apresenta como "NOTA GERAL" sem rótulo?

## §20 — Imagens (bloqueadores)

- [ ] Inventariei as imagens do post publicado **antes** de reescrever?
- [ ] Toda imagem que existia no corpo tem destino na nova versão (ou justificativa)?
- [ ] Todo `src` veio da API de mídia, com o nome de arquivo exato?
- [ ] Cada imagem tem `alt` descritivo (sem emoji) e legenda?
- [ ] As imagens do corpo têm `loading="lazy"`?
- [ ] O artigo tem mais do que apenas a foto do autor no corpo?
- [ ] Rodei `python3 tools/checar_imagens.py articles/<arquivo>.html` (0 erros)?

## §22 — Preservação de imagens (BLOQUEADOR ABSOLUTO)

Regra permanente do cliente: **nunca remover imagens ao atualizar um artigo.**

- [ ] Inventariei as imagens ANTES de começar a editar?
- [ ] Toda imagem da versão anterior continua presente na nova?
- [ ] Rodei `python3 tools/checar_imagens_preservadas.py articles/<arquivo>.html` com 0 perdas?
- [ ] Se alguma imagem saiu, tenho autorização explícita do cliente registrada?
- [ ] Aproveitei imagens órfãs do produto que já estão na biblioteca?
