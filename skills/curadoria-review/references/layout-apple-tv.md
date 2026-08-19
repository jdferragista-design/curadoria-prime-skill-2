# Layout canônico — Curadoria Prime

Versão: 2.2
Referência visual principal: Apple TV 4K
Status: CANÔNICO

Este documento define a composição e a ordem do layout.

Ele NÃO substitui:

- regras de veracidade do `SKILL.md`;
- Régua Curadoria Prime v2.0;
- política de fontes;
- templates HTML LOCKED.

Em conflito:

`SKILL.md` → metodologia → template → este documento.

O HTML literal dos componentes vive em:

- `assets/template-review.md`
- `assets/template-vs.md`
- `assets/template-lista.md`

Este documento NÃO autoriza o Agent a reinterpretar visualmente esses
templates.

---

# 1. PRINCÍPIO VISUAL

A Curadoria Prime usa:

MARCA DO PRODUTO
→ Hero e cabeçalho principal de comparação.

PLATAFORMA
→ CTA/botão comercial.

SEMÁFORO EDITORIAL
→ vale/depende/espera, positivo/negativo, risco/status.

ÂMBAR JURÍDICO
→ tipo de análise, metodologia, transparência e avisos.

Esses sistemas de cores possuem funções diferentes.

Não misturar.

Exemplos proibidos:

- Hero laranja porque existe CTA Amazon;
- botão Amazon usando preto Apple;
- botão ML usando cor Samsung;
- card de prós usando cor da fabricante;
- box de metodologia usando gradiente do produto.

---

# 2. IMPLEMENTAÇÃO

A implementação canônica atual usa:

- blocos Gutenberg;
- `<!-- wp:html -->` quando previsto;
- estilo inline;
- componentes HTML explícitos.

Não existe autorização para substituir o template por:

- novo Design System `.cp-*`;
- Tailwind;
- CSS-in-JS;
- framework;
- tabela Markdown;
- cards Markdown.

Se o template define style inline, preserve.

---

# 3. FIDELIDADE

Valores presentes nos componentes LOCKED são literais.

Exemplo:

`padding: 28px 30px`

não significa:

"aproximadamente 30px".

Significa:

`28px 30px`.

Igualmente:

- radius;
- gap;
- font-size;
- cor;
- border;
- shadow;
- grid;
- min-width.

Somente os slots explicitamente variáveis podem mudar.

---

# 4. FORMATOS

Existem três formatos editoriais:

## REVIEW

Um produto.

Base visual:

Apple TV 4K.

## VS

Dois ou três produtos em confronto direto.

Mesma família visual do REVIEW, com tabela lado a lado e seções
individuais de produto.

## LISTA/GUIA

Vários produtos.

Usa componentes compartilhados e cards repetíveis.

Guias regulatórios/informacionais podem utilizar módulos específicos,
mas não substituem o template LISTA/GUIA sem classificação explícita.

---

# 5. ORDEM CANÔNICA — REVIEW

Não reordenar.

1. Meta SEO interna
2. Hero textual
3. HERO-01
4. Tipo de análise
5. Lead/recorte quando previsto
6. Metodologia
7. Prova social
8. Índice
9. Introdução/abertura
10. Transparência de afiliado
11. Resposta rápida
12. Onde comprar / CTA topo
13. Prós e contras
14. Ficha técnica
15. Seções de decisão
16. Comparativo
17. Comprar agora ou esperar, quando aplicável
18. Para quem é / não é
19. Notas — Régua v2.0
20. FAQ
21. Veredito
22. Escolha rápida
23. CTAs finais
24. Fontes consultadas
25. Última atualização
26. Byline, somente quando aprovado
27. Aviso de afiliado final

THUMB-01 NÃO faz parte dessa sequência.

THUMB-01 é Featured Image do WordPress.

---

# 6. HERO TEXTUAL — REVIEW

O Hero é o bloco-gradiente canônico da Apple TV.

Não é imagem.

Não é o H1 nativo do WordPress.

Não é barra branca de chips.

Estrutura:

[kicker]
[lead/resumo]
[badges]

Depois dele vem:

HERO-01

como imagem.

---

