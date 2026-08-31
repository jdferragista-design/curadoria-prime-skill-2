# 🛡️ Compliance Checklist — Curadoria Prime Editorial Skill

Este documento é a autoridade máxima de conformidade visual e estrutural. **Todo artigo reconstruído ou criado deve ser validado contra este checklist antes da entrega final.**

---

## 🌐 Regras Universais (Todos os Modelos)

### 🏗️ Estrutura e HTML
- [ ] **Envelopamento:** Todo HTML customizado deve estar envolto em `<!-- wp:html -->` e `<!-- /wp:html -->`.
- [ ] **Mímica de Código:** Não usar tags semânticas modernas (como `<figure>` ou `<figcaption>`) se o modelo Golden usa `div` + `p`. A estrutura do código deve ser idêntica ao modelo.
- [ ] **Cores de Base:** Tabelas, Footers e Seções Neutras devem usar a paleta **Neutro Multi-marca** (`#0f172a` $\rightarrow$ `#020617`).
- [ ] **Imagens:** Todas as imagens devem possuir `loading="lazy"`, `display: block`, `margin: 0 auto` e `border-radius: 12px`.

### 📊 Régua v2.0 e Notas
- [ ] **Bloco "Como chegamos ao [nota]":** 
    - **Estilo:** `background: #fffbeb`, `border: 1px solid #fde68a`, `border-radius: 10px`, `padding: 14px 18px`, `margin: 22px 0`, `font-size: 13px`, `color: #78350f`, `line-height: 1.6`.
    - **Conteúdo:** Texto canônico sobre critérios e pesos fixos + link para `https://curadoriaprime.com/como-avaliamos/`.
- [ ] **Prova Social:** Mínimo de **4 blocos** (2 para Amazon e 2 para Mercado Livre).
    - **Amazon:** Borda lateral `#FF9900`.
    - **Mercado Livre:** Borda lateral `#3485DB`.

---

## 📑 Regras por Tipo de Modelo

### 1. Review de Produto Único (`modelo-review-golden.html`)
- [ ] **Hero Banner:** Gradiente da **Cor Oficial da Marca** $\rightarrow$ Neutro.
- [ ] **Hero Image:** Estrutura `div` $\rightarrow$ `img` $\rightarrow$ `p` (Legenda).
- [ ] **Dimensões de Imagem:** `max-width: 1000px`, `box-shadow: 0 4px 16px rgba(0,0,0,.14)`.
- [ ] **Sequência Obrigatória:**
    1. Tipo de Análise $\rightarrow$ 2. Meta SEO $\rightarrow$ 3. Hero $\rightarrow$ 4. Metodologia $\rightarrow$ 5. Prova Social $\rightarrow$ 6. Índice $\rightarrow$ 7. Resposta Rápida (3 col) $\rightarrow$ 8. Onde Comprar $\rightarrow$ 9. Ficha Técnica $\rightarrow$ 10. Análise $\rightarrow$ 11. Prós/Contras $\rightarrow$ 12. Para quem é $\rightarrow$ 13. FAQ $\rightarrow$ 14. Veredito (Régua) $\rightarrow$ 15. Cálculo Nota $\rightarrow$ 16. Escolha Rápida $\rightarrow$ 17. Author Box.

### 2. Comparativo 1v1 (`modelo-vs-golden.html`)
- [ ] **Hero Banner:** Gradiente **Neutro Azul** (`#1428A0` $\rightarrow$ `#0a1550`).
- [ ] **Hero Image:** Estrutura `<figure>` (específico deste modelo).
- [ ] **Tabela Comparativa:** Header Azul (`#1428A0`).
- [ ] **Sequência Obrigatória:**
    1. Transparência $\rightarrow$ 2. Hero $\rightarrow$ 3. Imagem Comparativa $\rightarrow$ 4. Metodologia $\rightarrow$ 5. Prova Social $\rightarrow$ 6. Índice $\rightarrow$ 7. Lead $\rightarrow$ 8. Resposta Rápida (2 col: Custo-benefício vs Desempenho) $\rightarrow$ 9. Tabela Comparativa $\rightarrow$ 10. Análises Individuais $\rightarrow$ 11. Régua Comparada $\rightarrow$ 12. Veredito $\rightarrow$ 13. Cálculo Nota $\rightarrow$ 14. Onde Comprar.

### 3. Guia / Lista (`modelo-lista-golden.html`)
- [ ] **Hero Banner:** Gradiente **Neutro Escuro** (`#1a1a2e` $\rightarrow$ `#16213e`).
- [ ] **Metodologia:** Formato de lista com checkmarks (`✓`).
- [ ] **Imagens:** `max-width: 900px` (Hero) / `500px` (Produtos), `box-shadow: rgba(90,79,207,.12)`.
- [ ] **Sequência Obrigatória:**
    1. Hero $\rightarrow$ 2. Separador $\rightarrow$ 3. Metodologia $\rightarrow$ 4. Transparência $\rightarrow$ 5. Resposta Rápida (Lista) $\rightarrow$ 6. Critérios de Avaliação $\rightarrow$ 7. Produtos Ranqueados (cada um com: Imagem $\rightarrow$ Pills $\rightarrow$ Lead $\rightarrow$ Ficha Técnica $\rightarrow$ Destaques $\rightarrow$ Atenção $\rightarrow$ Veredito $\rightarrow$ Link $\rightarrow$ Box Compra) $\rightarrow$ 8. Tabela Comparativa Final $\rightarrow$ 9. FAQ.

---

## 🚫 Proibidos (Zero Tolerance)
- [ ] **NÃO** usar `<figure>` em Reviews de Produto Único.
- [ ] **NÃO** usar cores da marca em Tabelas ou Footers.
- [ ] **NÃO** alterar as dimensões de sombra (`rgba`) ou largura de imagem do modelo.
- [ ] **NÃO** omitir o link de metodologia no bloco de cálculo da nota.
