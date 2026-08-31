# Schema JSON-LD + snippet (Rank Math/Yoast) — convenções verificadas

Regras de consistência entre o **comentário META SEO** (topo do HTML), o
**JSON-LD `@graph`** e o **snippet** do editor. Nenhuma é pega pelo
`checar_conformidade.py` — validar manualmente (ou via script ad-hoc).

## Datas do Article (REGRA RECORRENTE — cuidado)

`dateModified` NUNCA pode ser anterior a `datePublished`.

- Ao AGENDAR um artigo novo, `datePublished` = data/hora do agendamento
  (ex: `2026-09-04T08:00:00-03:00`).
- `dateModified` deve ser **igual ou posterior** a `datePublished`. Se o
  conteúdo está fechado e a data de verificação (captura de preço) é anterior
  ao agendamento, **use a data de agendamento nos DOIS** — a data de
  verificação continua no corpo ("verificado em 31/08") e no LEDGER, não
  precisa constar no schema.
- Defeito que já ressurgiu 2× (24/08 e 31/08): deixar `dateModified` = data de
  captura, anterior ao `datePublished` agendado. Página não tem "modificação"
  antes de publicar. **Sempre checar `dateModified >= datePublished`.**

## JSON-LD headline/description devem ESPELHAR o META SEO

O bloco `@graph > Article` precisa ter `headline` idêntico ao `Título:` do
comentário e `description` idêntico à `Descrição:` do comentário. Se um mudar
e o outro não, o schema descreve uma coisa e o snippet mostra outra. Após
editar a meta, conferir igualdade byte a byte (título e descrição).

## Limites do snippet (Rank Math / Yoast)

| Campo | Limite | Observação |
| --- | --- | --- |
| Título | ≤60 chars · ≤580px | keyword na frente; corta/trunca se passar |
| Descrição | ≤160 chars · ≤920px | keep keyword; não listar TODOS os produtos se estourar |
| Slug | ≤75 chars | geralmente ok; validar |

Pitfall real (sessão Switch 31/08): a descrição listando os 5 produtos por
extenso ("..., Super Mario Bros. Wonder, Mario Party Superstars e uma opção
retrô com ressalva.") passou de 160. **Abraviar nomes redundantes** (Mario
Wonder no lugar de Super Mario Bros. Wonder) e validar o char count do resultado.
Uma "melhoria" de descrição pode facilmente estourar o limite — conferir
SEMPRE o comprimento final, não apenas reescrever.

## Validação rápida (script ad-hoc, padrão da casa)

```python
import re, json, os
H = open(ART, encoding="utf-8").read()
tit  = re.search(r'Título: (.*)', H).group(1).strip()
desc = re.search(r'Descrição: (.*)', H).group(1).strip()
art  = json.loads(re.findall(r'<script type="application/ld\+json">(.*?)</script>', H, re.S)[0])["@graph"][0]
assert len(tit) <= 60,   "titulo estoura 60"
assert len(desc) <= 160, "descricao estoura 160"
assert art["headline"] == tit and art["description"] == desc, "JSON-LD != META SEO"
assert art["dateModified"] >= art["datePublished"], "dateModified antes de datePublished"
```

## Criar/agendar NOVO artigo — checklist do schema

- [ ] `datePublished` = data/hora do agendamento (fuso -03:00)
- [ ] `dateModified` >= `datePublished` (se fechado, igualar à publicação)
- [ ] `headline` == `Título:` do META SEO
- [ ] `description` == `Descrição:` do META SEO
- [ ] título ≤60 chars · descrição ≤160 chars · slug ≤75 chars
- [ ] `mainEntityOfPage` aponta para o canonical/slug correto
- [ ] `image` (Article) é um link vivo (200) — usar hero ou foto do produto-âncora
