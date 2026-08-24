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

## Pendências abertas

| Item | Prazo/condição |
| --- | --- |
| Re-verificar preços/estoque do tablet-infantil antes de publicar | 10/09/2026 (nota em comentário HTML no arquivo) |
| Agendar/publicar `guia-volta-as-aulas-tech-2026-7-itens.html` | aguardando decisão do editor |
| Agendar/publicar `tablet-infantil-dia-das-criancas-2026-3-melhores.html` | após re-verificação de 10/09 |
| Confirmar colagem dos `-JA-COLADO` em `articles/correcoes/` (rodada 20-23/08) | já confirmado por diff — ver RELATORIO-CORRECOES |
| Git: working tree com mudanças não commitadas (artigos antigos apagados, skills assets, auditoria, html_output novo) | commit quando o editor pedir |

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
