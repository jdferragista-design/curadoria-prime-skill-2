---
name: curadoria-mercado
description: >-
  Pesquisa aprofundada de mercado (Amazon, Mercado Livre, loja oficial)
  para cada artigo da Curadoria Prime. Use before writing buy cards,
  CTAs, "onde comprar", preços, ou ao decidir se um SKU fica no guia.
  Also use when the user pede pesquisa de mercado, análise de anúncio,
  loja confiável, internacional vs nacional, ou "qual fica no artigo".
---

# Curadoria Mercado

Skill **obrigatória em todo artigo** (review, guia, atualização).
Roda **antes** de gravar preço, CTA ou card de compra.

Não publica. Não inventa preço, estoque, vendedor, Anatel, caixa
nem “loja oficial”. Sem captura do dia, o SKU não entra como indicação.

A skill irmã [curadoria-review](../curadoria-review/SKILL.md) redige.
Esta decide **o que o varejo brasileiro sustenta**.

Leia junto:

- [assets/template-relatorio-mercado.md](assets/template-relatorio-mercado.md)
- [references/armadilhas-marketplace.md](references/armadilhas-marketplace.md)
- [references/historico-preco.md](references/historico-preco.md)
- [assets/historico-precos/LEDGER.csv](assets/historico-precos/LEDGER.csv)
- [../curadoria-review/references/regras-editoriais.md](../curadoria-review/references/regras-editoriais.md)
- [../curadoria-review/references/cores.md](../curadoria-review/references/cores.md)

## Quando rodar

1. Artigo novo — depois do briefing, **antes** da redação dos cards.
2. Atualização — ao recapturar preço ou trocar afiliado.
3. Guia com N produtos — **um SKU de cada vez**, depois o cruzamento.
4. Sempre que o editor colar print/preço ou perguntar “fica no artigo?”.

Sem `RELATÓRIO DE MERCADO`, o HTML de compra **não é escrito**.

## O que a pesquisa precisa responder

Para cada SKU:

1. **Qual unidade é?** Código (SM-X520, ZAFR0856BR, A2696, A3354…).
   Wi-Fi ≠ 5G ≠ Cellular. 64 ≠ 128 ≠ 256. Cor só se mudar o anúncio.
2. **Quem vende?** Loja da marca, loja oficial no marketplace,
   seller terceiro, catálogo multi-vendedor, internacional, usado,
   recondicionado.
3. **Quanto custa hoje?** Pix / à vista / 12x, de/por, data, URL.
4. **O anúncio é o mesmo produto da ficha oficial?**
5. **O preço ganha de outro SKU já recomendado no site?**
   Se perde em preço **e** em ficha, não é alternativa — é ruído.
6. **Dá para indicar o checkout?** Se a resposta for “depende do
   vendedor”, não há CTA. Há alerta.

## Protocolo (nessa ordem)

### 1. Ficha oficial BR

- Fabricante `.com/br` ou Newsroom BR. Sem página BR: declarar.
- Anotar: modelo, caixa, IP, caneta, garantia anunciada pela marca.
- Loja oficial da marca (Apple Store, Samsung Shop, Lenovo.com):
  preço de **tabela**, não “o preço do mercado”.

### 2. Amazon Brasil

- Abrir o anúncio, não o resultado da busca.
- Registrar: vendedor (loja Samsung / Apple / Lenovo / outro),
  variante, Pix, 12x, nota da **página** (não do site inteiro),
  data, se diz “internacional”, “importado”, “recondicionado”.
- “Escolha da Amazon” e “+N compras no mês” **não** são prova de
  qualidade nem de unidade nacional.
- Sem short link afiliado confiável: peça ao editor. Não invente
  `link.amazon/…`.

### 3. Mercado Livre

- Separar **anúncio de um vendedor** de **catálogo** (`/p/MLB…`).
- Catálogo: nota e “+N vendidos” são do **catálogo**, não da loja.
  Não vira CTA. Pode virar alerta.
