# Imagens para o post 3523 — QCY T13 ANC

Atualizado em 18/08/2026, **depois** de o cliente subir os 3 arquivos no
WordPress (IDs 4960, 4961, 4962) e da verificação de identidade do modelo.

---

## ⚠️ RESULTADO DA VERIFICAÇÃO: só 1 das 3 é do T13 ANC

A ressalva registrada na versão anterior deste arquivo **se confirmou**.

O T13 ANC tem código de modelo **HT06** (SKU oficial `HT06-BLACK` / `HT06-WHITE`,
GTIN 6957141407882 / 6957141407899). O T13 comum é `T13-BLACK` / `T13-WHITE`.
São produtos diferentes: o T13 **não tem ANC**, usa driver de 7,2 mm e
Bluetooth 5.1; o T13 ANC usa 10 mm, BT 5.3 e ANC de até 28–30 dB.

No CDN da QCY o nome do arquivo carrega o código do modelo (`HT06_-1_…` vs
`T13_-2_…`). Cruzei o hash MD5 de cada arquivo com o catálogo oficial:

| Arquivo | Origem no CDN da QCY | Modelo | Situação |
|---|---|---|---|
| `qcy-t13-anc-branco-estojo-aberto` | `HT06_-2_58b1fcdf….png` | **T13 ANC** ✅ | **inserida no artigo** |
| `qcy-t13-anc-preto-fones-estojo` | `T13_-2_73789273….png` | T13 comum ❌ | **não usar** |
| `qcy-t13-anc-branco-vista-frontal` | não bateu com nenhum HT06 | indefinido ⚠️ | **não usar** |

Sobre a terceira: nenhum hash do catálogo HT06 bateu. Na comparação visual
(dHash) ela ficou **muito mais perto das fotos do T13 comum** (distância 13)
do que das do T13 ANC (distância 42–44). O estojo dela tem berços internos
cinza em formato de gota e dobradiça diferente — o mesmo do T13 comum. O
estojo do T13 ANC é liso, com logo QCY no topo. Sem confirmação positiva,
ela fica fora.

**Nenhuma das duas rejeitadas precisa ser apagada da biblioteca** — ficam
disponíveis caso um dia a Curadoria publique um review do T13 comum.

---

## O que foi inserido no artigo

**Seção 5 — Design, ergonomia e conforto** (estava sem imagem):

```
https://curadoriaprime.com/wp-content/uploads/2026/08/qcy-t13-anc-branco-estojo-aberto.webp
```

- `alt`: QCY T13 ANC branco com o estojo de carregamento aberto, os earbuds
  nos compartimentos L e R e um fone em destaque
- legenda: Haste curta e ponteira de silicone: o formato que fecha o canal e
  sustenta o isolamento passivo
- `width="800" height="800"`, `loading="lazy"`, `decoding="async"`

**Seção 10 — App QCY, modo jogo e EQ** (imagem 4965, enviada em 18/08):

```
https://curadoriaprime.com/wp-content/uploads/2026/08/QCY-T13-ANC-app-equalizador-tela-smartphone.webp
```

- `alt`: QCY T13 ANC preto ao lado de um smartphone rodando um jogo, com o
  estojo de carregamento aberto
- legenda: Modo jogo: a QCY declara cerca de 68 ms de latência, ativado pelo app
- `width="1024" height="1024"`, `loading="lazy"`, `decoding="async"`

### Remanejamento que isso exigiu

A imagem antiga `b0350ffe-…png` já ilustrava o app e ficava **imediatamente
antes** do H2 da seção 10. Com a nova logo depois do mesmo H2, as duas
apareceriam coladas, só separadas pelo título. Movi a antiga para a
**seção 7 (ANC de 28dB)**, que estava sem imagem, e ajustei a legenda para o
tema da seção: "Os modos de cancelamento são alternados pelo app: ANC,
Transparência e desligado". Nenhuma imagem foi removida — total foi de 6 para 7.

## Correção extra aplicada

As 4 imagens que já estavam no artigo declaravam `width="758" height="505"`
(proporção 3:2), mas os arquivos reais na biblioteca são **quadrados** ou
panorâmicos. Proporção errada no atributo faz o navegador reservar um espaço
com formato errado e a página "pula" quando a imagem carrega (CLS). Corrigido
contra as dimensões reais da API de mídia:

| Arquivo | Antes | Agora |
|---|---|---|
| `qcy-t13-anc-destaque.webp` | 758×505 | 1424×748 |
| `cn-11134207-…jpeg` | 758×505 | 800×800 |
| `pessoa-usando-o-qcy-t13-anc-…jpeg` | 758×505 | 2048×2048 |
| `b0350ffe-…png` | 758×505 | 1024×1024 |

## Cobertura visual final (7 imagens)

| Posição | Imagem |
|---|---|
| hero | `qcy-t13-anc-destaque.webp` |
| 4. O que vem na caixa | `cn-11134207-…jpeg` |
| 5. Design | `qcy-t13-anc-branco-estojo-aberto.webp` ← nova |
| 6. Qualidade de som | `pessoa-usando-…transporte-publico.jpeg` |
| 7. ANC de 28dB | `b0350ffe-…png` ← remanejada |
| 10. App QCY | `QCY-T13-ANC-app-equalizador-…webp` ← nova |
| caixa do autor | `cristiano-curadoria-prime.jpg` |

As seções 8, 9 e 11–14 seguem sem imagem — são seções de análise (chamadas,
bateria, prós/contras, comparativo, problemas, veredito), onde o modelo Apple
TV 4K também não usa foto. Não é lacuna.

## Nota sobre o checker

`python3 tools/checar_imagens.py` acusa
`[src-existe] Arquivo não encontrado na biblioteca` para as **duas** imagens novas.
É **falso-positivo conhecido**: o export `imagens/curadoriaprime.WordPress.2026-08-17.xml`
tem anexos só até 16/08 e as imagens subiram em 18/08 (IDs 4960 às 10:49 e
4965 às 11:58). Confirmado ao vivo pela API `/wp-json/wp/v2/media/<id>`.
O erro some sozinho no próximo export do WordPress.
