# Verificação antes de concluir

Adaptado de dois padrões públicos, aprovados pelo cliente em 18/08/2026:

- **`obra/superpowers` — verification-before-completion** (MIT): evidência antes de
  qualquer afirmação de conclusão.
- **`trailofbits` — ask-questions-if-underspecified** (MIT): perguntar antes de
  executar quando o pedido admite mais de uma leitura.

Nada aqui altera regra editorial. É disciplina de processo — e existe porque os
três erros abaixo aconteceram **nesta skill**, não em teoria.

---

## Parte 1 — A Lei de Ferro

```
NENHUMA AFIRMAÇÃO DE CONCLUSÃO SEM EVIDÊNCIA FRESCA
```

Se o comando de verificação não foi executado **nesta mensagem**, não é possível
afirmar que passou.

### A função-portão

Antes de declarar qualquer status ou expressar satisfação:

1. **IDENTIFICAR** — qual comando prova esta afirmação?
2. **RODAR** — executar o comando completo, agora, não reaproveitar saída anterior.
3. **LER** — a saída inteira: código de saída, número de erros, contagem.
4. **CONFERIR** — a saída confirma a afirmação?
   - Não → declarar o estado real, com a evidência.
   - Sim → fazer a afirmação **junto** com a evidência.
5. **SÓ ENTÃO** afirmar.

Pular qualquer passo é mentir, não verificar.

### Tabela de evidência exigida (contexto Curadoria Prime)

| Afirmação | Evidência obrigatória | NÃO basta |
|---|---|---|
| "checker 14/14" | saída de `checar_conformidade.py` nesta resposta | rodada anterior; "não mexi nisso" |
| "aplicado no artigo" | `grep` no arquivo **em `articles/`** | ter editado o modelo em `skills/` |
| "imagem existe" | API de mídia ao vivo (`/wp-json/wp/v2/media?search=`) | export XML (é foto de uma data) |
| "está no ar" | `fetch_page` do post publicado | o cliente ter dito que colou |
| "estado atualizado" | `checar_estado.py` com 0 divergências | ter escrito o `.md` na mesma rodada |
| "imagens preservadas" | `checar_imagens_preservadas.py` | contar `<img>` de cabeça |
| "preço verificado" | captura própria com data | resultado de busca; página de catálogo |
| "nenhuma imagem perdida" | saída da trava, com o total antes → depois | "só troquei a URL" |
| "commit e push feitos" | `git log --oneline -1` + saída do push | `git commit` sem conferir rejeição |
| "link funciona" | `fetch_page` retornando conteúdo real | o link "parecer" certo |

### Sinais de alerta — parar e verificar

- Usar "deve estar", "provavelmente", "parece que".
- Expressar satisfação **antes** da verificação ("Pronto!", "Feito!", "Perfeito!").
- Estar prestes a commitar ou entregar sem rodar o checker.
- Confiar em verificação parcial (um grep em vez do arquivo inteiro).
- Pensar "só desta vez".
- Qualquer redação que **implique** sucesso sem ter rodado a prova.

### Racionalizações e a resposta a cada uma

| Desculpa | Realidade |
|---|---|
| "Deveria funcionar agora" | RODE a verificação |
| "Tenho certeza" | Confiança não é evidência |
| "Só desta vez" | Não há exceção |
| "O checker passou" | O checker não testa imagem, nem estado, nem o que está no ar |
| "O cliente disse que colou" | Conferir com `fetch_page` — pode ter colado versão anterior |
| "Está no export" | O export é de uma data; a biblioteca muda |
| "Editei o modelo" | Modelo não é artigo. O leitor lê o artigo |

### Os três casos reais que originaram esta regra (17–18/08/2026)

1. **"As 4 alterações estão aplicadas."** Foram aplicadas em
   `skills/.../modelo-layout-apple-tv-4k.html`. Nenhum artigo mudou. O cliente
   respondeu: *"não vi nem uma mudança"*.
   → Evidência que faltava: `grep` no arquivo em `articles/`.

2. **"3548 concluído."** `audit/estado-3548.md` continuou declarando nota 8,2 e
   4.261 palavras quando o artigo tinha 8,0 e 5.239.
   → Evidência que faltava: comparar o `.md` com o artigo (hoje `checar_estado.py`).

3. **"2 imagens quebradas em presentes-tech."** Testei contra o export de 17/08;
   o cliente havia convertido o arquivo para WebP em 15/08. As imagens estavam
   corretas no ar.
   → Evidência que faltava: API de mídia ao vivo + página publicada.

---

## Parte 2 — Perguntar quando o pedido é ambíguo

Um pedido está subespecificado quando, **depois de uma leitura rápida do
repositório**, ainda não está claro:

- **objetivo** — o que muda e o que permanece;
- **feito** — como se reconhece a conclusão;
- **escopo** — quais arquivos e seções entram;
- **restrições** — modelo a seguir, regra editorial aplicável, limite de tamanho;
- **origem do dado** — dump, captura própria, ficha do fabricante;
- **reversibilidade** — vai para o ar? altera post publicado?

Havendo duas leituras plausíveis, tratar como ambíguo.

### Como perguntar

- No máximo **1 a 5 perguntas**, as que eliminam ramos inteiros de trabalho.
- Numeradas, curtas, escaneáveis — nunca em parágrafo corrido.
- Alternativas objetivas, com a **recomendada marcada**.
- Sempre uma saída rápida: *"responda `padrão` para aceitar as recomendadas"*.

### Enquanto as respostas essenciais não chegam

**Não** editar arquivos, não commitar, não reescrever seção.
**Pode** fazer descoberta de baixo risco e claramente rotulada: ler o modelo,
inspecionar o artigo, consultar a biblioteca de mídia.

Se o cliente pedir para seguir sem responder: listar as suposições em lista
numerada e pedir confirmação antes de executar.

### Antipadrões

- Perguntar o que uma leitura rápida responde. **Ler `template-review.md`
  resolve; perguntar "qual é o modelo?" depois de reescrever 6 artigos, não.**
- Pergunta aberta quando múltipla escolha resolveria mais rápido.
- Mais de cinco perguntas de uma vez.

### O caso real (18/08/2026)

Reescrevi seis artigos replicando o formato dos que já estavam no ar. O
`SKILL.md` declara desde a primeira linha que o modelo canônico é
`assets/template-review.md`. Só perguntei qual era o modelo **depois** de o
cliente estranhar o resultado.

O template diz, na abertura: *"Apague seção que não decide a compra."* Eu vinha
fazendo o inverso — empilhando camadas. O artigo do Redmi chegou a 5.333
palavras, 27 minutos de leitura, para um fone de R$ 78,99.

**Custo:** seis artigos fora do padrão, retrabalho em todos.
**Preço de evitar:** uma leitura de arquivo, antes de começar.
