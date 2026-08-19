# Cores canônicas — Curadoria Prime

Versão: 2.2

As cores possuem função semântica.

Existem quatro famílias independentes:

1. MARCA → Hero e cabeçalho comparativo;
2. PLATAFORMA → CTA;
3. SEMÁFORO → decisão/status;
4. JURÍDICO → transparência/metodologia.

Não misturar funções.

---

# 1. HERO — MARCA

O Hero de REVIEW usa a marca do SKU principal.

| Marca | Primary | Secondary | Accent |
| --- | --- | --- | --- |
| Apple | `#1d1d1f` | `#000000` | `#2997ff` |
| Samsung | `#1428A0` | `#0B1A6B` | `#2189FF` |
| Xiaomi / Redmi / Poco | `#FF6900` | `#C2410C` | `#FFE4CC` |
| Motorola | `#1E4D8C` | `#102A4C` | `#7EB6E8` |
| Lenovo | `#E2231A` | `#8B1210` | `#FFD6D4` |
| Anker / Soundcore | `#00A9E0` | `#0077A3` | `#B8ECFA` |
| JBL | `#FF3300` | `#991F00` | `#FFD6CC` |
| Guia multi-marca | `#0f172a` | `#020617` | `#e2e8f0` |

Marca ausente da tabela:

não inventar cor "porque combina".

Pesquisar identidade oficial ou utilizar neutro multi-marca até
aprovação.

---

# 2. HEADER DE TABELA

REVIEW:

preferir `BRAND_PRIMARY`.

VS com marcas diferentes:

usar neutro:

`#0f172a`

salvo template explicitamente aprovado.

LISTA multi-marca:

`#0f172a`.

Não vestir comparativo multi-marca como se pertencesse a uma das marcas
sem motivo editorial.

---

# 3. PLATAFORMA — CTA

CTA sempre segue o DESTINO.

## Amazon

Fundo:

`#ff9900` → `#ff8500`

Texto:

`#ffffff`

Sombra:

`rgba(255,150,0,.3)`

## Mercado Livre

Fundo:

`#2d3277` → `#1a1f5c`

Texto:

`#ffe600`

Sombra:

`rgba(45,50,119,.3)`

## Apple Store

Fundo:

`#1d1d1f` → `#000000`

Texto:

`#ffffff`

Sombra:

`rgba(0,0,0,.3)`

## Samsung Shop

Fundo:

`#1428A0` → `#0B1A6B`

Texto:

`#ffffff`

Sombra:

`rgba(20,40,160,.3)`

## Oficial genérica / sem afiliado

Fundo:

`#111827` → `#030712`

Texto:

`#ffffff`

Sombra:

`rgba(0,0,0,.25)`

---

# 4. GEOMETRIA CTA

LOCKED:

`padding: 12px 20px`

`border-radius: 8px`

`font-weight: 800`

`font-size: 15px`

`flex: 1`

`min-width: 150px`

`text-align: center`

Rótulo preferencial:

`Ver na {{LOJA}} — {{PREÇO}}`

Preço somente quando validado.

Sem preço:

`Ver na {{LOJA}}`

---

# 5. LINKS AFILIADOS

Sempre:

`rel="sponsored nofollow noopener noreferrer"`

Não usar apenas:

`sponsored`

ou:

`nofollow`

como padrões diferentes entre templates.

---

# 6. JURÍDICO

Tipo de análise, metodologia e transparência:

Fundo:

`#fffbeb`

Borda:

`#fde68a`

Texto:

`#78350f`

Esse sistema NÃO muda com fabricante.

---

# 7. SEMÁFORO EDITORIAL

## Verde

`#f0fdf4`
`#22c55e`
`#166534`

Uso:

- vale;
- positivo;
- opção adequada;
- status permitido quando normativo.

## Azul

`#eff6ff`
`#3b82f6`
`#1e40af`

Uso:

- depende;
- perfil alternativo;
- informação/procedimento.

## Âmbar

`#fffbeb`
`#f59e0b`
`#92400e`

Uso:

- espera;
- ressalva;
- autorização;
- atenção.

## Vermelho

`#fef2f2`
`#ef4444`
`#991b1b`

Uso:

- negativo;
- risco;
- proibido;
- limitação crítica.

Semáforo não é marca.

Semáforo não é CTA.

---

# 8. NEUTROS

Background:

`#f8fafc`

Border:

`#e2e8f0`

Texto secundário:

`#64748b`

Texto forte:

`#1e293b`

Usos:

- FAQ;
- índice;
- relatos;
- cards secundários.

---

# 9. GUIA REGULATÓRIO — EXCEÇÃO

Ciano regulatório:

PRIMARY:

`#0e7490`

SECONDARY:

`#164e63`

ACCENT:

`#67e8f9`

Alerta:

`#fbbf24`

Só utilizar em subtipo explicitamente classificado como:

GUIA_REGULATORIO.

Exemplos:

- regras ANAC;
- limites de Wh;
- permitido/proibido.

Não utilizar como cor genérica de:

- Anker;
- Basike;
- power bank;
- guia multi-marca.

---

# 10. PROIBIÇÕES

Proibido:

- Hero Amazon;
- botão Amazon preto Apple;
- botão ML amarelo chapado;
- CTA verde genérico para marketplace;
- ciano regulatório em review comum;
- roxo inventado como "tema premium";
- trocar cores por estética;
- usar cor de marca em box jurídico;
- usar cor de plataforma em prós/contras.

Cores são função, não decoração.
