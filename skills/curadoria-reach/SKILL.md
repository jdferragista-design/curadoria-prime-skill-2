---
name: curadoria-reach
description: >-
  Pesquisa auxiliar da Curadoria Prime via Agent-Reach (yt-dlp + Jina Reader +
  RSS). Use quando precisar de consenso técnico de reviews no YouTube (PT-BR),
  ler fichas oficiais de fabricante, ou monitorar fontes. NÃO cobre Amazon/ML.
---

# Curadoria Reach — pesquisa auxiliar (Agent-Reach)

Skill **auxiliar** de pesquisa. Complementa `curadoria-review` e
`curadoria-mercado`. Não substitui o gate de mercado (Amazon/ML continuam via
browser-harness/curl/captura do editor).

Instalada em venv isolado (PEP 668 não permite install global):

```bash
source ~/.agent-reach-venv/bin/activate
```

## Quando rodar

1. **Consenso técnico (Régua v2.0, 10%)** — busca e transcrição de reviews
   independentes no YouTube (de preferência PT-BR) sobre o produto analisado.
2. **Ficha oficial** — leitura de páginas de fabricante via Jina Reader quando
   curl/bloqueios atrapalham.
3. **Monitoramento** — RSS de blogs de tecnologia para sinais do produto.

## YouTube — consenso técnico

### Buscar reviews (título, duração, views)

```bash
yt-dlp "ytsearch5:galaxy tab a9 review" --print "%(title)s | %(duration_string)s | %(view_count)s"
```

### Baixar transcrição automática em PT-BR

```bash
VIDEO_ID=$(yt-dlp "ytsearch1:Tablet BOM e BARATO Galaxy Tab A9 vale a pena" --print "%(id)s" | head -1)
yt-dlp --skip-download --write-auto-subs --sub-langs "pt" --sub-format vtt \
  -o /tmp/ytsubs "https://www.youtube.com/watch?v=$VIDEO_ID"
```

### Limpar o VTT para leitura

```bash
sed 's/<[^>]*>//g' /tmp/ytsubs.pt.vtt | grep -vE "^\s*$|^WEBVTT|^NOTE|-->|[0-9]{2}:[0-9]{2}" \
  | sed 's/^[0-9.:]*\s*//' | tr -s ' \n' ' '
```

## Jina Reader — páginas oficiais

```bash
curl -s "https://r.jina.ai/URL_DO_FABRICANTE"
```

Retorna a página como Markdown limpo. Verificar se a URL está correta antes
(URL errada retorna o 404 da própria página, não erro do Jina).

## RSS — monitoramento

```bash
source ~/.agent-reach-venv/bin/activate
python3 -c "
import feedparser
f = feedparser.parse('URL_DO_FEED')
for e in f.entries[:5]: print(e.title, '|', e.link)
"
```

## Health check

```bash
source ~/.agent-reach-venv/bin/activate
agent-reach install --env=auto   # read-only, lista canais disponíveis
```

## Pitfalls

- **Amazon/ML NÃO são cobertos** — preço, estoque e CTA continuam pelo fluxo
  de `curadoria-mercado` (browser-harness/curl/captura do editor). Não usar
  esta skill para preço.
- **Reddit/Twitter/Facebook/Instagram** exigem cookie ou sessão Chrome logada
  (OpenCLI) — mesma barreira do ML; só usar se o editor prover credenciais.
- **yt-dlp precisa de JS runtime**: já configurado em
  `~/.config/yt-dlp/config` (`--js-runtimes node`). Se quebrar, rodar
  `agent-reach install --env=auto` para diagnóstico.
- **Auto-subs às vezes não existem** — se falhar, tentar sem `--write-auto-subs`
  (legendas manuais) ou outro vídeo.
- **Nunca citar alegação de review como teste próprio** — regra da casa:
  "segundo o review publicado por X", atribuído, com data. Review de terceiro
  alimenta Consenso técnico, nunca vira experiência da Curadoria.
- **Fórum/YouTube não substitui ficha oficial** para especificações (§6
  metodologia). Usar para sinais, padrões e consenso, não como prova técnica.
- **Herdado do README do Agent-Reach**: é seletor/instalador/roteador, os
  comandos acima usam as ferramentas upstream (yt-dlp, curl/Jina) diretamente.
