# ESTADO — 3139 (Samsung S90F QD-OLED review)

**Status:** ✅ FECHADO — versão correta publicada e conferida no ar (17/08/2026)

- URL: https://curadoriaprime.com/samsung-s90f-qd-oled-review/
- Título: Samsung S90F Vale a Pena em 2026? Review QD-OLED 4K 144Hz
- Entregável: `articles/samsung-s90f-qd-oled-review.html`
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **Links de afiliado** com `rel="sponsored noopener noreferrer nofollow"` (4 links: 2 Samsung + 2 LG). Os botões "Comparar Preços: LG C5" do publicado estavam SEM href (quebrados) — corrigidos.
- **"dados de compradores verificados" / "47 avaliações verificadas"** → "avaliações publicadas por compradores".
- **Alegação de uso removida**: "É frustrante voltar para controle comum depois de usar Magic Remote" e "navega 3-5x/5x mais rápido" → suavizadas (sem medição inventada).
- **Citações sem fonte verificável removidas** (5 blockquotes: "Usuário verificado", "Comunidade gamer Reddit (9,5/10)", "Review técnico em fórum", "fóruns especializados") → **"Síntese editorial dos relatos"** sem aspas/nome.
- **Placeholders vazados removidos**: "[INSERIR FOTO 3]", "[INSERIR FOTO 6]", "Nome do arquivo:", "Alt text:", "Legenda:" (eram TODO do rascunho publicado).
- **Texto duplicado/truncado corrigido** ("ente melhores que na LG C5.", "as HDMI 2.1... Empate técnico.") e typos "WOOLD" → "WOLED" (3×).
- **Superlativos suavizados**: "imbatível", "vence", "vencedor", "mágica tecnológica", "impossíveis", "Para 80% das pessoas".
- **Box de metodologia** com "não testamos esta unidade fisicamente".
- **Preços atualizados (16/08/2026)**: Samsung S90F ~R$ 6.478 (ML); LG C5 ~R$ 5.851–6.595. A diferença hoje é ~R$ 600 (não R$ 1.000 como no publicado).
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + Product (S90F, reviewRating 9,3/10 com worstRating) + FAQPage + BreadcrumbList (`tv-e-home-theater`); autor "Cristiano Martins"; sem aggregateRating/offers.
- **Bloco de autor canônico** + "Fontes consultadas" (Samsung, LG, Rtings.com) + "Veja também" (3153, 3226).

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 4/4 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.273 palavras · valor-agregado completo · imparcialidade 6 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 32/32 · ul 2/2 · ol 2/2 · p 57/57 · h2 11/11 · li 16/16 · a 21/21.
Zero base64. Zero citação inventada.
```

## Dados de mercado coletados (16/08/2026)

| TV | Amazon BR | Mercado Livre | Estoque |
|---|---|---|---|
| Samsung S90F 55" QD-OLED | ASIN B0FNT5H95K — **sem oferta em destaque** (só terceiros: Fast Shop R$ 5.939 / Samsung R$ 7.289) | **MLB54140106** (Fast Shop, R$ 6.478) — shortlink `2fDo1zK` OK | ✅ ML · ⚠️ Amazon (terceiros) |
| LG OLED C5 55" | ASIN B0F5X3WY5N — **"Não disponível" (esgotado)** | **MLB53613524** (R$ 6.525) — shortlink antigo `1rZFCkW` quebrado | ✅ ML · ❌ Amazon |

- **Atualizado no artigo (16/08):** os dois modelos estão **sem estoque na Amazon BR** — botões de compra apontam para o **Mercado Livre** (única loja com disponibilidade), com nota explícita de estoque. 4 links ML, todos sponsored. Zero botão Amazon.
- Samsung Amazon BR: 4,8/5 em ~39 avaliações (dado mantido só como contexto, sem botão).
- ⚠️ **Cliente deve gerar novo shortlink ML para a LG C5** (MLB53613524) — o atual `1rZFCkW` resolve para lista vazia.

## ✅ RECONFERIDO NO AR (17/08/2026) — RESOLVIDO

O cliente recolou o conteúdo. A versão publicada agora **corresponde** ao arquivo
do repo. Conferido via WP REST API (`posts/3139`, `modified` = 2026-08-16T21:03:21)
e via página renderizada:

| Sintoma da versão antiga | Estado no ar em 17/08/2026 |
|---|---|
| botão LG C5 no shortlink quebrado `1rZFCkW` | ✅ substituído pelo link canônico `/p/MLB53613524` |
| "Avaliação na loja: 4,9/5 · 47" | ✅ agora "4,8/5 em cerca de 38 avaliações (16/08/2026)" |
| sem nota de "sem estoque" na Amazon | ✅ presente nos dois CTAs (topo e rodapé) |
| botões Amazon | ✅ removidos; 4 links, todos Mercado Livre |
| aviso de estoque + gancho LG C6 | ✅ presente nos dois CTAs |
| bloco de autor | ✅ canônico (foto + bio Uberlândia + x.com/CuradoriaPrime) |
| JSON-LD | ✅ `@graph` TechArticle + Product (9,3/10, worstRating) + FAQPage + BreadcrumbList, sem `aggregateRating`, sem `offers`, sem `<br/>`, autor "Cristiano Martins" |
| "Fontes consultadas" | ✅ presente (Samsung, LG, Rtings + nota ML/Amazon) |

Revalidação local do arquivo: `python3 tools/checar_conformidade.py articles/samsung-s90f-qd-oled-review.html`
→ **✅ Aprovado — 0 erros, 0 alertas**; `rel="sponsored noopener noreferrer nofollow"` em 4/4
links de afiliado; zero base64.

### Histórico do problema (16/08/2026)

O artigo **publicado** está com uma **versão antiga** (a primeira reescrita), não a final. Sintomas no ar:

- Botão "Comparar com LG C5" ainda aponta para o shortlink **`1rZFCkW` (quebrado — lista vazia)**;
- Ainda mostra "Avaliação na loja: 4,9/5 · 47" (versão antiga; o correto é "Amazon BR: 4,8/5 · ~39");
- Sem a nota de "sem estoque" na Amazon e sem os botões ML-only com link direto `/p/MLB53613524`.

**Ação:** recolher o conteúdo de `articles/samsung-s90f-qd-oled-review.html` (versão atual do repo) substituindo o publicado. → **FEITO pelo cliente em 16/08/2026 21:03; conferido em 17/08/2026.**

## Aviso de estoque + gancho C6 (adicionado 16/08/2026)

Adicionado aviso "estoque baixo ou zerado" nos dois CTAs (topo e rodapé),
apontando o provável motivo: a chegada da sucessora **LG C6 (2026)**. O aviso
termina com o gancho "Em breve: review dedicado da LG C6 aqui na Curadoria
Prime" — quando o post da C6 for publicado, trocar o texto pelo link real.

## Pendências FORA do arquivo (painel / cliente)

1. ~~**Colar no WP** substituindo o conteúdo atual (Editor de Código).~~ ✅ FEITO (16/08, conferido 17/08).
2. ⚠️ **Amazon BR SEM estoque nos dois modelos (16/08/2026)** — resolvido no artigo: botões apontam para o Mercado Livre. Se a Amazon voltar a ter estoque, ASINs registrados: S90F `B0FNT5H95K` · C5 `B0F5X3WY5N`.
3. ⚠️ **Cliente deve gerar novo shortlink ML para a LG C5** (MLB53613524) — o `1rZFCkW` está quebrado (lista vazia). O artigo usa o link canônico como fallback.
4. Shortlink Samsung S90F (`2fDo1zK`) OK → MLB54140106.
5. ~~Contagem "47 avaliações / 4,9/5"~~ ✅ resolvida: Amazon BR hoje = 4,8/5 em ~39 avaliações.
6. Título SEO: manter "144Hz" e conferir "QD-OLED" no H1.
