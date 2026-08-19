# Voz, SEO, Régua, schema e alegações sensíveis

Versão: 2.2

Canônico de comportamento:

`../SKILL.md`

Canônico de política editorial:

`regras-editoriais.md`

Este documento detalha voz e redação.

Não redefine a Régua Curadoria Prime.

---

# 1. TOM

Português brasileiro.

Claro.

Direto.

Moderado.

Segunda pessoa quando ajudar a decisão.

Comprimento = complexidade da decisão.

Não meta de palavras.

Preferir:

- é adequado para;
- pode ser uma boa escolha se;
- a principal limitação é;
- pelos dados consultados;
- nesta faixa de preço;
- segundo a fabricante;
- segundo o teste de X;
- na consulta de DD/MM/AAAA.

Evitar:

- perfeito;
- imbatível;
- sem defeitos;
- compra obrigatória;
- revolucionário;
- nunca dá problema;
- vale cada centavo sem critério;
- melhor do Brasil;
- custo-benefício imbatível;
- unanimidade;
- comprovadamente superior sem prova.

---

# 2. NÃO FAZER

Não:

- copiar frase de concorrente;
- copiar conclusão;
- reescrever fabricante como análise;
- introdução vazia;
- repetir veredito em todas as seções;
- keyword stuffing;
- FAQ genérico;
- prometer imparcialidade absoluta;
- prometer certeza maior que a evidência.

---

# 3. EMOJIS

Usar principalmente:

- títulos;
- componentes visuais canônicos.

Evitar emoji em texto corrido.

Não adicionar emoji em toda frase.

---

# 4. VALOR EDITORIAL

Todo artigo deve demonstrar interpretação própria útil.

Exemplos:

- perfil adequado;
- quem deve evitar;
- faixa racional;
- custo por recurso;
- Brasil vs importado;
- compatibilidade;
- homologação;
- suporte;
- custo de acessório;
- problemas recorrentes;
- matriz de decisão;
- longevidade;
- divergência de fichas.

Não tratar quantidade exata desses elementos como regra oficial do
Google.

A política da Curadoria pode exigir um padrão mínimo, mas nunca invente
análise apenas para atingir quota.

---

# 5. SEO

Antes de criar:

- consulta;
- intenção;
- problema;
- decisão;
- página existente.

Uma intenção por URL.

Review X e "X vale a pena" geralmente são a mesma intenção.

Evitar canibalização.

---

# 6. TÍTULO E H1

Descrever a página.

Sem:

- "teste";
- "testamos";

quando não houve teste.

Não adicionar ano apenas para freshness.

Ano pode existir quando realmente fizer parte da intenção/contexto
editorial.

---

# 7. META DESCRIPTION

Descrever:

- produto/tema;
- decisão;
- principal diferencial.

Não inventar:

- preço;
- nota;
- oferta;
- estoque.

Não prometer resultado que o artigo não entrega.

---

# 8. ALT

Descritivo e factual.

Não usar:

- LSI;
- stuffing;
- keyword artificial;
- "vale a pena" quando não descreve imagem.

---

# 9. LINKS INTERNOS

Adicionar somente quando ajudarem:

- rival;
- comparativo;
- categoria;
- metodologia;
- review relacionado.

Sem cota fixa.

Sem bloco de links mortos.

---

# 10. URL E FRESHNESS

Preservar:

- URL;
- slug;
- canonical.

Não criar nova URL só para trocar ano.

`dateModified` somente após mudança substancial.

Registrar atualização relevante.

---

# 11. RÉGUA EDITORIAL

A única Régua vigente é:

Curadoria Prime v2.0 — agosto/2026.

Critérios:

- Custo-benefício — 30%
- Satisfação verificada — 25%
- Ficha técnica — 20%
- Recursos e usabilidade — 10%
- Consenso técnico — 10%
- Confiança e suporte — 5%

Não criar "critérios da categoria" substitutos.

Aspectos da categoria entram como evidência dentro desses seis.

---

# 12. NOTAS

Nota não é obrigatória quando falta evidência.

Quando houver:

- escala 0–10;
- incrementos de 0,5;
- seis critérios;
- pesos públicos;
- justificativa;
- cálculo;
- selo;
- coerência.

