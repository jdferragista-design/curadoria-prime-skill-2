# `tools/` — as regras editoriais como código executável

As skills em `skills/` ensinam um modelo a escrever certo. Esta pasta **verifica
mecanicamente** que ele escreveu certo, e bloqueia a publicação quando não escreveu.

A diferença importa: uma regra em markdown depende de o modelo tê-la lido e
obedecido naquele momento. Uma regra em código roda sempre, do mesmo jeito, e
retorna exit 1. Das duas, só a segunda impede um erro de chegar ao ar às 2h da manhã.

**Fonte canônica das regras: [`../skills/curadoria-review/references/regras-editoriais.md`](../skills/curadoria-review/references/regras-editoriais.md).**
(O arquivo homônimo na raiz é apenas um ponteiro — não edite lá.)
Os scripts implementam aquele documento. Quando os dois divergirem, o documento
está certo e o script tem um bug.

---

## Os cinco scripts

| Script | O que faz | Quando roda |
|---|---|---|
| `gerar_artigo.py` | JSON do produto → HTML no padrão do site | ao produzir |
| `checar_conformidade.py` | **trava** — 16 checagens, exit 1 se reprovar | antes de publicar |
| `ledger.py` | registra e consulta capturas reais de preço | ao pesquisar mercado |
| `corrigir_artigos.py` | remediação em lote dos artigos já no ar | mutirão de correção |
| `publicar_wp.py` | envia como rascunho via WP REST API | ao publicar |
| `openrouter.py` | acesso a LLMs via OpenRouter (chat, modelos) | pesquisa/escrita assistida |

Todos são Python 3 puro, sem dependência externa. Rodam com `python3 <script> --help`.

---

## Fluxo completo

```
pesquisa de mercado
    └─ ledger.py add        ← registra o preço que você VIU, com data
    └─ ledger.py frase      ← diz o que esse histórico autoriza afirmar
              ↓
       produto.json
              ↓
    gerar_artigo.py         ← monta o HTML
              ↓
    checar_conformidade.py  ← TRAVA. exit 1 = não publica.
              ↓
    publicar_wp.py          ← rascunho no WordPress (nunca publica direto)
```

O `publicar_wp.py` chama a trava sozinho e aborta se ela reprovar. Existe
`--forcar` para override, mas se você está usando, pare e pergunte por quê.

---

## `gerar_artigo.py`

```bash
python3 gerar_artigo.py exemplo-produto.json -o artigo.html
python3 gerar_artigo.py exemplo-produto.json -o artigo.html --schema
```

Replica a estrutura de 17 seções dos artigos do site: transparência → CTA →
prós/contras → specs → seções de análise → comparativo → para quem é → FAQ →
veredito → CTA final → fontes.

**O `--schema` é opt-in por decisão editorial (§7.3).** Sem a flag, nenhum JSON-LD
é emitido. Com ela, o script **exige** a chave `editor` no JSON e falha com exit 1
se faltar — porque §2.6 diz que a assinatura é do humano que revisou e aprovou,
não da organização. O `author` sai como `Person`, nunca `Organization`.

O schema nunca emite `aggregateRating`, `ratingCount` ou `reviewCount` (§2.4):
publicar nota agregada de terceiros como se fosse nossa é declarar uma avaliação
que não fizemos.

`exemplo-produto.json` documenta o contrato de entrada completo.

## `checar_conformidade.py`

```bash
python3 checar_conformidade.py artigo.html
python3 checar_conformidade.py 'articles/*.html' --resumo
python3 checar_conformidade.py artigo.html --json produto.json
```

Exit 1 se houver qualquer ERRO. É isto que você pluga num pre-commit ou num CI.

Checa, entre outras coisas: alegação de teste físico que não fizemos (§2.2),
`rel="sponsored"` em todo link de afiliado, divulgação de afiliado presente
(CDC/CONAR), autoria, fontes, data, densidade de palavra-chave, `aggregateRating`
externo (§2.4), `author` que não seja `Person` (§2.6), placeholders esquecidos.

Sabe distinguir uma alegação real de uma negação — "não testamos fisicamente"
não dispara o alarme que "testamos a fundo" dispara.

**Validado contra corpus externo:** rodado sobre os 4 artigos de `../articles/`,
escritos por outra ferramenta seguindo as mesmas regras. Três passaram com zero
erros. Duas implementações independentes das mesmas políticas concordando é a
melhor evidência disponível de que ambas leram o documento certo.

## `ledger.py`

```bash
python3 ledger.py add --data 2026-08-13 --sku galaxy-tab-s10-fe \
    --codigo SM-X520 --variante wifi-128 --loja amazon --tipo anuncio \
    --pix 2789 --url "https://link.amazon/B0..." \
    --artigo /tablets-para-volta-as-aulas-2026/

python3 ledger.py frase --sku galaxy-tab-s10-fe --variante wifi-128
python3 ledger.py validar
python3 ledger.py ver --sku galaxy-tab-s10-fe
```

Opera sobre `../skills/curadoria-mercado/assets/historico-precos/LEDGER.csv`.

Esse CSV é o ativo proprietário mais valioso do projeto: é a única coisa no site
que nenhum concorrente pode copiar da página do fabricante. Um histórico de preço
observado com data é experiência de primeira mão — exatamente o que o Google diz
faltar nos sites de afiliado que ele penaliza.

O `frase` é o subcomando que mais protege. Ele lê quantas capturas você tem e
responde o que você pode escrever:

