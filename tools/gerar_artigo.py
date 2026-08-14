#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gerar_artigo.py — Gerador de artigos HTML no padrão Curadoria Prime
====================================================================
Recebe um JSON com os dados do produto e devolve o HTML pronto para
colar no WordPress (ou publicar via publicar_wp.py).

Uso:
    python3 gerar_artigo.py exemplo-produto.json -o artigo.html

O template replica exatamente a estrutura dos seus artigos:
  bloco de transparência -> CTA de compra -> prós/contras -> specs ->
  seções de análise -> comparativo -> para quem é -> FAQ -> veredito ->
  CTA final -> fontes consultadas
"""

import json
import argparse
import sys
from datetime import datetime

# ---------------------------------------------------------------- paleta
C = {
    "roxo":      "#5a4fcf",
    "roxo_esc":  "#2d3277",
    "tinta":     "#1a1a2e",
    "cinza":     "#7c7c9a",
    "borda":     "#e9ecef",
    "amazon_a":  "#FF9900",
    "amazon_b":  "#FFB84D",
    "amazon_tx": "#232F3E",
    "meli_a":    "#3485DB",
    "meli_b":    "#5BA3E8",
    "verde":     "#16a34a",
    "vermelho":  "#dc2626",
}


def bloco_transparencia():
    return f"""<div style="background:#f8f8ff;border:1px solid #e2e2f0;border-radius:10px;padding:14px 20px;margin-bottom:28px;font-size:13.5px;color:{C['cinza']};line-height:1.65;">
  📣 <strong style="color:{C['tinta']};">Transparência:</strong> Este conteúdo contém links de afiliado da Amazon e do Mercado Livre. Se você comprar pelo nosso link, podemos receber uma pequena comissão — sem custo adicional para você. Isso nos ajuda a continuar produzindo reviews gratuitos e independentes.
  <a href="https://curadoriaprime.com/transparencia-curadoria-prime/" target="_blank" rel="noopener" style="color:{C['roxo']};text-decoration:underline;font-weight:600;">Saiba mais sobre nossa política de transparência →</a>
</div>"""


def bloco_autor(p):
    """Assinatura + data + metodologia VISÍVEL no topo (E-E-A-T).

    O Google avalia 'Quem, Como e Por quê'. A metodologia enterrada em nota de
    rodapé não cumpre o 'Como'. Este bloco responde aos três no primeiro scroll.
    """
    # §2.6 — a assinatura é do humano que conferiu e aprovou. Se o JSON traz
    # 'editor', ele assina. Senão, cai para a equipe (aceitável no rascunho,
    # mas o editor humano deve assumir a assinatura antes de publicar).
    autor = p.get("editor") or p.get("revisado_por") or p.get("autor", "Equipe Curadoria Prime")
    data = p.get("data_verificacao", "")
    linha_data = f" · Análise verificada em {data}" if data else ""
    return f"""<div style="border-left:3px solid {C['roxo']};padding:12px 18px;margin-bottom:24px;font-size:14px;color:{C['cinza']};line-height:1.7;">
  <strong style="color:{C['tinta']};">Por {autor}</strong>{linha_data}<br/>
  <span><strong style="color:{C['tinta']};">Tipo de análise:</strong> pesquisa editorial baseada em especificações
  oficiais, testes independentes e relatos publicados por compradores.
  <strong style="color:{C['tinta']};">A Curadoria Prime não testou esta unidade fisicamente.</strong>
  <a href="https://curadoriaprime.com/isencao-de-responsabilidade-curadoria-prime/" target="_blank" rel="noopener" style="color:{C['roxo']};text-decoration:underline;">Como avaliamos →</a></span>
