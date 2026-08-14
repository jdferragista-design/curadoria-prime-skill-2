# Ledger de preços — Curadoria Prime

Uma linha = uma captura real. A skill `curadoria-mercado` acrescenta
ao fechar o relatório. O humano pode colar print; a IA preenche a linha.

Arquivo: [LEDGER.csv](LEDGER.csv)

Colunas:

| Campo | Exemplo |
| --- | --- |
| data | 2026-08-12 |
| sku_id | galaxy-tab-s10-fe |
| codigo | SM-X520 |
| variante | wifi-128 |
| loja | amazon \| ml \| samsung \| apple \| outro |
| tipo | anuncio \| catalogo \| tabela-marca |
| preco_pix | 3127.07 |
| preco_12x_parcela | 283.33 |
| preco_12x_total | 3398.97 |
| de | 4199 |
| vendedor | loja-samsung \| loja-oficial-apple \| terceiro \| internacional |
| url | https://… |
| artigo | /tablets-para-volta-as-aulas-2026/ |
| obs | |

`preco_pix` vazio = só parcelado naquele dia. Não inventar Pix.
`tipo=catalogo` não alimenta frase de tendência no artigo.
