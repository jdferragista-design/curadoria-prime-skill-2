# MEMÓRIA — curadoria-prime-skill-2

Registro operacional das sessões de trabalho. Objetivo: qualquer sessão futura
retomar exatamente daqui sem re-diagnóstico.

---

## Sessão 29/08/2026 — browser-harness instalado + guia melhores-smartphones-custo-beneficio-2026 criado

### Estado encontrado ao retomar

- Pauta de 15 dias aprovada; primeiro item: `/melhores-smartphones-custo-beneficio-2026/` (02/09).
- Pedido do dono: instalar o **browser-harness** para melhorar criação/atualização de artigos.
- Todos os dados de preço/rating foram coletados ANTES com curl/WebSearch; nesta sessão o fluxo passou a usar browser-harness.

### O que foi feito

**1. Browser-harness instalado e conectado (configurado em 29/08/2026)**
- `uv 0.12.7` instalado em `~/.local/bin`; `browser-harness 0.1.10` via `uv tool install --python 3.12`.
- Skill registrada em `~/.claude/skills/browser-harness/SKILL.md` (o dono rodou o comando — o classificador do Claude exige confirmação explícita do usuário para instalar pacote externo e escrever nessa pasta).
- Conexão ao Chrome local via CDP: `chrome://inspect/#remote-debugging` → marcar "Allow remote debugging".
- Gravações locais **desabilitadas** (default). Comando único `.ll: `browser-harness` com heredoc Python (`print(page_info())`).
- Uso: para scraping dinâmico/preço autenticado, preferir browser-harness; para HTML estático, `curl` com UA de navegador continua.

**2. Artigo `melhores-smartphones-custo-beneficio-2026` (AGENDADO 02/09/2026 08:00)**
- Re-angle aprovado pelo dono: guia "melhores celulares custo-benefício 2026" por faixas de preço (até R$ 1.000 / R$ 1.000–1.600 / acima de R$ 2.000), maximizando link interno para os 5 reviews já publicados.
- Arquivo: `articles/html_output/melhores-smartphones-custo-beneficio-2026.html` · 2.668 palavras · nota guia **8,2/10** (Régua v2.0) · produto-âncora **Redmi Note 15 Pro 5G**.
- **Dados reais capturados via browser-harness na Amazon em 29/08/2026**:
  - Galaxy A16 5G → R$ 892 · 4,8★ · 1.085 avaliações
  - Galaxy S24 FE → R$ 1.414 · 4,6★ · 180 avaliações
  - Moto G56 5G → R$ 1.599 · 4,8★ · 1.584 avaliações
  - Redmi Note 14 Pro+ → R$ 2.049 · 4,5★ · 134 avaliações
  - Redmi Note 15 Pro → R$ 2.055 · 4,8★ · 308 avaliações
- Links de afiliado reais extraídos dos reviews publicados (link.amazon/B0bJP0Zmr G56/A16, B02dV4jSd N15P, B0cenYgnK N14P+, meli.la/*).
- **Imagens**: todas reais do WP Media — hero nova `hero-melhores-smartphones-custo-beneficio-2026-scaled.webp` + fotos dos 5 produtos vindas dos reviews (frente-atras G56, D_NQ_NP ML A16, redmi-note-15-pro-5g-preto-frente-verso, Redmi-Note-14-Pro-Plus-5g-1800x984, galaxy-s24-review-2026.png).
- Prompts de geração de imagem (hero 970×546 + destaque 1200×600): `articles/html_output/PROMPTS-IMAGENS-melhores-smartphones-custo-beneficio-2026.md`.
- Checker: **0 erros** (JSON-LD TechArticle+ItemList+FAQPage, 12 links sponsored, honestidade, fontes URL reais).
- Único alerta não-bloqueante: "galaxy" 3,7% (keyword-stuffing; aceitável pois é marca Samsung em 3 produtos).
- Fila: registrado como **AGENDADO 02/09/2026 08:00** em `fila-atualizacao.md`. Pendência: re-verificar preços no dia.

### Lições aprendidas

- **ASINs podem estar trocados na busca da Amazon**: o primeiro resultado de "redmi note 15 pro" retornou outro produto (R$ 4.949, 1★). SEMPRE abrir a página de produto (confirmar título) antes de gravar preço/ASIN.
- **Seletores da Amazon variam**: `#productTitle`/`.a-price-whole` só existem na página de produto; na listagem usar `[data-component-type="s-search-result"]`. Algumas buscas retornam revendedor caro — cruzar com o review publicado (que já tem o ASIN/link de afiliado correto).
- **Mercado Livre via browser-harness**: `.poly-card` e `.ui-search-layout__item` não retornaram; preços do ML em buscas vieram muito altos (revendedor). Para o ML, confiar nos links de afiliado do review publicado + WebSearch.
- **Instalar ferramenta externa exige confirmação do usuário**: o classificador do Claude bloqueia `uv tool install` e escrita em `~/.claude/skills/` até o usuário confirmar explicitamente (run manual via `!`, ou regra de permissão). Não contornar o bloqueio.
- **Imagens dos produtos devem vir do WP Media dos reviews publicados**, nunca placeholder inventado — o dono pediu explicitamente.

---

## Sessão 24/08/2026 — retomada e fechamento dos 3 guias novos

### Estado encontrado ao retomar

- `power-bank-no-aviao` aprovado; `guia-volta-as-aulas` e `tablet-infantil`
  bloqueados no `checar_conformidade.py`.
- Auditoria dos 48 artigos (`audit/auditoria-48-artigos.csv`) já regenerada com
  checagens de schema (JSON-LD inválido, `aggregateRating`/`reviewCount` §2.4).

### Correções aplicadas

**1. `articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html`**
- Tag `<script type="application/ld+json">` duplicada na linha 595 removida
  (causava "JSON-LD inválido" — bloqueio).
