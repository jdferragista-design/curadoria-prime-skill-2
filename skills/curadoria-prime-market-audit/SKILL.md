---
name: curadoria-prime-market-audit
description: Use when auditing curadoriaprime.com prices. Validates data.
---

# Curadoria Prime Market Audit

Esta skill governa a verificação de se os preços e "veredictos" em reviews publicadas
no `curadoriaprime.com` ainda estão exatos em relação ao mercado atual.

## 🎯 Objetivo central

Garantir que nenhum usuário veja um preço desatualizado ou um veredicto "Recomendado"
para um produto que disparou de preço ou caiu de qualidade/consenso.

## 🛠️ Workflow operacional

### 1. Descoberta (regra do "Sitemap Primeiro")
**Nunca dependa apenas do repositório GitHub** para saber o que está publicado — site e repo divergem.
- **Ação:** extrair URLs de `https://curadoriaprime.com/post-sitemap.xml`.
- **Objetivo:** lista definitiva de URLs vivas.

### 2. Extração de conteúdo
Para cada artigo a auditar:
- **Ação:** usar `web_extract` na URL viva.
- **Objetivo:** identificar o produto exato, o preço listado no site e o veredicto atual (ex.: "Recomendado").

### 3. Pesquisa de mercado (prioridade de afiliado)
Buscar o menor preço e a disponibilidade atuais.
- **Lojas prioritárias:** **Amazon**, **Mercado Livre** e **Shopee** (usuário é afiliado).
- **Lojas secundárias:** Magalu, Casas Bahia, etc. (usar só se nenhuma oferta afiliada for competitiva).
- **Verificação:** checar versões "Global" vs "Nacional" em produtos Xiaomi/importados para não enganar com preço.

### 4. Veredicto & análise
- **Status OK:** o preço do site está numa margem razoável (ex.: ±5%) do melhor offer afiliado, ou o melhor offer é maior.
- **Status ATUALIZAR:**
    - Queda significativa de preço em loja afiliada.
    - Produto indisponível nas lojas primárias.
    - Nova versão lançada, tornando a review atual obsoleta.

## 🎨 Estilo de comunicação (modo silencioso)
Ao auditar em "lotes" (ex.: 10 artigos de uma vez), usar **modo silencioso** para não poluir o chat:
- **NÃO** postar tabelas individuais nem logs detalhados por produto.
- **POSTAR** um resumo conciso: total de artigos auditados, contagem de "OK", contagem de
  "ATUALIZAR" e menções breves às quedas de preço mais críticas.

## ⚠️ Armadilhas & restrições

- **Zero invenção:** nunca fabricar preço ou SKU. Se a busca for inconclusiva, marque como
  "Não verificado" e pergunte ao usuário.
- **Integridade do afiliado:** sempre priorizar achar a oferta na Amazon, Mercado Livre ou
  Shopee antes de sugerir uma atualização.
- **Controle de versão:** desconfiar do preço da "Versão Chinesa" ser menor que o da "Versão Global".
  Sempre buscar o preço Global para reviews brasileiras.
