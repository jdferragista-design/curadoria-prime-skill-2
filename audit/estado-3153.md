# ESTADO — 3153 (Samsung U8600F vs LG AU801 vs Philips 50PUG7019)

**Status:** ✅ PUBLICADO NO AR (conferido 16/08/2026)

- URL: https://curadoriaprime.com/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019/
- Título: Samsung U8600F vs LG AU801 vs Philips 50PUG7019: Qual TV 4K 50″ Comprar?
- Entregável: `articles/samsung-u8600f-vs-lg-au801-vs-philips-50pug7019.html`
- Data da reescrita: 16/08/2026

## O que foi corrigido

- **9 links de afiliado** agora com `rel="sponsored noopener noreferrer nofollow"` (3 topo + 3 tabela + 3 rodapé).
- **Shortlink Amazon da Samsung unificado** em `amzn.to/4biQQdq` (o publicado tinha 2: `4biQQdq` no topo e `4rhzNx7` na tabela/rodapé). Escolhi `4biQQdq` por ser o mesmo já usado no review 3181 (LG AU801) na tabela comparativa — mantém consistência entre artigos.
- **Alegações de teste/tempos não medidos removidas**: "Depois de usar, é impossível voltar", "Tizen é rápido / Netflix abre em 2-3 segundos", "digitar a senha fica até 5× mais rápido", tempos de boot "15-20s | 20-25s | 25-30s". Seção "Desempenho real: qual é mais rápida?" eliminada (sem números inventados).
- **"dados de compradores verificados" → "avaliações publicadas por compradores"** (transparência + metodologia).
- **Citações/nomes não verificáveis removidos** ("Leandro", "Múltiplos compradores", e todas as aspas de comprador). Substituídos por **"Síntese editorial dos relatos"** (sem aspas, sem nome) — padrão §4.2, com base nos relatos reais do Mercado Livre coletados via API.
- **Box de metodologia** com "não testamos estas unidades fisicamente" + selo "Testado por nós" contextualizado.
- **"Pontos de Atenção"** (h4 + `<ul>` com 3 itens) em cada uma das 3 TVs.
- **Preços em faixa com data de consulta (16/08/2026)** e aviso de volatilidade; diferenças de preço recomputadas e suavizadas (o publicado tinha erro aritmético: R$ 113/R$ 77/R$ 190 quando o correto era R$ 213/R$ 47/R$ 260).
- **Superlativos suavizados**: "mais popular", "vence", "Tizen é rápido", "de outro nível", "impossível voltar", "não mentem", "ranking nº X".
- **JSON-LD limpo** em `wp:html` SEM `<br />`: TechArticle + ItemList (3 TVs) + FAQPage (4 perguntas) + BreadcrumbList (`tv-e-home-theater`); autor "Cristiano Martins"; **sem aggregateRating, sem offers, sem aspa reta** ("50 polegadas" nas strings).
- **Bloco de autor canônico** (foto + bio + X) com "Por Cristiano Martins".
- **"Fontes consultadas"** + "Veja também" (3226, 3181, 3183 — slugs reais).
- **Philips 50PUG7300 (sucessora 2025) adicionada como OPÇÃO** na seção da Philips — com botões próprios (Amazon `B09uCSSBI` + Mercado Livre `27D4FgZ`, fornecidos pelo cliente), "Pontos de Atenção" próprio e inclusão no ItemList do JSON-LD (4 itens). A 50PUG7019 permanece como está.

## Validação (checar_conformidade.py)

```
✅ Aprovado. — 0 erros, 0 alertas.
rel-sponsored 11/11 · divulgação antes dos links · autoria · metodologia ·
honestidade (não testamos fisicamente) · fontes · data · teste-fisico 0 ·
profundidade 2.828 palavras · valor-agregado completo · imparcialidade 3 contras ·
schema válido (parse OK, sem aggregateRating).
Balanço: div 43/43 · ul 7/7 · p 68/68 · h2 11/11 · h4 4/4 · li 27/27. Zero base64.
```

## Dados de mercado coletados (16/08/2026)

| TV | Loja | Preço hoje | Identificador |
|---|---|---|---|
| Samsung U8600F 50" | Amazon | R$ 2.399 à vista (Pix/NuPay); 12x R$ 206,32; outros vendedores a partir de R$ 2.440 | ASIN B0F5X4LL89 |
| LG AU801 50" | Mercado Livre | R$ 2.242 no Pix (de R$ 2.361) | MLB61517857 |
| Philips 50PUG7019 50" | Mercado Livre | volátil: R$ 1.894 (fev/2026) → anúncio em destaque R$ 3.390 (ago/2026) | MLB43158430 |
| Philips 50PUG7300 50" (opção, 2025) | Amazon / ML | R$ 2.199 (Amazon) · R$ 1.935 Pix (ML) | B0FPBPX7WF / MLB57723340 |

- Shortlinks Philips 50PUG7300 (cliente): Amazon `https://link.amazon/B09uCSSBI` · ML `https://meli.la/27D4FgZ`.

- Avaliações Amazon (fev/2026, mantidas do publicado com data): Samsung 4,7/5 (~194) · LG 4,9/5 (~815) · Philips 4,8/5 (~9 mil).
- Relatos ML coletados via API (MLB61517857 e MLB43158430) usados só como síntese editorial.

## Aviso de estoque + gancho 50PUG7300 (adicionado 16/08/2026)

Na opção "50PUG7300", o texto agora aponta estoque baixo/zerado da 7019 como
prova de que a sucessora está tomando o lugar + gancho "Em breve: review
dedicado da 50PUG7300". Trocar pelo link real quando o post sair.

## Pendências FORA do arquivo (painel / cliente)

1. **Colar no WP** substituindo o conteúdo atual (Editor de Código).
2. Rank Math > título SEO: manter "50″" ou trocar por "50 polegadas" (mesma pendência do 3181).
3. **Confirmar o shortlink Amazon da Samsung** (unificado em `4biQQdq`; o `4rhzNx7` foi descartado — se o `4rhzNx7` for o correto, trocar nas 3 ocorrências).
4. **Specs Philips a conferir** (herdadas do publicado): "3x HDMI 2.1" e "tempo de resposta 8 ms".
5. ✅ **Aviso editorial (Philips) RESOLVIDO:** a 50PUG7300 (sucessora, 2025) entrou como opção com venda ativa e preço estável — resolve o "fim de linha" da 50PUG7019 sem mexer no slug/título do artigo.

## Inconsistência cross-artigo (registrar, não bloquear)

- **Processador LG AU801**: 3153 e o listing ML dizem "α7 AI Gen 8"; o review 3181 (já entregue) diz "α7 AI de quinta geração / Gen 5". Conferir qual é o oficial (LG Brasil) e alinhar o 3181 se necessário.
