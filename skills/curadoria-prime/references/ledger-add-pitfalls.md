# ledger.py add — armadilhas de linha de comando (sessão 31/08/2026)

## Tipos de item que NÃO têm código de fabricante

`ledger.py` exige `--codigo` com valor (argparse). Para **jogos** (mídia física,
sem SKU de fabricante — ex: Mario Kart 8, Mario Wonder, Mario Party) e para
**produtos de marca genérica** (ex: Retro Game Stick), NÃO existe código.

- NUNCA passar `--codigo` vazio como token solto:
  `--codigo --variante midia-fisica` → **error: argument --codigo: expected one
  argument** (o argparse engole o próximo flag como valor).
- Passar string vazia explícita: `--codigo ""`.

Uso correto:
```bash
python3 tools/ledger.py add --data 2026-08-31 --sku mario-kart-8-deluxe \
  --codigo "" --variante midia-fisica --loja amazon --tipo anuncio \
  --pix 324.57 --url "https://link.amazon/B028hyTBk" \
  --artigo "/melhores-jogos-nintendo-switch-2026/" --obs "4,9/5 1081 aval"
```

Convenção de `variante` para jogos: `midia-fisica` (todas as franquias usam a
mesma variante, então a chave dedup data+sku+loja+variante continua única por
loja).

## "desconto de fachada" (alerta em `add` e `validar`)

Quando `--de` (preço riscado) mal supera o `--pix` (de < pix*1.05), o ledger
avisa e o `validar` marca alerta. **Regra da casa:** NÃO destacar esse "de" no
card do artigo. Exemplo real: ML Mario Kart 8 `--de 319 --pix 309` → `de` só 3%
maior. No card, escrever apenas o preço real ("R$ 309 no Pix") e remover o
"(de R$ 319, 3% off)".

## `ledger.py validar` pode reportar erros que NÃO são seus

O `validar` varre o arquivo INTEIRO. Erros pré-existentes de outras sessões
aparecem junto com os seus (ex: `apple-tv-4k-3gen` com `--tipo sem-estoque` — tipo
inválido — e `lenovo-idea-tab` sem coluna de preço, ambos capturas de 29/08).
Antes de "consertar", conferir a data/linha: só corrigir os erros das suas
capturas do dia; erros antigos são de outro artigo e não bloqueiam o seu.
(Os erros do `validar` são apenas sobre integridade do CSV; o gate de publicação
é o `checar_conformidade.py` no HTML.)

## Fluxo que funcionou (31/08)

1. Registrar 1 linha por SKU × loja (`amazon`, depois `ml`), sempre com `--data`,
   `--pix`, `--url` e `--artigo`.
2. `validar` ao final — esperar os alertas de "desconto de fachada" e os erros
   pré-existentes; auditar só os seus.
3. Depois de cada `add` de uma mesma loja, o `frase` mostra quantas capturas
   sustentam afirmação — 2 pontos (Amazon + ML) já permitem "subiu/caiu".
