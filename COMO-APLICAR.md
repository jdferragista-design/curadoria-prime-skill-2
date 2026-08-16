# Como aplicar — patch de padrões editoriais

Instruções para o agente do outro chat. **Não é preciso ler nenhuma análise anterior.**
Tudo aqui roda offline: sem WordPress, sem credencial, sem rede, sem dependência externa.

---

## Contexto em 5 linhas

O repo `curadoria-prime-skill-2` tinha **duas listas divergentes** de padrões de teste físico:
uma em `tools/checar_conformidade.py` (o gate que bloqueia) e outra em `tools/corrigir_artigos.py`.
A do gate era a mais fraca. **6 das 7 frases vetadas pela regra 1 do `SKILL.md` passavam sem erro.**

É o mesmo problema que as regras em markdown já tiveram (duas cópias de 728 linhas, resolvido com
um ponteiro) — agora em Python. A solução é a mesma: uma fonte única, importada pelos dois.

---

## O que este patch faz

| Arquivo | Ação |
|---|---|
| `tools/padroes_editoriais.py` | **novo** — fonte única dos padrões |
| `tools/tests/test_padroes_editoriais.py` | **novo** — 10 testes de regressão |
| `tools/checar_conformidade.py` | 2 linhas trocadas por um import |
| `tools/corrigir_artigos.py` | 2 linhas trocadas por um import + 2 correções de regra |

Resultado medido: **regra 1 sai de 1/7 para 7/7 detecções, com 0 falsos positivos.**

Nenhuma regra editorial é alterada. `regras-editoriais.md` não é tocado.
O patch só faz o código passar a cumprir o que o documento já dizia.

---

## Passo 1 — copiar os dois arquivos novos

```bash
cd /caminho/do/curadoria-prime-skill-2
mkdir -p tools/tests
# copie para cá:
#   tools/padroes_editoriais.py
#   tools/tests/test_padroes_editoriais.py
```

## Passo 2 — `checar_conformidade.py`

Localize as duas listas e **substitua pelo import**:

```python
# REMOVER: PADROES_TESTE_FISICO = [ ... 16 itens ... ]
# REMOVER: PADROES_ENCHIMENTO   = [ ... 14 itens ... ]

# ADICIONAR, logo após os imports do topo:
from padroes_editoriais import (
    PADROES_TESTE_FISICO,
    PADROES_ENCHIMENTO,
    PADROES_PROVA_SOCIAL_INDEVIDA,
)
```

Nada mais muda: os nomes das constantes são idênticos, o resto do arquivo segue funcionando.

## Passo 3 — `corrigir_artigos.py`

**3a. Substituir as listas locais:**

```python
# REMOVER: PADROES_TESTE = [ ... ]
# REMOVER: PADROES_TESTE_SCHEMA = PADROES_TESTE + [ ... ]

# ADICIONAR:
from padroes_editoriais import PADROES_TESTE_FISICO
PADROES_TESTE = PADROES_TESTE_FISICO
PADROES_TESTE_SCHEMA = PADROES_TESTE_FISICO
```

**3b. Corrigir a violação da §16** (linha ~89):

```python
# ANTES — o script carimba um nome fixo no author.name do schema:
AUTOR_CANONICO = "Cristiano Martins"

# DEPOIS — §16: a assinatura é do humano que conferir e aprovar.
# O script não decide autoria. Sem valor definido, não mexe no campo.
AUTOR_CANONICO = os.environ.get("CP_AUTOR_APROVADOR") or None
```

E onde o valor é usado (linhas ~349-350, ~578), envolva com a guarda:

```python
if AUTOR_CANONICO and obj.get("name") != AUTOR_CANONICO:
    obj["name"] = AUTOR_CANONICO
```

> Sem `CP_AUTOR_APROVADOR` no ambiente, o script deixa `author.name` como está.
> Isso é o comportamento correto: quem aprova assina, no momento da aprovação.

**3c. Corrigir a violação da §6** (linha ~103, dentro de `BLOCO_DIVULGACAO`):

