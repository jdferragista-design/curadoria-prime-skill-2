# MEMÓRIA — curadoria-prime-skill-2

Registro operacional das sessões de trabalho. Objetivo: qualquer sessão futura
retomar exatamente daqui sem re-diagnóstico.

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
