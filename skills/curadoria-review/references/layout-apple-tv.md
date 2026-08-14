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