- Conferir: Loja Oficial da marca vs terceiro; Full vs não;
  nacional vs internacional; novo vs usado/recondicionado.
- Título mentiroso é comum: “Redmi Pad 7” no lugar de Pad 7;
  FE no lugar de FE+; 5G no anúncio Wi-Fi.
- Sem `meli.la/…` do editor: não invente.

### 4. Cruzar as três prateleiras

Montar a matriz do template. Preencher **fica / ressalva / fora**.

### 5. Anexar ao histórico

Acrescentar cada preço **novo** do dia em
[LEDGER.csv](assets/historico-precos/LEDGER.csv). Regras:
[historico-preco.md](references/historico-preco.md).

- 1 ponto no ledger → o artigo só diz “nesta data”.
- 2 pontos (mesma loja + variante) → pode dizer subiu/caiu.
- 3+ → faixa observada pela casa. Nunca “piso da internet”.

### 6. Só então escrever cards

- CTA só em checkout que passou no gate.
- Cor do botão = plataforma ([cores.md](../curadoria-review/references/cores.md)).
- Verde (“menor preço”) é **selo**, não cor da loja.
- Loja oficial da marca: botão sem `sponsored` se o link não é afiliado.
- Preço nos botões só com captura datada do editor.

## Gate — o SKU só vira indicação se

- [ ] Código / variante conferidos no anúncio **e** na ficha.
- [ ] Pelo menos um checkout nacional identificável **ou** o texto
      assume internacional com ressalva e **não** trata como compra segura.
- [ ] Preço do dia com loja + condição. Sem preço = sem R$ no botão.
- [ ] Não perde, ao mesmo tempo, de preço e de ficha para outro
      produto já indicado no mesmo site (ou no mesmo guia).
- [ ] Catálogo multi-vendedor não é o único “preço”.
- [ ] 64 GB, internacional, usado e “global” estão explícitos se existirem.

Se falhar um item: **fora da indicação**. Pode aparecer em
“ficou de fora, e por quê”.

## Vereditos possíveis (usar estes rótulos)

| Rótulo | O que fazer no artigo |
| --- | --- |
| **FICA** | Card + CTA + preço datado |
| **FICA COM RESSALVA** | Card + alerta âmbar **antes** do CTA (internacional, garantia, variante) |
| **SÓ UMA LOJA** | CTA só no checkout limpo; a outra loja vira “não indicamos” |
| **FORA** | Caixa “ficou de fora” — sem botão de compra |
| **SEM DADO** | Não escrever R$. Pedir captura ao editor |

## Entrega obrigatória

Título exatamente:

`RELATÓRIO DE MERCADO`

Depois: `VEREDITO POR SKU` → `O QUE FICA / O QUE SAI` →
`PREÇOS DO DIA` → `HISTÓRICO (ledger da casa)` →
`LINKS QUE FALTAM` → `RISCOS DE CHECKOUT`.

Use o [template](assets/template-relatorio-mercado.md).
Só então a skill de review monta o HTML.

## Proibido

- Inventar short link, Pix, “loja oficial”, Anatel, conteúdo da caixa.
- Copiar nota/volume do catálogo ML como se fosse de um seller.
- Tratar internacional como nacional porque o preço é bom.
- Indicar o mais barato do search sem abrir o anúncio.
- Manter SKU no guia só porque o artigo antigo tinha 7 itens.
- Rodar pesquisa “por cima” e já escrever os cards no mesmo fôlego
  sem o relatório.
- Inventar série histórica, “piso”, Black Friday futura ou gráfico
  de terceiro sem URL e data.

## Relação com o editor

O humano cola print ou URL. A skill não “acha o menor preço da
internet”. Ela classifica o que ele trouxe e o que as páginas
oficiais mostram.

Se faltar a outra loja: devolver **o link que ele deve abrir**,
não um preço inventado.
