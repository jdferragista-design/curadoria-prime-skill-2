#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
gerar_artigo.py v2.0 — Gerador de artigos HTML no padrão Golden Curadoria Prime
Tipos: LISTA, REVIEW, VS.
Uso: python3 gerar_artigo.py exemplo.json -o artigo.html [--schema] [--tipo lista|review|vs]
"""

import json, argparse, sys, re
from datetime import datetime, date

# --- Paleta canônica ---
C = {
    "roxo": "#5a4fcf", "roxo_esc": "#2d3277", "tinta": "#1a1a2e",
    "cinza": "#7c7c9a", "cinza_claro": "#e2e2f0", "borda": "#e9ecef",
    "fundo": "#f8f8ff",
    "amazon_a": "#FF9900", "amazon_b": "#FFB84D", "amazon_tx": "#232F3E",
    "meli_a": "#3485DB", "meli_b": "#5BA3E8",
    "verde": "#16a34a", "verde_bg": "#f0fdf4",
    "vermelho": "#dc2626", "vermelho_bg": "#fef2f2",
    "hero_bg": "#1a1a2e", "hero_bg2": "#16213e",
    "grad_roxo": "linear-gradient(135deg,#5a4fcf 0%,#764ba2 100%)",
}

# --- Helpers ---
def _iso(data_br):
    if not data_br: return date.today().isoformat()
    try: return datetime.strptime(data_br.strip(), "%d/%m/%Y").strftime("%Y-%m-%d")
    except ValueError: return date.today().isoformat()

def _hoje_br(): return date.today().strftime("%d/%m/%Y")
def _data_br(data): return data if data else _hoje_br()

def _wp_html(body): return f"<!-- wp:html -->\n{body}\n<!-- /wp:html -->"
def _wp_heading(text, level=2):
    return f'<!-- wp:heading {{"className":"wp-block-heading"}} -->\n<h{level} class="wp-block-heading">{text}</h{level}>\n<!-- /wp:heading -->'
def _wp_paragraph(text):
    return f'<!-- wp:paragraph {{"className":"wp-block-paragraph"}} -->\n<p class="wp-block-paragraph">{text}</p>\n<!-- /wp:paragraph -->'
def _wp_separator(): return '<!-- wp:separator -->\n<hr class="wp-block-separator has-alpha-channel-opacity"/>\n<!-- /wp:separator -->'

def _hero_badge(text):
    return f'<span style="background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.3);padding:6px 14px;border-radius:100px;font-size:13px;font-weight:bold;">{text}</span>'

def _botao_amazon(url):
    return (f'<a style="flex:1;min-width:140px;background:linear-gradient(135deg,{C["amazon_a"]} 0%,{C["amazon_b"]} 100%);'
            f'color:{C["amazon_tx"]};text-decoration:none;padding:14px 20px;border-radius:10px;font-weight:bold;'
            f'text-align:center;font-size:14px;box-shadow:0 2px 8px rgba(255,153,0,.3);" href="{url}" '
            f'target="_blank" rel="sponsored noopener noreferrer nofollow">Ver na Amazon</a>')

def _botao_ml(url):
    return (f'<a style="flex:1;min-width:140px;background:linear-gradient(135deg,{C["meli_a"]} 0%,{C["meli_b"]} 100%);'
            f'color:#fff;text-decoration:none;padding:14px 20px;border-radius:10px;font-weight:bold;'
            f'text-align:center;font-size:14px;box-shadow:0 2px 8px rgba(52,133,219,.3);" href="{url}" '
            f'target="_blank" rel="sponsored noopener noreferrer nofollow">Ver no Mercado Livre</a>')

def _botoes_produto(links):
    out = []
    if links.get("amazon"): out.append(_botao_amazon(links["amazon"]))
    if links.get("mercadolivre"): out.append(_botao_ml(links["mercadolivre"]))
    return "\n".join(out)

# --- Blocos compartilhados ---
def bloco_meta_seo(p):
    titulo = p.get("titulo") or p.get("produto", {}).get("nome", "")
    return (f'<!-- wp:html -->\n<!--\nMETA SEO\nTitulo: {p.get("titulo_seo", titulo)}\n'
            f'Descricao: {p.get("meta_description", "")}\nURL: {p.get("slug", "")}\n'
            f'Atualizado: {_data_br(p.get("data_verificacao"))}\n-->\n<!-- /wp:html -->')

def bloco_hero(p):
    k = p.get("kicker", "Guia Atualizado")
    badges = "\n".join(_hero_badge(b) for b in p.get("hero_badges", []))
    return _wp_html(f'<div style="background:linear-gradient(135deg,{C["hero_bg"]} 0%,{C["hero_bg2"]} 100%);'
                    f'color:#fff;padding:28px 30px;border-radius:14px;margin-bottom:30px;font-size:15.5px;line-height:1.75;">'
                    f'<div style="display:inline-block;background:rgba(255,255,255,.2);border:1px solid rgba(255,255,255,.3);'
                    f'font-size:11px;font-weight:bold;letter-spacing:.1em;text-transform:uppercase;padding:4px 12px;'
                    f'border-radius:100px;margin-bottom:12px;">{k}</div>'
                    f'<p style="margin:0 0 16px;font-size:20px;font-weight:700;color:#fff;">{p["titulo"]}</p>'
                    f'<p style="margin:0 0 16px;color:#e2e2f0;font-size:15px;line-height:1.7;">{p.get("descricao_hero","")}</p>'
                    f'<div style="display:flex;flex-wrap:wrap;gap:10px;">{badges}</div></div>')

def bloco_transparencia():
    return _wp_html(f'<div style="background:{C["fundo"]};border:1px solid {C["cinza_claro"]};border-radius:10px;'
                    f'padding:14px 20px;margin-bottom:28px;font-size:13.5px;color:{C["cinza"]};line-height:1.65;">'
                    f'Transparência: este guia contem links de afiliados (Amazon e Mercado Livre). Se voce comprar por eles,'
                    f' recebemos uma comissão sem custo adicional para voce. O ranking e editorial e nao e influenciado pelas lojas.'
                    f' <a href="https://curadoriaprime.com/transparencia-curadoria-prime/" style="color:{C["roxo"]};text-decoration:underline;font-weight:600;">Saiba mais</a></div>')

def bloco_metodologia():
    return _wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-left:4px solid {C["roxo"]};'
                    f'border-radius:12px;padding:18px 22px;margin-bottom:28px;box-shadow:0 2px 8px rgba(90,79,207,.07);">'
                    f'<p style="font-size:14px;font-weight:bold;color:{C["tinta"]};margin:0 0 12px;text-transform:uppercase;'
                    f'letter-spacing:.06em;">Metodologia deste guia</p>'
                    f'<p style="margin:0 0 12px;color:#4a4a68;font-size:14.5px;line-height:1.7;">Cada modelo da lista passou pela '
                    f'<strong style="color:{C["tinta"]};">Regua Curadoria Prime v2.0</strong>:</p>'
                    f'<p style="margin:0 0 8px;padding:8px 0 8px 28px;position:relative;color:#4a4a68;border-bottom:1px solid #f0f0f8;'
                    f'font-size:15px;"><span style="position:absolute;left:0;color:{C["roxo"]};font-weight:800;">V</span>'
                    f'<strong style="color:{C["tinta"]};">Especificações oficiais</strong> dos fabricantes</p>'
                    f'<p style="margin:0 0 8px;padding:8px 0 8px 28px;position:relative;color:#4a4a68;border-bottom:1px solid #f0f0f8;'
                    f'font-size:15px;"><span style="position:absolute;left:0;color:{C["roxo"]};font-weight:800;">V</span>'
                    f'<strong style="color:{C["tinta"]};">Testes publicados por canais especializados</strong></p>'
                    f'<p style="margin:0 0 8px;padding:8px 0 8px 28px;position:relative;color:#4a4a68;border-bottom:1px solid #f0f0f8;'
                    f'font-size:15px;"><span style="position:absolute;left:0;color:{C["roxo"]};font-weight:800;">V</span>'
                    f'<strong style="color:{C["tinta"]};">Leitura das avaliacoes publicadas por compradores</strong></p>'
                    f'<p style="margin:0 0 8px;padding:8px 0 8px 28px;position:relative;color:#4a4a68;font-size:15px;">'
                    f'<span style="position:absolute;left:0;color:{C["roxo"]};font-weight:800;">V</span>'
                    f'<strong style="color:{C["tinta"]};">Comparativo de mercado</strong> e síntese independente</p>'
                    f'<p style="margin:12px 0 0;color:{C["cinza"]};font-size:13.5px;line-height:1.7;">'
                    f'<strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. A Curadoria Prime não testou estas unidades fisicamente.'
                    f' <a href="https://curadoriaprime.com/sobre-a-curadoria-prime/" style="color:{C["roxo"]};text-decoration:underline;font-weight:600;">Entenda nossa metodologia</a></p></div>')

def bloco_resposta_rapida(p):
    items = p.get("resposta_rapida", [])
    if not items: return ""
    lis = "\n".join(f'<li><strong>{i["rotulo"]}:</strong> {i["texto"]}</li>' for i in items)
    data = _data_br(p.get("data_verificacao"))
    return _wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-radius:12px;padding:18px 22px;margin-bottom:28px;">'
                    f'<p style="font-size:14px;font-weight:bold;color:{C["tinta"]};margin:0 0 12px;text-transform:uppercase;letter-spacing:.06em;">O veredito em 15 segundos (preços de {data}):</p>'
                    f'<ul style="margin:0;padding-left:20px;line-height:2;">{lis}</ul></div>')

def bloco_critérios(p):
    n = p.get("num_produtos", 5)
    return _wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-radius:12px;padding:18px 22px;margin-bottom:28px;">'
                    f'<p style="margin:0 0 12px;color:#4a4a68;font-size:15px;">Para entrar neste Top {n}, cada modelo foi avaliado nos mesmos seis critérios da Regua v2.0:</p>'
                    f'<ul style="margin:0;padding-left:20px;line-height:2;">'
                    f'<li><strong>Custo-benefício (30%):</strong> o que o produto entrega pelo preco praticado hoje</li>'
                    f'<li><strong>Satisfação verificada (25%):</strong> volume e teor das avaliacoes na Amazon e ML</li>'
                    f'<li><strong>Ficha técnica (20%):</strong> especificações oficiais comparadas aos rivais da faixa</li>'
                    f'<li><strong>Recursos e usabilidade (10%):</strong> recursos extras relevantes</li>'
                    f'<li><strong>Consenso técnico (10%):</strong> convergência entre reviews de especialistas</li>'
                    f'<li><strong>Confiança e suporte (5%):</strong> garantia, assistência e histórico da marca</li>'
                    f'</ul></div>')

def bloco_faq(p):
    faqs = p.get("faq", [])
    if not faqs: return ""
    cards = ""
    for i, q in enumerate(faqs, 1):
        cards += (f'<div style="background:#fff;border-radius:12px;margin-bottom:10px;border:1px solid {C["cinza_claro"]};'
                  f'overflow:hidden;box-shadow:0 2px 8px rgba(90,79,207,.07);">'
                  f'<p style="padding:16px 20px;font-size:15px;font-weight:bold;color:{C["roxo"]};margin:0;border-bottom:1px solid {C["cinza_claro"]};">{i}. {q["pergunta"]}</p>'
                  f'<p style="padding:14px 20px;color:#4a4a68;font-size:15px;margin:0;line-height:1.7;">{q["resposta"]}</p></div>\n')
    return _wp_html(cards)

def bloco_conclusao(p):
    texto = p.get("conclusao", "")
    items = p.get("conclusao_items", [])
    if not texto and not items: return ""
    out = [_wp_heading(f"10. Conclusao: qual {p.get('categoria','produto')} escolher?")]
    if texto: out.append(_wp_paragraph(texto))
    if items:
        lis = "\n".join(f"<li>{i}</li>" for i in items)
        out.append(_wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-radius:12px;padding:18px 22px;margin-bottom:28px;">'
                            f'<ul style="margin:0;padding-left:20px;line-height:2;">{lis}</ul></div>'))
    return "\n\n".join(out)

def bloco_para_quem_nao(p):
    items = p.get("para_quem_nao", [])
    if not items: return ""
    lis = "\n".join(f"<li>{i}</li>" for i in items)
    return (_wp_heading("Para quem NÃO é (e o que evitar)") + "\n\n"
            + _wp_html(f'<div style="background:{C["vermelho_bg"]};border:1px solid #fecdd3;border-left:4px solid #e11d48;'
                       f'border-radius:8px;padding:16px 20px;margin-bottom:28px;">'
                       f'<p style="margin:0 0 10px;font-size:14.5px;color:#9f1239;line-height:1.7;">Não vale a pena para você se...</p>'
                       f'<ul style="margin:0;padding-left:20px;line-height:1.8;color:#9f1239;font-size:14.5px;">{lis}</ul></div>'))

def bloco_escolha_rapida(p):
    texto = p.get("escolha_rapida_texto", "")
    botoes = _botoes_produto(p.get("escolha_rapida_links", {}))
    if not texto and not botoes: return ""
    data = _data_br(p.get("data_verificacao"))
    return _wp_html(f'<div style="background:{C["grad_roxo"]};border-radius:14px;padding:28px 30px;margin-bottom:30px;text-align:center;">'
                    f'<p style="font-size:13px;font-weight:bold;text-transform:uppercase;letter-spacing:.08em;color:rgba(255,255,255,.8);margin:0 0 12px;">Escolha rapida</p>'
                    f'<p style="font-size:16px;color:#fff;margin:0 0 8px;">{texto}</p>'
                    f'<p style="font-size:12px;color:rgba(255,255,255,.5);margin:0 0 16px;">Preços verificados em {data} - sujeitos a alteracao.</p>'
                    f'<div style="display:flex;justify-content:center;flex-wrap:wrap;gap:12px;">{botoes}</div></div>')

def bloco_cluster_links(p):
    links = p.get("cluster_links", [])
    if not links: return ""
    lis = "\n".join(f'<li><a href="{l["url"]}" target="_blank" rel="noopener">{l["titulo"]}</a></li>' for l in links)
    cat = p.get("categoria", "Curadoria")
    return (_wp_heading(f"Analises completas do cluster de {cat}", level=3) + "\n\n"
            + _wp_html(f'<div style="background:#fff;border-left:4px solid {C["roxo"]};border-radius:10px;padding:18px 22px;margin:28px 0;box-shadow:0 2px 8px rgba(90,79,207,.08);">'
                       f'<ul style="margin:0;padding-left:20px;line-height:2;">{lis}</ul></div>'))

def bloco_fontes(p):
    fontes = p.get("fontes", [])
    if not fontes: return ""
    lis = "\n".join(f'<li><a href="{f["url"]}" target="_blank" rel="noopener">{f["titulo"]}</a></li>' for f in fontes)
    return (_wp_heading("Fontes consultadas", level=3) + "\n\n"
            + _wp_html(f'<div style="background:#f8f9fa;border-left:4px solid {C["roxo"]};padding:16px 20px;margin:24px 0;border-radius:6px;">'
                       f'<ul style="margin:0;padding-left:20px;line-height:1.9;font-size:14px;color:#4a4a68;">{lis}</ul></div>'))

def bloco_revisao(p):
    texto = p.get("revisao_texto", "")
    if not texto: return ""
    return _wp_html(f'<div style="background:{C["grad_roxo"]};color:rgba(255,255,255,.9);padding:18px 24px;border-radius:12px;">'
                    f'<p style="margin:0;font-size:13.5px;line-height:1.75;">{texto}</p></div>')

def bloco_byline(p):
    autor = p.get("autor", {})
    if not autor.get("nome"): return ""
    return _wp_html(f'<div style="display:flex;gap:16px;align-items:center;background:{C["fundo"]};border:1px solid {C["cinza_claro"]};'
                    f'border-radius:12px;padding:18px 20px;margin:28px 0 20px;">'
                    f'<img src="{autor.get("img","")}" alt="{autor.get("alt",autor["nome"])}" width="72" height="72" loading="lazy" decoding="async" style="width:72px;height:72px;border-radius:50%;object-fit:cover;flex-shrink:0;">'
                    f'<div style="font-size:13.5px;line-height:1.6;color:#4a4a68;">'
                    f'<strong style="font-size:14.5px;color:{C["tinta"]};">{autor["nome"]}</strong> - {autor.get("papel","Editor")}<br>'
                    f'<span style="color:{C["cinza"]};">{autor.get("bio","")}</span>'
                    f' <a href="{autor.get("social","#")}" rel="noopener" target="_blank" style="color:#1d4ed8;font-weight:600;text-decoration:none;">Seguir no X</a></div></div>')

# --- Blocos de produto (lista) ---
def bloco_produto(prod, idx, p):
    data = _data_br(p.get("data_verificacao"))
    medalhas = ["1", "2", "3", "4", "5", "6", "7"]
    medalha = medalhas[idx] if idx < len(medalhas) else f"{idx+1}."
    label = prod.get("rotulo", f"{idx+1} lugar")
    selo_preco = f'<span style="background:#f5f5fb;border:1px solid {C["cinza_claro"]};padding:6px 14px;border-radius:100px;font-size:13px;font-weight:bold;color:{C["tinta"]};">{medalha} {label}</span>'
    badge_preco = f'<span style="background:#f5f5fb;border:1px solid {C["cinza_claro"]};padding:6px 14px;border-radius:100px;font-size:13px;font-weight:bold;color:{C["tinta"]};">{prod["preco_label"]} verificado {data}</span>'

    img_html = ""
    if prod.get("img_url"):
        img_html = (f'<div style="margin-bottom:20px;"><img src="{prod["img_url"]}" style="width:100%;max-width:500px;height:auto;border-radius:12px;display:block;margin:0 auto;box-shadow:0 4px 16px rgba(90,79,207,.12);" alt="{prod.get("img_alt",prod["nome"])}" loading="lazy" decoding="async" width="758" height="505">'
                    f'<p style="text-align:center;font-size:12px;color:{C["cinza"]};margin:8px 0 0;">{prod.get("img_caption","")}</p></div>')

    specs = prod.get("specs", {})
    spec_rows = "\n".join(
        f'<tr><td style="padding:10px 14px;border-bottom:1px solid {C["cinza_claro"]};font-weight:600;width:40%;">{k}</td>'
        f'<td style="padding:10px 14px;border-bottom:1px solid {C["cinza_claro"]};">{v}</td></tr>'
        for k, v in specs.items()
    )
    ficha = ""
    if spec_rows:
        ficha = _wp_html(f'<div style="overflow-x:auto;border-radius:12px;box-shadow:0 6px 24px rgba(90,79,207,.12);margin-bottom:20px;">'
                         f'<table style="width:100%;border-collapse:collapse;font-size:14.5px;min-width:500px;">'
                         f'<thead><tr style="background:linear-gradient(135deg,{C["roxo"]},#764ba2);color:#fff;">'
                         f'<th style="padding:12px 16px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.06em;width:40%;">Especificacao</th>'
                         f'<th style="padding:12px 16px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.06em;">Detalhe</th></tr></thead>'
                         f'<tbody>{spec_rows}</tbody></table></div>')

    destaques = prod.get("destaques", [])
    destaques_html = ""
    if destaques:
        lis = "\n".join(f"<li>{d}</li>" for d in destaques)
        destaques_html = _wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-radius:12px;padding:18px 22px;margin-bottom:20px;"><ul style="margin:0;padding-left:20px;line-height:1.8;">{lis}</ul></div>')

    atencao = prod.get("atencao", [])
    atencao_html = ""
    if atencao:
        lis = "\n".join(f"<li>{a}</li>" for a in atencao)
        atencao_html = _wp_html(f'<div style="background:{C["vermelho_bg"]};border:1px solid #fecdd3;border-left:4px solid #e11d48;border-radius:8px;padding:16px 20px;margin-bottom:20px;">'
                                f'<h3 class="wp-block-heading" style="font-size:16px;color:#9f1239;margin:0 0 12px;">Contras e Pontos de Atenção</h3>'
                                f'<ul style="margin:0;padding-left:20px;line-height:1.8;color:#9f1239;font-size:14.5px;">{lis}</ul></div>')

    veredito_texto = prod.get("veredito", "")
    veredito_html = ""
    if veredito_texto:
        veredito_html = _wp_html(f'<div style="background:{C["verde_bg"]};border-left:4px solid #22c55e;border-radius:8px;padding:16px 20px;margin-bottom:20px;">'
                                 f'<p style="font-size:15px;font-weight:bold;color:#14532d;margin:0 0 8px;">Veredito:</p>'
                                 f'<p style="color:#166534;font-size:14.5px;margin:0;line-height:1.7;">{veredito_texto}</p></div>')

    link_review = ""
    if prod.get("review_url"):
        link_review = _wp_paragraph(f'Leia a <a href="{prod["review_url"]}"><strong>análise completa do {prod["nome"]}</strong></a>.')

    botoes = _botoes_produto(prod.get("links", {}))
    box_compra = ""
    if botoes:
        buy_info = prod.get("buy_info", "")
        box_compra = _wp_html(f'<div style="background:{C["fundo"]};border-radius:12px;padding:20px 22px;margin-bottom:36px;text-align:center;">'
                              f'<p style="font-size:13px;font-weight:bold;text-transform:uppercase;letter-spacing:.08em;color:{C["cinza"]};margin:0 0 14px;">{prod["nome"]}</p>'
                              f'<p style="font-size:14px;color:#4a4a68;margin:0 0 12px;">{buy_info}</p>'
                              f'<div style="display:flex;justify-content:center;flex-wrap:wrap;gap:12px;">{botoes}</div>'
                              f'<p style="font-size:12px;color:#9c9cb8;margin:10px 0 0;">Marketplaces alteram preços sem aviso - confirme o valor na loja.</p></div>')

    secoes = [
        _wp_heading(f"{idx+3}. {medalha} {prod['nome']} - {prod.get('subtitulo', label)}"),
        _wp_html(f'<div style="display:flex;flex-wrap:wrap;gap:10px;margin-bottom:16px;">{selo_preco}\n{badge_preco}</div>'),
        img_html,
        _wp_paragraph(prod.get("descricao", "")),
        _wp_heading("Ficha técnica", level=3) if spec_rows else "",
        ficha,
        _wp_heading("O que ele faz de melhor", level=3) if destaques else "",
        destaques_html,
        atencao_html,
        veredito_html,
        link_review,
        box_compra,
    ]
    return "\n\n".join(s for s in secoes if s)

def bloco_tabela_comparativa(p):
    produtos = p.get("produtos", [])
    if not produtos: return ""
    campos = p.get("tabela_campos", ["Preco", "Rating", "Indicado para"])
    cabecalho = "".join(
        f'<th style="padding:12px 14px;text-align:left;font-size:12px;text-transform:uppercase;letter-spacing:.06em;">{c}</th>'
        for c in ["Produto"] + campos
    )
    linhas = ""
    for i, prod in enumerate(produtos):
        bg = "#fff" if i % 2 == 0 else "#fafaff"
        vals = [prod.get("nome", "")]
        for campo in campos:
            vals.append(prod.get("tabela", {}).get(campo, "-"))
        tds = "".join(f'<td style="padding:11px 14px;border-bottom:1px solid {C["cinza_claro"]};">{v}</td>' for v in vals)
        linhas += f'<tr style="background:{bg};">{tds}</tr>\n'
    footnote = p.get("tabela_footnote", f"Preços verificados em {_data_br(p.get('data_verificacao'))} - sujeitos a alteracao.")
    return _wp_html(f'<div style="overflow-x:auto;border-radius:12px;box-shadow:0 6px 24px rgba(90,79,207,.12);margin-bottom:12px;">'
                    f'<table style="width:100%;border-collapse:collapse;font-size:14px;min-width:640px;">'
                    f'<thead><tr style="background:linear-gradient(135deg,{C["roxo"]},#764ba2);color:#fff;">{cabecalho}</tr></thead>'
                    f'<tbody>{linhas}</tbody></table>'
                    f'<p style="margin:8px 0 0;font-size:12.5px;color:{C["cinza"]};">{footnote}</p></div>')

# --- JSON-LD para lista ---
def schema_jsonld_lista(p):
    data_pub = _iso(p.get("data_publicacao"))
    data_mod = _iso(p.get("data_verificacao"))
    url = f"https://curadoriaprime.com/{p.get('slug', '')}/"
    autor = (p.get("autor", {}) or {}).get("nome", "Cristiano Martins")
    hero_img = p.get("hero_img", "https://curadoriaprime.com/wp-content/uploads/2026/08/placeholder.jpg")
    graph = [{"@type": "Article", "headline": p.get("titulo_seo", p["titulo"]), "image": hero_img,
              "datePublished": data_pub, "dateModified": data_mod, "inLanguage": "pt-BR",
              "author": {"@type": "Person", "name": autor, "url": "https://curadoriaprime.com/sobre-a-curadoria-prime/"},
              "publisher": {"@type": "Organization", "name": "Curadoria Prime", "url": "https://curadoriaprime.com/",
                            "logo": {"@type": "ImageObject", "url": "https://curadoriaprime.com/wp-content/uploads/2026/08/logo-curadoria-prime.png"}},
              "mainEntityOfPage": url, "description": p.get("meta_description", "")}]
    produtos = p.get("produtos", [])
    if produtos:
        graph.append({"@type": "ItemList", "name": f"Top {len(produtos)} {p.get('categoria','produtos')}",
                       "numberOfItems": len(produtos), "itemListOrder": "https://schema.org/ItemListOrderAscending",
                       "itemListElement": [{"@type": "ListItem", "position": i+1, "item": {"@type": "Product", "name": pr["nome"]}}
                                           for i, pr in enumerate(produtos)]})
    faqs = p.get("faq", [])
    if faqs:
        graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q["pergunta"],
                        "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}} for q in faqs]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": 1, "name": "Inicio", "item": "https://curadoriaprime.com/"},
        {"@type": "ListItem", "position": 2, "name": p.get("categoria", "Reviews"), "item": f"https://curadoriaprime.com/{p.get('categoria_url','')}/"},
        {"@type": "ListItem", "position": 3, "name": p.get("titulo_seo", p["titulo"])}]})
    return _wp_html(f'<script type="application/ld+json">\n{json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, indent=2)}\n</script>')

# --- Montagem dos 3 tipos ---
def montar_lista(p, com_schema=False):
    partes = [
        bloco_meta_seo(p), bloco_hero(p), _wp_separator(),
        bloco_metodologia(), bloco_transparencia(),
        _wp_heading(f"1. Resposta Rápida: qual {p.get('categoria','produto')} comprar para cada perfil"),
        bloco_resposta_rapida(p),
        _wp_heading("2. Critérios de avaliação"), bloco_critérios(p),
    ]
    for i, prod in enumerate(p.get("produtos", [])):
        partes.append(bloco_produto(prod, i, p))
    partes.append(_wp_heading("8. Tabela comparativa lado a lado"))
    partes.append(bloco_tabela_comparativa(p))
    partes.append(bloco_para_quem_nao(p))
    partes.append(_wp_heading("9. Perguntas Frequentes"))
    partes.append(bloco_faq(p))
    partes.append(bloco_conclusao(p))
    partes.append(bloco_escolha_rapida(p))
    partes.append(bloco_cluster_links(p))
    partes.append(bloco_fontes(p))
    partes.append(bloco_revisao(p))
    partes.append(bloco_byline(p))
    if com_schema: partes.append(schema_jsonld_lista(p))
    return "\n\n\n".join(p for p in partes if p)

def montar_review(p, com_schema=False):
    prod = p.get("produto", p)
    autor_nome = (p.get("autor", {}) or {}).get("nome", "Equipe Curadoria Prime")
    data = _data_br(p.get("data_verificacao"))
    autor_bloco = _wp_html(f'<div style="background:{C["fundo"]};border:1px solid {C["cinza_claro"]};border-left:4px solid {C["roxo"]};'
                           f'border-radius:12px;padding:18px 22px;margin-bottom:28px;">'
                           f'<p style="font-size:14px;font-weight:bold;color:{C["tinta"]};margin:0 0 12px;">Por {autor_nome} - Análise verificada em {data}</p>'
                           f'<p style="margin:0;color:#4a4a68;font-size:14px;"><strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. <strong>A Curadoria Prime não testou esta unidade fisicamente.</strong>'
                           f' <a href="https://curadoriaprime.com/isencao-de-responsabilidade-curadoria-prime/" style="color:{C["roxo"]};text-decoration:underline;">Como avaliamos</a></p></div>')
    partes = [bloco_meta_seo(p), autor_bloco, bloco_transparencia(),
              _wp_heading(f"{prod.get('nome','Produto')} Vale a Pena? Análise Completa 2026")]
    for par in prod.get("introducao", []):
        partes.append(_wp_paragraph(par))
    if prod.get("links"):
        links = prod.get("links", {})
        botoes = _botoes_produto(links)
        if botoes:
            selo = ""
            if prod.get("nota") and prod.get("nota") >= 7:
                selo = f'<span style="background:linear-gradient(135deg,{C["vermelho"]} 0%,#991b1b 100%);color:#fff;padding:4px 12px;border-radius:20px;font-size:13px;font-weight:800;white-space:nowrap;">Recomendado 2026</span>'
            aval = f'R$ {prod["preco"]}' if prod.get("preco") else ""
            if prod.get("avaliacoes"): aval += f' +{prod["avaliacoes"]} avaliacoes'
            partes.append(_wp_html(f'<div style="background:#fff;border:1px solid {C["cinza_claro"]};border-radius:20px;padding:35px 25px;margin-top:40px;box-shadow:0 4px 20px rgba(0,0,0,.05);">'
                                   f'<h3 style="text-align:center;color:{C["roxo_esc"]};font-size:22px;margin:0 0 30px 0;">Onde Comprar: Melhores Preços de Hoje</h3>'
                                   f'<div style="background:#fff;border:2px solid {C["vermelho"]};border-radius:14px;padding:20px;margin-bottom:18px;">'
                                   f'<div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:15px;">{selo}'
                                   f'<span style="font-weight:bold;color:#1a1f36;font-size:17px;">{prod["nome"]} <span style="font-weight:400;color:#888;font-size:14px;">{aval}</span></span></div>'
                                   f'<div style="display:flex;gap:12px;flex-wrap:wrap;justify-content:center;">{botoes}</div>'
                                   f'<p style="text-align:center;font-size:12px;color:#888;margin:12px 0 0;">{" . ".join(prod.get("selos",[]))}</p></div>'
                                   f'<p style="text-align:center;font-size:12px;color:#999;margin:0;">Preços verificados em {data} e sujeitos a alteracao sem aviso previo.</p></div>'))
    if prod.get("pros") or prod.get("contras"):
        li_p = "\n".join(f"<li>{x}</li>" for x in prod.get("pros",[]))
        li_c = "\n".join(f"<li>{x}</li>" for x in prod.get("contras",[]))
        partes.append(_wp_heading("Prós e Contras"))
        partes.append(_wp_html(f'<div style="display:flex;gap:20px;flex-wrap:wrap;margin:24px 0;">'
                               f'<div style="flex:1;min-width:260px;background:{C["verde_bg"]};border-left:4px solid {C["verde"]};border-radius:8px;padding:18px 22px;">'
                               f'<h3 style="margin-top:0;color:#15803d;font-size:18px;">Pontos Positivos</h3>'
                               f'<ul style="margin:0;padding-left:20px;line-height:1.8;">{li_p}</ul></div>'
                               f'<div style="flex:1;min-width:260px;background:{C["vermelho_bg"]};border-left:4px solid {C["vermelho"]};border-radius:8px;padding:18px 22px;">'
                               f'<h3 style="margin-top:0;color:#b91c1c;font-size:18px;">Contras e Pontos de Atenção</h3>'
                               f'<ul style="margin:0;padding-left:20px;line-height:1.8;">{li_c}</ul></div></div>'))
    if prod.get("specs"):
        specs = prod.get("specs", {})
        linhas = "\n".join(f'<tr><td style="padding:10px 14px;border-bottom:1px solid {C["cinza_claro"]};font-weight:600;width:38%;">{k}</td>'
                           f'<td style="padding:10px 14px;border-bottom:1px solid {C["cinza_claro"]};">{v}</td></tr>' for k,v in specs.items())
        partes.append(_wp_heading("Especificações Técnicas Completas"))
        partes.append(_wp_html(f'<figure class="wp-block-table has-fixed-layout"><table><tbody>{linhas}</tbody></table></figure>'))
    for sec in prod.get("secoes", []):
        partes.append(_wp_heading(sec.get("titulo","")))
        for par in sec.get("paragrafos",[]):
            partes.append(_wp_paragraph(par))
    if prod.get("comparativo"):
        comp = prod["comparativo"]
        cabec = "".join(f'<th style="padding:12px 14px;background:{C["roxo_esc"]};color:#fff;text-align:left;">{c}</th>' for c in comp["colunas"])
        trs = ""
        for i, linha in enumerate(comp["linhas"]):
            bg = "#fff" if i % 2 == 0 else "#fafaff"
            tds = "".join(f'<td style="padding:11px 14px;border-bottom:1px solid {C["cinza_claro"]};">{c}</td>' for c in linha)
            trs += f'<tr style="background:{bg};">{tds}</tr>\n'
        partes.append(_wp_html(f'<figure class="wp-block-table"><table><thead><tr>{cabec}</tr></thead><tbody>{trs}</tbody></table></figure>'))
    if prod.get("para_quem_sim") or prod.get("para_quem_nao"):
        li_s = "\n".join(f"<li>{x}</li>" for x in prod.get("para_quem_sim",[]))
        li_n = "\n".join(f"<li>{x}</li>" for x in prod.get("para_quem_nao",[]))
        partes.append(_wp_heading("Para Quem É / Para Quem NÃO É"))
        partes.append(_wp_html(f'<h3 class="wp-block-heading">SIM - Vale a pena para voce se...</h3>'
                               f'<ul style="line-height:1.9;">{li_s}</ul>'
                               f'<h3 class="wp-block-heading">NÃO - Não vale a pena se...</h3>'
                               f'<ul style="line-height:1.9;">{li_n}</ul>'))
    if prod.get("faq"):
        partes.append(_wp_heading("Perguntas Frequentes"))
        partes.append(bloco_faq(prod))
    if prod.get("veredito") or prod.get("nota"):
        partes.append(_wp_heading(f"Veredito Final: {prod['nome']} Vale a Pena em 2026?"))
        if prod.get("nota"):
            nota = prod["nota"]
            cor = C["verde"] if nota >= 8 else ("#f59e0b" if nota >= 7 else C["vermelho"])
            partes.append(_wp_html(f'<div style="background:linear-gradient(135deg,{C["fundo"]} 0%,#eef0ff 100%);border-radius:16px;padding:28px;margin:24px 0;text-align:center;">'
                                   f'<div style="font-size:52px;font-weight:800;color:{cor};line-height:1;">{nota}<span style="font-size:26px;color:#999;">/10</span></div>'
                                   f'<p style="margin:10px 0 0;color:{C["cinza"]};font-size:14px;font-weight:600;">Nota Curadoria Prime</p></div>'))
        for par in prod.get("veredito", []):
            partes.append(_wp_paragraph(par))
    partes.append(bloco_fontes(p))
    partes.append(bloco_byline(p))
    if com_schema:
        editor = (p.get("autor", {}) or {}).get("nome") or p.get("editor") or p.get("revisado_por")
        if not editor:
            print("AVISO: --schema pedido mas falta 'autor.nome' ou 'editor' no JSON. Schema omitido.")
        else:
            prod_nome = prod.get("nome", "Produto")
            marca = prod.get("marca", "")
            review = {"@type": "Review", "itemReviewed": {"@type": "Product", "name": prod_nome, "brand": {"@type": "Brand", "name": marca}},
                      "author": {"@type": "Person", "name": editor}, "publisher": {"@type": "Organization", "name": "Curadoria Prime"},
                      "reviewAspect": "Especificações oficiais do fabricante, testes independentes publicados e relatos de compradores",
                      "datePublished": _iso(p.get("data_publicacao"))}
            if prod.get("nota") is not None:
                review["reviewRating"] = {"@type": "Rating", "ratingValue": prod["nota"], "bestRating": 10, "worstRating": 0}
            grafo = [review]
            if prod.get("faq"):
                grafo.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q["pergunta"],
                              "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}} for q in prod["faq"]]})
            partes.append(_wp_html(f'<script type="application/ld+json">\n{json.dumps({"@context":"https://schema.org","@graph":grafo}, ensure_ascii=False, indent=2)}\n</script>'))
    return "\n\n".join(partes)

def montar_vs(p, com_schema=False):
    pa, pb = p["produto_a"], p["produto_b"]
    autor_nome = (p.get("autor", {}) or {}).get("nome", "Equipe Curadoria Prime")
    data = _data_br(p.get("data_verificacao"))
    hero_grad = f"linear-gradient(135deg,{p.get('hero_brand_primary','#1428A0')} 0%,{p.get('hero_brand_secondary','#0a1550')} 100%)"
    accent = p.get("hero_brand_accent", "#fde68a")
    partes = [
        bloco_meta_seo(p),
        _wp_html(hero_grad),
        _wp_html(f'<div style="background:{C["fundo"]};border:1px solid {C["cinza_claro"]};border-left:4px solid {C["roxo"]};'
                 f'border-radius:12px;padding:18px 22px;margin-bottom:28px;">'
                 f'<p style="font-size:14px;font-weight:bold;color:{C["tinta"]};margin:0 0 12px;">Por {autor_nome} - Análise verificada em {data}</p>'
                 f'<p style="margin:0;color:#4a4a68;font-size:14px;"><strong>Tipo de análise:</strong> pesquisa editorial baseada em especificações oficiais, testes independentes e relatos publicados por compradores. <strong>Não testamos estas unidades fisicamente.</strong>'
                 f' <a href="https://curadoriaprime.com/isencao-de-responsabilidade-curadoria-prime/" style="color:{C["roxo"]};text-decoration:underline;">Como avaliamos</a></p></div>'),
        bloco_transparencia(),
    ]
    for par in p.get("introducao", []): partes.append(_wp_paragraph(par))
    # Secoes de analise (profundidade editorial)
    for sec in p.get("secoes_analise", []):
        partes.append(_wp_heading(sec.get("titulo", "")))
        for par in sec.get("paragrafos", []):
            partes.append(_wp_paragraph(par))
    if p.get("resposta_rapida_custo") or p.get("resposta_rapida_desempenho"):
        partes.append(_wp_heading("Resposta rapida: qual escolher?"))
        partes.append(_wp_html(f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:28px;">'
                               f'<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:12px;padding:18px;font-size:14px;line-height:1.6;">'
                               f'<p style="margin:0 0 8px;font-size:15px;font-weight:700;color:#166534;">Melhor custo-benefício</p>'
                               f'<p>{p.get("resposta_rapida_custo","")}</p></div>'
                               f'<div style="background:#eff6ff;border:2px solid #3b82f6;border-radius:12px;padding:18px;font-size:14px;line-height:1.6;">'
                               f'<p style="margin:0 0 8px;font-size:15px;font-weight:700;color:#1e40af;">Melhor desempenho</p>'
                               f'<p>{p.get("resposta_rapida_desempenho","")}</p></div></div>'))
    # Tabela
    header = p.get("tabela", {}).get("header", "linear-gradient(135deg,#1428A0,#0a1550)")
    linhas = p.get("tabela", {}).get("linhas", [])
    rows = "\n".join(
        f'<tr style="background:{"#fff" if i%2==0 else "#f8fafc"};">'
        + "".join(f'<td style="padding:12px 14px;{"text-align:left;" if j==0 else "text-align:center;"}">{c}</td>' for j, c in enumerate(linha))
        + f'</tr>'
        for i, linha in enumerate(linhas)
    )
    partes.append(_wp_heading(f"Tabela comparativa: {pa['nome']} vs {pb['nome']}"))
    partes.append(_wp_paragraph(f"Dados verificados em {data}"))
    partes.append(_wp_html(f'<div style="overflow-x:auto;margin-bottom:28px;"><table style="width:100%;border-collapse:collapse;font-size:13.5px;min-width:640px;">'
                           f'<thead><tr style="background:{header};color:#fff;">'
                           f'<th style="padding:12px 14px;text-align:left;">Criterio</th>'
                           f'<th style="padding:12px 14px;text-align:center;">{pa["nome"]}</th>'
                           f'<th style="padding:12px 14px;text-align:center;">{pb["nome"]}</th></tr></thead>'
                           f'<tbody>{rows}</tbody></table></div>'))
    # Produto A
    for prod, nome_key in [(pa, "a"), (pb, "b")]:
        pros = "\n".join(f'<li style="margin:0 0 8px 0;padding-left:24px;position:relative;"><span style="position:absolute;left:0;color:#22c55e;font-weight:800;">V</span>{x}</li>' for x in prod.get("pros",[]))
        cons = "\n".join(f'<li style="margin:0 0 8px 0;padding-left:24px;position:relative;"><span style="position:absolute;left:0;color:#ef4444;font-weight:800;">X</span>{x}</li>' for x in prod.get("contras",[]))
        partes.append(_wp_heading(f"{prod['nome']} - nota {prod['nota']}/10"))
        partes.append(_wp_paragraph(prod.get("descricao","")))
        if prod.get("img"):
            partes.append(_wp_html(f'<figure style="margin:20px 0;text-align:center;"><img src="{prod["img"]}" alt="{prod.get("img_alt",prod["nome"])}" style="width:100%;max-width:600px;height:auto;border-radius:12px;display:block;margin:0 auto;" loading="lazy">'
                                   f'<figcaption style="font-size:12.5px;color:#888;text-align:center;margin-top:8px;">{prod.get("img_caption",prod["nome"])}</figcaption></figure>'))
        partes.append(_wp_html(f'<div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(300px,1fr));gap:20px;margin:25px 0;">'
                               f'<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:12px;padding:24px;">'
                               f'<h3 style="margin:0 0 16px 0;font-size:18px;color:#166534;">Pontos Positivos</h3>'
                               f'<ul style="list-style:none;padding:0;margin:0;">{pros}</ul></div>'
                               f'<div style="background:#fef2f2;border:2px solid #ef4444;border-radius:12px;padding:24px;">'
                               f'<h3 style="margin:0 0 16px 0;font-size:18px;color:#991b1b;">Contras e Pontos Negativos</h3>'
                               f'<ul style="list-style:none;padding:0;margin:0;">{cons}</ul></div></div>'))
        botoes = _botoes_produto(prod.get("links", {}))
        if botoes:
            partes.append(_wp_html(f'<div style="background:#f8fafc;border-radius:12px;padding:20px 22px;margin:20px 0 36px;text-align:center;">'
                                   f'<p style="font-size:13px;font-weight:bold;text-transform:uppercase;letter-spacing:.08em;color:#64748b;margin:0 0 14px;">{prod["nome"]} - melhores ofertas</p>'
                                   f'<div style="display:flex;justify-content:center;flex-wrap:wrap;gap:12px;">{botoes}</div>'
                                   f'<p style="font-size:12px;color:#9c9cb8;margin:10px 0 0;">Preços verificados em {data} - sujeitos a alteracao.</p></div>'))
    # Para quem
    quem_a = "\n".join(f"<li>{x}</li>" for x in pa.get("quem", []))
    quem_b = "\n".join(f"<li>{x}</li>" for x in pb.get("quem", []))
    if quem_a or quem_b:
        partes.append(_wp_heading(f"Compre o {pa['nome']} se... / Compre o {pb['nome']} se..."))
        partes.append(_wp_html(f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:28px;">'
                               f'<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:12px;padding:18px;">'
                               f'<h3 style="margin:0 0 12px 0;font-size:16px;color:#166534;">Compre o {pa["nome"]} se...</h3>'
                               f'<ul style="margin:0;padding-left:18px;font-size:14px;line-height:1.7;">{quem_a}</ul></div>'
                               f'<div style="background:#eff6ff;border:2px solid #3b82f6;border-radius:12px;padding:18px;">'
                               f'<h3 style="margin:0 0 12px 0;font-size:16px;color:#1e40af;">Compre o {pb["nome"]} se...</h3>'
                               f'<ul style="margin:0;padding-left:18px;font-size:14px;line-height:1.7;">{quem_b}</ul></div></div>'))
    # Para quem NÃO é (sinal de valor agregado)
    quem_nao = p.get("para_quem_nao", [])
    if quem_nao:
        lis = "\n".join(f"<li>{x}</li>" for i, x in enumerate(quem_nao))
        partes.append(_wp_heading("Para quem NÃO é (e o que evitar)"))
        partes.append(_wp_html(f'<div style="background:{C["vermelho_bg"]};border:1px solid #fecdd3;border-left:4px solid #e11d48;'
                               f'border-radius:8px;padding:16px 20px;margin-bottom:28px;">'
                               f'<p style="margin:0 0 10px;font-size:14.5px;color:#9f1239;line-height:1.7;">Não vale a pena para você se...</p>'
                               f'<ul style="margin:0;padding-left:20px;line-height:1.8;color:#9f1239;font-size:14.5px;">{lis}</ul></div>'))
    # Veredito
    nota_a, nota_b = pa.get("nota", 0), pb.get("nota", 0)
    v = pa if nota_a >= nota_b else pb
    out_v = pb if nota_a >= nota_b else pa
    partes.append(_wp_heading("Veredito Final: qual comprar?"))
    partes.append(_wp_html(f'<div style="display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-bottom:28px;">'
                           f'<div style="background:#f0fdf4;border:2px solid #22c55e;border-radius:12px;padding:18px;">'
                           f'<p style="margin:0 0 8px;font-size:15px;font-weight:700;color:#166534;">Vencedor: {v["nome"]}</p>'
                           f'<p style="font-size:14px;line-height:1.6;color:#166534;">{p.get("veredito_vencedor","")}</p></div>'
                           f'<div style="background:#eff6ff;border:2px solid #3b82f6;border-radius:12px;padding:18px;">'
                           f'<p style="margin:0 0 8px;font-size:15px;font-weight:700;color:#1e40af;">{out_v["nome"]} vale a pena se...</p>'
                           f'<p style="font-size:14px;line-height:1.6;color:#1e40af;">{p.get("veredito_perdedor","")}</p></div></div>'))
    # FAQ + fontes + byline
    if p.get("faq"):
        partes.append(_wp_heading("Perguntas Frequentes"))
        partes.append(bloco_faq(p))
    partes.append(bloco_fontes(p))
    partes.append(bloco_byline(p))
    if com_schema:
        graph = [{"@type": "Article", "headline": p.get("titulo_seo", p["titulo"]),
                  "datePublished": _iso(p.get("data_publicacao")), "dateModified": _iso(p.get("data_verificacao")), "inLanguage": "pt-BR",
                  "author": {"@type": "Person", "name": autor_nome, "url": "https://curadoriaprime.com/sobre-a-curadoria-prime/"},
                  "publisher": {"@type": "Organization", "name": "Curadoria Prime", "url": "https://curadoriaprime.com/"},
                  "mainEntityOfPage": f"https://curadoriaprime.com/{p.get('slug','')}/",
                  "description": p.get("meta_description", "")},
                 {"@type": "ItemList", "name": f"{pa['nome']} vs {pb['nome']}", "numberOfItems": 2,
                  "itemListElement": [{"@type": "ListItem", "position": 1, "item": {"@type": "Product", "name": pa["nome"]}},
                                      {"@type": "ListItem", "position": 2, "item": {"@type": "Product", "name": pb["nome"]}}]}]
        faqs = p.get("faq", [])
        if faqs:
            graph.append({"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q["pergunta"],
                            "acceptedAnswer": {"@type": "Answer", "text": q["resposta"]}} for q in faqs]})
        partes.append(_wp_html(f'<script type="application/ld+json">\n{json.dumps({"@context":"https://schema.org","@graph":graph}, ensure_ascii=False, indent=2)}\n</script>'))
    return "\n\n".join(partes)

# --- CLI ---
def main():
    ap = argparse.ArgumentParser(description="Gera artigo HTML no padrao Golden Curadoria Prime")
    ap.add_argument("json", help="arquivo JSON com os dados do artigo")
    ap.add_argument("-o", "--output", default="artigo.html", help="arquivo de saida")
    ap.add_argument("--schema", action="store_true", help="emite o JSON-LD @graph")
    ap.add_argument("--tipo", choices=["lista", "review", "vs"], default="lista", help="tipo de artigo")
    a = ap.parse_args()
    with open(a.json, encoding="utf-8") as f: p = json.load(f)
    if a.tipo == "lista": html = montar_lista(p, com_schema=a.schema)
    elif a.tipo == "review": html = montar_review(p, com_schema=a.schema)
    elif a.tipo == "vs": html = montar_vs(p, com_schema=a.schema)
    else: sys.exit(f"Tipo desconhecido: {a.tipo}")
    with open(a.output, "w", encoding="utf-8") as f: f.write(html)
    palavras = len(re.sub("<[^>]+>", " ", html).split())
    print(f"Gerado: {a.output}")
    print(f"   {len(html):,} chars | ~{palavras:,} palavras")
    if palavras < 1500: print(f"   ~{palavras:,} palavras - o padrao e ~3.000. Expanda as secoes.")
    if a.schema: print("   JSON-LD @graph emitido")
    else: print("   Sem JSON-LD (use --schema para ativar)")

if __name__ == "__main__":
    main()