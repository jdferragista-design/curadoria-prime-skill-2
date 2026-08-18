# Layout canônico — padrão Apple TV 4K

Referência visual e de blocos: [apple-tv-4k](https://curadoriaprime.com/apple-tv-4k/).

Mantemos a **ordem, os cards e o ritmo** dessa página. Não mantemos
as frases que violam as regras da casa ou o Google (“testamos a fundo”,
nota de loja como se fosse nossa, assinatura automática).

**Cores:** hero = paleta oficial da **marca do produto**. Botões =
cores oficiais da **plataforma** (Amazon, ML, Apple Store, Samsung).
Tokens em [cores.md](cores.md). Não misturar as duas paletas.

## Ordem dos blocos (não reordene)

1. **Hero** — imagem larga + H1 honesto (sem “teste” sem teste).
2. **Tipo de análise** — box no texto oficial das regras.
3. **Lead** — 3–6 linhas: o que é, 2–3 fatos da ficha, a pergunta, a tese.
4. **Barra de recorte** — dados da **consulta editorial**, não estrelas
   de marketplace como badge do site.
   - Faixa de preço + data
   - Data de atualização real
   - Opcional: “Nas lojas, em [data]: Amazon x,x/5 (N) · ML x,x/5 (N)”
     como texto de terceiro, nunca como `AggregateRating`.
5. **Metodologia** — 1 parágrafo + link `/sobre-a-curadoria-prime/`.
6. **Síntese editorial dos relatos** — padrões Amazon/ML com data.
   Aspas só em transcrição fiel. Sem “verificados” sem selo.
7. **Índice âncora** — numerado, como a Apple TV (1️⃣ 2️⃣ …).
8. **Abertura** — o problema do leitor + a tensão (preço, rival, esperar).
9. **Transparência de afiliado** — texto oficial + `rel="sponsored nofollow"`.
10. **Resposta rápida** — três cards: vale / depende / pode esperar.
11. **Onde comprar** — 2–3 cards de preço (menor preço, compra segura,
    marketplace). Alerta de internacional / geração / estoque.
12. **Ficha técnica oficial** — tabela, só fonte primária.
13. **Seções de decisão** — H2 por eixo (design, imagem, ecossistema…).
    Em cada uma: fato → terceiro atribuído → interpretação.
14. **Comparativo** — tabela de rivais com preço da mesma data.
15. **Comprar agora ou esperar** — se houver rumor/geração; rumor rotulado.
16. **Prós e contras** — dois grupos, coerentes com o veredito.
17. **Para quem é / não é** — bullets.
18. **FAQ** — dúvidas de compra, 6–10.
19. **Veredito** — síntese + notas parciais **se** houver critério.
    Sem nota se a base for fraca.
20. **CTAs de loja** de novo, com preço e ressalva.
21. **Caixa do editor** — só depois da aprovação humana (nome que o
    editor informar). Link para `/bio-do-cristian/` e `/nossa-prova/`
    se for o Cristiano.
22. **Fontes consultadas** — URLs diretas + data.
23. **Histórico de atualização** — só se a mudança for substancial.

Guias: mesma casca (hero, tipo, transparência, resposta rápida por
perfil, cards de produto, comparativo, alertas, FAQ, fontes). Ver
`assets/template-guia.md`.

## O que o layout Apple TV acerta (preserve)

- Resposta na primeira tela.
- Preço com data, Pix vs. 12x, loja oficial vs. internacional.
- Alerta de SKU/geração (A2737 vs. A1842).
- Link sem comissão quando é o melhor preço nacional.
- Rumor com veículo e data.
- Comparativo que admite rival barato.
- Fontes no rodapé.

## O que o layout Apple TV no ar ainda erra (corrija em toda atualização)

- “Testamos a fundo” sem unidade na mão.
- Barra ⭐ Amazon/ML com cara de nota do site.
- “compra verificada” sem selo visível na captura.
- Assinatura automática no rascunho da IA.
- Schema de estrelas de loja, se o plugin do WP estiver injetando.

## WordPress

- Preserve URL e canonical.
- Não troque o slug.
- `dateModified` só após esta atualização substancial.
- Título SEO ≤ ~60 caracteres, sem “teste” falso.
- Alt text factual.
- Imagem `Gemini_` / `Firefly_` / `ChatGPT-Image`: legenda oficial de IA
  se puder parecer foto de teste.
- Links afiliados: `rel="sponsored nofollow"`.
- Conferir Yoast/Rank Math/schema plugin: remover AggregateRating externo.

---

## Alterações do cliente ao layout canônico (18/08/2026)

Ajustes aprovados sobre a casca Apple TV 4K. Valem para **todo review novo
ou atualizado** e já estão aplicados em
`assets/modelos/modelo-layout-apple-tv-4k.html`.

### 1. Índice do conteúdo — 2 colunas fixas

Era `repeat(auto-fit, minmax(220px, 1fr))`, que virava 3 colunas em telas
largas e desalinhava a numeração. Agora:

```
grid-template-columns: repeat(2, 1fr); gap: 8px 18px;
```

### 2. Resposta rápida — 4 blocos (era 3)

Ao trio "✅ vale / 🤔 depende / ⏳ pode esperar" soma-se um quarto card:

```
❌ Não vale a pena se você…   (fundo #fef2f2, borda #ef4444, título #991b1b)
```

Deve trazer o perfil para quem o produto **não** serve, o motivo objetivo e a
alternativa concreta, com modelo e faixa de preço da mesma data. É o card que
protege o leitor de uma compra errada — e o que mais gera confiança.

### 3. Onde comprar — cards de venda SEM imagem

Os cards de preço trazem apenas selo, loja, valor, condição e botão. **Nenhuma
foto do produto dentro do card**: a imagem repetida empurra o preço para baixo
da dobra e atrasa a decisão.

**Em guias**, a imagem do produto vai na **introdução do item** (antes ou logo
após o H3 daquele produto), nunca dentro do bloco de compra.

### 4. Veredito — notas em blocos de 3

A grade de notas parciais passa a ser fixa em três por linha:

```
grid-template-columns: repeat(3, 1fr);
```

Mantém o alinhamento previsível em vez de reflow por largura.
