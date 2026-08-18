# ESTADO — 3523 (QCY T13 ANC · `qcy-t13-anc-review-2026-vale-a-pena`)

**Status:** ✅ REESCRITO e REORDENADO em 18/08/2026 · checker 14/14, 0 erros · 6624 palavras · nota 8,5/10 ⭐ · 7 imagens (6 no corpo)

> ⏳ **AGUARDANDO APROVAÇÃO DO CLIENTE.** Artigo alinhado ao modelo canônico
> (casca Apple TV 4K) com as 4 alterações: índice em 2 colunas · resposta
> rápida em 4 cards · cards de venda sem imagem · notas do veredito em grade
> 3×3. Pendente a recolagem no WordPress.

**Arquivo:** `articles/qcy-t13-anc-review-2026-vale-a-pena.html`

## 🔴 Achado crítico: ordem das seções fora do padrão

Era **o desvio mais grave do cluster**. "Onde comprar" era a **última** seção
do artigo — depois do veredito e do FAQ — e a ficha técnica, a penúltima. O
leitor precisava percorrer o texto inteiro para achar preço e onde comprar.

**Nova ordem** (padrão do modelo): 1. ⚡ Resposta rápida → 2. 🛒 Onde comprar
→ 3. 📋 Ficha técnica → 4–14 seções de decisão → FAQ. Faixa de preço, fontes,
caixa do autor e JSON-LD permanecem no rodapé.

## ➕ Adicionado / corrigido nesta rodada

- **Seção "⚡ Resposta rápida"** criada com os 4 cards (vale / depende /
  espera / não vale), citando Galaxy Buds Core e Edifier W820NB pelo nome e a
  faixa R$ 186–199.
- **Grade de notas 3×3** no veredito, com as 6 notas reais do scorecard mais a
  nota geral 8,5 — batem com o `ratingValue` do JSON-LD.
- **Índice reconstruído** a partir dos H2 reais: `repeat(2, 1fr)`, 14 itens.
- **Scorecard longo condensado**: 5.773 → 1.172 caracteres, com link para
  `/como-avaliamos/`. Fontes recolhidas em `<details>`.
- **Enxugamento** (pedido do cliente): 6.246 → 5.773 palavras. Saiu do FAQ a
  pergunta "por que o ANC chia com vento" (duplicava a seção 7) e o bloco
  "Entrega e nota fiscal" foi condensado de 163 para 62 palavras — é queixa de
  logística de vendedor, não do produto.

## 🖼️ Imagens (18/08/2026)

Cobertura final, 7 imagens:

| Posição | Arquivo |
|---|---|
| hero | `qcy-t13-anc-destaque.webp` |
| 4. O que vem na caixa | `cn-11134207-…jpeg` |
| 5. Design | `qcy-t13-anc-branco-estojo-aberto.webp` ← nova |
| 6. Qualidade de som | `pessoa-usando-…transporte-publico.jpeg` |
| 7. ANC de 28dB | `b0350ffe-…png` ← remanejada |
| 10. App QCY | `QCY-T13-ANC-app-equalizador-…webp` ← nova |
| caixa do autor | `cristiano-curadoria-prime.jpg` |

### 🔴 Duas imagens rejeitadas por modelo trocado

O T13 ANC é o modelo **HT06**; o T13 comum é outro produto (sem ANC, driver
7,2 mm, BT 5.1). No CDN da QCY o nome do arquivo carrega o código do modelo.
Cruzando o MD5 de cada candidata com o catálogo oficial:

- `qcy-t13-anc-branco-estojo-aberto` → `HT06_-2_58b1fcdf…` = **T13 ANC** ✅ usada
- `qcy-t13-anc-preto-fones-estojo` → `T13_-2_73789273…` = T13 comum ❌ **rejeitada**
- `qcy-t13-anc-branco-vista-frontal` → nenhum HT06 bateu; dHash a 13 do T13
  comum contra 44 do ANC ❌ **rejeitada**

O cliente confirmou visualmente que a preta é de outro produto. As duas
rejeitadas permanecem na biblioteca do WordPress, sem uso.

### Correção de layout shift

As 4 imagens preexistentes declaravam `width="758" height="505"`, mas os
arquivos reais são 1424×748, 800×800, 2048×2048 e 1024×1024. Proporção errada
no atributo faz o navegador reservar espaço com formato errado. Corrigido
contra as dimensões reais da API de mídia.

## Validação (rodada em 18/08/2026)

| Campo | Valor real |
|---|---|
| Nota (JSON-LD e texto) | **8,5/10** ⭐ |
| Palavras (contagem do `checar_estado.py`) | 6624 |
| Palavras visíveis (sem JSON-LD e `<details>`) | 5.802 |
| H2 | 16 |
| Imagens | 7 (6 no corpo) |
| Links afiliados com `rel` | 6, 100% |
| `offers` / `aggregateRating` | 0 / 0 ✅ |
| Perguntas no FAQPage | 5 |
| Link da régua | `/como-avaliamos/` ✅ |

Conformidade 14/14 · alt, lazy e width/height em todas · tags balanceadas ·
JSON-LD válido · zero "compra verificada" no corpo (a única ocorrência está no
comentário de cabeçalho, descrevendo a correção já feita).

⚠️ `checar_imagens.py` acusa 2 erros `[src-existe]` para as imagens novas. É
**falso-positivo**: o export `imagens/curadoriaprime.WordPress.2026-08-17.xml`
tem anexos até 16/08 e os uploads foram em 18/08 (IDs 4960 às 10:49 e 4965 às
11:58, confirmados via `/wp-json/wp/v2/media/<id>`). Some no próximo export.

## Scorecard v2.0 (soma 8,675 → 8,5)

| Critério | Peso | Nota |
|---|---|---|
| Custo-benefício | 30% | 9,5 |
| Satisfação verificada | 25% | 9,0 |
| Ficha técnica | 20% | 8,0 |
| Recursos e usabilidade | 10% | 8,5 |
| Consenso técnico | 10% | 8,0 |
| Confiança e suporte | 5% | 6,5 |

**Sem caixa de "nota revisada"** — diferente de Redmi (8,2→8,0), Edifier
(8,8→8,5) e JBL (8,4→8,5), a nota do QCY **nunca mudou**: já era 8,5 antes da
régua v2.0 e continuou 8,5 no recálculo. O commit `6f52fa1`, que realinhou as
notas do cluster, não alterou este arquivo. Não há revisão a comunicar.

## 🔴 Pendências

- Recolagem no WordPress (o arquivo local está à frente do publicado).
- Seções 8, 9 e 11–14 sem imagem — são de análise pura, como no modelo. Não é lacuna.
- Avaliar "Comprar agora ou esperar" como seção própria; hoje o tema está
  diluído na faixa de preço. Mesma lacuna aberta no 3548.

---

⚠️ Regenerar os números deste arquivo **por script** ao alterar o artigo
(§24). Nunca digitar de memória — foi assim que 3548 e 3550 dessincronizaram.