- Adicionada seção "⚖️ Prós e contras do kit completo" (grid verde/vermelho,
  padrão golden) entre "Escolha Rápida" e "Para quem é".
- Resultado: ✅ aprovado · 2.439 palavras · 0 erros/avisos.

**2. `articles/html_output/tablet-infantil-dia-das-criancas-2026-3-melhores.html`**
- Bloqueio [teste-fisico]: "Testamos na teoria (fichas oficiais + avaliações de
  pais)" → "Analisamos as fichas técnicas oficiais ... cruzamos com relatos
  publicados por pais".
- **3 citações falsas de pais removidas** (marcadas `[EXEMPLO]` nas linhas 62/65/68)
  → substituídas por resumos neutros das avaliações agregadas verificáveis
  (nota média + volume + data). Nota ao editor movida para comentário HTML.
  Lição: não reescrever citação fake em outra alegação não verificada.
- Data futura visível `🕒 Atualizado: 10/09/2026 [RE-VERIFICAR]` →
  `🕒 Verificado: 08/08/2026`.
- Badge hero "Controle parental testado" → "comparado".
- Notas de edição ("re-verificar em 10/09") retiradas do texto visível;
  mantidas apenas em comentários HTML.
- Link oficial Positivo perdeu `rel="sponsored noopener noreferrer nofollow"`
  (fonte editorial ≠ afiliado).
- Typo "Samsung Kids e alternatives testados" → "alternativas analisadas".
- Adicionada seção "🚫 Para quem NÃO vale a pena" (4 casos, inclui SBP <2 anos).
- Resultado: ✅ aprovado · 2.484 palavras · 0 erros/avisos · densidade "kids" normal.

**3. `power-bank-no-aviao-regras-anac-2026.html`** — já estava aprovado; nada
de conteúdo alterado nesta sessão.

### Publicação

- `/power-bank-no-aviao-2026/` — **FINALIZADO E AGENDADO pelo editor para
  25/08/2026 08:00** (título Rank Math: "Power Bank no Avião: Não Seja Barrado
  no Raio-X — Regras ANAC 2026"). Cabeçalho interno do arquivo atualizado para
  refletir o agendamento. Badge "Atualizado: 07/08/2026" preservado (é a data
  da última verificação factual).
- Fila atualizada: entrada nova em P1 marcada CONCLUIDO/agendado.

### Correção tardia 24/08 — guia-volta-as-aulas (achado na revisão manual)

O checker não pega estrutura HTML quebrada. Achados e corrigidos:

1. **Parágrafo do hero truncado**: "...para te dar o [blocos da Régua
   injetados aqui] veredito definitivo." — os dois blocos Régua v2.0
   ("Como chegamos às notas" + "Notas por critério"/Nota Geral) estavam
   DENTRO da frase, dentro do box gradiente do hero. Frase completada com
   `<strong>veredito definitivo</strong>` e blocos realocados para a posição
   canônica: entre FAQ e Veredito Final.
2. `mainEntityOfPage` apontava `/kit-volta-as-aulas-tech-2026/` ≠ canonical
   `/guia-volta-as-aulas-tech-2026-7-itens/` → alinhado ao canonical.
3. `dateModified` (05/08) anterior ao `datePublished` (19/08) → 24/08/2026.
4. Cabeçalho Rank Math (título/slug/meta/pré-publicação) adicionado após
   `<body>`, no padrão do power-bank.
5. Validação pós-fix: tags div/p balanceadas (101/101, 36/36), JSON-LD ok,
   checker 0 erros.

**Lição**: rodar também checagem de balanço de tags + leitura visual do topo
do arquivo; o `checar_conformidade.py` valida conteúdo, não montagem.

### O que ainda falta no guia-volta-as-aulas (para o editor)

| Item | Detalhe |
| --- | --- |
| Re-coleta de preços/links | última coleta 05/08/2026 (~20 dias) — re-verificar antes de agendar |
| Upload de imagens no WP Media | hero `hero-kit-volta-aulas-2026.jpg` + 7 fotos de produto hoje hotlinkadas de `m.media-amazon.com` |
| Definir data de publicação/agendamento | datePublished placeholder 19/08; ajustar ao agendar |


### Validação final (24/08)

```
python3 tools/checar_conformidade.py articles/html_output/*.html
→ 3 arquivo(s), 0 erro(s) total.
```

---

## Sessão 24/08/2026 (noite) — fechamento do guia-volta-as-aulas

### Mercado: recaptura dos 14 links de afiliado (Amazon + ML, 7 produtos)

- Preços mudaram em 12 das 14 URLs. Novo total do kit: **R$ 1.563,97**
  (era R$ 1.569,03). Range do título: "de R$ 69 a R$ 639".
- Destaques: M185 Amazon 67,19→68,90 (Pix); K380s Amazon 193,99→197,99
  (a Amazon hoje lista a variante "K380s"); JBL Amazon 235→232; Anker 737
  Amazon **636,64→748,99** (+18%, A1695) — menor preço agora é o ML
  **R$ 639 cupom** (modelo A1289 24K/140W); AX12 ML 179,10→**169,15** Pix;
  UGREEN ML 89→99; suporte Amazon 170,05→**157,93** Pix.
- **Achado P0**: os links da seção 7 NÃO entregam mais o "Suporte PRINCASE"
  — a Amazon hoje vende um suporte genérico giratório 360° com ventoinha
  (R$ 157,93, vendedor terceiro/FBA; ML R$ 188). Seção reescrita para o
  produto real (specs: metal, 4–26 cm, gira 360°, ventoinha, até 10 kg);
  card "Pontos de atenção" trocado para aviso de vendedores terceiros;
  foto antiga do PRINCASE removida → placeholder uploads/suporte-giratorio-
  notebook-ventoinha.jpg (editor sobe a correta antes de publicar).
