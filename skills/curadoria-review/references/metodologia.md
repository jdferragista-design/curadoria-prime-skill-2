# Fontes, disclaimers e o que a IA pode afirmar

Canônico: [regras-editoriais.md](regras-editoriais.md) §§2–4 e 8.
Página pública: [Sobre a Curadoria Prime](https://curadoriaprime.com/sobre-a-curadoria-prime/).

A pesquisa do site tem 5 etapas. Elas descrevem o **trabalho editorial**.
Não autorizam linguagem de teste físico.

## Hierarquia de fontes

1. **Primária** — fabricante, manual, documentação técnica, Anatel ou
   norma oficial. Preferir página `.com/br` e variante brasileira.
2. **Teste independente identificável** — publicação, laboratório ou
   canal com método e evidência. Creditar veículo + data. Não copiar
   parágrafo. Não narrar o teste deles como “nós”.
3. **Comercial** — Amazon, Mercado Livre, loja oficial: só preço,
   disponibilidade, variante e relatos de compradores.
4. **Fórum e rede social** — só para achar problema relatado. Nunca
   como única prova de fato técnico.

Não invente cota artificial de fontes se elas repetem a mesma ficha.
Qualidade e diversidade > quantidade.

## Conflito entre fontes

1. Não escolher em silêncio o dado mais conveniente.
2. Conferir região, variante, firmware, unidade e data.
3. Explicar a divergência no texto.
4. Priorizar manual e documentação da versão brasileira.
5. Se o conflito não se resolve, a conclusão fica **incerta**.

## Sem teste físico (padrão)

Formulações permitidas:

- “analisamos as especificações oficiais”
- “segundo o teste publicado por [fonte]”
- “nos testes independentes consultados”
- “compradores relatam” / “relatos publicados”
- “a ficha técnica informa”
- “a partir do cruzamento das fontes”
- “a análise editorial indica”

Proibidas sem evidência do §2.2: testamos, usamos por X dias, na nossa
bancada, em nosso teste, no uso real percebemos, comprovamos, medimos,
fizemos unboxing, colocamos lado a lado, testado por nós, qualquer
sensorial de contato.

**Box obrigatório:**

```markdown
**Tipo de análise:** pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou esta unidade fisicamente.
```

## Teste próprio (só com as 8 evidências)

O editor precisa entregar: responsável; data e duração; origem da
unidade (comprada, emprestada, cedida); modelo/variante; protocolo e
condições; medições ou observações; fotos originais; limitações.

Se faltar um item, **não** é “Testado por nós”.

```markdown
**Tipo de análise:** teste próprio realizado por [nome], entre [datas], com uma unidade [modelo/variante]. Consulte abaixo o protocolo, as condições e as limitações.
```

## Avaliações de compradores

Permitido: padrões recorrentes; elogios vs. reclamações; plataforma +
data; distinguir variante e país; síntese editorial.

Proibido:

- “compradores verificados” sem selo explícito da plataforma;
- “milhares foram analisados” sem método e quantidade reais;
- aspas em paráfrase;
- frase “representativa” inventada;
- usar review de loja como prova definitiva de spec, segurança ou desempenho;
- esconder reclamação recorrente para converter.

Síntese padrão:

> **Síntese editorial dos relatos:** compradores elogiam [padrão], enquanto as reclamações mais recorrentes envolvem [padrão].

Aspas: transcrição fiel, curta, verificável, com plataforma e data.
Não reproduzir texto longo protegido.

Se o artigo declarar volume grande de avaliações, registrar internamente
(não precisa ir ao texto público, mas precisa existir na entrega):
plataformas, data ou intervalo, quantidade aproximada, variante,
critérios temáticos, limitações/duplicatas/região.

## Pesquisa de mercado (obrigatória)

Antes de card ou CTA, rodar a skill
[curadoria-mercado](../../curadoria-mercado/SKILL.md).
Varejo não é “colar o menor preço do search”. É classificar o
checkout: código, vendedor, nacional vs internacional, catálogo vs
anúncio, e se o SKU ainda faz sentido contra o que o site já indica.

## Preço e disponibilidade

Todo preço leva loja, data da consulta, condição (Pix, cupom, 12x) e
o aviso de que preço e estoque podem mudar.

Não escrever “menor preço garantido”, “melhor preço da internet” ou
“oferta válida” sem verificação objetiva e atual. Não inventar
`priceValidUntil`. `Offer` no schema só com dado atualizado na hora
da publicação ou atualização automática.

## Afiliado

```markdown
**Transparência:** este artigo contém links de afiliado. Se você comprar por meio deles, a Curadoria Prime pode receber uma comissão, sem custo adicional para você. Isso não altera nossos critérios editoriais.
```

- `rel="sponsored nofollow"` em todo link afiliado.
- Alternativa sem comissão entra se for melhor para o perfil, e o
  texto diz que não gera comissão.
- Comissão não muda nota, ordem de guia nem veredito.
- Sem CTA em todo parágrafo e sem urgência falsa.

## Fontes consultadas (obrigatório)

Nomes + URLs diretas. Data de consulta em preço, estoque, nota e
quantidade de avaliações.

Agrupar:

1. Oficiais do fabricante / regulador
2. Testes independentes e histórico factual
3. Rumores (a palavra **rumor** + veículo + data)
4. Varejo (página específica da Amazon, do ML, da loja oficial)

Sem essa seção, o artigo não está pronto para revisão humana.
