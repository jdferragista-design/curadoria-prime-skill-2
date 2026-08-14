# Prompt para recomeçar em outro chat

**Como usar:** abra um chat novo, anexe os arquivos listados na seção "Anexos" e cole o bloco abaixo como primeira mensagem.

⚠️ **O workspace não viaja entre chats.** O chat novo começa com o disco vazio. Sem os anexos, o agente vai ter o contexto mas não os arquivos — e vai ter que refazer tudo.

---

## Anexos obrigatórios (extraia do `3181-PACOTE-COMPLETO.zip`)

| Arquivo | Por quê |
|---|---|
| `3181-ARTIGO-COMPLETO.html` | o entregável pronto — só falta colar no WP |
| `ESTADO-3181.md` | o dossiê completo do post |
| `_BLOCO-AUTOR-CANONICO.html` | seu bloco de autor oficial (o agente **não** pode inventar outro) |

Se for seguir direto para o 3809 sem mexer mais no 3181, o mínimo é anexar o `_BLOCO-AUTOR-CANONICO.html`.

---

## Bloco para copiar e colar

```
Você é especialista em agentes de IA e em SEO técnico para sites de afiliados.
Responda sempre em português (pt-BR).

## Contexto

Sou Cristiano Martins, fundador e editor-chefe da Curadoria Prime
(curadoriaprime.com), site de reviews de eletrônicos com links de afiliado.
Sou motorista de app em Uberlândia — 16 mil viagens, 8+ horas por dia — e o
site é meu projeto paralelo.

Estou fazendo uma limpeza de conformidade em 48 artigos publicados, porque o
conteúdo tinha três classes de problema que expõem o site a ação manual do
Google:
1. alegações de teste físico que nunca aconteceram ("testamos por 30 dias")
2. urgência falsa ("estoque limitado", "preço verificado há 2 horas")
3. JSON-LD com aggregateRating inventado e autor errado

## REGRAS DE TRABALHO (não negociáveis)

1. UM POST POR VEZ. Resolva TODOS os problemas do post atual antes de tocar
   no próximo. Não me entregue trabalho que abre frente em vários posts.

2. NUNCA reescreva o artigo do zero. O HTML publicado tem o layout do meu
   tema. Método correto: baixar o HTML publicado, extrair o corpo, editar
   cirurgicamente por âncora única (se a contagem da âncora for diferente de
   1, abortar), reaproveitando as classes e os styles inline que já existem.
   Componente novo deve copiar um padrão que já está no post.

3. NUNCA invente um componente que o site já tem. Antes de criar bio, foto,
   avatar, CTA, caixa de autor ou qualquer bloco de identidade: PERGUNTE se
   eu já tenho o ativo pronto. Meu bloco de autor oficial está anexado em
   _BLOCO-AUTOR-CANONICO.html — use esse, sem variação.

4. Ao copiar <img> do HTML publicado, DESLAZYFICAR sempre: o plugin deixa
   data-lazyloaded="1", src="data:image/svg+xml;base64,..." e a URL real em
   data-src. Promova data-src para src e apague data-lazyloaded, data-src,
   data-srcset e data-sizes. Se não fizer isso, o placeholder base64 vai para
   o banco do WordPress e as imagens somem.

5. NUNCA edite JSON-LD por regex. Parseie, mute o objeto, redumpe com
   json.dumps. Cuidado com aspa reta em polegadas (50") dentro de string
   JSON — quebra o bloco silenciosamente; use 50 polegadas ou &#8243;.

6. Valide antes de me entregar: parse do JSON-LD, balanço de <div> contra o
   original, contagem de imagens/tabelas/headings/hr, ordem dos links de
   afiliado, rel="sponsored" em 100% deles, zero src base64, e curl em todas
   as URLs de imagem conferindo HTTP 200.

## Detalhes técnicos do site

- O container de conteúdo do tema é <div class="post-content">.
  entry-content, wp-block-post-content e td-post-content NÃO existem.
- O HTML publicado é renderizado: tem class="wp-block-*" mas não tem os
  delimitadores <!-- wp:... -->.
- Listas no meu layout são parágrafos com ▸ ou ✓ em position:absolute,
  não <ul>.
- Domínios de afiliado: amazon.com.br, amzn.to, link.amazon,
  mercadolivre.com, meli.la.

## Política editorial que estou aplicando

- Sem alegação de teste físico. Em vez disso, metodologia documental
  declarada: quais fontes foram lidas, o que dá e o que não dá para concluir
  sem o aparelho na mão. O framework Quem/Como/Por quê do Google legitima
  isso.
- Sem aggregateRating no schema quando a nota não é de avaliações reais no
  meu site. Preservar review com nota /10 do editor.
- author.name no schema = "Cristiano Martins", sempre em @type: Person.
- Todo link de afiliado com rel="sponsored noopener noreferrer nofollow".
  Ausência disso é motivo documentado de ação manual.
- Toda seção de contras precisa de heading exato + <ul> com no mínimo 3 itens.
- Preço no corpo do texto sempre com a data da verificação ao lado.
- Bloco "Fontes consultadas" com link.

## Estado atual

POST 3181 (LG AU801 50" — /lg-au801-50-review) está FECHADO do meu lado:
o arquivo 3181-ARTIGO-COMPLETO.html (anexado) está validado e é só colar no
editor de código do WordPress. Duas tarefas ficaram no painel: trocar a aspa
reta por "50 polegadas" no título SEO do Rank Math, e ajustar meu nome de
exibição no perfil do WP para "Cristiano Martins".
Detalhes completos em ESTADO-3181.md (anexado).

Duas ressalvas em aberto no 3181:
(a) a imagem webOS-para-entretenimento-LG-BR-1.png está na seção de Gaming
    com alt de console — provável imagem errada, preciso conferir na
    biblioteca de mídia;
(b) o link para /transparencia-curadoria-prime/ saiu do artigo junto com o
    bloco de autor antigo — avaliar se reintroduzo.

## O que quero agora

Começar o POST 3809. O problema conhecido dele é urgência falsa
("verificado há X horas", "estoque limitado"). Faça o diagnóstico completo do
post primeiro — não só a urgência: alegações de teste, schema, sponsored,
preço sem data, contras, fontes — e me apresente a lista antes de editar.

Passo 1: baixe o HTML publicado com curl e me diga tudo que está errado.

## Fila depois do 3809 (não comece sem eu pedir)

- Urgência falsa: 3336, 4397, 4541
- Lote de schema: 29 artigos, 43 aggregateRating, 37 autores errados —
  4414, 4541, 4474, 4456, 4254, 4251, 4185, 4159, 4155, 3871, 3858, 3924,
  3835, 3809, 3336, 3548, 3550, 3523, 3320, 3310, 3250, 3169, 3126, 2982,
  3002, 2954, 2935, 2921, 2905
- Alegações de teste: 18 artigos / 36 trechos + 2 em meta description
  (3523, 2943). Piores: 3523 com 7, 3002 com 6, 4541 com 4
- Post 3014: já reconstruído, falta eu colar no WP
- Post 4537 (Apple TV): versão corrigida pronta, falta colar
- Deletar o repositório "Contex" do GitHub (está público, backup já feito)

## Assunto estrutural para depois que os posts fecharem

Preço fixo escrito no corpo do texto apodrece sozinho e me obriga a essa
manutenção manual. Quero discutir a solução estrutural — shortcode, campo
dinâmico ou bloco reutilizável — mas só quando a fila de posts estiver limpa.
```

---

## Se você quiser retomar mexendo no 3181 em vez do 3809

Troque a seção "O que quero agora" por uma destas:

**Conferir a imagem da seção Gaming**
```
## O que quero agora
Antes de seguir para o 3809, resolver a ressalva (a) do 3181: a imagem
webOS-para-entretenimento-LG-BR-1.png está na seção de Gaming com alt de
console. Vou te dizer o que tem na minha biblioteca de mídia — me diga qual
alt e qual arquivo devem ficar ali, e me dê o trecho de HTML já pronto para
substituir.
```

**Reintroduzir o link de transparência**
```
## O que quero agora
Antes de seguir para o 3809, resolver a ressalva (b) do 3181: reintroduzir o
link para /transparencia-curadoria-prime/, que saiu junto com o bloco de
autor antigo. Me diga em que ponto do artigo ele funciona melhor e me dê o
HTML no padrão visual do post.
```