- Contagens de avaliações não-recapturadas mantidas com rótulo duplo no box
  ("avaliações coletadas em 05/08 · preços re-verificados em 24/08").
  Números duvidosos do hub (30.181 vs 6.442 inconsistentes) removidos → "—"
  na tabela e frase qualitativa na seção.
- LEDGER: +14 capturas (2026-08-24), `validar` sem erros.
- **Aviso Anker 737 reforçado (pedido do editor)**: Amazon e ML vendem itens
  DIFERENTES — Amazon só tem A1695 (25K/165W, R$ 748,99); o A1289
  (24K/140W, R$ 639 cupom) é exclusivo do Mercado Livre. Aviso destacado
  no card da seção 4, nota curta no card-âncora, reforço no parágrafo e
  nos "Pontos de atenção" (`tools/patch_guia_d.py`).

### Correções estruturais que o checker não pega

1. `mainEntityOfPage` apontava `/kit-volta-as-aulas-tech-2026/` → alinhado
   ao canonical `/guia-volta-as-aulas-tech-2026-7-itens/` (o fix reportado
   na sessão anterior NÃO havia persistido no arquivo).
2. `</script></script>` duplicado após o JSON-LD → um único fechamento.

### Como foi editado

Patches auditáveis em `tools/patch_guia_{a,b1,b2,b3,b4,c}.py`: cada par
old→new exige contagem == 1, abortando sem gravar se divergir. 93+7
substituições aplicadas. Lição: NÃO disparar múltiplas edições editor no
MESMO arquivo em paralelo — uma sobrescreveu a outra (header Rank Math
precisou ser reaplicado).

### Validação final

```
python3 tools/checar_conformidade.py articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html
→ ✅ Aprovado · 0 erro(s) · 2.480 palavras
tags balanceadas (div 101/101 etc.) · JSON-LD parseável · soma das ofertas = R$ 1.563,97
```

### Reposicionamento editorial (25/08, pedido do editor)

Editor não quer publicar com tema "volta às aulas" no fim de agosto.
Escolhido o ângulo **evergreen**: "7 Melhores Techs Custo-Benefício para
Trabalhar e Estudar (2026)".

- Novo keyword foco: `melhores techs custo-benefício` (14 menções exatas +
  6 variantes naturais no corpo; casos de uso de estudo/trabalho mantidos).
- Novo slug/canonical/mainEntityOfPage: `/melhores-techs-custo-beneficio-2026/`.
- Arquivo renomeado: `articles/html_output/melhores-techs-custo-beneficio-2026.html`.
- Hero renomeado: `hero-melhores-techs-custo-beneficio-2026.jpg` (antes do upload!).
- Meta description e JSON-LD (headline/description/name/FAQ question) reescritos.
- Patches: `tools/patch_guia_e.py` (20 pares + 8 alts), `tools/patch_guia_f.py`
  (alt do hero + ref da imagem x3). Grep final: ZERO resíduos de volta às aulas.
- Lição: o fix do `mainEntityOfPage` reportado na sessão anterior não tinha
  persistido por edições paralelas no mesmo arquivo — sempre serializar.

### Alinhamento ao padrão golden (25/08, apontado pelo editor)

Editor marcou 5 seções fora do padrão. Comparação feita com os modelos
golden (`modelo-lista-golden.html` e `modelo-review-golden.html`):

1. **⚡ Escolha Rápida** → agora 3 blocos FIXOS lado a lado
   (`repeat(3, 1fr)` + fallback 1 coluna <782px), cards com borda superior
   colorida por cenário.
2. **📊 Como chegamos às notas** → substituído pelo box amarelo 🧮 do
   review-golden ("Como chegamos à nota 8,5", texto corrido com os pesos +
   link como-avaliamos).
3. **📊 Notas por critério** → substituído pelo bloco de avaliação golden:
   cabeçalho com badge escuro "8.5/10 ⭐ Recomendado" + grid 3×2 de critérios
   (label uppercase, nota 36px colorida — âmbar p/ 7,0–7,5, verde p/ ≥8,0)
   com `<style>` responsivo (782px→2col, 480px→1col). Nota Geral antiga
   incorporada ao badge.
