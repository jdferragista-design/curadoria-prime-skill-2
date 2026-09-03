---
name: content-layout-audit
description: "Verify content against a Golden Model. Audit markers."
version: 1.1.0
author: Hermes Agent
license: MIT
---

# Content Layout Audit

Audita a integridade visual e estrutural do conteúdo (HTML/CMS) quando não há render
em navegador. Em vez de adivinhar, o agente faz uma **Auditoria por Marcadores**.

## Regra de ouro (nova)

Cada tipo de conteúdo tem um golden próprio no repo de skills:
- **Review** → `skills/curadoria-review/assets/modelos/modelo-review-golden.html`
- **Lista** → `skills/curadoria-review/assets/modelos/modelo-lista-golden.html`
- **VS** → `skills/curadoria-review/assets/modelos/modelo-vs-golden.html`

As paletas **diferem entre tipos** (ex.: `#5a4fcf/#764ba2` é do lista; o review usa
`#2997ff`). Audite sempre com o golden do tipo correspondente. Os marcadores para
**reviews** estão em `references/curadoria-prime-review-standards.md`.

## Workflow

1. **Carregar a fonte de verdade**: o golden do tipo correspondente (ou `references/
   curadoria-prime-review-standards.md` para review).
2. **Extrair o alvo**: ler o src bruto do conteúdo a auditar (HTML/JSON).
3. **Auditar por marcadores**:
   - **Marcadores visuais**: hex codes, gradientes e classes que definem a identidade.
   - **Marcadores estruturais**: presença e ordem das seções obrigatórias.
   - **Integridade de tags**: tags balanceadas, aninhamento correto, ausência de fragmentos.
   - **Marcadores de conteúdo**: rótulos obrigatórios ("Onde Comprar", "Veredito") presentes e corretos.
4. **Relatar como checklist**: binário Confirmado ✅ / Faltando ❌ / Incorreto ⚠️, com trecho do src como evidência.

## Armadilhas & Invariantes

- **Sem adivinhação**: não assuma que uma seção está "certa" só porque o texto existe; verifique as tags/classes.
- **Src bruto apenas**: nunca audite uma versão resumida do conteúdo.
- **Evidência explícita**: cada "Confirmado" deve vir com um trecho do código.
- **Checagem de limite**: se um marcador obrigatório faltar, marque como Faltando, não como Confirmado.

## Formato do relatório (exemplo)

- [✅] **Cor primária**: encontrado `#2997ff` no destaque do header.
- [✅] **Hero section**: `<div style="background: linear-gradient(135deg,#1d1d1f 0%,#000000 100%);...">` no topo.
- [⚠️] **Prós/Contras**: pontos presentes, mas wrapper `<ul>` obrigatório ausente.
- [❌] **Box de transparência**: `background: #fffbeb` não encontrado no src.
