# RELATÓRIO DE CORREÇÕES P0 — 27/08/2026

Correção em lote dos **18 artigos de maior risco** identificados na auditoria
(`audit/auditoria-48-artigos.csv`) e confirmados ao vivo via WP REST API
(`tools/checar_conformidade.py`).

**Resultado final:** **18/18 artigos com 0 erros de bloqueio** (✅ "Publicável
após revisar os alertas" ou "Aprovado").

Todos os arquivos: `articles/html_output/*.html` (lidos do `content.rendered`
da API pública, corrigidos localmente).

---

## O que foi corrigido

### 1. `aggregateRating` / `reviewCount` / `ratingCount` no JSON-LD (§2.4)
Removidos **de 16 artigos**. O §2.4 proíbe publicar nota agregada de terceiros
(Amazon/ML) como se fosse avaliação da Curadoria no schema.

- samsung-hw-b400f-review
- xiaomi-smart-band-10-vale-a-pena
- samsung-galaxy-book4-review-2026
- samsung-galaxy-s25-5g-review
- iphone-16e-review-2026
- soundcore-liberty-4-nc-vale-a-pena
- galaxy-s24-fe-em-2026
- samsung-u8100f-smart-tv-4k-review
- samsung-u8600f-review
- jbl-cinema-sb180-review-vale-a-pena
- xiaomi-smart-band-9-active-vale-a-pena
- galaxy-watch7-44mm-vale-a-pena
- tcl-c6k-review-2026
- xiaomi-redmi-note-14-pro-plus-review-2026
- lenovo-ideapad-slim-3-notebook-2026
- purificador-de-agua-electrolux-pe12g-review

### 2. JSON-LD corrompido por wpautop (`<br />` dentro do `<script>`)
Limpeza das tags HTML injetadas pelo WordPress, que tornavam o schema inválido:

- presentes-dia-dos-pais-tech-ate-300 (**66 `<br />`**)
- apple-tv-4k (**61 `<br />`**)

### 3. Estrutura JSON-LD quebrada
- **purificador-de-agua-electrolux-pe12g-review**: `BreadcrumbList` estava
  dentro do array `mainEntity` do `FAQPage` (faltava `]`). Movido para o nível
  de `@graph`.

### 4. Descrição JSON-LD com aspas internas não escapadas
- **xiaomi-smart-band-10-vale-a-pena**: `"tela AMOLED 1,72", bateria...`
  quebrava o parser (a aspa fechava a string). String reescrita sem aspas
  internas.

### 5. Alegações de teste físico reescritas (§3/§4 + §5)
- **samsung-hw-b400f-review (3310)**:
  - "Em nossos testes, o modo Voice Enhance aplicou..." → atribuído a
    documentação oficial + relatos de compradores.
  - Adicionada declaração canônica **"Tipo de análise"** (A Curadoria Prime não
    testou esta unidade fisicamente).
- **samsung-galaxy-book4-review-2026 (4185)**:
  - Citação "Usei a quase 1 mês" (mbuyer review) reenquadrada como **relato
    publicado de comprador** (não experiência nossa).
  - Adicionada declaração de ausência de teste no box da metodologia.

---

## Alertas restantes (não bloqueiam — pendência editorial)

| Tipo | Artigos | Ação recomendada |
|---|---|---|
| `data` | 14 artigos | Preços/notas sem data visível de verificação — editor precisa de captura datada recente (30 dias) |
| `divulgacao` | 11 artigos | Aviso de afiliado após o 1º link — mover o bloco para antes do primeiro CTA |
| `honestidade` | 7 artigos | Não declaram explicitamente ausência de teste físico — \$5 exige a ressalva |
| `imparcialidade`/`valor-agregado` | 9 artigos | Falta bloco de contras / sinal de valor — melhoria editorial |
| `keyword-stuffing` | 6 artigos | Densidade de marca alta (ex.: 'galaxy', 'apple') — naturalizar |
| `profundidade` | 1 artigo | abaixo do padrão (~3.000 palavras) |

## Pendências para o editor humano

1. **Aplicar no WordPress**: exigirá `WP_USER` e `WP_APP_PASSWORD` para gravar
   via API (`tools/corrigir_artigos.py` entendendo o raw). Sem essa credencial,
   os arquivos corrigidos ficam em `articles/html_output/` prontos para colagem.
2. Confirmar a `data` de verificação de cada artigo antes de atualizar.
3. Revisar a reescrita das 3 alegações de teste (3316 e 4185) no navegador.
4. Os outros 30 artigos da auditoria não eram P0 de bloqueio (ou já corrigidos
   nos lotes anteriores 20–23/08).

---

## Validação

Comando:
`python3 tools/checar_conformidade.py 'articles/html_output/*.html'`

Resultado: **0 erros em 18 arquivos** · JSON-LD 100% válido · sem
`aggregateRating`/`reviewCount`/`ratingCount` · links de afiliado já com
`rel="sponsored"`.