</div>"""


def botoes_loja(links):
    """Gera os botões Amazon / Mercado Livre."""
    out = []
    if links.get("amazon"):
        out.append(
            f"""<a style="flex:1;min-width:140px;background:linear-gradient(135deg,{C['amazon_a']} 0%,{C['amazon_b']} 100%);color:{C['amazon_tx']};text-decoration:none;padding:14px 20px;border-radius:10px;font-weight:bold;text-align:center;font-size:14px;box-shadow:0 2px 8px rgba(255,153,0,.3);" href="{links['amazon']}" target="_blank" rel="sponsored noopener noreferrer nofollow">🔥 Ver na Amazon</a>"""
        )
    if links.get("mercadolivre"):
        out.append(
            f"""<a style="flex:1;min-width:140px;background:linear-gradient(135deg,{C['meli_a']} 0%,{C['meli_b']} 100%);color:#fff;text-decoration:none;padding:14px 20px;border-radius:10px;font-weight:bold;text-align:center;font-size:14px;box-shadow:0 2px 8px rgba(52,133,219,.3);" href="{links['mercadolivre']}" target="_blank" rel="sponsored noopener noreferrer nofollow">🛒 Ver no Mercado Livre</a>"""
        )
    return "\n      ".join(out)


def card_compra(p, destaque=True, titulo="🛒 Onde Comprar: Melhores Preços de Hoje"):
    selo = (
        f"""<span style="background:linear-gradient(135deg,{C['vermelho']} 0%,#991b1b 100%);color:#fff;padding:4px 12px;border-radius:20px;font-size:13px;font-weight:800;white-space:nowrap;">⭐ Recomendado 2026</span>"""
        if destaque else ""
    )
    aval = f'~R$ {p["preco"]}' if p.get("preco") else ""
    if p.get("avaliacoes"):
        aval += f' | +{p["avaliacoes"]} avaliações'
    selos = "".join(f" | ✅ {s}" for s in p.get("selos", []))
    selos = selos.lstrip(" |") if selos else ""

    return f"""<div style="background:#fff;border:1px solid {C['borda']};border-radius:20px;padding:35px 25px;margin-top:40px;box-shadow:0 4px 20px rgba(0,0,0,.05);">
  <h3 style="text-align:center;color:{C['roxo_esc']};font-size:22px;margin:0 0 30px 0;">{titulo}</h3>
  <div style="background:#fff;border:2px solid {C['vermelho']};border-radius:14px;padding:20px;margin-bottom:18px;">
    <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:15px;">
      {selo}
      <span style="font-weight:bold;color:#1a1f36;font-size:17px;">{p['nome']} <span style="font-weight:400;color:#888;font-size:14px;">{aval}</span></span>
    </div>
    <div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">
      {botoes_loja(p.get('links', {}))}
    </div>
    <p style="text-align:center;font-size:12px;color:#888;margin:12px 0 0;">{selos}</p>
  </div>
  <p style="text-align:center;font-size:12px;color:#999;margin:0;">⚠️ Preços verificados em {p.get('data_verificacao', datetime.now().strftime('%d/%m/%Y'))} e sujeitos a alteração sem aviso prévio.</p>
</div>"""


def lista_pros_contras(pros, contras):
    li_p = "\n".join(f"<li>{x}</li>" for x in pros)
    li_c = "\n".join(f"<li>{x}</li>" for x in contras)
    return f"""<h2 class="wp-block-heading">✅ Prós e Contras</h2>

<div style="display:flex;gap:20px;flex-wrap:wrap;margin:24px 0;">
  <div style="flex:1;min-width:260px;background:#f0fdf4;border-left:4px solid {C['verde']};border-radius:8px;padding:18px 22px;">
    <h3 style="margin-top:0;color:#15803d;font-size:18px;">✅ Pontos Positivos</h3>
    <ul style="margin:0;padding-left:20px;line-height:1.8;">
{li_p}
    </ul>
  </div>
  <div style="flex:1;min-width:260px;background:#fef2f2;border-left:4px solid {C['vermelho']};border-radius:8px;padding:18px 22px;">
    <h3 style="margin-top:0;color:#b91c1c;font-size:18px;">❌ Pontos de Atenção</h3>
    <ul style="margin:0;padding-left:20px;line-height:1.8;">
{li_c}
    </ul>
  </div>
</div>"""


def tabela_specs(specs):
    linhas = "\n".join(
        f"<tr><td style='padding:10px 14px;border-bottom:1px solid {C['borda']};font-weight:600;width:38%;'>{k}</td>"
        f"<td style='padding:10px 14px;border-bottom:1px solid {C['borda']};'>{v}</td></tr>"
        for k, v in specs.items()
    )
    return f"""<h2 class="wp-block-heading">📋 Especificações Técnicas Completas</h2>

<figure class="wp-block-table has-fixed-layout"><table>
<tbody>
{linhas}
</tbody>
</table></figure>"""


def tabela_comparativo(comp):
    if not comp:
        return ""
    cabec = comp["colunas"]
    th = "".join(
        f"<th style='padding:12px 14px;background:{C['roxo_esc']};color:#fff;text-align:left;'>{c}</th>"
        for c in cabec
    )
    trs = ""
    for i, linha in enumerate(comp["linhas"]):
        bg = "#fff" if i % 2 == 0 else "#fafaff"
        tds = "".join(
            f"<td style='padding:11px 14px;border-bottom:1px solid {C['borda']};'>{c}</td>"
            for c in linha
        )
        trs += f"<tr style='background:{bg};'>{tds}</tr>\n"
    return f"""<h2 class="wp-block-heading">📊 Comparativo com Concorrentes Diretos</h2>

