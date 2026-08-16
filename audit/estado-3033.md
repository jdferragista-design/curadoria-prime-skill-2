# ESTADO — 3033 (Good Vision Kit 2 Câmeras Wi-Fi review)

**Status:** ✅ REWRITE CONCLUÍDO e validado (aguardando colagem no WP pelo cliente)

- URL: https://curadoriaprime.com/good-vision-kit-cameras-wifi-review/
- Título: Good Vision Kit 2 Câmeras Wi-Fi Vale a Pena em 2026? Review
- Entregável: `articles/good-vision-kit-cameras-wifi-review.html`
- Categoria: `casa-inteligente-e-seguranca` (427)
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **2 links de afiliado** com `rel="sponsored noopener noreferrer nofollow"` (CTA topo + rodapé; o publicado tinha 3 âncoras, consolidei em 2 botões — todos agora sponsored).
- **"dados de compradores verificados"** → "avaliações publicadas por compradores" + box de metodologia com "não testamos estas unidades fisicamente".
- **"Pontos de Atenção"** (h4 + `<ul>` 5 itens) — o publicado usava "Desvantagens" (heading não reconhecido pela §2.7).
- **Nota editorial 7,8/10** + **"para quem NÃO é"** — faltavam no publicado (o checker exige "nota" e "para quem não é").
- **"à prova d'água" → "resistente à água (IP66), não submersível"** (§6 — alegação absoluta).
- **Alternativas comparadas** (kits 4K G.Eye A28 / iCSee A28B na mesma faixa) — dá o sinal "comparativo" e valor editorial real.
- **Preço com data + aviso**: anúncio vinculado (R$ 350) aparece com "anúncio pausado / última unidade" em 16/08/2026 — o artigo orienta a conferir disponibilidade.
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + Product (reviewRating 7,8/10) + FAQPage + BreadcrumbList (`casa-inteligente-e-seguranca`); autor "Cristiano Martins"; sem aggregateRating/offers.
- **Bloco de autor canônico** + "Fontes consultadas" + "Veja também" (3052, 2884 — slugs reais).
- **Imagens**: hero local + 2 imagens fornecidas pelo cliente (lente dupla giratória `D_Q_NP_2X_690824...` e visão noturna colorida `D_NQ_NP_2X_669910...`), ambas já em URL local do WP (`/uploads/2026/01/`).

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 2/2 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.126 palavras · valor-agregado completo · imparcialidade 6 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 25/25 · ul 2/2 · p 67/67 · h2 15/15 · li 11/11 · a 16/16. Zero base64.
```

## Dados de mercado (16/08/2026)

| Item | Valor |
|---|---|
| Produto | Kit 2 Câmeras Wi-Fi Good Vision CAMGV (lente dupla giratória, 3MP) |
| Shortlink | `mercadolivre.com/sec/2w2H2mP` → MLB-5806065456 |
| Preço | R$ 350 no anúncio vinculado — mas **"Anúncio pausado" / "Último disponível"** |
| Specs-chave | 3MP (2048×1536) · PTZ · Wi-Fi/BT/LAN · IP66 · cartão 128GB · visão noturna 49,9m · 20 FPS |

## Pendências FORA do arquivo (painel / cliente)

1. **Colar no WP** substituindo o conteúdo atual (Editor de Código).
2. ⚠️ **Anúncio vinculado "pausado"**: o shortlink `2w2H2mP` cai num anúncio pausado/última unidade (16/08/2026). O leitor pode chegar numa página sem estoque. **Conferir/regenerar o link de afiliado** (ou trocar por outro vendedor do mesmo kit).
3. ~~Imagens hotlink~~ ✅ RESOLVIDO: o cliente forneceu 2 imagens locais (lente dupla giratória + visão noturna colorida), já aplicadas no artigo. Nenhum hotlink externo restante.