4. **❓ Perguntas Frequentes** → 6 Q&A convertidos para os cards roxos do
   lista-golden (#5a4fcf) com sombra.
5. **📑 Índice do conteúdo** → inicialmente removido por engano (nenhum
   golden tem índice). Editor corrigiu: era para MUDAR PARA O PADRÃO.
   Restaurado em `tools/patch_guia_h.py` com a linguagem visual dos goldens
   (card branco #e2e2f0, título uppercase, setas ▸ roxas #5a4fcf, links
   cinza, 2 colunas c/ fallback mobile). Bônus: as âncoras antigas
   `#resposta-rapida` e `#tabela` eram QUEBRADAS (nunca existiram como id);
   novo índice tem 12 itens, todos verificados contra os ids reais.

Patches: `tools/patch_guia_g_blocks_{a,b}.py` (templates) +
`tools/patch_guia_g.py` (lógica por âncoras; FAQ via regex com assert de 6).
Validação: checker 0 erros, tags balanceadas, JSON-LD íntegro, zero resíduos
das versões antigas.

### Pendências restantes deste guia (só o editor resolve)

| Item | Detalhe |
| --- | --- |
| Upload de imagens no WP Media | hero + 7 fotos (foto do suporte é a do modelo giratório c/ ventoinha) |
| Definir data/agendamento | datePublished segue placeholder 19/08 até agendar |

---

## Pendências abertas

| Item | Prazo/condição |
| --- | --- |
| Re-verificar preços/estoque do tablet-infantil antes de publicar | 10/09/2026 (nota em comentário HTML no arquivo) |
| ~~Agendar/publicar `guia-volta-as-aulas-tech-2026-7-itens.html`~~ | **24/08**: conteúdo 100% fechado (mercado re-verificado, checker 0 erros) — estado PRONTO_PARA_REVISAO; faltam só imagens no WP Media + decisão de agendamento |
| Agendar/publicar `tablet-infantil-dia-das-criancas-2026-3-melhores.html` | após re-verificação de 10/09 |
| Confirmar colagem dos `-JA-COLADO` em `articles/correcoes/` (rodada 20-23/08) | já confirmado por diff — ver RELATORIO-CORRECOES |
| ~~Git: working tree com mudanças não commitadas~~ | **CONCLUIDO 24/08** — commits rebased sobre origin/main; `.gitignore` raiz criado. **Dados sensíveis FICAM FORA do repo**: `opencode.json` (com apiKey), `*.bak`, `*.odt` e node_modules ignorados. Incidente corrigido: um commit chegou a incluir o `opencode.json` e foi eliminado do histórico por rebase-drop ANTES de qualquer push — nada vazou ao remoto; ficheiro restaurado no disco. Push ao origin ainda pendente. |

---

## Convenções da casa que esta sessão reforçou

- Nunca publicar nota agregada de terceiros como nossa (`aggregateRating`,
  `reviewCount`, `ratingCount` no JSON-LD) — §2.4.
- Fontes editoriais (manuais, páginas oficiais) NÃO levam `rel="sponsored"`;
  só deep-links de afiliado.
- Sem alegação de teste físico sem selo "Testado por nós"; usar
  "analisamos especificações + relatos de compradores".
- Citação textual de consumidor só com fonte real verificável (nome
  semi-anonimizado + data + plataforma). Placeholder `[EXEMPLO]` nunca viaja
  para produção.
- Datas visíveis = datas de verificação real; instruções de fluxo vão em
  comentário HTML.

---

## Sessão 25/08/2026 — fechamento visual e de fontes do `melhores-techs-custo-beneficio-2026`

Arquivo: `articles/html_output/melhores-techs-custo-beneficio-2026.html`

### 1. 🏆 Veredito Final — visual realinhado ao golden
- O bloco destoava: fundo azul `#dbeafe` + borda `#1a1f5c` e grid de **4 métricas
  inventadas** (9,0 Custo-benefício · 8,8 Qualidade · 8,5 Cobertura · 8,5 Prova
  social) que não pertencem à Régua v2.0 e contradiziam o bloco de avaliação
  canônico já presente no artigo.
- Substituído pelo componente canônico `💡 Veredito:` (fundo `#f0fdf4` + borda
  esquerda `#22c55e`), texto do veredito mantido, nota **8,5/10 (Régua v2.0)**
  agora coerente com o badge do bloco de avaliação.

### 2. 🔄 Alternativas e upgrades — 3 blocos lado a lado
- Grid `auto-fit minmax(280px)` → **`repeat(3, 1fr)` fixo** (padrão Escolha
  Rápida) + fallback `@media <782px → 1 coluna`. ID wrapper `#alternativas-blocks`.

### 3. 📚 Fontes consultadas — reconstruída (editor apontou escassez)
- Antes: só 5 homepages institucionais + frase sem links → falso positivo do
  checker (conta `<li><a>`, reportava "~0 itens").
- Agora: lista `<ul><li>` com **~6 itens**, fichas oficiais reais fornecidas
  pelo editor + preços com `rel="sponsored"`:
  - Anker 737 A1289 (`anker.com/products/a1289`) — confirmado ao vivo 24.000mAh/140W
  - TP‑Link Archer AX12 BR (`tp-link.com/br/.../archer-ax12/`) — confirmada BR
  - JBL Wave Buds 2 (`jbl.com.br/WAVE-BUDS-2.html`) — URL do editor (fetch 403)
  - Logitech Pebble Keys 2 (`logitech.com/pt-br/shop/p/pebble-keys-2`) + homepage
  - UGREEN BR Hub 5‑in‑1 (`ugreenofficial.com.br/.../ugreen-ultra-slim-5-in-1-usb-c-hub`) — confirmado ao vivo (HDMI 4K30, 2× USB‑A, Ethernet)
  - Xiaomi Mi BR Power Bank 10.000mAh 22,5W (`mibrasil.com.br/...p5652`)
  - Amazon/ML com data 24/08
- Nota: JBL, Logitech e Mi/Brasil **bloquearam o fetch** — usadas as URLs do
  editor como fonte editorial; confirmação visual final fica com o editor.

### 4. Correção de VERACIDADE no card de upgrade (§7 / regra final)
- O card dizia `Xiaomi 10.000mAh (R$ 149) e economize ~R$ 490`. **R$ 149 sem
  origem no LEDGER** (só há Xiaomi *Pad* lá). Preço inventado → removido.
- Rescrito: "troque o Anker 737 por um Xiaomi 10.000mAh 22,5W — economiza
  (valor varia; veja o preço do dia na loja oficial Xiaomi Brasil)" + link real
  da loja oficial na seção de fontes.

### Validação
```
python3 tools/checar_conformidade.py articles/html_output/melhores-techs-custo-beneficio-2026.html
→ ✅ Aprovado · 0 erros · 2.740 palavras · fontes ~6 itens · 18 afiliados com rel="sponsored"
div 110/110 · ul 9/9 · nenhum resíduo de "R$ 149"/"economize 490"
```

### Pendências deste guia (só o editor)
| Item | Detalhe |
| --- | --- |
| Subir imagens no WP Media | hero `hero-melhores-techs-custo-beneficio-2026.jpg` + 7 fotos |
| Definir agendamento | datePublished 19/08 está como placeholder até agendar |
| Confirmar visual JBL/Logitech/Mi | fetch bloqueado por bot; conferir páginas antes do ar |
| Preço do Xiaomi 10.000mAh | quando capturar, voltar o R$ com data no card e adicionar ao LEDGER |

### Lições desta sessão
- O `checar_conformidade.py` não mede QUALIDADE de fontes — só presença
  (`<li><a>`). Revisão humana segue necessária para rastreabilidade (§14).
- Link de afiliado na seção de fontes PRECISA de `rel="sponsored"`, senão o
  gate bloqueia (pegou na primeira passada).
- Preço "de upgrade/alternativa" sem origem em captura (LEDGER) = dado não
  rastreável → omitir, não inventar.

---

## Sessão 25/08/2026 (tarde) — tablet-infantil: capturas reais do editor aplicadas

Arquivo: `articles/html_output/tablet-infantil-dia-das-criancas-2026-3-melhores.html`
Patch auditável: `tools/patch_tablet_infantil_mercado.py` (40 substituições, count==1).

### Contexto
Avaliação prévia apontou: HTML quebrado no índice (bloco de avaliação "engolido"
pelo href do item 🔟), 3 famílias de notas conflitantes (9,0/8,5/8,5 vs 8.9/8.7/8.3
vs Nota Geral 7,5), preço do Positivo 383 vs 499, e LEDGER vazio para os 3 SKUs.

### Capturas reais do editor (25/08/2026)
1. **Multi Kid Pad NB425 (Multilaser)** — ML: ⭐ 4,4/5 · **129 opiniões** · R$ **856,75** Pix
   (de R$ 1.229, 30% OFF) · R$ 866,75 outros meios. Amazon: ⭐ **2,9/5** · **24 globais**
   (10 BR) · R$ **884,44** (de R$ 949,99, 6% off) · URL `link.amazon/B0alnCFJU`.
   Relatos: elogios a resistência/tela; críticas fortes a travamento, superaquecimento
   e **bateria que para de carregar** (múltiplos relatos <1 ano).
2. **Galaxy Tab A9 64GB/4GB prata** — ML: ⭐ **4,9/5** · **1.345 opiniões** · Loja oficial
   Samsung · MAIS VENDIDO (11º em Tablets Samsung) · R$ **1.114** Pix / R$ 1.124 outros.
   **Amazon sem estoque do Tab A9** (anúncio atual = A9+ 11", outro aparelho).

### O que foi alterado no HTML
- **Notas unificadas**: Multi 9,0→**7,0/10** (dados contradizem 9,0); A9 e Vision → 8,5/10
  em todo o artigo (tabela, H2, veredito, cards, JSON-LD ratingValues).
- **Ranking reordenado**: Tab A9 vira a recomendação "mais confiável"; Multi passa a
  "melhor custo-benefício em tela grande, com ressalva de durabilidade".
- **Preços**: Multi R$ 856,75 (Pix) / 884,44 (Amazon); Tab A9 R$ 1.114 (Pix) — aplicados
  em hero, badges, tabela, resposta rápida, veredito, cards e FAQ (HTML + JSON-LD).
- **Prova social** reescrita com dados reais (ML 4,4/5·129 e Amazon 2,9/5·24 do Multi;
  ML 4,9/5·1.345 do A9). Removido "4,8/5 · ~1.200" e "4,5/5 · 4.663" (não batiam).
- **CTA do Tab A9**: botão Amazon REMOVIDO (aponta p/ A9+ 11" errado e sem estoque);
  aviso âmbar + botão único ML.
- **CTA do Multi**: href Amazon atualizado para `B0alnCFJU` (URL da captura do editor).
- **HTML quebrado corrigido**: item 🔟 do índice agora `#veredito`; bloco "Como chegamos
  às notas" + "Notas por critério" virou bloco `wp:html` próprio (antes engolido pelo href).
- **mainEntityOfPage** alinhado ao canonical `/tablet-infantil-dia-das-criancas-2026-3-melhores/`.
- **Fontes** reestruturada em `<ul><li>` (4 itens) com datas de verificação/re-verificação.

### LEDGER
+4 capturas (2026-08-25): `multi-kid-pad-nb425/ml` e `/amazon`, `galaxy-tab-a9/ml`,
`positivo-vision-tab-7-minions/ml`. `ledger.py validar` → 0 erros, alertas esperados
(3 linhas novas sem URL de ML — captura do editor não trouxe URL de anúncio; 1 "desconto
de fachada" no Tab A9).

### Parte 2 — Positivo Vision Tab 7 (captura real do editor)
Patch: `tools/patch_tablet_infantil_positivo.py` (15 substituições).
Dados reais: ML ⭐ **4,7/5 · ~1.196 opiniões** · MAIS VENDIDO (9º Tablets Positivo) ·
R$ **571,12 Pix** (de R$ 629) / R$ 581,12 outros / 10x R$ 58,11 · inclui **capa + mochila**.
Relatos: custo-benefício/design/resistência elogiados; bateria curta (~2–3h), esquenta,
câmera fraca, Android Go limita apps.
- Preço corrigido em hero/badge/tabela/resposta rápida/card/veredito/fontes
  (**resolveu o conflito R$ 383 vs R$ 499 — ambos errados**); faixa do badge → "De R$ 571 a R$ 1.124".
- Hero "**+18 mil avaliações**" removido (real: ~2.700 somadas nas lojas).
- Frase truncada da seção Vision completada ("A capa protetora" sem continuação) +
  capa/mochila inclusas + ressalvas reais.
- Card de avaliação do Vision reescrito (era "Amazon 4,6/5 · ~640", não confirmado).

### Parte 3 — Amazon do Vision Tab 7 (captura real do editor)
Patch: `tools/patch_tablet_infantil_amazon_vision.py` (12 substituições).
Dados reais: Amazon **R$ 409,52 Pix/NuPay** (de R$ 626,92) / R$ 455,04 em 9x R$ 50,56 ·
⭐ **4,1/5 · 38 globais** (19 BR) · loja oficial Positivo · kit inclui **só capa** (sem mochila).
URL da captura: `link.amazon/B0cJleAj2` — botão Amazon do card atualizado para ela.
- Vision vira o mais barato do comparativo: **R$ 409,52 (Amazon, só capa) vs R$ 571,12
  (ML, capa + mochila)** — kit varia por loja, explicitado em hero/resposta rápida/
  tabela/card/seção/fontes/veredito.
- Card de avaliação do Vision agora mostra ML 4,7/5·1.196 E Amazon 4,1/5·38.
- Badge faixa → "De R$ 409 a R$ 1.124". "Escolha da Amazon" NÃO usado como selo
  (regra da skill mercado).

### Parte 4 — reorganização estrutural e visual para o padrão canônico
Script: `tools/reorganiza_tablet_infantil.py` (fatiamento por linhas com asserts de limites).
**Ordem anterior estava fora do padrão**: byline no topo, box "Tipo de análise" duplicado
(antes do hero E após a byline), bloco Régua logo após o índice (antes da intro e dos
produtos), transparência depois da intro, sem "Última atualização".
**Nova ordem (= melhores-techs aprovado)**:
1. Transparência → 2. Hero (escurecido #9B2226→#5C1013; era vermelho claro #FF6B6B)
→ 3. Hero image → 4. Prova social → 5. Índice golden (setas ▸ roxas, card branco,
2 colunas; eram emojis numerados) → 6. Intro → 7. Tipo de análise (1× só) →
8. Metodologia → 9. Resposta rápida → 10. Tabela → 11-13. Produtos →
14. Controle parental → 15. Idade → 16. Para quem NÃO → 17. Quando comprar →
18. FAQ em cards roxos (eram boxes cinza) → 19. **Régua movida p/ pos-FAQ**
(posição canônica) → 20. Veredito + **box 💡 verde** com o resumo → 21. Onde comprar →
22. Fontes → 23. 📌 Última atualização (novo) → 24. Byline movida p/ o fim →
25. Aviso de afiliado → JSON-LD.
Extras: adicionado `<!-- /wp:html -->` faltante do bloco Régua (perdido no FIX B
da sessão anterior); box "Tipo de análise" duplicado do topo removido.
Validação: div 88/88 · ul 8/8 · li 36/36 · p 44/44 · checker 0 erros · 2.897 palavras.

### Validação final (25/08, pós-reorganização)
```
checker: ✅ Aprovado · 0 erros · 2.733 palavras · 7 afiliados rel=sponsored
balanço: div 87/87 · ul 7/7 · li 26/26 (o +1 de '<li' é o <link> do head)
resíduos: zero de 9,0/10 · 8.9/8.7/8.3 · 4,8/5 · ~1.200 · R$ 898/759/1.299 (mantido R$ 899
apenas como histórico do Prime Day)
```

### Pendências que seguem para o editor (BLOQUEIAM o fechamento)
| Item | Detalhe |
| --- | --- |
| ~~Recapturar Positivo Vision Tab 7~~ | **RESOLVIDO 25/08** — R$ 571,12 Pix · 4,7/5 · 1.196 opiniões; conflito 383 vs 499 eliminado |
| **URLs de ML dos 3 SKUs** | capturas do editor não trouxeram URL de anúncio ML (LEDGER alerta "sem URL" nas linhas novas) |
| **Upload de imagens no WP Media** | hero `tablet-infantil-dia-criancas-2026-hero-970x600.webp`, thumb `...-1376x768.webp`, 3 produtos `-420.webp` |
| **Agendamento** | datePublished/dateModified = 12/09/2026 (placeholder) |
| **Re-verificar em 10/09/2026** | véspera da Semana da Criança (nota em comentário HTML) |

### Lições desta sessão
- HTML quebrado (bloco engolido por atributo `href`) NÃO é pego pelo checker — validar
  balanço de div + ler o topo sempre.
- O `editor` grava `\n` literal em strings Python ao inserir com quebra no JSON; para
  `replace` com strings multilinha do HTML, usar âncoras que incluam contexto único
  (ex.: prefixo `</div></div>`) para evitar colisão count=2.
- Notas por produto podem coexistir com "Nota Geral" do guia (Régua v2.0) — mas números
  por produto devem ser ÚNICOS em todo o artigo (tabela/H2/veredito/cards/JSON-LD).
- Amazon "sem estoque" + link apontando para outro modelo = CTA removido + aviso âmbar
  (nunca deixar botão de produto errado no ar).

## Sessão 25/08/2026 — Parte 5: padronização visual completa do tablet-infantil

Pedido do editor: 7 pontos fora do padrão. Corrigido via `tools/patch_tablet_infantil_visual.py`:
1. **Índice** → padrão golden (`id="indice-conteudo"`, 2 colunas fixas em grid com 2 `<ul>`,
   setas ▸ roxas, media query; título sem dois-pontos). Antes: `columns: 2` CSS.
2. **O que dizem as avaliações** → agora **6 cards (1 por plataforma × 3 produtos)** com
   citações literais das capturas de 25/08 (ML azul `#3485DB`, Amazon laranja `#FF9900`):
   Kid Pad ML 4,4/5·129 + Amazon 2,9/5·24 (Priscila A., jun/2025); A9 ML 4,9/5·1.345 +
   Amazon **sem estoque** (card informativo, sem avaliação inventada); Vision ML 4,7/5·1.196
   + Amazon 4,1/5·38 (José Antonio V., ago/2026). Nomes semi-anonimizados + data + plataforma.
3. **Resposta rápida** → 3 blocos lado a lado FIXOS `repeat(3,1fr)` (cards brancos,
   borda superior colorida verde/azul/âmbar) — padrão Escolha Rápida do melhores-techs.
4. **Qual tablet para cada idade?** → mesmo padrão `repeat(3,1fr)` lado a lado.
5. **Régua** ('Como chegamos às notas' + 'Notas por critério') → substituídos pelo bloco
   de avaliação golden (`id="avaliacao-tablets-infantil"`): cabeçalho com 3 badges escuros
   (7.0 Multi / 8.5 Galaxy / 8.5 Vision) + grid 3×2 de critérios com números grandes +
   caixa 🧮 explicando a metodologia. **Eliminada a "Nota Geral 7,5" órfã** (4ª família de
   notas conflitantes que ainda restava).
6. **Botões Onde Comprar**: ML vermelho do tema (#9B2226) e azul Samsung (#1428A0)
   → **padrão oficial ML** (`linear-gradient(135deg,#2d3277,#1a1f5c)`, texto `#ffe600`);
   botões Amazon já laranja oficial (#ff9900→#ff8500) ganharam sombra padrão.
   Cores de referência: `alternativas-galaxy-tab-s10-fe-ipad-estudar-JA-COLADO.html`.

Validação: checker 0 erros (3.112 palavras); div 104/104, ul 8/8, li 30/30, p 38/38;
zero resíduos ('Nota Geral', 'columns: 2', gradientes antigos).

Lição: ao reconstruir blocos aninhados (outer > p + grid > cards), conferir se o fecho
tem um `</div>` para CADA nível aberto — o patch saiu com 1 div a menos e só o balanço pegou.

## Sessão 25/08/2026 — Parte 6: agendamento confirmado no WP

Editor agendou os dois guias no WordPress:
- `melhores-techs-custo-beneficio-2026` → **AGENDADO 27/08/2026 08:00**
- `tablet-infantil-dia-das-criancas-2026-3-melhores` → **AGENDADO 29/08/2026 08:00**

`fila-atualizacao.md` atualizada (techs PRONTO_PARA_REVISAO → AGENDADO; tablet-infantil
incluído na P1). Pendências que continuam abertas até a data de publicação:
1. Imagens: conferir upload no WP Media — tablet usa caminhos `/2026/09/*.webp`
   (hero 970x600, thumb, 3 produtos 420) — URL do HTML precisa bater com o arquivo real.
2. LEDGER: faltam URLs dos anúncios ML dos 3 SKUs do tablet (capturas não trouxeram links).
3. Re-verificação de preços do tablet em **10/09/2026** (véspera da Semana da Criança).
4. Commit do trabalho desta sessão ainda pendente de aprovação do editor.

## Sessão 25/08/2026 — Parte 7: correção editorial do Tab A9

Editor apontou: **o Galaxy Tab A9 não é um tablet infantil**. Corrigido via
`tools/patch_tablet_a9_convencional.py` + `_b.py` (+ 1 ajuste direto no hero):
o artigo agora deixa explícito em TODOS os pontos que o Tab A9 é um
**tablet convencional de entrada usado em modo Samsung Kids + capa avulsa**
(não modelo infantil de fábrica): hero, índice, intro, resposta rápida, H2 da seção,
tabela (coluna "Galaxy A9 (modo Kids)*" + legenda nova dos asteriscos TFT/capa),
card de idade 9–12, bullet "para quem NÃO vale", 2 FAQs, veredito, card de compra,
JSON-LD (itemListElement + acceptedAnswer). Resíduos zerados; checker 0 erros;
tags balanceadas; JSON-LD válido.

Lição de processo: script de patch em 2 partes NÃO pode re-ler o arquivo do disco
no meio (`s = open(F).read()`) — descarta as edições em memória da parte anterior.
E validações em paralelo podem medir o arquivo antes de o patch terminar:
validar sempre DEPOIS, em comando separado.

## Sessão 25/08/2026 — Parte 8: auditoria ao vivo das imagens (curl HTTP status)

Editor informou que todas as imagens estão no WP. Verificação ao vivo (curl):
- **tablet-infantil**: 4 imagens `/2026/08/` → 200 OK (hero, Kid, A9, Vision) ✓
- **tablet-infantil**: thumb `2026/09/tablet-...-thumb-1376x768.webp` → **404**
  (nem em /2026/08/ com variantes de nome) — pendente: subir OU colar URL real.
- **melhores-techs**: avatar do autor tinha TYPO — `cristian-curadoria-prime.jpg`
  → corrigido para `cristiano-curadoria-prime.jpg` (**200 OK** confirmado ao vivo).
- **melhores-techs**: ainda 404 (não encontradas variantes): 
  `hero-melhores-techs-custo-beneficio-2026.jpg` e
  `suporte-giratorio-notebook-ventoinha.jpg` — pendente: subir OU colar URLs reais.

Lição: "está no WP" precisa ser conferido por HTTP status do link exato do HTML —
nomes parecidos (cristian/cristiano) e pasta do mês do upload derrubam imagem no ar.

## Sessão 27/08/2026 — Parte 9: correção P0 (18 artigos) + aplicação no WordPress

- **Diagnóstico** (`audit/auditoria-48-artigos.csv`): 18 artigos de maior risco —
  16 com `aggregateRating`/`reviewCount`/`ratingCount` no JSON-LD (§2.4),
  2 com JSON-LD quebrado por wpautop (`<br />` dentro do `<script>`),
  1 com estrutura @graph corrompida (purificador), 2 com alegação de teste
  físico (§3) e 7 sem declaração de ausência de teste.
- **Correção local**: `tools/corrigir_p0_artigos.py` + `tools/adicionar_honestidade.py`
  → 18/18 com 0 erros no `checar_conformidade.py`. Commit `18bd18b`.
  Declaração canônica: "A Curadoria Prime **não testou esta unidade**
  fisicamente" (o checker casa com "não testou" — não usar "este aparelho").
- **Aplicação no WP** (`tools/aplicar_wp_p0.py`): pipeline-check (render público
  → pipeline → igualdade byte a byte com os locais), raw autenticado com
  backup (`articles/wp_raw_backups/`), espelho processado e validado
  (`articles/wp_raw_mirror/`), PUT por post com verificação + auditoria do
  render. **18/18 gravados e conferidos** (blocos de 3 posts, sleep 2s).
- **Lição 1 — raw ≠ render**: o WP guarda o raw com aspas retas e texturiza
  no render (`&#8220;`/`&#8221;`); literais de correção precisam das duas
  variantes. Dentro de `<script>` não há texturização (raw == render).
- **Lição 2 — wpautop engole comentários HTML no render** (`<!-- x -->` some):
  diff byte a byte contra o render gera falsa divergência; o gate de gravação
  são as checagens objetivas sobre o raw (`--validar`).
- **Lição 3 — pipeline-check antes de gravar**: aplicar o pipeline ao render
  público e exigir igualdade com os arquivos corrigidos provou cobertura 100%
  e pegou 5 divergências que o checker de 16 pontos não detectava (duplicata
  de declaração no hw-b400f, vírgula órfã do soundcore, aspas do band-10).
- **Pendências editoriais** (não bloqueiam): data de verificação (14),
  posição da divulgação de afiliado (11), bloco de contras (9), densidade de
  keyword (6), revisão visual das citações reescritas (ids 3310 e 4185).





## Sessão 30/08/2026 — Implementação do Cluster "Dia das Crianças 2026" e Guia de Agentes

### Objetivo
Produzir o conteúdo do cluster "Dia das Crianças 2026", iniciando pelo hub/pillar guide, garantindo conformidade total com o padrão visual Golden.

### O que foi feito

**1. Guia  (Clonagem do Padrão Golden)**
- Realizado rewrite estrutural profundo para espelhamento técnico do `modelo-lista-golden.html`.
- **Implementações Visuais:**
    - Hero block com gradientes específicos.
    - Metodologia com acentos em `#5a4fcf`.
    - Seção "Matemática da Curadoria" com pesos percentuais de avaliação.
    - **Sequência Modular de Produtos:** Imagem $\rightarrow$ Badges de Rank $\rightarrow$ Texto $\rightarrow$ Tabela Técnica (degradê roxo) $\rightarrow$ Prós (setas ▸) $\rightarrow$ Pontos de Atenção (borda vermelha grossa) $\rightarrow$ Veredito $\rightarrow$ Box de Compra centralizado.
    - Conclusão com Tabela de Resumo e box "⚡ Escolha rápida" (Grid `repeat(3, 1fr)` com fallback mobile).
    - Bloco de links do Cluster de Apoio e Rodapé Editorial.
    - Bloco do Autor com dimensões de foto `72x72`.
- **Técnico & SEO:**
    - Implementação de JSON-LD `@graph` complexo (Article, ItemList, FAQ, Breadcrumb).
    - Correção de links de afiliado para `rel="sponsored noopener noreferrer"`.

**2. Criação do arquivo `agent.md`**
- Estabelecimento de diretrizes mandatórias para agentes de IA.
- **Regras principais:**
    - Fidelidade absoluta ao modelo canônico (proibido improvisar layouts).
    - Padronização de cores (`#5a4fcf`, `#fde68a`) e componentes visuais.
    - Compliance editorial: mínimo de 1500 palavras, proibição de citações fictícias e obrigatoriedade de fontes reais.
    - Fluxo de validação: Comparação visual $\rightarrow$ `checar_conformidade.py` $\rightarrow$ Balanço de tags.

### Próximos Passos
- Iniciar a produção dos artigos "spoke" (apoio), começando por: "Tech Kids 2026: Melhores Tablets e Gadgets Educativos para Crianças".

## Sessão 30/08/2026 — Implementação do Cluster "Dia das Crianças 2026" e Guia de Agentes

### Objetivo
Produzir o conteúdo do cluster "Dia das Crianças 2026", iniciando pelo hub/pillar guide, garantindo conformidade total com o padrão visual Golden.

### O que foi feito

**1. Guia `guia-presentes-dia-das-criancas-2026.html` (Clonagem do Padrão Golden)**
- Realizado rewrite estrutural profundo para espelhamento técnico do `modelo-lista-golden.html`.
- **Implementações Visuais:**
    - Hero block com gradientes específicos.
    - Metodologia com acentos em `#5a4fcf`.
    - Seção "Matemática da Curadoria" com pesos percentuais de avaliação.
    - **Sequência Modular de Produtos:** Imagem $\rightarrow$ Badges de Rank $\rightarrow$ Texto $\rightarrow$ Tabela Técnica (degradê roxo) $\rightarrow$ Prós (setas ▸) $\rightarrow$ Pontos de Atenção (borda vermelha grossa) $\rightarrow$ Veredito $\rightarrow$ Box de Compra centralizado.
    - Conclusão com Tabela de Resumo e box "⚡ Escolha rápida" (Grid `repeat(3, 1fr)` com fallback mobile).
    - Bloco de links do Cluster de Apoio e Rodapé Editorial.
    - Bloco do Autor com dimensões de foto `72x72`.
- **Técnico & SEO:**
    - Implementação de JSON-LD `@graph` complexo (Article, ItemList, FAQ, Breadcrumb).
    - Correção de links de afiliado para `rel="sponsored noopener noreferrer"`.

**2. Criação do arquivo `agent.md`**
- Estabelecimento de diretrizes mandatórias para agentes de IA.
- **Regras principais:**
    - Fidelidade absoluta ao modelo canônico (proibido improvisar layouts).
    - Padronização de cores (`#5a4fcf`, `#fde68a`) e componentes visuais.
    - Compliance editorial: mínimo de 1500 palavras, proibição de citações fictícias e obrigatoriedade de fontes reais.
    - Fluxo de validação: Comparação visual $\rightarrow$ `checar_conformidade.py` $\rightarrow$ Balanço de tags.

### Próximos Passos
- Iniciar a produção dos artigos "spoke" (apoio), começando por: "Tech Kids 2026: Melhores Tablets e Gadgets Educativos para Crianças".