<figure class="wp-block-table"><table>
<thead><tr>{th}</tr></thead>
<tbody>
{trs}</tbody>
</table></figure>"""


def secoes_analise(secoes):
    out = []
    for s in secoes:
        paras = "\n\n".join(
            f'<p class="wp-block-paragraph">{par}</p>' for par in s["paragrafos"]
        )
        out.append(f"""<h2 class="wp-block-heading">{s['titulo']}</h2>

{paras}""")
    return "\n\n".join(out)


def para_quem(sim, nao):
    li_s = "\n".join(f"<li>{x}</li>" for x in sim)
    li_n = "\n".join(f"<li>{x}</li>" for x in nao)
    return f"""<h2 class="wp-block-heading">🎯 Para Quem É / Para Quem NÃO É</h2>

<h3 class="wp-block-heading">✅ SIM — Vale a pena para você se…</h3>
<ul style="line-height:1.9;">
{li_s}
</ul>

<h3 class="wp-block-heading">❌ NÃO — Não vale a pena se…</h3>
<ul style="line-height:1.9;">
{li_n}
</ul>"""


def faq(itens):
    blocos = ""
    for q in itens:
        blocos += f"""<div style="border:1px solid {C['borda']};border-radius:10px;padding:16px 20px;margin-bottom:12px;background:#fff;">
  <p style="margin:0 0 8px;font-weight:700;color:{C['roxo_esc']};font-size:16px;">❓ {q['pergunta']}</p>
  <p style="margin:0;line-height:1.7;color:#444;">{q['resposta']}</p>
</div>
"""
    return f"""<h2 class="wp-block-heading">❓ Perguntas Frequentes</h2>

{blocos}"""


def veredito(p):
    nota = p["nota"]
    cor = C["verde"] if nota >= 8 else ("#f59e0b" if nota >= 7 else C["vermelho"])
    paras = "\n\n".join(f'<p class="wp-block-paragraph">{x}</p>' for x in p["veredito"])
    return f"""<h2 class="wp-block-heading">✅ Veredito Final: {p['nome']} Vale a Pena em 2026?</h2>

<div style="background:linear-gradient(135deg,#f8f8ff 0%,#eef0ff 100%);border-radius:16px;padding:28px;margin:24px 0;text-align:center;">
  <div style="font-size:52px;font-weight:800;color:{cor};line-height:1;">{nota}<span style="font-size:26px;color:#999;">/10</span></div>
  <p style="margin:10px 0 0;color:{C['cinza']};font-size:14px;font-weight:600;">Nota Curadoria Prime</p>
</div>

{paras}"""


def fontes(lista):
    li = "\n".join(
        f'<li><a href="{f["url"]}" target="_blank" rel="noopener">{f["titulo"]}</a></li>'
        for f in lista
    )
    return f"""<hr class="wp-block-separator has-alpha-channel-opacity"/>

<h4 class="wp-block-heading">📚 Fontes Consultadas</h4>
<ul style="font-size:14px;color:{C['cinza']};line-height:1.8;">
{li}
</ul>