```python
# ANTES — viola §6 ("compradores verificados" sem selo da plataforma):
'pesquisa técnica e dados de compradores verificados. '

# DEPOIS:
'pesquisa técnica e relatos publicados por compradores. '
```

E na tabela de substituições (linha ~432), que hoje corrige uma violação criando outra:

```python
# ANTES:
"testamos": "analisamos as especificações e cruzamos com relatos de compradores verificados",
# DEPOIS:
"testamos": "analisamos as especificações e cruzamos com relatos publicados por compradores",
```

## Passo 4 — rodar os testes

```bash
cd tools && python3 -m unittest discover tests -v
```

**Esperado: 10 testes, todos passando.**

Se `test_autor_canonico_nao_e_pessoa` ou `test_bloco_divulgacao_do_projeto_esta_limpo` falharem,
o passo 3b/3c não foi aplicado. Essas duas falhas são intencionais no estado atual do repo —
elas existem para travar exatamente esses dois bugs.

## Passo 5 — verificar que nada quebrou

```bash
python3 gerar_artigo.py exemplo-produto.json -o /tmp/a.html
python3 checar_conformidade.py /tmp/a.html --json exemplo-produto.json; echo "exit=$?"
```

Deve continuar retornando `exit=1` pelos placeholders `SEU-CODIGO-AQUI` — mesmo comportamento de antes.

---

## O que mudou no comportamento

**Passa a ser pego (era falso-negativo):**
`na nossa bancada` · `colocamos à prova` · `testado por nós` · `após N dias de uso` ·
`comprovamos` · `em nosso teste` (singular) · `no nosso laboratório` · `nossa unidade` ·
`desempacotamos` · `seguramos` · `sentimos na mão`

**Continua passando (correto):**
- A ressalva `"a Curadoria Prime não testou esta unidade fisicamente"` — a lógica de negação já existente cuida disso
- Teste de **terceiro** com atribuição (`"a Rtings testou e mediu 1.400 nits"`) — §3.4 permite
- Depoimento de comprador entre aspas — a lógica de citação já existente cuida disso

> `\btestou\b` foi deliberadamente **deixado de fora**: pegaria teste de terceiro, que é permitido.
> A alegação indevida é sempre em 1ª pessoa, e essa está coberta.

**Novo, em nível ALERTA (nunca bloqueia):**
21 padrões de vocabulário genérico de IA em PT-BR — `robusto`, `ecossistema`, `de ponta`,
`divisor de águas`, `potencializar`, `em termos de`, `abrangente`, `inovador`, `transformador`…
Adaptados do `ai-writing-detox` (jamditis/claude-skills-journalism, CC BY 4.0).
Estilo é ALERTA por decisão de projeto: só veracidade e transparência bloqueiam (§15).

---

## Commit sugerido

```
fix(tools): fonte única de padrões editoriais + correção de §6 e §16

checar_conformidade.py e corrigir_artigos.py mantinham listas divergentes
de padrões de teste físico. A do gate — o script que bloqueia — era a mais
fraca: 6 das 7 frases vetadas pela regra 1 do SKILL.md passavam sem erro.

Unifica em tools/padroes_editoriais.py, importado pelos dois. Regra 1 sai
de 1/7 para 7/7 detecções, com 0 falsos positivos (10 testes cobrem os
dois lados: pega o que a regra veta, não pega a ressalva correta nem
teste de terceiro atribuído, que §3.4 permite).

Corrige duas violações que o próprio código introduziria ao rodar:
- AUTOR_CANONICO carimbava "Cristiano Martins" no author.name (§16 exige
  que a assinatura seja do humano que aprovou, definida na aprovação)
- BLOCO_DIVULGACAO dizia "compradores verificados" (§6 exige selo
  explícito da plataforma); seria injetado nos 10 artigos sem divulgação

Acrescenta 21 padrões PT-BR de vocabulário genérico de IA, em nível
ALERTA. Adaptado de ai-writing-detox (CC BY 4.0).
```