Não usar:

8,7
9,2.

Não criar precisão falsa.

---

# 13. SATISFAÇÃO E COMISSÃO

Quantidade de ratings externos NÃO entra automaticamente como pontos
numéricos sem análise metodológica.

A comissão nunca entra na nota.

Link comercial nunca entra na nota.

Satisfação verificada deve obedecer à metodologia v2.0 e ao
SATISFACTION_GATE.

---

# 14. SELOS

9,0–10:

🏆 Melhor da categoria

8,0–8,5:

⭐ Recomendado

7,0–7,5:

👍 Bom com ressalvas

6,0–6,5:

⚖️ Existem alternativas melhores

< 6,0:

⚠️ Não recomendado

Não usar faixa antiga 8,0–8,9.

A nota só possui passos de 0,5.

---

# 15. SCHEMA

Não gerar por padrão.

Proibido usar como rating próprio:

- Amazon;
- ML;
- fabricante;
- qualquer nota externa.

Não preencher:

`Product.aggregateRating`
`ratingCount`
`reviewCount`

com dados externos apresentados como avaliação da Curadoria.

---

# 16. REVIEW SCHEMA

Somente quando solicitado e compatível com a implementação atual.

Se houver Review editorial:

- autor humano real;
- ratingValue igual ao visível;
- bestRating;
- worstRating;
- sem count externo.

A IA não inventa autor.

---

# 17. OFFER

Preço somente com dado válido.

`priceValidUntil` somente quando houver validade real confirmada.

Data da consulta não é:

`priceValidUntil`.

Nunca inventar data futura.

---

# 18. ALEGAÇÕES SENSÍVEIS

Sem fonte e atribuição:

não usar:

- nível médico;
- precisão profissional;
- 100%;
- totalmente à prova d'água;
- indestrutível;
- garantido;
- sem risco;
- comprovado cientificamente;
- mais seguro;
- melhor do Brasil.

Promessa do fabricante:

`segundo a fabricante`.

Não virar conclusão independente.

---

# 19. SAÚDE

Não diagnosticar.

Diferenciar:

- bem-estar;
- monitoramento;
- dispositivo/função regulamentada.

Não inventar ANVISA.

Quando necessário:

**Os recursos de saúde são destinados a acompanhamento pessoal e não
substituem avaliação, diagnóstico ou equipamento médico.**

---

# 20. AUTOMOTIVO

Não incentivar uso inseguro.

Verificar:

- tensão;
- instalação;
- compatibilidade;
- homologação;
- legislação.

Não declarar que acessório aumenta segurança sem base.

Experiência pessoal do autor como motorista somente:

- se verdadeira;
- relevante;
- aprovada pelo editor;
- assinada pelo humano.

---

# 21. IMAGENS

Imagem de IA não pode sugerir teste próprio.

Não chamar de oficial sem origem confirmada.

Foto de teste próprio só se original/documentada pelo editor.

Alt factual.

O plano operacional de imagens é definido no SKILL.

---

# 22. PREÇO

Formato:

`R$ 1.465,85`

Sempre com data quando apresentado como valor de mercado atual.

Não escrever:

"oferta atual"

sem verificação atual.

---

# 23. RATINGS EXTERNOS

Forma adequada:

`Na Amazon, o anúncio consultado em 12/08/2026 exibia nota 4,8/5 em aproximadamente 1.700 avaliações.`

Não escrever:

`1.700 compradores aprovaram`.

Não somar plataformas.

Não chamar de nota da Curadoria.

---

# 24. RUMOR

Sempre:

- palavra "rumor";
- veículo;
- data.

Nunca escrever rumor como lançamento confirmado.

---

# 25. SUPERLATIVOS

Antes de:

"o melhor"

"líder"

"referência absoluta"

perguntar:

Há comparação e fontes suficientes?

Se não:

reescrever de forma proporcional à evidência.

---

# 26. REGRA FINAL DE VOZ

Prefira precisão à empolgação.

Prefira condição à promessa.

Prefira:

"adequado para X"

a:

"perfeito para todos".

Prefira:

"segundo X"

a:

"comprovadamente".

Prefira:

"os dados sugerem"

a:

"não há dúvida",

quando houver incerteza legítima.
