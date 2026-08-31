# checar_conformidade.py — regex literais e armadilhas

Detalhe das checagens do checker do projeto (`tools/checar_conformidade.py`).
Descoberto ao validar `guia-presentes-dia-das-criancas-2026.html` (31/08/2026).

## Regex LITERAIS (o checker não faz lematização)

O checker usa `re.search(r"padrão", texto, re.I)` — casa **substring literal**,
não a palavra derivada. Exemplos reais que derrubaram:

| O texto tinha | O checker queria | Resultado |
| --- | --- | --- |
| "Tabela **comparativa** lado a lado" | `comparativo` | ❌ alerta valor-agregado |
| "Pontos de Atenção" (blocos de contras) | `contras` ou `pontos negativos` | ❌ alerta valor-agregado |
| "Para quem NÃO vale a pena **presentear** com tech" | `não vale a pena para` | ❌ não casou (faltava "para") |
| "Para quem NÃO é indicado" | `quem n[ãa]o é` | ✅ casa |

**Lição:** para satisfazer os sinais de valor-agregado, use as palavras exatas
do regex no texto visível:
- `comparativo` (não "comparativa")
- `contras` (ou renomeie o H3 "Pontos de Atenção" → "Contras e Pontos de Atenção")
- `não vale a pena para` / `quem não é` com a preposição que o padrão exige
- `perguntas frequentes` / `veredito` / `\d,\d/10`

## Sinais de valor agregado (regra `valor-agregado`)

```
comparativo|vs\.?\s
contras|pontos negativos
não é para|não vale a pena para|evite se|quem n[ãa]o é|pense duas vezes
perguntas frequentes|faq
veredito|nota final|\d[,.]\d\s*/\s*10
```

## DOMINIOS_AFILIADO (o que conta como link de afiliado)

```python
DOMINIOS_AFILIADO = ["link.amazon", "meli.la", "amzn.to", "mercadolivre.com", "amazon.com.br"]
```

⚠️ **"amazon.com.br" e "mercadolivre.com" contam como afiliado.** Um link de
fonte editorial para página de CATEGORIA dessas lojas (ex: homepage de busca)
dispara "sem rel=sponsored" se não tiver `rel="sponsored"`. A regra da casa diz
que fonte editorial NÃO leva sponsored — portanto, em vez de marcar sponsored,
**remover o link de categoria das Fontes consultadas** (deixar só o texto).

## O que o checker NÃO pega (validar manualmente)

- **Tag HTML quebrada** — ex: `</a>` escrito como `<///a>`, `</li>` como `</li>>`.
  Grep manual: `grep -n '<///a>\|</li>>' artigo.html`
- **Balanço de tags** — `div 68/68`, `ul 12/12`, etc. Script Python:
  ```python
  for tag in ["div","ul","li","p","a","h2","h3","table","tr","td","th","script","span","ol"]:
      a = len(re.findall(rf"<{tag}[\s>]>", html)); b = len(re.findall(rf"</{tag}>", html))
      assert a == b, f"{tag} {a}/{b}"
  ```
  ⚠️ **INCLUA `img` NA LISTA DE VOID ELEMENT SE HARDFORÇAR VERIFICAÇÃO — OU
  EXCLUA-OS.** `<img>`, `<br>`, `<hr>`, `<input>`, `<meta>` são elementos void:
  NÃO têm tag de fechamento. Um ad-hoc script que conta `<img ...>` como
  abertura e espera `</img>` (contagem 0) gera falso FAIL (`img 6/0`). Solução:
  não listar `img` no loop acima, ou, se listar, contar só abertura e ignorar
  o fecho (0 esperado). O HTML5 é válido sem `</img>`.
- **JSON-LD duplicado `] ]`** — editar via `index()`/`slice()` deixa um `]`
  a mais. Sempre rodar `json.loads()` depois de mexer no JSON-LD.
- **Emoji VS16** — emojis no HTML podem ter variation selector (U+FE0F) que
  quebra `str.replace`/`count` byte-a-byte em heredoc. Usar regex só com âncoras
  ASCII (ex: `re.search(r'<h2[^>]*>(\d+)\.\s', s)`).

## Gate de mercado que o checker não valida (decisão editorial)

- **Internacional + mais caro = FORA:** se a única opção num marketplace é
  importada (ex: REXQualis EUA a R$ 331,54) e o mesmo produto nacional no
  outro marketplace é mais barato (R$ 294,44 Amazon), o rótulo é FORA.
  Remover o botão e adicionar nota `"ficou de fora"` com justificativa.
- **Catálogo ML ≠ anúncio:** link `/p/MLB...` é catálogo multi-vendedor, não
  CTA seguro. Exigir link de anúncio de um vendedor identificado.

## Ad-hoc verification script pattern

Após editar o HTML (trocar links, preços, reestruturar), gerar evidência
verificável com script temporário antes de declarar a tarefa:

```bash
cat > /tmp/hermes-verify-<nome>.py << 'VERIFY'
import re, json, subprocess, sys
# ... checker + balanço + JSON-LD + confirmações especificas ...
VERIFY
python3 /tmp/hermes-verify-<name>.py && rm -f /tmp/hermes-verify-<nome>.py
```

Rodar, exibir saída, depois limpar. Isto não substitui a suite formal
(que não existe) — é evidência ad-hoc para o sistema e auditoria pessoal.

## Comando padrão de validação

```bash
python3 tools/checar_conformidade.py articles/html_output/artigo.html
# ✅ Aprovado = 0 erros, 0 alertas (exit 0)
# exit 1 = bloqueia publicação
```