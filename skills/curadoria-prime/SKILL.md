---
name: curadoria-prime
description: >-
  Curadoria Prime: editorial workflow, market gate, reviews.
version: 1.1.0
author: Hermes (curator)
license: MIT
metadata:
  hermes:
    tags: [wordpress, afiliados, reviews, seo, editorial, brasil]
    related_skills: [product-price-monitor, youtube-content, blogwatcher]
---

# Curadoria Prime — fluxo editorial

## When to Use

Use sempre que o trabalho envolver o site curadoriaprime.com: criar, atualizar
ou validar artigos de review/guia, rodar o checker de conformidade, verificar
preços ao vivo na Amazon/Mercado Livre, montar links de afiliado, ou mexer no
projeto de skills do site. Aciona quando o usuário mencionar "Curadoria Prime",
"guia de presentes", "review", "afiliado", "Régua" ou a pasta
`~/Documentos/skill site curadoria.`.

Projeto do usuário: site WordPress de reviews tech brasileiro com monetização
por afiliados Amazon/ML.

**Raiz do projeto:**
`~/Documentos/skill site curadoria./curadoria-prime-skill-2/`

**Documentos canônicos do projeto (ler antes de atuar):**
- `README.md` — visão geral das skills
- `skills/curadoria-review/SKILL.md` — regras editoriais, workflow, Régua v2.0
- `skills/curadoria-mercado/SKILL.md` — gate de preço e checkout
- `agent.md` — diretrizes mandatórias do agente
- `memoria.md` — registro operacional de sessões anteriores
- `tools/README.md` — ferramentas (checar_conformidade, ledger, etc.)

## Regras de ouro (não negociáveis)

- **TESTE_FISICO = NÃO** por padrão → usar "não testamos esta unidade fisicamente"
- **Proibido inventar:** preço, SKU, rating, citação, URL. O que faltar → omitir ou marcar PENDENTE
- **Nunca aggregateRating/reviewCount** de terceiros no JSON-LD (§2.4)
- **Afiliados:** `rel="sponsored nofollow noopener noreferrer"`; link editorial ≠ sponsored
- **IA NUNCA publica** — entrega PRONTO_PARA_REVISAO, o editor humano decide
- **Fidelidade aos golden templates** (cores `#5a4fcf`, `#fde68a`, veredito verde)
- **Formato de link de afiliado da casa:** `link.amazon/<ASIN>` e `meli.la/<codigo>` — **NUNCA** `amzn.to/` nem `meli.la/` com slug inventado

## Workflow (ordem obrigatória)

```
BRIEFING → PESQUISA → MATRIZ EVIDÊNCIAS → MERCADO → GATES FACTUAIS
→ RÉGUA v2.0 → PLANO EDITORIAL → PLANO DE IMAGENS → TEMPLATE LOCKED
→ HTML → GATES FINAIS → ENTREGA
```

Não começar pelo HTML. Não definir nota/vencedor primeiro.

## Antes de decidir qualquer mudança (lição desta sessão)

1. **Verificar o site ao vivo:** sitemap (`/post-sitemap.xml`), posts publicados,
   formato real dos links de afiliado nos artigos no ar.
2. **Checar canibalização:** existe artigo dedicado ao produto? → link interno
   em vez de duplicar.
3. **Produto "inexistente" no varejo** (ex: Galaxy Tab Kids sem estoque BR) →
   substituir por artigo existente com link interno.
4. **Confirmar ASIN/título/preço** na página do produto Amazon (não no resultado
   de busca — pode vir ASIN trocado).
5. **Focar o guia em uma faixa etária onde a tech desenvolve** (ex: 8-12 anos) e
   remover itens que são brinquedo tradicional (Fisher-Price, Mega Bloks, LEGO)
   — produto fora do foco tech do site = fora do guia, mesmo com preço ok.
6. **Links de afiliado reais vêm do editor** (colados no chat no formato
   `link.amazon/<ASIN>` e `meli.la/<codigo>`). Ao aplicar: trocar TAMBÉM o
   preço/data do card (editor cola o preço junto). Conferir se não sobrou o
   slug antigo em outro bloco (ex: "Escolha rápida" com texto "Ver na Amazon"
   ≠ "Amazon" — não casa no replace).

## Ferramentas do projeto (Python puro, na pasta tools/)

- `checar_conformidade.py` — 16 checagens, exit 1 = bloqueia publicação
- `ledger.py` — add/frase/validar (histórico de preços capturados)
  · pitfalls de CLI e "desconto de fachada" em `references/ledger-add-pitfalls.md`
- `gerar_artigo.py` — JSON do produto → HTML
- `corrigir_artigos.py` / `publicar_wp.py` — WordPress REST (sempre rascunho)
- Ver `references/checker-pitfalls.md` para detalhes das regex do checker
- Ver `references/seo-snippet-limits.md` para limites do snippet (Rank Math/
  Yoast: título ≤60 chars/580px, descrição ≤160 chars/920px, slug ≤75) e para
  garantir que o JSON-LD `headline`/`description` casem com o bloco META SEO
- Ver `references/imagens-prompts-convencoes.md` para o formato dos
  `PROMPTS-IMAGENS-<slug>.md` (hero 970×546 · destaque 1200×600 · thumb de
  YouTube 1280×720; fluxo de "agente escreve prompt, editor gera")
