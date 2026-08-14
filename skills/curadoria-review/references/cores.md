# Cores — duas paletas, sem misturar

Regra da casa (12/08/2026):

1. **Hero** = cores oficiais da **marca do produto**.
2. **CTAs / botões de compra** = cores oficiais da **plataforma** (loja).

Não pintar o hero com laranja Amazon. Não pintar o botão da Amazon com preto Apple. Não inventar ciano, roxo ou “tema do artigo” no lugar da marca.

## Hero (marca do produto)

O bloco-gradiente do topo (kicker + lead + chips) usa o par oficial da fabricante do SKU principal. Highlight do lead = segunda cor da marca (nunca amarelo de multa, a menos que a marca seja amarela).

| Marca | Fundo (gradiente 135°) | Highlight do lead | Quando usar |
| --- | --- | --- | --- |
| Apple | `#1d1d1f` → `#000000` | `#2997ff` | iPhone, iPad, Apple TV, Pencil, Watch |
| Samsung | `#1428A0` → `#0B1A6B` | `#2189FF` | Galaxy Tab, S, Buds, TV, Book |
| Xiaomi / Redmi / Poco | `#FF6900` → `#C2410C` | `#FFE4CC` | Redmi, Pad, Band |
| Motorola | `#1E4D8C` → `#102A4C` | `#7EB6E8` | Moto G, Edge |
| Lenovo | `#E2231A` → `#8B1210` | `#FFD6D4` | IdeaPad, Tab |
| Anker / Soundcore | `#00A9E0` → `#0077A3` | `#B8ECFA` | 737, Nano, Liberty |
| JBL | `#FF3300` → `#991F00` | `#FFD6CC` | fones, soundbar |
| Sem marca única (guia multi) | Neutro `#0f172a` → `#020617` | `#e2e8f0` | Lista com 2+ marcas; **não** vestir de Samsung nem de Apple |

O modelo 2 (power bank) usou ciano `#0e7490`. Isso **não** é cor oficial de Anker, Basike nem ANAC. Em guia multi-marca, preferir o neutro da última linha — ou o hero da marca do item âncora, se o editor declarar um âncora.

Cabeçalho de tabela no mesmo artigo: mesma cor de fundo do hero (Apple preto, Samsung azul, guia neutro). Não reutilizar o ciano do modelo 2 como padrão.

Box jurídico (tipo de análise, metodologia, afiliado) **não** segue a marca: continua âmbar `#fffbeb` / `#fde68a` / `#78350f`.

## CTAs (plataforma)

Botão = loja de destino. Sempre.

| Plataforma | Fundo | Texto | Sombra |
| --- | --- | --- | --- |
| Amazon | `#ff9900` → `#ff8500` | `#ffffff` | `rgba(255,150,0,.3)` |
| Mercado Livre | `#2d3277` → `#1a1f5c` | `#ffe600` | `rgba(45,50,119,.3)` |
| Apple Store | `#1d1d1f` → `#000000` | `#ffffff` | `rgba(0,0,0,.3)` |
| Samsung Shop | `#1428A0` → `#0B1A6B` | `#ffffff` | `rgba(20,40,160,.3)` |
| Loja sem afiliado / oficial genérica | `#111827` → `#030712` | `#ffffff` | `rgba(0,0,0,.25)` |

Forma fixa (os dois modelos): `padding 12px 20px`, raio **8px**, peso **800**, 15px, `flex: 1`, `min-width: 150px`. Rótulo: `Ver na [loja] — R$ …`.

Proibido:

- Botão ML amarelo chapado com texto preto.
- Botão Amazon preto ou azul da marca do produto.
- Botão “comprar” verde genérico no card de oferta (verde fica no *pill* de “menor preço”, não no CTA da loja).
- Hero laranja porque “vende na Amazon”.

## Semáforo editorial (não é marca, não é loja)

Verde / azul / âmbar / vermelho dos cards vale–depende–espera, livre–autorização–proibido, prós/contras: **sistema de decisão**. Não substitui a pele do hero nem a cor do botão.
