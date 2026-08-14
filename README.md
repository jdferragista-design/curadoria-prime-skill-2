# Ai-skill — Curadoria Prime

Skill editorial para o [curadoriaprime.com](https://curadoriaprime.com), alinhada às [regras editoriais](skills/curadoria-review/references/regras-editoriais.md) (v1.0, 12/08/2026 — **fonte canônica**; o arquivo homônimo na raiz é só um ponteiro).

## Avaliação rápida do site

O posicionamento é o ativo: curadoria independente, sem bancada em todo produto, renda de afiliado declarada. O review da Apple TV 4K e o guia de Dia dos Pais acertam preço datado, alerta de versão e veredito por perfil. O catálogo ainda escorrega para vitrine (“testamos a fundo”, superlativo, prova social de loja no topo).

As regras de IA são **mais rígidas** do que alguns textos já no ar. A skill segue as regras, não o deslize.

## A skill: `curadoria-review`

Implementa o documento editorial: 20 regras absolutas, briefing antes de redigir, diagnóstico antes de atualizar, checklist de bloqueio, schema só a pedido.

```
skills/curadoria-review/
├── SKILL.md
├── references/
│   ├── regras-editoriais.md      # FONTE CANÔNICA v1.0 (§1–§17)
│   ├── metodologia.md
│   ├── analise-visual-apple-tv.md
│   └── voz-e-regras.md
└── assets/
    ├── template-review.md
    ├── template-guia.md
    ├── checklist-bloqueio.md     # espelho parcial da §15
    └── modelos/                  # HTML de referência (Gutenberg)
```

### Onde editar as regras

Só em `skills/curadoria-review/references/regras-editoriais.md`. Até 13/08/2026
havia duas cópias byte a byte idênticas de 728 linhas; a da raiz virou ponteiro.
Ao mexer na §15, confira também `assets/checklist-bloqueio.md`, que a resume.

O que a primeira versão da skill fazia e as regras vetam — e foi corrigido:

| Antes | Regra |
| --- | --- |
| Assinava Cristiano Martins | §2.6 — assinatura só do humano que aprovou |
| “compradores verificados” como padrão | §4.2 — só com selo explícito da plataforma |
| Nota 0–10 quase obrigatória | §7.1 — nota é opcional e criteriosa |
| Prova social Amazon/ML no hero | §2.4 / §4 — dado de terceiro, com data, sem schema agregado |
| `[VERIFICAR]` no texto final | §2.3 — `[VERIFICAÇÃO HUMANA NECESSÁRIA]` só no rascunho |
| Sem menção a AggregateRating | §2.4 — proibido copiar nota de loja para dados estruturados |
| Sem `rel="sponsored nofollow"` | §8 |
| Título com ano por padrão | §9.2 / §9.4 — ano não é verniz de atualização |

## Como usar

```bash
cp -R skills/curadoria-review ~/.claude/skills/curadoria-review
# ou
mkdir -p .claude/skills
cp -R skills/curadoria-review .claude/skills/curadoria-review
```

Peça review, guia, atualização ou auditoria. Sem fonte, a skill omite, declara incerteza ou marca conferência humana — não inventa. Não declare o texto pronto para o ar enquanto o checklist tiver “não”.

## Atualizar o site (Google + layout Apple TV 4K)

Não reescrever o catálogo de uma vez: o Google trata volume sem valor original como [scaled content abuse](https://developers.google.com/search/docs/essentials/spam-policies#scaled-content).

O padrão visual é a [Apple TV 4K](https://curadoriaprime.com/apple-tv-4k/) (`references/layout-apple-tv.md`). O texto segue as regras da casa **e** o Google (`references/google-search.md`): people-first, Who/How/Why, sem `AggregateRating` de loja, `rel="sponsored nofollow"`, evidência de trabalho (preço datado, ficha oficial, rivais) — sem fingir bancada.

Fila P0→P3: `skills/curadoria-review/assets/fila-atualizacao.md`.
Cadência de revisão, estados de frescor e gatilhos: **§17** das regras.

Comece pelos dois guias de tablet (canibalização) e pela própria Apple TV 4K (tirar “testamos a fundo”). Uma URL por pedido, com fontes do dia.

## Remediação dos artigos publicados

`tools/corrigir_artigos.py` **v2** corrige o que é mecânico nos artigos no ar:
`rel="sponsored"` ausente e bloco de divulgação faltando. Alegação de teste
físico ele apenas lista — reescrita é humana (§2.2).

```bash
export WP_USER="..."
export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"   # senha de APLICAÇÃO, com espaços

python3 tools/corrigir_artigos.py --dry-run --id 2943   # confira: "fonte: content.raw"
python3 tools/corrigir_artigos.py --aplicar --id 2943   # um artigo, confira no navegador
python3 tools/corrigir_artigos.py --dry-run             # lote: 15 artigos
```

> **A v1 deste script corrompia o layout.** Lia `content.rendered` e gravava de
> volta em `content`, fazendo o WordPress rodar `wpautop` sobre HTML já
> processado: +355 `<br />` no post 2943, +491 no 3226, +266 no 3183. A v2 lê o
> fonte com `context=edit`, faz backup antes de gravar, relê o post depois e
> restaura sozinha se detectar reprocessamento. Ela **recusa** gravar sem
> credencial válida — por isso o `--dry-run` também exige as variáveis.
