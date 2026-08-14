# `audit/` — estado real dos artigos publicados e o que vem pela frente

Duas coisas: o que está errado no ar hoje, e o que se pretende publicar.
Nessa ordem — corrigir vem antes de produzir.

---

## `auditoria-48-artigos.csv`

Varredura dos 48 posts publicados em curadoriaprime.com, feita via WP REST API
em 13/08/2026, com `tools/checar_conformidade.py`.

### O resultado

**27 dos 48 artigos (56%) têm pelo menos um problema.**

| Problema | Ocorrências | Artigos |
|---|---|---|
| Alegação de teste físico que não foi feito | 37 | 19 |
| Link de afiliado sem `rel="sponsored"` | 48 | 12 |
| Sem divulgação de afiliado | 10 | 10 |

Maior risco por volume de ocorrências: posts **3153** (26), **3226** (23),
**3523** (21), **3139** (18), **3002** (18), **3183** (17), **3545** (13),
**3033** (11), **2888** (11), **2884** (11), **4251** (10), **2892** (9).

### Por que isso é urgente e não cosmético

As duas primeiras categorias têm consequência concreta, não teórica.

Afirmar "testamos" sobre um produto que não foi testado é publicidade enganosa
pelo **art. 37 do CDC**. Não é uma questão de estilo editorial.

Link de afiliado sem `rel="sponsored"` é motivo documentado de **ação manual** do
Google. E o padrão de penalização mais próximo deste site — sites de afiliado com
comparações geradas por IA, sem experiência de primeira mão — teve perdas de
**40–70% de tráfego** no update de março de 2026.

### Um caso que merece atenção

Os posts **4537** (`/apple-tv-4k`) e **4541** contêm, no mesmo texto, a ressalva
correta de que não houve teste físico **e** a frase "Testamos a fundo".

Ao corrigir: **remova a alegação, nunca a ressalva.** É fácil fazer o inverso por
distração, e o inverso é o pior resultado possível.

### Substituições sugeridas

A coluna `SUGESTOES` do CSV traz a reescrita para cada trecho. O padrão:

| Em vez de | Escreva |
|---|---|
| "testamos" | "analisamos as especificações e cruzamos com relatos publicados por compradores" |
| "unboxing" | "o que vem na caixa" |
| "medimos" | "os dados oficiais indicam" |

### Como corrigir

```bash
python3 tools/corrigir_artigos.py --dry-run              # ver o que mudaria
python3 tools/corrigir_artigos.py --relatorio-alegacoes  # trechos p/ reescrita humana
export WP_USER="..." WP_APP_PASSWORD="..."
python3 tools/corrigir_artigos.py --aplicar
```

`rel` e divulgação o script resolve. As 37 alegações de teste exigem reescrita
humana — mudam o significado do texto.

### Um item de higiene

IDs **4474** e **4476** são o mesmo artigo (`tablets-para-volta-as-aulas-2026`).
Conteúdo duplicado competindo consigo mesmo. Consolidar com 301 do 4474 para o 4476.

---

## `pauta-90-dias.csv`

36 pautas entre 18/08 e 18/12/2026: 18 listas, 6 guias de Black Friday a partir
de 15/09 (mais uma página viva em 13/11), e a consolidação da duplicata em 25/09.

**Esta pauta está deliberadamente atrás da fila de correção.**

Com 27 artigos defeituosos no ar, publicar conteúdo novo aumenta a superfície de
risco antes de reduzi-la. A skill `curadoria-review` já estabelece a prioridade
certa — atualizar o que existe, ~1 artigo/dia — e ela vence enquanto o passivo
não for zerado.

Ordem recomendada:

1. **P0** — 12 artigos de maior risco: remover alegações de teste, adicionar `rel`
2. **P1** — os 15 restantes com problema
3. **P2** — consolidar a duplicata 4474/4476
4. **P3** — só então retomar a pauta, com a trava rodando em cada publicação

Os guias de Black Friday têm data-limite real (15/09 em diante) e são a única
parte da pauta que talvez não possa esperar o passivo inteiro. Se precisar
sobrepor, sobreponha esses — nunca as listas comuns.

---

## Reproduzir a auditoria

```bash
python3 tools/checar_conformidade.py 'articles/*.html' --resumo
```

Para reavaliar o site publicado, a WP REST API está aberta em
`https://curadoriaprime.com/wp-json/wp/v2/posts?per_page=50`.