# 7. HERO — GEOMETRIA LOCKED

Wrapper:

`background: linear-gradient(135deg, {{BRAND_PRIMARY}} 0%, {{BRAND_SECONDARY}} 100%)`

`color: #fff`

`padding: 28px 30px`

`border-radius: 14px`

`margin-bottom: 30px`

`font-size: 15.5px`

`line-height: 1.75`

Não alterar.

---

# 8. KICKER DO HERO

Review:

`📌 Review Completo — {{ANO}}`

Visual:

- `display: inline-block`
- background `rgba(255,255,255,.16)`
- border `1px solid rgba(255,255,255,.28)`
- font-size `11px`
- font-weight `bold`
- letter-spacing `.1em`
- text-transform `uppercase`
- padding `4px 12px`
- radius `100px`
- margin-bottom `12px`

É rótulo de gênero.

Não usar para rating ou preço.

---

# 9. LEAD DO HERO

Visual:

- margin `0 0 16px`
- font-size `18px`
- font-weight `600`
- color `#fff`

Destaques usam:

`{{BRAND_ACCENT}}`

Somente elementos de decisão relevantes devem receber highlight.

Não pintar o parágrafo inteiro.

Conteúdo deve sintetizar:

- produto;
- variante;
- fatos decisivos;
- mercado quando confirmado;
- principal tensão de compra.

Sem "testamos a fundo" quando não houve teste físico.

---

# 10. BADGES DO HERO

Container:

`display: flex`
`flex-wrap: wrap`
`gap: 10px`

Cada pill:

- background `rgba(255,255,255,.16)`
- border `1px solid rgba(255,255,255,.28)`
- padding `6px 14px`
- radius `100px`
- font-size `13px`

Badges possíveis:

- Amazon;
- Mercado Livre;
- preço/faixa;
- atualização.

Somente renderizar dado confirmado.

A nota Amazon continua sendo nota Amazon.

A nota Mercado Livre continua sendo nota Mercado Livre.

Não apresentar como rating da Curadoria Prime.

---

# 11. HERO-01

É a imagem principal DENTRO do artigo.

Vem imediatamente após o Hero textual.

Não entra dentro do gradiente.

Enquanto não houver URL WP:

`<!-- CP-IMAGE:HERO-01 -->`

Visual final segue o template:

- largura responsiva;
- radius 12px;
- sombra canônica;
- legenda factual.

Não duplicar com outra "imagem principal".

---

# 12. THUMB-01

É exclusivamente:

Imagem destacada do WordPress.

Não entra no HTML.

É especificada no RELATÓRIO DE IMAGENS.

---

# 13. BOXES JURÍDICOS

Tipo de análise, metodologia e transparência não usam a cor da marca.

Base:

- `#fffbeb`
- border `#fde68a`
- texto `#78350f`

Esses elementos representam:

compliance/transparência.

Não vitrine.

---

# 14. PROVA SOCIAL

Padrão preferencial:

2 × 2

Objetivo:

- 2 Amazon;
- 2 Mercado Livre.

Visual:

neutro + filete da plataforma.

Amazon:

`#FF9900`

Mercado Livre:

`#3485DB`

Mas a quantidade é determinada pela evidência.

Nunca inventar para completar quatro cards.

---

# 15. ÍNDICE

Grid responsivo conforme template.

Usar âncoras reais.

Não criar item no índice para seção inexistente.

Não deixar link quebrado após remover seção condicional.

---

# 16. RESPOSTA RÁPIDA

Componente semântico de três cards:

## Vale

background `#f0fdf4`
border `#22c55e`
título `#166534`

## Depende

background `#eff6ff`
border `#3b82f6`
título `#1e40af`

## Pode esperar

background `#fffbeb`
border `#f59e0b`
título `#92400e`

Grid:

`repeat(auto-fit, minmax(280px, 1fr))`

gap:

`16px`

Hierarquia:

DECISÃO
→ CONDIÇÃO
→ DETALHE.

Não transformar preço no elemento principal desses cards.

---

# 17. CARDS DE COMPRA

REVIEW usa cards empilhados.

Não três colunas e-commerce iguais.

Wrapper:

