# ESTADO — 3226 (Samsung HW-B400F vs JBL Cinema SB180 vs LG SQC1)

**Status:** ✅ REWRITE CONCLUÍDO e validado (aguardando colagem no WP pelo cliente)

- URL: https://curadoriaprime.com/samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1/
- Título: Samsung HW-B400F vs JBL SB180 vs LG SQC1: Qual Soundbar Comprar?
- Entregável: `articles/samsung-hw-b400f-vs-jbl-cinema-sb180-vs-lg-sqc1.html`
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **9 links de afiliado** com `rel="sponsored noopener noreferrer nofollow"` (3 topo + 3 tabela + 3 rodapé).
- **Divulgação**: já existia no ar (adicionada em 14/08), mas dizia "dados de compradores verificados" → "avaliações publicadas por compradores". Adicionado **box de metodologia** com "não testamos estas unidades fisicamente".
- **"Pontos de Atenção"** (h4 + `<ul>` com 3 itens) em cada uma das 3 soundbars (o publicado usava "O que não funciona tão bem" em parágrafos).
- **Preços em faixa com data (16/08/2026)** + aviso de volatilidade; valores do publicado (R$ 698/1.020/1.190) eram de fev/2026.
- **Spec Samsung corrigida**: 40 W RMS (2×20 W) — o publicado confundia com "20 W" de consumo em operação.
- **Superlativos suavizados**: "a mais vendida", "vence", "domina", "campeã", "definitivo", "imbatível", "Vencedor geral".
- **Link "Veja também" corrigido**: o publicado apontava para o slug quebrado `samsung-u8600f-vs-lg-au801-vs-philips-50pug7019-qual-tv-4k-50-comprar/` → corrigido para o slug real `samsung-u8600f-vs-lg-au801-vs-philips-50pug7019/`.
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + ItemList (3 soundbars) + FAQPage (4 perguntas) + BreadcrumbList (`tv-e-home-theater`); autor "Cristiano Martins"; sem aggregateRating/offers.
- **Bloco de autor canônico** + "Fontes consultadas" + "Veja também" (3153, 3310, 3320 — slugs reais).

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 9/9 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.444 palavras · valor-agregado completo · imparcialidade 3 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 35/35 · ul 6/6 · p 62/62 · h2 11/11 · h4 3/3 · li 24/24 · a 27/27.
Zero base64.
```

## Dados de mercado coletados (16/08/2026)

| Soundbar | Specs-chave | Preço hoje | Identificador |
|---|---|---|---|
| Samsung HW-B400F (2025) | 2.0, 40W RMS, BT 4.2, HDMI ARC, Night Mode, One Remote | R$ 595 (KaBuM) a R$ 698 (Amazon) | ASIN B0FJHYW5BK |
| JBL Cinema SB180 | 2.1, sub 6,5″ 40Hz, 110W RMS, BT 5.3, HDMI ARC | R$ 838,95 (ML) / R$ 849 (Amazon) | MLB34289961 · ASIN B0CT922NH7 |
| LG SQC1 (2024) | 2.1, 160W RMS, sub MDF 5,25″, sem HDMI ARC, BT 4.0 | fev/2026 ~R$ 1.190 → ago/2026 R$ 1.651 (estoque reduzido) | MLB42238664 |

- JBL Amazon: 4,8/5 (~1.500 avaliações, 16/08/2026) — único rating re-verificado.

## Pendências FORA do arquivo (painel / cliente)

1. **Colar no WP** substituindo o conteúdo atual (Editor de Código).
2. **Título do post**: o publicado diz "JBL SB180"; o nome oficial do produto é "JBL Cinema SB180" — padronizar no título SEO/H1 se quiser.
3. **Specs LG SQC1 a conferir** (herdadas do publicado): "Bluetooth 4.0" e "sem HDMI ARC".
4. ⚠️ **LG SQC1 (2024) com estoque reduzido**: preço saltou de ~R$ 1.190 (fev) para R$ 1.651 (ago). A tese original "melhor watt por real" está enfraquecida — o artigo foi ajustado para "confira a oferta atual", mas vale reavaliar (§17.2 nível 1). A sucessora natural é a **LG S40T** (~R$ 894 no ML, ago/2026), caso o cliente queira trocar depois — mesmo tratamento dado à Philips no 3153.
5. **Frequência de graves Samsung/LG**: a ficha não informa; manter "não informado" (não inventar).
