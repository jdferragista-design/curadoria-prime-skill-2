# Imagens de artigos — convenção de prompts (curadoriaprime.com)

Onde fica o artefato: `articles/html_output/PROMPTS-IMAGENS-<slug>.md`.
Registro por sessão: smartphones (29/08) e games Switch (31/08) usaram o MESMO
fluxo. Não há pipeline de geração no projeto (sem skill `curadoria-imagens`, sem
GPU/comfy-cli no ambiente do agente) — logo a convenção do projeto é:

## Fluxo padrão
1. O agente monta o resto do artigo (título, preços, cards) primeiro.
2. O agente escreve um `PROMPTS-IMAGENS-<slug>.md` com: objetivo (voz ativa),
   descrição p/ o editor, **prompt EN**, **variante PT**, checklist de aceite e
   destino dos arquivos.
3. O **editor gera** na ferramenta dele e sobe no WP Media.
4. Agente verifica **HTTP 200 do link exato** no HTML antes de declarar pronto.

Quando o usuário pedir "gera a imagem hero/thumbnail", se NÃO há gerador
operacional (sem comfy-cli, sem servidor, sem torch, sem API key de geração),
NÃO tentar "gerar" no vazio: escrever os prompts prontos no padrão da casa e
avisar que o editor gera. Descobrir antes: `command -v comfy`, 
`curl -s http://127.0.0.1:8188/system_stats`, `python3 -c "import torch"`.

## Formatos (dimensões finais)
| Uso | Tamanho | Nota |
| --- | --- | --- |
| Hero (topo do artigo) | 970×546 (16:9) | entra no `src` da seção hero |
| Destaque / og:image / card do blog | 1200×600 (2:1) | imagem destacada no painel |
| Thumbnail de YouTube | 1280×720 (16:9) | capa de vídeo / share |

## Identidade visual (fundo)
- Guia multi-marca (lista de produtos): gradiente `#1a1a2e → #16213e` (bate com
  o hero HTML).
- Review de marca única: primária da marca (ver `references/cores.md`), ex
  `#1a1f5c → #0d1130` p/ fundo escuro premium de guia.

## Regras de conteúdo da imagem (não negociáveis)
- **Sem texto legível** — geradores de IA erram português. Usar número/ícone
  gráfico se quiser contar itens, nunca frase.
- **Sem logos de terceiros** além do próprio produto; sem marca d'água.
- **Produto-âncora em destaque**, demais em fileira/aglomerados.
- **Nomes de arquivo descritivos** e coerentes com o slug do artigo.

## Check de aceite (copiar do arquivo gerado)
`[ ] produto-âncora é o destaque` · `[ ] fundo na identidade` ·
`[ ] sem texto/logo/marca d'água` · `[ ] hero 970×546` · `[ ] destaque 1280×720`.

## Pendência que NÃO bloqueia o HTML
O JSON-LD `Article.image` pode apontar para a foto do produto-âncora já no
WP Media mesmo sem hero dedicada — manter esse link vivo (200). Hero dedicado é
opcional; o gradiente do topo cobre o visual. O que vale como imagem destacada
do post é a `destaque`.
