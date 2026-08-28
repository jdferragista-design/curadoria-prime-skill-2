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
| `honestidade` | ~~7 artigos~~ → **0** | ✅ Resolvido em 27/08 — declaração de ausência de teste inserida nos 7 (mais as 2 já reescritas) |
| `imparcialidade`/`valor-agregado` | 9 artigos | Falta bloco de contras / sinal de valor — melhoria editorial |
| `keyword-stuffing` | 6 artigos | Densidade de marca alta (ex.: 'galaxy', 'apple') — naturalizar |
| `profundidade` | 1 artigo | abaixo do padrão (~3.000 palavras) |

## Pendências para o editor humano

1. **~~Aplicar no WordPress~~** — ✅ **CONCLUÍDO em 27/08**: 18/18 posts
   gravados via API sobre o `content.raw` (ver seção "Aplicação no
   WordPress" abaixo). Resta a conferência visual no navegador.
2. Confirmar a `data` de verificação de cada artigo antes de atualizar.
3. Revisar a reescrita das alegações de teste (3310 e 4185) no navegador.
4. Os outros 30 artigos da auditoria não eram P0 de bloqueio (ou já corrigidos
   nos lotes anteriores 20–23/08).

---

## Validação

Comando:
`python3 tools/checar_conformidade.py 'articles/html_output/*.html'`

Resultado: **0 erros em 18 arquivos** · JSON-LD 100% válido · sem
`aggregateRating`/`reviewCount`/`ratingCount` · links de afiliado já com
`rel="sponsored"`.

---

## Aplicação no WordPress (27/08/2026)

Executada via `tools/aplicar_wp_p0.py` com `WP_USER`/`WP_APP_PASSWORD` no
ambiente (nunca gravados em arquivo). Método em 5 etapas:

1. **`--pipeline-check`** — o pipeline local (`corrigir_p0_artigos` +
   `adicionar_honestidade`) aplicado ao **render público** de cada um dos 18
   posts reproduz **byte a byte** os arquivos corrigidos de
   `articles/html_output/`. Prova de cobertura 100% antes de tocar no WP.
   (Detectou e corrigiu: duplicata de declaração no hw-b400f, vírgula órfã
   do soundcore, padrão de estrutura do purificador, aspas do band-10 e a
   declaração inline do book4.)
2. **`--baixar`** — `content.raw` autenticado (`context=edit`) → backup em
   `articles/wp_raw_backups/{id}-{slug}-raw.html` + espelho em
   `articles/wp_raw_mirror/articles/html_output/`.
3. **`--processar` + `--validar`** — pipeline sobre o espelho; **18/18
   válidos** (JSON-LD parseia, sem aggregateRating/reviewCount/ratingCount,
   declarações presentes, alegações reescritas, sem `<br/>` no JSON-LD).
4. **`--gravar`** — PUT do raw por post + releitura de verificação +
   auditoria do render público (JSON-LD parseia, sem aggregateRating,
   declaração visível). **18/18 gravados e conferidos.** Divergência aborta
   o lote e restaura o backup (rollback automático — não foi necessário).
5. **Auditoria final** — checker de 16 pontos sobre o espelho: 18/18 com
   `✅ [honestidade]`, 18/18 publicáveis, 0 bloqueios. Render ao vivo
   conferido por HTTP em amostra (book4, purificador, iphone-16e).

| ID | Slug | Δ chars |
|---|---|---|
| 4537 | apple-tv-4k | −366 (61 `<br/>` fora do JSON-LD) |
| 2954 | galaxy-s24-fe-em-2026 | −133 (aggregateRating) |
| 3871 | galaxy-watch7-44mm-vale-a-pena | −132 (aggregateRating) |
| 2921 | iphone-16e-review-2026 | +81 (declaração) |
| 3250 | jbl-cinema-sb180-review-vale-a-pena | +121 (declaração) |
| 4456 | lenovo-ideapad-slim-3-notebook-2026 | +98 (declaração) |
| 4397 | presentes-dia-dos-pais-tech-ate-300 | −396 (66 `<br/>`) |
| 3014 | purificador-de-agua-electrolux-pe12g-review | −90 (estrutura JSON-LD) |
| 4185 | samsung-galaxy-book4-review-2026 | +115 (citação + declaração) |
| 2905 | samsung-galaxy-s25-5g-review | −113 (aggregateRating) |
| 3310 | samsung-hw-b400f-review | +179 (citação + declaração) |
| 3126 | samsung-u8100f-smart-tv-4k-review | +88 (declaração) |
| 3169 | samsung-u8600f-review | +89 (declaração) |
| 2935 | soundcore-liberty-4-nc-vale-a-pena | −126 (vírgula órfã) |
| 4155 | tcl-c6k-review-2026 | +85 (declaração) |
| 4159 | xiaomi-redmi-note-14-pro-plus-review-2026 | +88 (declaração) |
| 3924 | xiaomi-smart-band-10-vale-a-pena | −101 (aspas do description) |
| 3835 | xiaomi-smart-band-9-active-vale-a-pena | −113 (aggregateRating) |

**Detalhe técnico (raw ≠ render)**: o WP guarda o raw com aspas retas
(`"Usei…"`) e o render texturiza (`&#8220;Usei…&#8221;`). Os literais de
correção têm as duas variantes (entidade casa com render, reta casa com raw);
dentro de `<script>` não há texturização (raw == render). O WP re-texturiza
o novo raw e o render final fica idêntico ao arquivo corrigido.

**Pendências restantes (editor, não bloqueiam):** data de verificação em 14
artigos · posição da divulgação de afiliado em 11 · bloco de contras em 9 ·
densidade de keyword em 6 · revisão visual das citações reescritas
(hw-b400f id 3310 e galaxy-book4 id 4185).