- **1 captura** → só `"em 13/08/2026, R$ 2.789 na Amazon"`
- **2 capturas** → pode dizer `"subiu"` / `"caiu"`
- **3+** → pode dizer `"faixa observada pela Curadoria entre X e Y"`

E avisa quando a captura mais recente passou de 30 dias — preço velho não sustenta
bloco de compra.

Recusa: data no futuro, captura sem preço, duplicata exata, e URL de catálogo
`/p/MLB…` marcada como anúncio de vendedor (o preço do catálogo troca de dono sem
aviso — ver `../skills/curadoria-mercado/references/armadilhas-marketplace.md`).
Recaptura no mesmo dia é permitida com `--recaptura`, quando o preço mudou de fato.

## `corrigir_artigos.py` (v2)

```bash
export WP_USER="..." WP_APP_PASSWORD="xxxx xxxx xxxx xxxx"   # exigido até no dry-run

python3 corrigir_artigos.py --dry-run --id 2943   # confira: "fonte: content.raw"
python3 corrigir_artigos.py --aplicar --id 2943   # um artigo; confira no navegador
python3 corrigir_artigos.py --dry-run             # lote completo: 15 artigos
python3 corrigir_artigos.py --relatorio-alegacoes
```

Conserta sozinho só o que é mecânico e reversível: `rel="sponsored"` ausente e
bloco de divulgação ausente.

**Não** reescreve alegação falsa de teste. Isso muda o significado do texto e
exige um humano. O script lista os trechos e para.

### Por que a credencial é obrigatória mesmo no `--dry-run`

Sem autenticação a API devolve apenas `content.rendered` — o HTML **já processado
pelo `wpautop`**. A v1 lia isso e gravava de volta em `content`, fazendo o
WordPress reprocessar HTML já processado:

| post | `<br>` antes | depois |
|------|-------------:|-------:|
| 2943 | 10 | 365 |
| 3226 | 35 | 526 |
| 3183 |  2 | 268 |

Grids e flex quebram, e sem `context=edit` o fonte original não é recuperável.
A v2 lê o `raw` autenticado e **recusa** gravar se não tiver.

### Rede de segurança

1. **Backup** do raw em `backups/` antes de cada POST (ignorado pelo git).
2. **Verificação pós-gravação**: relê o post e compara `<br>`.
3. **Restauração automática** e interrupção do lote se detectar reprocessamento.

Não contorne com `--sem-verificacao`. `--tls-inseguro` existe para depurar rede e
é recusado junto com `--aplicar` — enviar senha de aplicação por canal não
verificado não é uma opção.

### Se der erro de TLS

```bash
curl -sS -o /dev/null -w '%{http_code}\n' https://curadoriaprime.com/wp-json/wp/v2/posts/2943
```

Se responder `200`, a API está no ar e o problema é a rede/proxy do ambiente onde
o script roda — não altere o script por causa disso. A v2 já tenta 3 vezes com
backoff antes de desistir.

## `publicar_wp.py`

```bash
export WP_USER="seu_usuario"
export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"
python3 publicar_wp.py artigo.html --titulo "..." --slug "..."
```

App Password: WordPress → Usuários → Perfil → "Senhas de aplicativo" → `agente-conteudo`.

Publica sempre como **rascunho**. Nunca como post público — a revisão humana é a
última linha e não deve ser automatizável.

## `openrouter.py`

```bash
export OPENROUTER_API_KEY="sk-or-..."
python3 openrouter.py chat --model openai/gpt-4o-mini \
  --prompt "Qual a capital do Brasil?"
python3 openrouter.py chat --model anthropic/claude-3-5-sonnet-20241022 \
  --prompt "Explique brevemente o que são headers HTTP"
python3 openrouter.py chat --prompt "..." --system "Responda como um especialista em tecnologia"
python3 openrouter.py modelos --limit 20
```

API key via `export OPENROUTER_API_KEY=...` (ou `--key` no CLI). Integração com a
API do OpenRouter (https://openrouter.ai) — gateway unificado de LLMs via endpoint
compatível com a OpenAI. Modelos suportados: GPT-4o, GPT-4o-mini, Claude 3.5, etc.

Útil para: pesquisa auxiliar (extrair dados de páginas oficiais), reescrever
textos, corrigir gramática, gerar prompts de imagem (via Vision models), ou
qualquer tarefa criativa apoiada pela curadoria.

Como módulo Python:
```python
from openrouter import chat_simples

texto = chat_simples(
  "Resuma em 3 linhas: Bluetooth 5.3 vs 5.2",
  model="openai/gpt-4o-mini",
  system_prompt="Você é um redator técnico do Curadoria Prime.",
  temperature=0.3,
  max_tokens=500,
)
```

Modelos qualificados/preferidos (em `MODELOS_PADRAO`):
- `gpt-4o-mini` — rápido e barato, bom para tarefas simples
- `gpt-4o` — equilibra velocidade, capacidade e custo
- `claude-3-5-sonnet` — análise profunda, reescrita editorial

---

## Rodar tudo de uma vez

```bash
python3 tools/ledger.py validar && \
python3 tools/checar_conformidade.py 'articles/*.html' --resumo
```

Bom candidato a pre-commit hook ou GitHub Action.

---

## O que estes scripts NÃO fazem

Não substituem a revisão humana e não deveriam. Eles pegam violação mecânica:
uma tag faltando, uma palavra proibida, um número sem fonte.

Não sabem dizer se a análise está *certa* — se a recomendação faz sentido, se o
comparativo é honesto, se o produto realmente serve para quem o texto diz que
serve. Isso continua sendo trabalho de gente, e é justamente o que §2.6 protege
ao exigir que a assinatura seja de uma pessoa.
