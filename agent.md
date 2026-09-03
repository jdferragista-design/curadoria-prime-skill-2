# AGENT — Diretrizes de Criação e Atualização de Artigos

Este documento define as regras mandatórias para qualquer agente que atue na criação ou edição de conteúdo para o Curadoria Prime.

## 1. Fidelidade ao Modelo Canônico (Regra de Ouro)
**Seguir fielmente o HTML golden do TIPO de conteúdo — ele é a régua canônica:**
- Review → `skills/curadoria-review/assets/modelos/modelo-review-golden.html`
- Lista → `skills/curadoria-review/assets/modelos/modelo-lista-golden.html`
- VS → `skills/curadoria-review/assets/modelos/modelo-vs-golden.html`
- Não improvisar layouts.
- Não remover blocos obrigatórios.
- Replicar pixel-perfeitamente cores, sombras, gradientes e espaçamentos.
- Manter a hierarquia de tags HTML e classes CSS do modelo.

## 2. Padrões Visuais e Cores
**Não existe uma paleta única entre os tipos.** Cada tipo usa a paleta do seu próprio
golden (ex.: o acento `#5a4fcf/#764ba2` é do **lista**; o review usa `#2997ff`). Sempre
consulte o golden do tipo. Referência para **REVIEW** (`modelo-review-golden.html`):
- **Header de impacto (hero):** `linear-gradient(135deg,#1d1d1f 0%,#000000 100%)`, texto `#fff`, destaque realçado em `#2997ff`.
- **Boxes de metodologia/transparência/nota (âmbar):** `#fffbeb` + borda `#fde68a` + texto `#78350f`.
- **Boxes de seção** ("O que dizem os compradores", "Índice"): `#f8fafc` + borda `#e2e8f0`, título `#1e293b`.
- **Grid de ofertas/compra:** container branco, borda `#e9ecef`; cards por loja — Amazon borda `#FF9900`, Mercado Livre borda `#3485DB`. CTAs por loja: ML `#2d3277→#1a1f5c`, Amazon `#ff9900→#ff8500`, dark `#1d1d1f→#000`.
- **Resposta rápida (grid 3 colunas):** ✅ `#f0fdf4`/`#22c55e` · 🤔 `#eff6ff`/`#3b82f6` · ⏳ `#fffbeb`/`#f59e0b`.
- **Veredito:** badge de nota `linear-gradient(135deg,#0f172a 0%,#1e1b4b 100%)`; scorecard em grid 3×2 (Custo-benefício `#f59e0b`, demais `#22c55e`).
- **Escolha Rápida:** container dark + grid `repeat(3, 1fr)` com fallback para 1 coluna em mobile (<782px).

## 3. Compliance Editorial e Conteúdo
- **Extensão:** Mínimo de ~1500 palavras para guias e reviews profundos.
- **Links de Afiliado:** Obrigatoriamente `rel="sponsored noopener noreferrer"`.
- **Fontes:** Seção "Fontes consultadas" com links reais e datados.
- **Honestidade:** 
    - Proibido alegar teste físico sem o selo "Testado por nós".
    - Usar: "Analisamos as fichas técnicas oficiais e cruzamos com relatos de compradores".
    - Proibido usar citações fictícias ou placeholders `[EXEMPLO]`.
- **Estrutura de Produto (Sequência Modular):**
    `Imagem` $\rightarrow$ `Badges de Rank` $\rightarrow$ `Texto` $\rightarrow$ `Tabela Técnica` $\rightarrow$ `Prós` $\rightarrow$ `Pontos de Atenção` $\rightarrow$ `Veredito` $\rightarrow$ `Box de Compra`.

## 4. Requisitos Técnicos (SEO & Schema)
- **JSON-LD:** Implementar obrigatoriamente o formato `@graph` contendo:
    - `Article` / `TechArticle`
    - `ItemList` (para guias)
    - `FAQPage`
    - `BreadcrumbList`
- **Imagens:** Nomes de arquivos descritivos e otimizados. Verificar status HTTP 200 antes de finalizar.
- **Âncoras:** Validar se todos os links do índice apontam para IDs existentes no documento.

## 5. Fluxo de Validação
1. **Comparação Visual:** Comparar o HTML gerado com o modelo Golden lado a lado.
2. **Check de Compliance:** Rodar `tools/checar_conformidade.py`.
3. **Balanço de Tags:** Verificar se todas as `<div>` e `<ul>` foram fechadas corretamente.
