# Seleção de produto — guia de games (sessão 31/08/2026)

## Contexto
Pivot do hub `guia-presentes-dia-das-criancas-2026` de "presentes tech"/8-12
para **guia de games** com faixa ampliada a "até 14/15 anos" e teto de preço
R$ 1.500 (definido pelo editor como alto para a faixa).

## Lição central: não inflar com acessórios
O editor rejeitou a proposta de preencher a faixa com headset/controle:
> "esses acessórios não fazem sentido para esses games."

Motivo: Switch Lite já vem com 2 joy-cons embutidos; Retro Game Stick já vem
com 2 controles. Headset gamer e controle sem fio são ruído para esses alvos —
não agregam ao produto que se está recomendando. Acessório só entra quando
acrescenta (ex: um 2º controle para um console que aceita multiplayer local,
mas NÃO se o console já inclui).

## O vão de preço R$ 500–1.200 é real (não preencher com lixo)
Fato verificado por busca ao vivo: no Brasil não há **console de marca** entre
~R$ 450 (acessórios premium) e R$ 1.366 (Switch Lite nacional). Tudo que cai em
R$ 500–1.200 é console retrô portátil **genérico importado** com rating baixo:
- R36S (DELURA): 3,9★ · 483 aval · R$ 209–215
- Anbernic RG35XX H / Miyoo Mini Flip: 3,4–3,7★ · R$ 602–695 · marcados "14-15+"
- Super Retro / VARENZIA / Oásis OIH-5911: 3,0–3,8★ · 3–30 aval · R$ 161–367
- Game Stick Retrô "20.000 jogos": 3,4★ · 97 aval · R$ 124

Regra: rating < 4,0 + marca genérica + "N jogos" inflado = NÃO indicar como
recomendação central. O vão fica declarado em vez de ser tapado.

## Seleção aprovada (produtos verificados ao vivo 31/08/2026)

### Console (melhor presente de games)
- Nintendo Switch Lite Turquesa (nacional): R$ 1.366,67 de 1.899 · 4,8★ · 1.855
  aval · 7% off Pix · 12x R$ 123,79 (total 1.485,48) · Amazon=B06MejMa2, ML=2mReGbQ

### 3 jogos físicos de franquia mainstream (todos 4,7★+)
| Jogo | Preço | Rating | ASIN |
|---|---|---|---|
| Mario Kart 8 Deluxe | R$ 324,57 | 4,9★ · 1.081 | B0BK2RYTYH |
| Super Mario Bros. Wonder | R$ 339,89 | 4,8★ · 10.918 | B0C8VHZR14 |
| Mario Party Superstars | R$ 329,97 | 4,7★ · 15.517 | B097B2HQ5R |

Notas:
- **Título oficial da Nintendo** (o "Nintendo, Jogo, Super Mario Bros. Wonder"
  de 4,9★ · 1.487 aval · R$ 274,55, ASIN acabando em B0CF3JFY5T/B0C8VHZR14)
  convive com o "Compatível com" da GAMER HUT. Preferir o oficial/produto
  primário.
- Jogos que **não estavam disponíveis** e foram trocados: Mario Party
  Jamboree (0 resultados), Mario Odyssey físico (não existe na Amazon BR —
  só guia Prima de R$ 649 e Captain Toad). Zelda Tears of the Kingdom estava
  R$ 551 (versão Switch 2) — fora do teto.

### Custo-benefício (declinado honestamente)
- Retro Game Stick Lite 4K 64GB + 2 controles: R$ 132,90 · 3,8★ · 82 aval ·
  vendido por Tikva Store · ASIN B0GH8Q3X47. Proposta ótima (plug-and-play na
  TV) mas rating baixo → deve vir com ressalva explícita no texto, não como
  recomendação limpa.

## Estrutura final do guia de games
Console principal (Switch Lite) + 3 jogos físicos + 1 opção custo-benefício com
ressalva = R$ 132 (retro) → R$ 324–339 (jogos) → R$ 1.366 (console).

## Técnica de extração de ASIN via browser_console (Amazon)
```js
// Todos os ASIN da página de busca
Array.from(document.querySelectorAll('a[href*="/dp/"]'))
  .map(a => a.href.split('?')[0])
  .filter((v,i,arr) => arr.indexOf(v) === i)
```
Para filtrar por card + preço/rating em paralelo, percorrer
`document.querySelectorAll('div[data-component-type="s-search-result"]')`,
ler `card.querySelector('h2')` e `card.querySelector('.a-price .a-offscreen')`.

**Armadilha:** regex filter com `?` ou `:` dentro de literal causa
`SyntaxError: Unexpected token ':'`. Usar ternário limpo ou expressão sem
ponto-e-vírgula ambíguo. Recarregar a página antes de re-extrair (o resultado
de busca pode estar desatualizado/estático).

## LIÇÃO CRÍTICA: short link do editor prevalece sobre ASIN da busca

Ao criar um review individual (ex: Switch Lite), a busca ao vivo pode retornar
um ASIN **diferente** do usado no guia (ex: busca → `B09BDLVLW5`, guia →
`B06MejMa2`). **NÃO trocar o short link do editor com base no ASIN da busca.**

Motivo: o `/dp/B06MejMa2` direto pode abrir 404/erro no browser do agente
(bloqueio anti-bot/geo), mas o **`link.amazon/B06MejMa2` gerado pelo editor no
SiteStripe abre normalmente** e é o link afiliado correto da conta. O ASIN do
short link do editor é o que vale.

Regra: **o link do editor SEMPRE vence**. Ao gerar review, usar o short link
que o editor já forneceu no guia (`link.amazon/<ASIN>` + `meli.la/<codigo>`),
NUNCA o ASIN que o agente encontra na busca — salvo o editor confirmar troca.

Validação: pedir ao editor para testar o link (`link.amazon/...` abre?) antes
de considerar "ASIN desatualizado". A busca só serve para preço/rating atuais,
não para substituir o short link afiliado.
