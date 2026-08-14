# Tom, SEO, nota, schema e alegações sensíveis

Canônico: [regras-editoriais.md](regras-editoriais.md) §§5–10 e 16.

## Tom

Português brasileiro, claro, direto, moderado. Segunda pessoa quando
ajudar a decisão. Tamanho = complexidade da decisão, não meta de palavras.

Preferir:

- “é adequado para”
- “pode ser uma boa escolha se”
- “a principal limitação é”
- “pelos dados consultados”
- “nesta faixa de preço”

Evitar: perfeito, imbatível, sem defeitos, compra obrigatória,
revolucionário, nunca dá problema, vale cada centavo (sem critério),
o melhor do Brasil, custo-benefício imbatível.

Não:

- copiar estrutura, frase ou conclusão de concorrente;
- reescrever texto de fabricante como se fosse análise;
- introdução genérica para alongar;
- repetir a mesma conclusão em várias seções;
- keyword stuffing (nome do produto em toda frase);
- FAQ inútil (“o que é Bluetooth?”);
- prometer imparcialidade absoluta ou certeza que a fonte não dá.

Emojis: no máximo nos H2 de seção, com parcimônia. Sem emoji em
parágrafo corrido.

## Valor editorial mínimo

Todo artigo novo precisa de **pelo menos três** itens próprios, por
exemplo:

- recomendação por perfil e quem não deve comprar;
- custo por recurso / faixa em que vale ou deixa de valer;
- versão brasileira vs. importada;
- compatibilidade com aparelhos e serviços usados no Brasil;
- homologação, assistência e garantia no país;
- custo total com acessório obrigatório (HDMI, carregador, ponta);
- problemas recorrentes por frequência ou gravidade;
- matriz de decisão entre concorrentes;
- longevidade de software e suporte;
- divergência entre fichas de loja.

## SEO e arquitetura

Antes de criar página: consulta principal, intenção, problema do
leitor, decisão que a página resolve, diferença em relação ao que
já existe.

- Um artigo por intenção. “Review do X” e “X vale a pena?” na mesma
  pergunta = canibalização → atualizar/consolidar + 301, não terceira URL.
- Título e H1 descrevem o conteúdo. Sem “teste”/“testamos” sem teste
  documentado. Sem ano só para parecer atual.
- Responder a pergunta no início. Meta description sem promessa falsa.
- Alt text descreve a imagem, sem repetir palavra-chave à força.
- Links internos só se ajudarem a decisão (categoria, comparativo,
  rival, guia, metodologia). Sem cota fixa e sem bloco de links mortos.
- Preserve URL e canonical. Não altere slug. Não crie URL nova só
  para trocar o ano. `dateModified` só após mudança editorial real.
  Registrar no artigo o que mudou quando a atualização for relevante.

Tecnologia automotiva, enquanto o nicho valida:

`https://curadoriaprime.com/tecnologia-automotiva/`

Não sugerir outro domínio ou subdomínio. Pauta só se o produto for
tecnologia disponível no Brasil (Amazon/ML). Experiência do autor
como motorista só quando for verdadeira e relevante — e só se o
editor humano a assinar.

## Nota editorial

Não atribuir nota só porque outros artigos têm nota. Sem critérios
suficientes, publique **sem** nota.

Se houver nota:

- escala visível, de preferência 0 a 10;
- critérios da categoria e pesos ou explicação de importância;
- notas parciais verificáveis;
- justificativa da final;
- coerência com prós, contras e veredito;
- comissão, link e N de avaliações externas **não** pesam.

Calibragem (quando a nota existir):

| Faixa | Significa |
| --- | --- |
| 9.0–10 | Referência da categoria no preço; ressalvas menores |
| 8.0–8.9 | Adequado ao perfil certo; rivais vencem em algum eixo |
| 7.0–7.9 | Bom, com limitações claras |
| 6.0–6.9 | Só em promoção ou caso estreito |
| < 6 | Não indicar, ou indicar só como “evite se…” |

Nota da loja ≠ nota editorial.

## Schema

Não gerar schema por padrão.

Proibido: `Product.aggregateRating`, `ratingCount`, `reviewCount`
preenchidos com Amazon, ML, fabricante ou qualquer fonte externa.
Proibido somar nota 0–10 da casa com milhares de reviews de loja.

`AggregateRating` no site só existirá se, no futuro, o próprio site
coletar avaliações autênticas de leitores — e o total será só dessas.

Quando o editor pedir e a nota editorial existir, pode-se sugerir
`Review.reviewRating` com autor **humano real** (nome que o editor
informar), `ratingValue` / `bestRating` / `worstRating` iguais ao
visível, sem contagem externa.

`Offer` / `priceValidUntil` só com dado verificado na publicação ou
atualização automática.

## Alegações sensíveis

Sem atribuição e prova: nível médico, precisão profissional, 100% à
prova de vazamentos, totalmente à prova d’água, indestrutível,
garantido, sem risco, comprovado cientificamente, o mais seguro,
o melhor do Brasil.

Promessa do fabricante = “segundo a fabricante” + fonte. Não vira
conclusão independente.

**Saúde e wearables:** sem diagnóstico, prevenção, tratamento ou cura.
Diferenciar bem-estar de dispositivo médico. Citar autorização
regulatória só se ela se aplicar ao recurso, modelo e país.

> Os recursos de saúde são destinados a acompanhamento pessoal e não substituem avaliação, diagnóstico ou equipamento médico.

**Auto:** não incentivar tela, fone ou celular de forma insegura ao
dirigir. Verificar tensão, instalação, compatibilidade, homologação
e lei. Não declarar que acessório aumenta segurança sem condição e
evidência.

## Imagens

- IA fotorealista não pode parecer teste próprio.
- Legenda quando houver risco de interpretação errada (texto oficial
  das regras).
- Não chamar de oficial sem origem e permissão.
- Foto de “teste próprio” só se for original do editor.
- Alt descritivo e factual.

## Números e datas

- Preço: `R$ 1.465,85`.
- Nota de loja no texto: `Na Amazon, o produto apresentava nota 4,8/5 em aproximadamente 1.700 avaliações consultadas em 12/08/2026.`
- Datas no texto por extenso quando couber; ISO no checklist interno.

## Rumor

Sempre a palavra **rumor**, veículo e data. Nunca como lançamento.
