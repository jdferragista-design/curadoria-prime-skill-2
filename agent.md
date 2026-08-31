# AGENT — Diretrizes de Criação e Atualização de Artigos

Este documento define as regras mandatórias para qualquer agente que atue na criação ou edição de conteúdo para o Curadoria Prime.

## 1. Fidelidade ao Modelo Canônico (Regra de Ouro)
**Analisar o modelo canônico (ex: `modelo-lista-golden.html`) e seguir fielmente a estrutura, bloco e visual.**
- Não improvisar layouts.
- Não remover blocos obrigatórios.
- Replicar pixel-perfeitamente cores, sombras, gradientes e espaçamentos.
- Manter a hierarquia de tags HTML e classes CSS do modelo.

## 2. Padrões Visuais e Cores
- **Cores Primárias:** `#5a4fcf` (Roxo/Azul) para acentos, botões de índice e FAQs.
- **Cores de Destaque:** `#fde68a` (Amarelo) para boxes de metodologia/notas.
- **Vereditos:** Fundo `#f0fdf4` com borda esquerda `#22c55e` (verde).
- **Pontos de Atenção:** Bloco com borda esquerda grossa vermelha.
- **Escolha Rápida:** Grid de 3 colunas (`repeat(3, 1fr)`) com fallback para 1 coluna em mobile (<782px).

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
