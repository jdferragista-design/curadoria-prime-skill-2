# Histórico de preço

Sim, a skill guarda histórico. **Não** inventa gráfico. **Não**
raspa Amazon/ML em massa. **Não** cita “piso histórico da internet”
sem fonte nomeada.

## O que é viável

| Fonte | Usar? | Como |
| --- | --- | --- |
| Captura da casa (print do editor + relatório) | **Sim — padrão** | Uma linha no [LEDGER.csv](../assets/historico-precos/LEDGER.csv) por loja/variante/data |
| Zoom, Buscapé, Keepa, similar | Só se a página estiver aberta **hoje** | Creditar veículo + data. Não copiar o gráfico como se fosse nosso |
| Memória do artigo antigo no ar | Sim, se o preço estiver **datado** no HTML | Registrar a data que o texto declara, não “hoje” |
| Preço sem data no texto velho | Não | Não entra no ledger |
| API Keepa / scraper | Não, salvo o editor entregar chave e ToS ok | Fora do fluxo padrão |

O histórico da casa é o ativo: em 6–8 atualizações o SKU já tem
curva suficiente para a seção “comprar ou esperar”.

## O que o artigo pode dizer

| Capturas no ledger (mesmo SKU + mesma loja + mesma variante) | Texto permitido |
| --- | --- |
| 1 | “Nesta data (DD/MM), na [loja], R$ …” |
| 2 | “Em DD/MM estava R$ X; em DD/MM, R$ Y” — subiu / caiu / estável |
| 3+ em dias diferentes | “Faixa observada pela Curadoria, de R$ A a R$ B (loja, período)” |
| Qualquer N | Nunca “menor preço da internet”, “piso histórico garantido”, “vai cair na Black Friday” |

Tabela e Pix **não** se misturam na mesma série. Internacional e
nacional são séries diferentes. Wi-Fi e 5G também.

## Quando anexar

No fim de **todo** `RELATÓRIO DE MERCADO`:

1. Abrir `assets/historico-precos/LEDGER.csv`.
2. Acrescentar uma linha por preço **novo** do dia (não regravar
   linha antiga).
3. Preencher a seção `HISTÓRICO (ledger da casa)` do template.
4. Se houver 2+ pontos, a skill de review **pode** usar isso em
   “comprar agora ou esperar”. Com 1 ponto, essa seção não inventa
   tendência.

Chave da linha: `data + sku_id + loja + variante`.
Se a chave já existe com o mesmo preço, não duplicar.
Se o preço mudou no mesmo dia, atualizar a linha e notar no campo
`obs` (“recaptura no mesmo dia”).

## O que não vai para o HTML público

- Planilha inteira.
- Preço de catálogo ML usado como ponto da série (pode ir no ledger
  com `tipo=catalogo`, mas **não** entra na frase de tendência).
- Terceiro sem URL e data.
