#!/usr/bin/env python3
"""
reviews_ml.py — coleta avaliações REAIS do Mercado Livre (sem login).

Usa o endpoint público de catálogo que a própria vitrine do ML usa. Não requer
chave nem autenticação. Não inventa nada: só imprime o que a API devolve.

Uso:
    python3 tools/reviews_ml.py MLB38058572            # lista as 5 primeiras
    python3 tools/reviews_ml.py MLB38058572 --n 2      # só 2
    python3 tools/reviews_ml.py MLB38058572 --html     # gera bloco "O que dizem os compradores" (2 citações)

Onde achar o MLB_ID: na URL do produto https://www.mercadolivre.com.br/.../p/MLB38058572
"""
import argparse
import json
import urllib.request

BASE = "https://www.mercadolivre.com.br/noindex/catalog/reviews/{mlb}/search"
PARAMS = "noindex=true&siteId=MLB&limit={n}&offset=0&sort=relevancy"

UA = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126.0 Safari/537.36",
      "Accept-Language": "pt-BR,pt;q=0.9"}


def fetch(mlb: str, n: int = 5):
    url = f"{BASE.format(mlb=mlb)}?{PARAMS.format(n=n)}"
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r)


def linha(r):
    txt = r["comment"]["content"]["text"].replace("\n", " ").strip()
    br = r.get("country", "") != "Brasil"
    return {
        "nota": r.get("rating"),
        "data": r.get("date", ""),
        "pais": r.get("country", ""),
        "traduzido": br,
        "texto": txt,
    }


def to_html(mlb: str, nota_total: str, n: int = 2):
    """Gera o bloco MERCADO LIVRE (coluna) no padrão curadoria-reviews."""
    data = fetch(mlb, n + 4)  # pede a mais p/ descartar sem texto
    reviews = [linha(r) for r in data["reviews"] if linha(r)["texto"]][:n]
    out = ['<p style="margin:0 0 6px; font-size:12.5px; font-weight:700; color:#3485DB;">MERCADO LIVRE · {0}</p>'.format(nota_total)]
    for r in reviews:
        trad = " (traduzido)" if r["traduzido"] else ""
        out.append(
            '<p style="margin:0 0 8px; font-size:13px; color:#334155;">&#8220;{0}&#8221; '
            '<span style="color:#64748b;">— {1}&#9733;, {2}{3}</span></p>'
            .format(r["texto"], r["nota"], r["data"], trad)
        )
    return "\n".join(out)


def main():
    ap = argparse.ArgumentParser(description="Avaliações reais do Mercado Livre (sem login)")
    ap.add_argument("mlb", help="ID do catálogo (MLB...)")
    ap.add_argument("--n", type=int, default=5, help="quantas avaliações listar")
    ap.add_argument("--html", action="store_true", help="gerar bloco HTML (2 citações)")
    ap.add_argument("--nota", default="4,8★ (N)", help="nota/total p/ cabeçalho do bloco HTML")
    args = ap.parse_args()

    data = fetch(args.mlb, args.n + 4)
    reviews = [linha(r) for r in data["reviews"] if linha(r)["texto"]]

    if args.html:
        print(to_html(args.mlb, args.nota, n=args.n))
        return

    print(f"Total retornado: {len(reviews)}\n")
    for i, r in enumerate(reviews[: args.n], 1):
        trad = " (traduzido)" if r["traduzido"] else ""
        print(f"{i}. {r['nota']}★ · {r['data']}{trad}")
        print(f"   {r['texto'][:240]}")
        print()


if __name__ == "__main__":
    main()