<p style="font-size:13px;color:#999;font-style:italic;margin-top:18px;">
Metodologia: análise de especificações oficiais do fabricante, estudo de testes independentes
publicados, síntese de relatos de compradores e comparativo com produtos concorrentes na mesma
faixa de preço. Não recebemos produtos das fabricantes e não realizamos testes físicos próprios. <a href="https://curadoriaprime.com/isencao-de-responsabilidade-curadoria-prime/" target="_blank" rel="noopener">Leia nossa isenção de responsabilidade</a>.
</p>"""


def _iso(data_br):
    """Converte 'DD/MM/AAAA' em 'AAAA-MM-DD' para o schema.org."""
    if not data_br:
        return datetime.now().strftime("%Y-%m-%d")
    try:
        return datetime.strptime(data_br.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError:
        return datetime.now().strftime("%Y-%m-%d")


def schema_jsonld(p):
    """Schema.org Review + FAQPage.

    NÃO é gerado por padrão. Regras editoriais §7.3: "Não gerar schema por
    padrão. Só gerar quando solicitado e depois de validação técnica."
    Use a flag --schema do CLI para emitir.

    Restrições que este gerador respeita:
    - §2.4 — proibido usar nota/total de Amazon, ML ou fabricante como
      `aggregateRating`, `ratingCount` ou `reviewCount`. Aqui NUNCA emitimos
      esses campos: só `Review.reviewRating`, que é a nota editorial própria.
    - §2.6 / §7.3 — `author` deve ser a PESSOA humana que conferiu e aprovou.
      Organização não assina review. Sem `editor` no JSON, o schema é recusado.
    - §7.1 — nota é opcional. Sem nota, sai Review sem `reviewRating`.
    """
    editor = p.get("editor") or p.get("revisado_por")
    if not editor:
        raise ValueError(
            "Schema pedido, mas falta a chave 'editor' no JSON.\n"
            "   Regras editoriais §2.6: a assinatura é do humano que conferiu e\n"
            "   aprovou o conteúdo — não da organização, não de pessoa que não revisou.\n"
            "   Adicione:  \"editor\": \"Nome do Editor Responsável\""
        )

    review = {
        "@type": "Review",
        "itemReviewed": {
            "@type": "Product",
            "name": p["nome"],
            "brand": {"@type": "Brand", "name": p.get("marca", "")},
        },
        # §2.6 — Person, nunca Organization.
        "author": {"@type": "Person", "name": editor},
        "publisher": {"@type": "Organization", "name": "Curadoria Prime"},
        # 'Como' o review foi feito — E-E-A-T. Descreve o método documental
        # sem alegar teste físico e sem dizer "compradores verificados"
        # (§4.2: só com selo explícito da plataforma).
        "reviewAspect": (
            "Especificações oficiais do fabricante, testes independentes "
            "publicados e relatos de compradores"
        ),
        "datePublished": _iso(p.get("data_verificacao")),
    }

    # §7.1 — nota é opcional e criteriosa. Só entra no schema se existir de
    # fato e estiver visível na página.
    if p.get("nota") is not None:
        review["reviewRating"] = {
            "@type": "Rating",
            "ratingValue": p["nota"],
            "bestRating": 10,
            "worstRating": 0,
        }

    grafo = [review]

    faqs = [
        {
            "@type": "Question",
            "name": q["pergunta"],
            "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]},
        }
        for q in p.get("faq", [])
    ]
    if faqs:
        grafo.append({"@type": "FAQPage", "mainEntity": faqs})

    data = {"@context": "https://schema.org", "@graph": grafo}
    return (
        '<script type="application/ld+json">'
        + json.dumps(data, ensure_ascii=False, indent=2)
        + "</script>"
    )


def montar(p, com_schema=False):
    """Monta o HTML final.

    com_schema=False é o padrão por decisão editorial (§7.3): schema só sai
    quando o editor pede explicitamente e valida tecnicamente.
    """
    partes = [
        bloco_autor(p),
        bloco_transparencia(),
        f'<h2 class="wp-block-heading">{p["nome"]} Vale a Pena? Análise Completa 2026</h2>',
        "\n\n".join(f'<p class="wp-block-paragraph">{x}</p>' for x in p["introducao"]),
        card_compra(p),
        '<hr class="wp-block-separator has-alpha-channel-opacity"/>',
        lista_pros_contras(p["pros"], p["contras"]),
        tabela_specs(p["specs"]),
        secoes_analise(p["secoes"]),
        tabela_comparativo(p.get("comparativo")),
        para_quem(p["para_quem_sim"], p["para_quem_nao"]),
        faq(p["faq"]),
        veredito(p),
        card_compra(p, destaque=True, titulo="🏆 Pronto para Comprar? Melhores Ofertas"),
        fontes(p["fontes"]),
        schema_jsonld(p) if com_schema else "",
    ]
    return "\n\n\n".join(x for x in partes if x)


def main():
    ap = argparse.ArgumentParser(description="Gera artigo HTML no padrão Curadoria Prime")
    ap.add_argument("json", help="arquivo JSON com os dados do produto")
    ap.add_argument("-o", "--output", default="artigo.html", help="arquivo de saída")
    ap.add_argument(
        "--schema",
        action="store_true",
        help="emite o JSON-LD (Review + FAQPage). Desligado por padrão: regras "
        "editoriais §7.3 — schema só quando solicitado e validado. Exige a "
        "chave 'editor' no JSON (§2.6).",
    )
    a = ap.parse_args()

    with open(a.json, encoding="utf-8") as f:
        p = json.load(f)

    try:
        html = montar(p, com_schema=a.schema)
    except ValueError as e:
        sys.exit(f"❌ {e}")
    with open(a.output, "w", encoding="utf-8") as f:
        f.write(html)

    palavras = len(
        __import__("re").sub("<[^>]+>", " ", html).split()
    )
    print(f"✅ Gerado: {a.output}")
    print(f"   {len(html):,} chars | ~{palavras:,} palavras")
    if palavras < 2500:
        print(
            f"   ⚠️  {palavras:,} palavras — o padrão do site é ~3.000. "
            "Expanda as seções de análise."
        )
    if a.schema:
        print(f"   📐 JSON-LD emitido, assinado por: {p.get('editor') or p.get('revisado_por')}")
    else:
        print("   ℹ️  Sem JSON-LD (padrão §7.3). Use --schema quando for validar e publicar.")
    print(f"\n   Título sugerido: {p.get('titulo_seo', p['nome'])}")
    print(f"   Slug sugerido:   {p.get('slug', '')}")


if __name__ == "__main__":
    main()
