# Gerador de artigo v2.0 — `tools/gerar_artigo.py`

Gera HTML Gutenberg no padrão golden a partir de JSON. 3 tipos: LISTA, REVIEW, VS.

## Uso

```bash
python3 tools/gerar_artigo.py exemplo.json -o artigo.html --schema --tipo lista
```

- `--schema`: emite JSON-LD @graph (Article + ItemList + FAQPage + BreadcrumbList)
- `--tipo lista|review|vs`: default `lista`

## 1. Tipo LISTA (`--tipo lista`) — N produtos ranqueados

Arquivo de exemplo: `tools/exemplo-lista.json`

### Campos obrigatórios

| Campo | Tipo | Descrição |
|---|---|---|
| `titulo` | string | Título do H1 (hero) |
| `titulo_seo` | string | Título SEO (snippet, JSON-LD headline) |
| `slug` | string | Slug sem barras |
| `meta_description` | string | Meta description |
| `categoria` | string | Ex: "fones bluetooth" |
| `data_verificacao` | string | "DD/MM/AAAA" |
| `produtos[]` | array | Lista de produtos (array de objetos) |
| `produtos[].nome` | string | Nome do produto |
| `produtos[].preco_label` | string | Ex: "R$ 268,20 no Pix" |
| `produtos[].descricao` | string | Parágrafo de descrição |
| `produtos[].destaques[]` | array | Bullets de prós |
| `produtos[].atencao[]` | array | Bullets de contras |
| `produtos[].links.amazon` | string | URL de afiliado (opcional) |
| `produtos[].links.mercadolivre` | string | URL de afiliado (opcional) |

### Campos opcionais

| Campo | Descrição |
|---|---|
| `kicker` | Badge do hero (ex: "🎧 Guia Atualizado") |
| `descricao_hero` | Parágrafo no hero |
| `hero_badges[]` | Array de badges no hero |
| `hero_img` | URL da imagem hero (usada no JSON-LD) |
| `resposta_rapida[]` | Array de {rotulo, texto} |
| `produtos[].specs{}` | Dict de especificações chave:valor |
| `produtos[].rotulo` | Ex: "1º lugar · Escolha do Editor" |
| `produtos[].img_url` | URL da imagem do produto |
| `produtos[].img_alt` | Alt text |
| `produtos[].img_caption` | Legenda |
| `produtos[].veredito` | String do veredito verde |
| `produtos[].review_url` | Link para review completo |
| `produtos[].buy_info` | Info do box de compra |
| `produtos[].tabela{}` | Valores para a tabela comparativa |
| `tabela_campos[]` | Nomes das colunas da tabela |
| `tabela_footnote` | Nota de rodapé da tabela |
| `faq[]` | Array de {pergunta, resposta} |
| `conclusao` | Parágrafo de conclusão |
| `conclusao_items[]` | Array de strings (li) |
| `para_quem_nao[]` | Array de strings (li) — sinal de valor agregado |
| `escolha_rapida_texto` | Texto do bloco escuro "⚡ Escolha rápida" |
| `escolha_rapida_links{}` | Links {amazon, mercadolivre} |
| `cluster_links[]` | Array de {titulo, url} |
| `fontes[]` | Array de {titulo, url} |
| `revisao_texto` | Rodapé editorial |
| `autor{}` | {nome, papel, bio, img, alt, social} |

## 2. Tipo REVIEW (`--tipo review`) — 1 produto

Arquivo de exemplo: `tools/exemplo-produto.json`

### Campos obrigatórios

| Campo | Descrição |
|---|---|
| `nome` | Nome do produto (no topo do JSON, ou em `produto`) |
| `introducao[]` | Array de parágrafos |
| `data_verificacao` | "DD/MM/AAAA" |
| `editor` ou `autor.nome` | Nome do editor (para JSON-LD) |

### Seções suportadas

- `pros[]` / `contras[]` — prós e contras
- `specs{}` — ficha técnica
- `secoes[]` — array de {titulo, paragrafos[]}
- `comparativo{}` — {colunas[], linhas[][]}
- `para_quem_sim[]` / `para_quem_nao[]`
- `faq[]` — {pergunta, resposta}
- `veredito[]` — array de parágrafos
- `nota` — número (0-10)
- `links{}` — {amazon, mercadolivre}
- `fontes[]` — {titulo, url}

## 3. Tipo VS (`--tipo vs`) — comparativo 2-3

Arquivo de exemplo: `tools/exemplo-vs.json`

### Campos obrigatórios

| Campo | Descrição |
|---|---|
| `titulo` | Título do artigo |
| `produto_a{}` / `produto_b{}` | Objetos de produto |
| `produto_*.nome` | Nome |
| `produto_*.nota` | Número (0-10) |
| `produto_*.preco` | Ex: "R$ 3.299" |
| `produto_*.pros[]` | Array de prós |
| `produto_*.contras[]` | Array de contras |

### Seções opcionais

- `secoes_analise[]` — array de {titulo, paragrafos[]} — **necessário para profundidade**
- `introducao[]` — parágrafos iniciais
- `resposta_rapida_custo` / `resposta_rapida_desempenho` — texto dos cards rápidos
- `tabela{}` — {header, linhas[][]}
- `produto_*.quem[]` — bullets "Compre se..."
- `produto_*.links{}` — {amazon, mercadolivre}
- `produto_*.img` — URL da imagem
- `veredito_vencedor` / `veredito_perdedor` — texto dos cards de veredito
- `para_quem_nao[]` — sinal de valor agregado
- `faq[]` — {pergunta, resposta}
- `fontes[]` — {titulo, url}

## Labels do checker (valor-agregado)

Para **0 alertas** no `checar_conformidade.py`, o texto visível do artigo DEVE conter
os seguintes padrões regex (case-insensitive):

| Sinal | Regex | Exemplo que passa |
|---|---|---|
| Prós/contras | `contras\|pontos negativos` | "Contras e Pontos de Atenção" |
| Para quem não é | `não é para\|não vale a pena para\|quem n[ãa]o é\|evite se` | "Para quem NÃO é" + "Não vale a pena para você se..." |
| FAQ | `perguntas frequentes\|faq` | H2 "Perguntas Frequentes" |
| Veredito | `veredito\|nota final` | "Veredito:" ou "nota 8.0/10" |
| Profundidade | ≥1200 palavras | ≥1800 para OK, 1200-1800 alerta |

## Verificação ad-hoc

Após gerar, sempre rodar:

```bash
python3 tools/checar_conformidade.py artigo.html
python3 -c "
import re, json
html = open('artigo.html').read()
# balanço de tags
for t in ['div','p','ul','li','h2','h3','a','table','tr','td','th']:
    a = len(re.findall(f'<{t}[ >]', html))
    b = len(re.findall(f'</{t}>', html))
    assert a == b, f'{t}: {a}/{b}'
# JSON-LD parseável
m = re.search(r'<script type=\"application/ld\+json\">(.*?)</script>', html, re.DOTALL)
if m: json.loads(m.group(1))
print('OK')
"
```