- branco;
- padding `35px 25px`;
- radius `20px`;
- sombra suave.

Cada card:

[pill/função + loja + informação]
[imagem quando prevista]
[argumento]
[alerta quando necessário]
[CTA]

Hierarquia das ofertas é editorial, não simplesmente por comissão.

---

# 18. IMAGENS NOS CARDS DE COMPRA

Produto pequeno:

pode usar largura ampla.

Notebook/tablet/TV:

preferir aproximadamente:

- max-width 260px;
- max-height 170px;
- width auto;
- height auto;
- object-fit contain.

Imagem identifica SKU.

CTA informa preço.

---

# 19. CTAs

A cor vem da PLATAFORMA.

Forma base:

- padding `12px 20px`
- radius `8px`
- font-weight `800`
- font-size `15px`
- flex `1`
- min-width `150px`
- text-align `center`

Links afiliados:

`rel="sponsored nofollow noopener noreferrer"`

Não omitir `nofollow`.

---

# 20. TABELA COMPARATIVA — LOCKED

Este é o padrão canônico de tabela para REVIEW e VS.

Container:

`overflow-x: auto`
`margin-bottom: 28px`

Table:

`width: 100%`
`border-collapse: collapse`
`font-size: 13.5px`
`min-width: 640px`

Header:

`background: {{TABLE_HEADER}}`
`color: #fff`

Header cells:

`padding: 12px 14px`

Body cells:

`padding: 11px 14px`

Linhas:

alternar:

`#f8fafc`
`#fff`

Primeira coluna:

esquerda.

Colunas de produto:

centro.

---

# 21. TABELA — ESTRUTURA POR FORMATO

REVIEW:

`Critério | Produto | Rival 1 | Rival 2`

VS 1v1:

`Critério | Produto A | Produto B`

VS 3:

`Critério | A | B | C`

LISTA:

usar a estrutura prevista no template-lista.

Não converter para:

`Produto | Ganha | Perde | Perfil`

quando o template atual usar comparação lado a lado.

---

# 22. VENCEDORES NA TABELA

✅ somente quando houver vantagem factual defensável.

Empate:

não marcar vencedor arbitrário.

Preferência por perfil:

declarar como perfil, não superioridade absoluta.

---

# 23. NOTAS NA TABELA

Quando exibir Nota Curadoria Prime:

usar a Régua vigente do artigo.

Novo conteúdo v2.0:

somente múltiplos de 0,5.

Não gerar:

8,7.

Se nota histórica v1 aparecer em página antiga:

identificar a versão ou recalcular corretamente durante atualização.

---

# 24. PRÓS E CONTRAS — LOCKED

Grid:

`display: grid`

`grid-template-columns: repeat(auto-fit, minmax(300px, 1fr))`

`gap: 20px`

`margin: 25px 0`

## Positivos

background `#f0fdf4`

border `2px solid #22c55e`

radius `12px`

padding `24px`

heading `#166534`

divisor `#bbf7d0`

## Negativos

background `#fef2f2`

border `2px solid #ef4444`

radius `12px`

padding `24px`

heading `#991b1b`

divisor `#fecaca`

Itens:

`padding: 10px 0`

`font-size: 14.5px`

`line-height: 1.6`

Não inventar pontos para equilibrar quantidade.

---

# 25. SEÇÃO DE PRODUTO — VS/LISTA

Anatomia:

H2
→ posicionamento
→ IMG
→ dados principais
→ prós/contras
→ fonte específica.

Imagem pendente:

`<!-- CP-IMAGE:IMG-ID -->`

Todos os produtos usam a mesma estrutura.

---

# 26. FICHA TÉCNICA

Dados confirmados.

Prioridade:

fonte primária.

Não preencher célula só para manter tabela cheia.

Não utilizar marketplace como substituto silencioso da ficha oficial.

---

# 27. SEÇÕES DE DECISÃO

Variam por categoria.

Estrutura:

FATO
→ TERCEIRO quando relevante
→ RELATO quando relevante
→ INTERPRETAÇÃO.

Exemplos de eixos:

notebook:

- desempenho;
- tela;
- armazenamento;
- expansão;
- bateria.

