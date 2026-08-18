# ESTADO — 3548 (Redmi Buds 6 Play · `redmi-buds-6-play-review-2026-vale-a-pena`)

**Status:** ✅ REESCRITO em 17/08/2026 · checker 14/14, 0 erros · 5333 palavras · nota 8,0/10 · 8 imagens (6 no corpo)
**Arquivo:** `articles/redmi-buds-6-play-review-2026-vale-a-pena.html`

## 🔴 Achados críticos no publicado

### 1. URGÊNCIA VENCIDA NO AR
O card de compra dizia: *"chega grátis entre terça e quinta — **a tempo do Dia dos Pais (09/08)**"*.
Hoje é **17/08**: a data passou há mais de uma semana. É o mesmo erro já corrigido no guia 3336 em
14/08 ("chega antes do Dia dos Pais"), que reapareceu aqui. **Removido.**

### 2. "207 mil+ avaliações reais" — número inflado
Hero e corpo citavam **207.851 avaliações**. É o total do **catálogo** do Mercado Livre, que agrega
dezenas de variações e produtos correlatos — não são avaliações do anúncio analisado. Substituído
por descrição qualitativa (selo de mais vendido, nota alta consistente) sem número não verificável.

### 3. Três depoimentos com selo "compra verificada"
Mesma violação da regra 4.2 já corrigida no 3523: citações entre aspas com selo. → **síntese
editorial**, sem aspas e sem selo. Também saiu "compradores verificados" (2×) do bloco de metodologia.

### 4. Preços de 01/08 desatualizados — dois com erro de direção
| Produto | publicado (01/08) | **real (17/08)** | impacto |
|---|---|---|---|
| Redmi Buds 6 Play | R$ 79,90 Pix | **R$ 78,99** | menor |
| QCY T13 ANC | R$ 143,55 | **R$ 186,10 / R$ 199** | 🔴 grave |
| Galaxy Buds Core | R$ 242,19 | **R$ 219,31 / R$ 268,20** | corrigido |

O caso do QCY era o pior: o texto mandava o leitor ao QCY "por um pouco mais" citando R$ 143,55.
Hoje o QCY custa **2,5× o Redmi** — a recomendação mudava de sentido. Reescrita com o alerta.
Removido também o nome do vendedor ("GSOTECNO"), que muda a cada consulta.

### 5. "Problemas Comuns" com rótulo de frequência sem base
Os 4 itens traziam "Frequência: alta / moderada / baixa" **sem dump de avaliações**. Pela regra
§18.3 e pela lição §15.2, a seção foi renomeada para **"Limitações conhecidas"** e abre com um aviso
declarando que a lista é **dedutiva** (derivada da ficha técnica), não contagem. Nenhum item tem
rótulo de frequência.

## ➕ Adicionado
- **Faixa de preço dos últimos 6 meses** (regra §18): Redmi R$ 78 / R$ 79–120 / **R$ 78,99 no piso
  histórico** · QCY · Buds Core, com leitura por produto.
- Bloco **"Prós e contras"** (não existia): 8 prós + 7 Pontos de Atenção.
- Seção **"não é para quem"** com 5 perfis.
- JSON-LD `@graph` completo: Article + Review + FAQPage (5 perguntas espelhando a visível) +
  BreadcrumbList. Sem `offers`, sem `aggregateRating`, sem `priceValidUntil`.

## Preços verificados (17/08/2026)
`meli.la/1J2VMuY` → **MLB55462947**, R$ 78,99, azul celeste, selo mais vendido.
Cor preta R$ 98 · outra variação R$ 90,55 — **diferença de até R$ 20 pela cor**, avisado no card.

## Faixa histórica (mar–ago/2026)
Piso R$ 77,89 (KaBuM) · R$ 104,90 em 27/03 (Amazon) · R$ 113,99 em 01/12 (Magalu) · hoje R$ 78,99.
**Está no piso — não há motivo para esperar queda.**