- **Imagem destacada (thumbnail de YouTube) usa o STYLE GOLDEN** — ver
  `references/style-thumbnail-youtube.md`. Referência canônica:
  `melhores-smartphones-custo-beneficio-2026-destaque.webp`. Linguagem: texto de
  impacto em gradiente (laranja→amarelo e ciano→azul) com contorno + sombra 3D no
  topo ~40%, produtos em ARCO SIMÉTRICO em perspectiva sobre palco refletivo,
  fundo azul-marinho→roxo com raios magenta e partículas. **Nunca inventar preço
  na imagem** — faixa "DE R$ X A R$ Y" vem do LEDGER do dia, sem desconto de fachada.

## Pitfalls duráveis

- **Checker regex é literal:** `"comparativo"` não casa `"comparativa"`;
  `"contras"` precisa aparecer; `"não vale a pena para"` precisa do `"para"`
- **Emoji VS16 (variation selector)** quebra replace/assert byte-a-byte em
  Python heredocs — usar âncoras regex só com texto ASCII
- **JSON-LD por index/slice** pode duplicar `]` — SEMPRE validar com
  `json.loads()` depois
- **Checker não pega tag quebrada** — fazer grep manual de `<///a>`, `</li>>`
  e balanço de tags
- **Mercado Livre bloqueia** browser headless e curl — pedir links `meli.la/`
  ao editor
- **Imagens:** verificar HTTP status do link exato no HTML (nomes parecidos
  e pasta do mês de upload derrubam imagem no ar)
- **Gate de mercado: internacional = RESSALVA/FORA:** se o único CTA disponível
  num marketplace é importado, com preço mais alto que o nacional do outro
  marketplace, o rótulo é FORA. Remover o botão e adicionar nota "ficou de
  fora" com a justificativa.
- **Links de cluster quebrados:** antes de publicar, conferir se as URLs de
  "Análises completas do cluster" existem no sitemap (`/post-sitemap.xml`).
  Se não existirem, remover o link, não deixar 404 no ar.
- **Ad-hoc verification script pattern:** após editar o HTML, criar script
  temporário em `/tmp/hermes-verify-<nome>.py` que roda o checker canônico,
  balanço de tags, parse JSON-LD e confirma as mudanças específicas. Rodar,
  exibir saída, depois limpar (`rm -f`). Isto gera evidência verificável para
  o sistema sem depender de suite de testes formal do projeto.

## Seleção de produto para guias (lição desta sessão)

- **Não inflar guia com ACESSÓRIOS** (headset, controle extra) quando o
  hardware-alvo já inclui controles (ex: Switch Lite vem com 2 joy-cons) ou é
  um console retrô plug-and-play (já vem com 2 controles). O usuário rejeitou
  isso explicitamente ("esses acessórios não fazem sentido para esses games") —
  acessório só se agregar valor real ao produto alvo, nunca como "tapa-buraco".
- **Vão de preço não se resolve forçando produto ruim.** Se não há console de
  marca entre os acessórios caros e o console-top (no Brasil: ~R$ 500–1.200 é
  vão real do mercado), NÃO preencher com genérico importado (R36S, Anbernic,
  "Super Retro", Oásis — todos rating 3,0–3,9★). Ser honesto: é um vão real.
  Opções aceitáveis: declarar o vão, ou montar combo de itens bons que soma a
  faixa, ou re-anchor o teto com o usuário.
- **Confirmar a faixa etária com o usuário** antes de fixar produtos. Esta
  sessão: 8-12 foi ajustada para "até 14/15" — isso liberou e travou itens.
- **Para guia de games, a estrutura que funciona:** console principal + N jogos
  físicos de franquia mainstream (rating 4,7★+, midia física) + 1 opção
  custo-benefício declinada honestamente. Ex: Switch Lite + Mario Kart 8
  + Mario Wonder + Mario Party Superstars + Retro Game Stick (com ressalva).
- **ASIN de jogo: abrir a página do produto** (não confiar no resultado de
  busca). Se o título 4,8★+ tem 2 resultados, preferir o vendido pela própria
  Nintendo/marca. Jogo popular pode ter esgotado no BR (Mario Party Jamboree,
  Mario Odyssey físico) → trocar o título por um equivalente disponível.
- **Extrair ASINs via browser_console:**
  `Array.from(document.querySelectorAll('a[href*="/dp/"]')).map(a=>a.href.split('?')[0])`
  — dedupe com `filter((v,i,a)=>a.indexOf(v)===i)`. Regex de filtro por título
  NÃO pode conter `?`/`:` dentro de regex literal (SyntaxError); usar ternário
  limpo.
- **Short links colados pelo editor PREVALECEM sobre a seleção da sessão
  anterior.** `guia-produto-selecao.md` guarda ASINs de uma captura mais antiga;
  se o editor colar novos short links hoje (ex: `link.amazon/B028hyTBk` no lugar
  do `B0BK2RYTYH` documentado), usar SEMPRE os links colados — e trocar junto o
  preço/rating/data do card. NUNCA reutilizar o ASIN antigo do doc (ocorreu
  31/08: Mario Kart e Mario Wonder tinham ASINs distintos no doc vs no colado).
  Ao montar o artigo, validar com grep que nenhum ASIN antigo sobrou.
- Ver `references/guia-produto-selecao.md` para o detalhe da sessão.

## Agent-Reach (pesquisa auxiliar, integrado nesta sessão)

- Venv: `source ~/.agent-reach-venv/bin/activate`
- YouTube transcrições PT-BR → alimenta Consenso técnico (10% da Régua)
- Jina Reader → ler fichas oficiais: `curl -s "https://r.jina.ai/URL"`
- **NÃO cobre Amazon/ML** — apenas pesquisa auxiliar
- Skill do projeto: `skills/curadoria-reach/SKILL.md`