# Especificação visual — Curadoria Prime

Versão: 2.2
Status: referência técnica complementar

Fonte principal:

`../assets/modelos/modelo-layout-apple-tv-4k.html`

Este arquivo explica POR QUE os componentes são desenhados dessa forma.

Ele NÃO redefine:

- ordem do artigo;
- regras editoriais;
- Régua;
- HTML.

Para isso:

- ordem → `layout-apple-tv.md`
- cores → `cores.md`
- HTML → `assets/template-*.md`
- comportamento → `SKILL.md`

---

# 1. FAMÍLIA VISUAL

A Curadoria Prime não utiliza estética de e-commerce genérico.

O sistema combina:

MARCA
+
SEMÁFORO EDITORIAL
+
PLATAFORMA
+
JURÍDICO
+
NEUTROS.

Cada cor tem função.

---

# 2. GEOMETRIA

Raio típico:

- jurídico → 10px
- índice/relatos/scores → 10–12px
- Hero/cards principais → 14px
- wrapper de compra → 20px
- pills → 100px

Não normalizar tudo para o mesmo radius.

Essa variação faz parte da hierarquia.

---

# 3. TIPOGRAFIA

A identidade depende mais de:

- tamanho;
- peso;
- espaçamento;

do que de família tipográfica específica.

Hero:

kicker:
11px / bold / uppercase / tracking .1em

lead:
18px / 600

chips:
13px

cards:
14–15px

CTA:
15px / 800

Não introduzir nova fonte apenas para diferenciar produto.

---

# 4. HERO

É o único grande momento de identidade da marca.

Estrutura:

kicker
→ lead
→ chips.

A imagem vem depois.

O Hero não funciona como card de rating editorial.

A nota Curadoria Prime possui componente próprio mais abaixo.

---

# 5. RESPOSTA RÁPIDA

É sistema de decisão.

Não score.

Não e-commerce.

Três estados:

- vale;
- depende;
- espera.

Conteúdo:

perfil
→ condição
→ detalhe.

Preço pode ser mencionado como condição, mas não dominar visualmente.

---

# 6. COMPRA

REVIEW:

cards empilhados.

Objetivo:

uma decisão comercial por vez.

Não três colunas igualmente agressivas.

Hierarquia pode representar:

- menor preço;
- compra oficial/segura;
- alternativa nacional;
- marketplace;
- sem comissão.

Não pressupor que afiliado é melhor.

---

# 7. TABELA COMPARATIVA

O padrão é comparação por CRITÉRIO.

Visual:

- header forte;
- zebra;
- leitura horizontal;
- scroll em mobile.

Ela existe para reduzir carga cognitiva.

Não inserir dezenas de linhas sem poder decisório.

---

# 8. PRÓS E CONTRAS

Verde/vermelho.

Duas colunas responsivas.

A simetria é visual.

Não exige mesma quantidade de itens.

Não fabricar negativo para igualar altura.

---

# 9. NOTAS

A grade de notas é diferente de Resposta Rápida.

Resposta Rápida:

decisão do perfil.

Notas:

resultado metodológico.

Régua atual:

v2.0.

Sempre seis critérios aplicáveis, salvo N/A metodologicamente válido.

Desktop:

3 × 2.

---

# 10. FAQ

REVIEW/VS:

cards neutros empilhados.

Não accordion `<details>` no padrão atual.

Pergunta forte.

Resposta imediatamente visível.

Isso preserva consistência com páginas existentes.

---

# 11. FONTES E RODAPÉ

Fontes usam âmbar.

Objetivo:

indicar área de verificação e transparência.

Update box usa a mesma família.

Byline:

neutro.

Afiliado final:

neutro com filete da identidade autorizada.

Não transformar rodapé em novo Hero.

---

# 12. GUIA REGULATÓRIO

Existe uma segunda pele histórica:

Power Bank no Avião.

Use somente quando:

a intenção central é regra/limite/risco normativo.

Ciano:

`#0e7490 → #164e63`

Nesse gênero:

semáforo significa:

- livre;
- autorização;
- proibido.

Não utilizar essa pele para qualquer conteúdo sobre power banks.

A categoria do produto não determina esse visual.

A INTENÇÃO regulatória determina.

---

# 13. O QUE NÃO FAZER

Não:

- criar `.cp-atv`;
- introduzir stylesheet alternativo;
- transformar Hero em card branco;
- pôr imagem dentro do gradiente;
- criar três cards de compra lado a lado;
- usar ML amarelo chapado;
- substituir FAQ por accordion;
- substituir tabela comparativa por "ganha/perde";
- trocar inline styles por componentes novos;
- criar um tema visual diferente para Edifier, Acer, Apple etc.

O produto muda a pele do Hero.

Não muda a arquitetura do site.
