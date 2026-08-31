# Estilo Golden — Thumbnail de YouTube / imagem destacada

Padrão visual da Curadoria Prime para **imagem destacada** (og:image / capa de
card / thumbnail de YouTube) de guias e reviews.

**Referência canônica:** `melhores-smartphones-custo-beneficio-2026-destaque.webp`
(produto-âncora no centro, texto neon em gradiente, fundo escuro com raios).

---

## Formato
- **16:9** — `1280×720` (imagem destacada / thumbnail de YouTube).
- Cantos retos, sem moldura externa.
- O hero do artigo (970×546) pode usar a mesma linguagem, mas sem texto de impacto
  (o título fica em HTML); a thumbnail **pode** ter texto (é o fator de clique).

## Estrutura em dois blocos
1. **TOPO (~40% da altura):** texto de impacto + selos/categorias.
2. **BASE (~60% da altura):** produtos em **arco simétrico em perspectiva** sobre
   **palco refletivo** (espelho de vidro), o produto-âncora maior e central à
   frente, os demais recuando para as laterais.

## Tipografia e texto (fator de clique)
- **Título principal** — fonte grossa *impact*, **gradiente laranja→amarelo**,
  contorno escuro grosso + sombra dura (efeito 3D extrudado). Ex.: "MELHORES JOGOS SWITCH".
- **Subtítulo** — fonte grossa, **gradiente ciano→azul claro**, contorno branco fino
  + sombra escura. Ex.: "PARA PRESENTEAR".
- **Texto de apoio** — branco, sombra suave. Ex.: "GUIA COMPLETO: 2026!".
- **Faixa de preço (opcional)** — branco com contorno preto e leve gradiente
  amarelado no topo. Ex.: "DE R$ X A R$ Y".

⚠️ **Regra de conformidade:** nunca inventar preço na imagem. O valor de "DE R$ X
A R$ Y" deve vir do **LEDGER** do dia (captura real). Desconto de fachada no texto
da thumb = NÃO. Preço só com data de verificação no card do artigo.

## Paleta e fundo
- **Fundo:** gradiente escuro **azul-marinho profundo (base) → roxo (topo)**.
- **Raios de luz:** feixes geométricos **magenta** irradiando de trás do destaque
  para as laterais.
- **Partículas:** pequenos pontos de luz (tech/premium).
- **Iluminação:** cinematográfica, holofote atrás do item central, reflexos
  especulares fortes nos produtos.
- **Piso:** espelho refletivo escuro, reflexos nítidos porém esmaecidos e tingidos
  pela cor do fundo.

## Organização dos produtos
- Arco simétrico, produto-âncora **maior, mais à frente, frontal** (tela ligada).
- Os demais **recuam simetricamente** nas laterais, com leve sobreposição.
- Cada item frontal, com brilho/reflexo de estúdio.
- Se o produto tem "frente e costas", usar visão traseira (esq.) + frontal (dir.)
  como na referência de smartphones.

## Selos (opcional, discreto)
- **Estrela de 5 pontas** em gradiente laranja→amarelo, contorno branco grosso,
  sombra dura.
- **Pílulas de categoria** (placeholder) em cores distintas por faixa, preenchimento
  translúcido + contorno branco fino.
- Não poluir: se inserir, manter no canto/topo sem cobrir o produto-âncora.

## Prompt do gerador — o que sempre incluir
- Formato 16:9 (1280×720), "identical style to a neon product-buying-guide thumbnail".
- Topo ~40%: títulos de impacto em gradiente (laranja→amarelo e ciano→azul) com
  contorno e sombra dura; texto pequeno de apoio.
- Base ~60%: arco simétrico em perspectiva em palco refletivo, âncora central maior.
- Fundo: azul-marinho→roxo, raios magenta, partículas, holofote, piso de vidro.
- "sharp focus, ultra-detailed, 8k, no watermarks".
- Fornecer **EN** (primário) e **PT** (fallback).
- Texto em PT correto verificado (gerador erra texto — revisar sempre).

## Checklist de aceite
- [ ] Produto-âncora central, maior, à frente
- [ ] Arco simétrico com os demais itens
- [ ] Estilo fiel à referência (fundo azul→roxo, raios magenta, piso refletivo, letras 3D)
- [ ] Texto sem erro do gerador
- [ ] Preço na imagem (se houver) é do LEDGER do dia — sem desconto de fachada
- [ ] Sem marca d'água · cantos retos

## Nome de arquivo
- Thumbnail: `<slug>-destaque.jpg` (1280×720)
- Hero: `<slug>-hero.jpg` (970×546) — mesma linguagem, sem texto de impacto
