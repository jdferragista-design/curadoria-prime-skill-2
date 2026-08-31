# SEO snippet (Rank Math / Yoast) — limites e consistência JSON-LD

Aplicável a **todo artigo** da Curadoria Prime. O editor revisa no painel
(WP · Rank Math/Yoast) e o snippet precisa caber nos limites — senão o título
quebra e o rank sofre.

## Limites do snippet (Rank Math / Yoast)

| Campo | Limite | O que acontece ao estourar |
| --- | --- | --- |
| **Título** | 60 chars · ~580px | corta com "…" antes da palavra-chave, luxo de 1ª linha |
| **Descrição** | 160 chars · ~920px | corta o final — perde o CTA / a menção de produto |
| **Slug (permalink)** | 75 chars | o slug longo é truncado |

Os contadores do painel mostram `N / limite` e um aviso de **px** (ex:
`61 / 60 (595px / 580px)`). Os px são o critério real (a largura da célula do
Google); usar os px como referência de corte, não só o char.

Correção real de caso (31/08/2026, guia Switch):
- Título `Melhores Jogos de Nintendo Switch em 2026: Console + 4 Opções para
  Presentear` = **61 chars, estourou** (595px/580px). Curto para
  `Melhores Jogos de Nintendo Switch em 2026: 5 Opções` = **51 chars** ✓.
- Descrição com `... para presentear: ...` + nomes completos = **173 chars,
  estourou** (160). Curto para `Melhores jogos de Nintendo Switch em 2026:
  Switch Lite, Mario Kart 8, Mario Wonder, Mario Party Superstars e uma opção
  retrô com ressalva.` = **138 chars** ✓, mantendo keyword + produtos.
- Mantém a keyword na frente e os nomes principais; abreviação aceita no corpo
  da descrição (Mario Kart 8, Mario Wonder) — não precisa do nome completo.

## Consistência: JSON-LD deve casar com o META SEO

O Rank Math lê o comentário META SEO (bloco `<!-- ... -->` no topo do HTML) e
o JSON-LD `@graph[0].headline`/`description` são lidos pelo Google. **Os três
precisam coincidir:**

- `Comment META SEO: Título` == `JSON-LD Article.headline`
- `Comment META SEO: Descrição` == `JSON-LD Article.description`

Ajustar SEMPRE em 2 lugares (comentário + JSON-LD), nunca só num — senão o
snippet do painel e o rich result do Google contam histórias diferentes.
Validação quick:
```python
re.search(r'Título: (.*)', html).group(1).strip() != json_obj["@graph"][0]["headline"]
```
Se divergir, corrigir.

## Como validar os limites (script ad-hoc)

Rodar um script temporário que lê o bloco META SEO, mede `len()` dos campos,
confere contra 60/160/75 e compara com o JSON-LD. Exibir PASS/FAIL e limpar.
Nunca deixar o título > 60 chars nem a descrição > 160 chars no arquivo final.
