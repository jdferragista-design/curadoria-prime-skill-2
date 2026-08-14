#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ledger.py — acesso ao histórico de preços de primeira mão da Curadoria Prime.

O LEDGER.csv é o ativo proprietário mais valioso do projeto: é a única coisa
que nenhum concorrente pode copiar do site do fabricante. Este script existe
para que ele pare de ser editado à mão, onde erros silenciosos entram fácil
(data no formato errado, mesma captura duas vezes, preço inventado).

Arquivo:
    skills/curadoria-mercado/assets/historico-precos/LEDGER.csv

Regras que este script faz cumprir (references/historico-preco.md):
  - Uma linha = uma captura REAL, com data. Nunca uma estimativa.
  - Chave única: data + sku_id + loja + variante. Duplicata é recusada.
  - tipo=catalogo NÃO alimenta frase de tendência (catálogo /p/MLB… não é
    anúncio de vendedor — ver references/armadilhas-marketplace.md).
  - 1 captura  -> só "nesta data".
  - 2 capturas -> pode dizer "subiu"/"caiu".
  - 3+         -> pode dizer "faixa observada pela Curadoria".
  - NUNCA "menor preço da internet". Não temos como saber isso.

Uso:
    # registrar uma captura
    python3 ledger.py add --data 2026-08-13 --sku galaxy-tab-s10-fe \\
        --codigo SM-X520 --variante wifi-128 --loja amazon --tipo anuncio \\
        --pix 2789 --url "https://link.amazon/B0..." \\
        --artigo /tablets-para-volta-as-aulas-2026/

    # o que posso afirmar sobre este SKU hoje?
    python3 ledger.py frase --sku galaxy-tab-s10-fe --variante wifi-128

    # conferir a integridade do arquivo
    python3 ledger.py validar

    # ver o histórico
    python3 ledger.py ver --sku galaxy-tab-s10-fe