fone:

- áudio;
- ANC;
- bateria;
- conectividade;
- microfone.

TV:

- imagem;
- HDR;
- sistema;
- som;
- conectividade.

O conteúdo varia.

O componente visual não.

---

# 28. FAQ — REVIEW/VS

Padrão:

cards empilhados.

Container:

`margin-bottom: 28px`

Card:

- background `#f8fafc`
- border `1px solid #e2e8f0`
- radius `10px`
- padding `16px 20px`
- margin-bottom `12px`

Pergunta:

- margin `0 0 8px`
- font-weight `700`
- font-size `14.5px`

Resposta:

- margin `0`
- font-size `14px`
- line-height `1.65`

Perguntas numeradas.

Não converter para `<details>`.

Quantidade normal:

6–10.

---

# 29. FONTES CONSULTADAS — LOCKED

Wrapper:

- background `#fffbeb`
- border `1px solid #fde68a`
- radius `10px`
- padding `16px 20px`
- margin `24px 0`
- font-size `13px`
- color `#78350f`
- line-height `1.7`

Usar URLs diretas.

Identificar:

- oficiais;
- testes independentes;
- varejo;
- rumores.

Não escrever apenas nomes de sites sem URL quando a URL estiver
disponível.

---

# 30. UPDATE BOX

Quando aplicável:

- background `#fffbeb`
- border `1px solid #fde68a`
- radius `10px`
- padding `16px 20px`
- margin-bottom `24px`
- font-size `13px`
- color `#78350f`
- line-height `1.7`

Conteúdo:

- atualização real;
- produto/SKU;
- data de preços;
- aviso de variação.

---

# 31. BYLINE

Componente condicional.

Renderizar somente com:

`AUTHOR_APPROVED = SIM`

Não escolher autor automaticamente.

Não escrever nova bio.

Visual:

- display flex;
- gap 16px;
- align-items center;
- flex-wrap wrap;
- background `#f8fafc`;
- border `1px solid #e2e8f0`;
- radius `12px`;
- padding `18px 20px`;
- margin-bottom `28px`.

Avatar:

72 × 72
radius 50%.

---

# 32. AVISO AFILIADO FINAL

Visual:

- background `#f8fafc`
- border-top `3px solid {{BRAND_PRIMARY}}`
- radius `0 0 10px 10px`
- padding `14px 18px`
- font-size `12.5px`
- color `#64748b`
- line-height `1.6`

Não é necessário expor IDs internos das contas de afiliado.

Mensagem transparente e simples.

---

# 33. BLOCOS LOCKED

No REVIEW:

- Hero
- HERO-01
- Tipo de análise
- Metodologia
- Índice
- Afiliado
- Resposta rápida
- Prós/contras
- Ficha
- Para quem é/não é
- Notas quando houver
- FAQ
- Veredito
- Fontes

---

# 34. BLOCOS CONDICIONAIS

Podem desaparecer por falta de gatilho/evidência:

- prova social;
- CTA;
- comprar/esperar;
- rumor;
- histórico;
- byline;
- plataforma específica.

A ausência não muda a ordem relativa dos demais.

---

# 35. MODELO REGULATÓRIO / GUIA DE REGRA

O antigo modelo Power Bank no Avião representa um subtipo visual
regulatório.

Não utilizar automaticamente em qualquer LISTA.

Só usar quando a intenção central for:

- regra;
- limite;
- proibição;
- segurança normativa;
- autorização.

Exemplo:

"Power bank no avião: o que a ANAC permite?"

Nesse subtipo:

o semáforo representa status normativo:

- permitido;
- autorização;
- proibido.

Não representa opinião editorial.

---

# 36. GUIA MULTIMARCA COM PRODUTOS

Se a intenção for:

"melhores tablets"

"melhores fones"

"melhores câmeras"

não utilizar automaticamente o visual regulatório ciano.

Usar:

template LISTA/GUIA comercial normal

com Hero neutro multi-marca.

---

# 37. REGRA FINAL DE LAYOUT

O template HTML literal é a última autoridade visual.

Este documento descreve o sistema.

O template implementa.

O Agent preenche.

Não redesenha.