## 🔴 Pendência
Subir **dump de avaliações do Redmi** (Amazon + ML) para converter "Limitações conhecidas" em
frequência real, como foi feito em 3523/3527/3545. Enquanto não houver, a seção permanece declarada
como dedutiva.

## Validação
JSON-LD válido (4 tipos) · 0 offers/aggregateRating/priceValidUntil · 8 afiliados, 100% com `rel`
completo · tags balanceadas · 0 base64 · 0 "compra verificada" · 0 menção a Dia dos Pais.

---

## Corroboração por fontes externas (17/08/2026)

Cliente perguntou se dava para buscar os dados em outros sites, como o da própria marca. **Deu — e
encontrou erros que nenhuma leitura de avaliação pegaria.**

### 🔴 Três erros de ficha técnica corrigidos
| Item | O artigo dizia | **Ficha oficial (KaBuM + Casas Bahia)** |
|---|---|---|
| Codec | "SBC **e AAC**" | **SBC apenas** — sem AAC, aptX ou LDAC |
| Cabo de carregamento | não mencionado | **NÃO acompanha** — "deve ser adquirido separadamente" |
| Identificação | ausente | modelo **M2420E1** · Anatel **077062409185** |

O cabo é o mais sensível: o leitor compra achando que vem na caixa. Virou caixa de alerta própria.
Acrescentados também impedância (16 Ω) e capacidades reais (57 mAh por fone / 600 mAh no estojo).

### 🔴 Limitação real que não estava documentada
**Volume máximo baixo** — é a queixa que mais se repete entre os compradores europeus, aparecendo
até em avaliações 5 estrelas: *"uma desvantagem é que o volume máximo para música é um pouco baixo"*.
O PcComponentes lista "volume máximo" entre os pontos de melhoria citados pelos usuários.

Refinada também a queixa do microfone: é adequado para **chamadas**, mas ruim para **gravar áudios**
— distinção que os relatos fazem e o artigo não fazia.

### Fontes usadas e declaradas no texto
- **KaBuM / Casas Bahia** — ficha do fabricante, mais completa que a página oficial da Xiaomi.
- **PcComponentes (PT/ES)** — +300 opiniões nas cores preta e azul, média 4,6/5. **Declarado no
  artigo que são compradores europeus.**
- **Versus** — notas por critério: bateria 9,7 · conforto 9,4 · construção 9,3 · design 9,0 · **som 8,6**.
  Confirma o padrão: bateria é o destaque, som é o critério mais mediano.

### O aviso da seção mudou
Era: *"as limitações abaixo são deduzidas da ficha técnica"*. Agora declara o cruzamento de **três
fontes independentes** e explica que continua **sem rótulo de frequência**, porque frequência exige
contagem das avaliações brasileiras.

### Regra gravada — §18.6 em `regras-editoriais.md`
"Sem dump de avaliações? Use fontes alternativas (mas nomeie cada uma)", com tabela de
confiabilidade por tipo de fonte e 4 regras de uso (publicar só o que converge ou nomear a fonte;
dizer de onde veio; nunca virar rótulo de frequência; nunca passar relato estrangeiro como brasileiro).

**Validação:** checker 14/14, 0 erros · 4.794 palavras (era 4.261) · 0 `offers`/`aggregateRating` ·
8 afiliados 100% com `rel` · tags balanceadas · zero ocorrência de "SBC e AAC".


---

## Sincronização automática (17/08/2026)

Valores conferidos direto do arquivo, não digitados à mão:

| Campo | Valor real |
|---|---|
| Nota (JSON-LD e texto) | **8,0/10** |
| Palavras | 5333 |
| Imagens | 8 (6 no corpo) |
| Nota de revisão pública | presente |
| Link da régua | `/como-avaliamos/` ✅ |

⚠️ Este arquivo já esteve dessincronizado (achado C1 da auditoria): declarava nota e
contagem de palavras anteriores às correções. Ao alterar o artigo, **regenerar estes
campos** em vez de reescrevê-los de memória.