"""

import csv
import os
import sys
import argparse
from datetime import datetime, date

AQUI = os.path.dirname(os.path.abspath(__file__))
PADRAO = os.path.join(
    AQUI, "..", "skills", "curadoria-mercado", "assets", "historico-precos", "LEDGER.csv"
)

COLUNAS = [
    "data", "sku_id", "codigo", "variante", "loja", "tipo",
    "preco_pix", "preco_12x_parcela", "preco_12x_total", "de",
    "vendedor", "url", "artigo", "obs",
]

LOJAS = {"amazon", "ml", "samsung", "apple", "outro"}
TIPOS = {"anuncio", "catalogo", "tabela-marca"}
VENDEDORES = {"loja-samsung", "loja-oficial-apple", "terceiro", "internacional", ""}

# Idade a partir da qual uma captura não sustenta mais afirmação de preço.
DIAS_FRESCOR = 30


def caminho(args):
    return os.path.abspath(args.arquivo or PADRAO)


def ler(path):
    if not os.path.exists(path):
        sys.exit(f"❌ LEDGER não encontrado: {path}")
    with open(path, encoding="utf-8") as f:
        return list(csv.DictReader(f))


def escrever(path, linhas):
    with open(path, "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=COLUNAS)
        w.writeheader()
        for l in sorted(linhas, key=lambda x: (x["data"], x["sku_id"], x["loja"])):
            w.writerow({c: l.get(c, "") for c in COLUNAS})


def _num(v):
    if v in (None, ""):
        return None
    try:
        return float(str(v).replace(".", "").replace(",", ".")) if "," in str(v) else float(v)
    except ValueError:
        return None


# ─────────────────────────────────────────────────────────────── add ──

def cmd_add(args):
    path = caminho(args)
    linhas = ler(path)

    try:
        d = datetime.strptime(args.data, "%Y-%m-%d").date()
    except ValueError:
        sys.exit(f"❌ Data inválida: '{args.data}'. Use AAAA-MM-DD.")
    if d > date.today():
        sys.exit(f"❌ Data no futuro: {d}. Uma captura é um fato passado.")

    if args.loja not in LOJAS:
        sys.exit(f"❌ loja '{args.loja}' — use uma de: {', '.join(sorted(LOJAS))}")
    if args.tipo not in TIPOS:
        sys.exit(f"❌ tipo '{args.tipo}' — use uma de: {', '.join(sorted(TIPOS))}")
    if args.vendedor not in VENDEDORES:
        sys.exit(f"❌ vendedor '{args.vendedor}' — use: {', '.join(sorted(v for v in VENDEDORES if v))}")

    if not (args.pix or args.parcela):
        sys.exit("❌ Sem preço. Informe --pix e/ou --parcela.\n"
                 "   Campo vazio significa 'não havia esse preço no dia' — não invente.")

    if args.tipo == "anuncio" and args.loja == "ml" and "/p/MLB" in (args.url or ""):
        sys.exit("❌ URL de catálogo (/p/MLB…) marcada como 'anuncio'.\n"
                 "   Catálogo do Mercado Livre não é anúncio de vendedor — o preço\n"
                 "   muda de dono sem aviso. Use --tipo catalogo (ver\n"
                 "   references/armadilhas-marketplace.md).")

    chave = (args.data, args.sku, args.loja, args.variante)
    novo_preco = args.pix or args.total or ""
    for l in linhas:
        if (l["data"], l["sku_id"], l["loja"], l["variante"]) == chave:
            ant = l["preco_pix"] or l["preco_12x_total"] or ""
            if ant == novo_preco:
                sys.exit(f"❌ Captura idêntica já registrada para {chave} (R${ant}).\n"
                         "   Registrar duas vezes o mesmo preço infla o histórico.")
            if not args.recaptura:
                sys.exit(
                    f"❌ Já existe captura hoje para {chave}: R${ant} (nova: R${novo_preco}).\n"
                    "   Se o preço realmente mudou durante o dia, repita com --recaptura.\n"
                    "   Se você está corrigindo um erro de digitação, edite a linha existente.")
            print(f"   ℹ️  Recaptura intradiária: R${ant} → R${novo_preco}")

    nova = {
        "data": args.data, "sku_id": args.sku, "codigo": args.codigo,
        "variante": args.variante, "loja": args.loja, "tipo": args.tipo,
        "preco_pix": args.pix or "", "preco_12x_parcela": args.parcela or "",
        "preco_12x_total": args.total or "", "de": args.de or "",
        "vendedor": args.vendedor, "url": args.url, "artigo": args.artigo,
        "obs": args.obs,
    }
    linhas.append(nova)
    escrever(path, linhas)
    print(f"✅ Captura registrada: {args.sku} / {args.loja} / {args.data}")

    if args.de and args.pix:
        d_de, d_pix = _num(args.de), _num(args.pix)
        if d_de and d_pix and d_de < d_pix * 1.05:
            print(f"   ⚠️  'de' R${d_de:.0f} mal supera o preço real R${d_pix:.0f} — "
                  "desconto de fachada. Não destaque esse 'de' no artigo.")

    n = sum(1 for l in linhas
            if l["sku_id"] == args.sku and l["variante"] == args.variante
            and l["tipo"] != "catalogo")
    print(f"   {n} captura(s) válida(s) deste SKU. {_permissao(n)}")


def _permissao(n):
    if n <= 0:
        return "Nenhuma afirmação de preço permitida."
    if n == 1:
        return 'Pode dizer apenas: "nesta data, R$ X".'
    if n == 2:
        return 'Pode dizer: "subiu/caiu em relação a <data anterior>".'
    return 'Pode dizer: "faixa observada pela Curadoria entre <min> e <max>".'


# ───────────────────────────────────────────────────────────── frase ──

def cmd_frase(args):
    path = caminho(args)
    linhas = [l for l in ler(path)
              if l["sku_id"] == args.sku
              and (not args.variante or l["variante"] == args.variante)]

    if not linhas:
        print(f"❌ Nenhuma captura para '{args.sku}'.")
        print("   Sem RELATÓRIO DE MERCADO não se escreve bloco de compra (SKILL.md).")
        return 1

    uteis = sorted([l for l in linhas if l["tipo"] != "catalogo"], key=lambda x: x["data"])
    catalogo = [l for l in linhas if l["tipo"] == "catalogo"]

    print(f"\n📊 {args.sku}" + (f" / {args.variante}" if args.variante else ""))
    print(f"   {len(uteis)} captura(s) que sustentam afirmação; "
          f"{len(catalogo)} de catálogo (não contam para tendência).\n")

    if not uteis:
        print("   ⚠️  Só há capturas de catálogo. Nenhuma frase de preço é permitida.")
        return 1

    hoje = date.today()
    ultima = datetime.strptime(uteis[-1]["data"], "%Y-%m-%d").date()
    idade = (hoje - ultima).days

    precos = [(l["data"], _num(l["preco_pix"]) or _num(l["preco_12x_total"]), l["loja"])
              for l in uteis]
    precos = [p for p in precos if p[1]]

    print("   ✅ PODE ESCREVER:")
    if len(precos) == 1:
        d, v, loja = precos[0]
        print(f'      "Em {_br(d)}, R$ {v:,.0f} na {_loja(loja)}."'.replace(",", "."))
    elif len(precos) == 2:
        (d1, v1, _), (d2, v2, l2) = precos[0], precos[-1]
        verbo = "subiu" if v2 > v1 else ("caiu" if v2 < v1 else "manteve-se")
        print(f'      "Em {_br(d2)}, R$ {v2:,.0f} na {_loja(l2)} — '
              f'{verbo} em relação aos R$ {v1:,.0f} de {_br(d1)}."'.replace(",", "."))
    else:
        vs = [v for _, v, _ in precos]
        d2, v2, l2 = precos[-1]
        print(f'      "Faixa observada pela Curadoria entre {_br(precos[0][0])} e '
              f'{_br(d2)}: R$ {min(vs):,.0f} a R$ {max(vs):,.0f}."'.replace(",", "."))
        print(f'      "Na captura mais recente ({_br(d2)}): R$ {v2:,.0f} na {_loja(l2)}."'
              .replace(",", "."))

    print("\n   🚫 NUNCA ESCREVER:")
    print('      "menor preço da internet" · "o mais barato" · "imperdível"')
    print('      preço sem a data ao lado · preço de catálogo como se fosse de vendedor')

    if idade > DIAS_FRESCOR:
        print(f"\n   ⚠️  A captura mais recente tem {idade} dias ({_br(uteis[-1]['data'])}).")
        print("      Acima de 30 dias o preço não sustenta mais o bloco de compra.")
        print("      Recapture antes de publicar ou atualizar o artigo.")
    else:
        print(f"\n   🕐 Captura mais recente: {idade} dia(s) atrás. Dentro da validade.")
    return 0


def _br(iso):
    return datetime.strptime(iso, "%Y-%m-%d").strftime("%d/%m/%Y")


def _loja(k):
    return {"amazon": "Amazon", "ml": "Mercado Livre", "samsung": "Samsung",
            "apple": "Apple"}.get(k, k)


# ─────────────────────────────────────────────────────────── validar ──

def cmd_validar(args):
    path = caminho(args)
    linhas = ler(path)
    erros, alertas = [], []
    vistos = {}

    for i, l in enumerate(linhas, start=2):
        ref = f"linha {i} ({l.get('sku_id', '?')}/{l.get('loja', '?')}/{l.get('data', '?')})"

        try:
            d = datetime.strptime(l["data"], "%Y-%m-%d").date()
            if d > date.today():
                erros.append(f"{ref}: data no futuro.")
        except ValueError:
            erros.append(f"{ref}: data fora do formato AAAA-MM-DD.")

        if l["loja"] not in LOJAS:
            erros.append(f"{ref}: loja desconhecida '{l['loja']}'.")
        if l["tipo"] not in TIPOS:
            erros.append(f"{ref}: tipo desconhecido '{l['tipo']}'.")

        chave = (l["data"], l["sku_id"], l["loja"], l["variante"])
        if chave in vistos:
            ant_i, ant_preco = vistos[chave]
            atual_preco = l["preco_pix"] or l["preco_12x_total"]
            if atual_preco == ant_preco:
                erros.append(f"{ref}: duplica a linha {ant_i} com o mesmo preço.")
            else:
                # Recaptura intradiária é legítima: o preço mudou no mesmo dia.
                alertas.append(
                    f"{ref}: segunda captura do dia (linha {ant_i}: R${ant_preco} → "
                    f"R${atual_preco}). Legítimo se o preço mudou; no artigo, cite "
                    "apenas a mais recente do dia.")
        vistos[chave] = (i, l["preco_pix"] or l["preco_12x_total"])

        if not (l["preco_pix"] or l["preco_12x_parcela"] or l["preco_12x_total"]):
            erros.append(f"{ref}: nenhuma coluna de preço preenchida.")

        if l["tipo"] == "anuncio" and "/p/MLB" in l.get("url", ""):
            erros.append(f"{ref}: URL de catálogo marcada como anúncio.")

        if not l.get("url"):
            alertas.append(f"{ref}: sem URL — captura não auditável.")

        de, pix = _num(l.get("de")), _num(l.get("preco_pix"))
        if de and pix and de < pix:
            erros.append(f"{ref}: 'de' (R${de:.0f}) menor que o preço real (R${pix:.0f}).")
        elif de and pix and de < pix * 1.05:
            alertas.append(f"{ref}: 'de' quase igual ao preço real — desconto de fachada.")

    print(f"\n📒 {path}")
    print(f"   {len(linhas)} captura(s) · "
          f"{len({l['sku_id'] for l in linhas})} SKU(s) · "
          f"{len({l['artigo'] for l in linhas if l['artigo']})} artigo(s) citando\n")

    for e in erros:
        print(f" ❌ {e}")
    for a in alertas:
        print(f" ⚠️  {a}")

    if not erros and not alertas:
        print(" ✅ Ledger íntegro.")
    elif not erros:
        print(f"\n✅ Sem erros. {len(alertas)} alerta(s) para revisar.")
    else:
        print(f"\n🚫 {len(erros)} erro(s). Corrija antes de usar estes dados num artigo.")
        return 1
    return 0


# ─────────────────────────────────────────────────────────────── ver ──

def cmd_ver(args):
    path = caminho(args)
    linhas = [l for l in ler(path) if not args.sku or l["sku_id"] == args.sku]
    if not linhas:
        print(f"Nenhuma captura para '{args.sku}'.")
        return 1
    linhas.sort(key=lambda x: (x["sku_id"], x["variante"], x["data"]))
    atual = None
    for l in linhas:
        grupo = (l["sku_id"], l["variante"])
        if grupo != atual:
            atual = grupo
            print(f"\n── {l['sku_id']} / {l['variante']} ──")
        p = l["preco_pix"] or l["preco_12x_total"] or l["preco_12x_parcela"] + "×12"
        flag = "  [catálogo]" if l["tipo"] == "catalogo" else ""
        print(f"   {_br(l['data'])}  {_loja(l['loja']):<14} R$ {p:>9}{flag}")
    print()
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Histórico de preços de primeira mão da Curadoria Prime.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="Sem captura no ledger, o bloco de compra não pode ser escrito.",
    )
    ap.add_argument("--arquivo", help=f"caminho do LEDGER.csv (padrão: {PADRAO})")
    sub = ap.add_subparsers(dest="cmd", required=True)

    a = sub.add_parser("add", help="registrar uma captura real")
    a.add_argument("--data", required=True, help="AAAA-MM-DD")
    a.add_argument("--sku", required=True)
    a.add_argument("--codigo", default="", help="código do fabricante, ex. SM-X520")
    a.add_argument("--variante", required=True, help="ex. wifi-128")
    a.add_argument("--loja", required=True, choices=sorted(LOJAS))
    a.add_argument("--tipo", required=True, choices=sorted(TIPOS))
    a.add_argument("--pix", help="preço à vista/Pix")
    a.add_argument("--parcela", help="valor da parcela em 12×")
    a.add_argument("--total", help="total parcelado")
    a.add_argument("--de", help="preço 'de' riscado, se houver")
    a.add_argument("--vendedor", default="", choices=sorted(VENDEDORES))
    a.add_argument("--url", default="")
    a.add_argument("--artigo", default="")
    a.add_argument("--obs", default="")
    a.add_argument("--recaptura", action="store_true",
                   help="autoriza segunda captura no mesmo dia/loja (preço mudou)")
    a.set_defaults(func=cmd_add)

    f = sub.add_parser("frase", help="o que o ledger autoriza afirmar hoje")
    f.add_argument("--sku", required=True)
    f.add_argument("--variante", default="")
    f.set_defaults(func=cmd_frase)

    v = sub.add_parser("validar", help="conferir integridade do arquivo")
    v.set_defaults(func=cmd_validar)

    s = sub.add_parser("ver", help="histórico de um SKU")
    s.add_argument("--sku", default="")
    s.set_defaults(func=cmd_ver)

    args = ap.parse_args()
    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
