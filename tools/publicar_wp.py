#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
publicar_wp.py — Publica artigos no WordPress do Curadoria Prime via REST API
==============================================================================

PRÉ-REQUISITO — gerar um Application Password:
  1. WordPress > Usuários > Seu perfil
  2. Role até "Senhas de aplicativo"
  3. Nome: "agente-conteudo"  ->  Adicionar nova senha
  4. Copie a senha gerada (formato: xxxx xxxx xxxx xxxx xxxx xxxx)

Configure as variáveis de ambiente:
  export WP_USER="seu_usuario"
  export WP_APP_PASSWORD="xxxx xxxx xxxx xxxx xxxx xxxx"

USO:
  # publicar como rascunho (padrão e recomendado)
  python3 publicar_wp.py artigo-exemplo.html --meta exemplo-produto.json

  # agendar para uma data
  python3 publicar_wp.py artigo.html --meta produto.json --agendar "2026-08-20 08:00"

  # listar posts existentes
  python3 publicar_wp.py --listar

  # auditoria: checar links de afiliado quebrados em todos os posts
  python3 publicar_wp.py --auditar-links
"""

import os
import re
import sys
import json
import base64
import argparse
import subprocess
import urllib.request
import urllib.error
from datetime import datetime

SITE = "https://curadoriaprime.com"
API = f"{SITE}/wp-json/wp/v2"


# ----------------------------------------------------------------- helpers
def auth_header():
    user = os.environ.get("WP_USER")
    pwd = os.environ.get("WP_APP_PASSWORD")
    if not user or not pwd:
        sys.exit(
            "❌ Defina as variáveis de ambiente WP_USER e WP_APP_PASSWORD.\n"
            "   Veja as instruções no topo deste arquivo."
        )
    token = base64.b64encode(f"{user}:{pwd}".encode()).decode()
    return {"Authorization": f"Basic {token}"}


def req(url, method="GET", data=None, auth=False):
    headers = {"Content-Type": "application/json", "User-Agent": "CuradoriaPrime-Agent/1.0"}
    if auth:
        headers.update(auth_header())
    body = json.dumps(data).encode() if data else None
    r = urllib.request.Request(url, data=body, headers=headers, method=method)
    try:
        with urllib.request.urlopen(r, timeout=45) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        detalhe = e.read().decode()[:500]
        sys.exit(f"❌ HTTP {e.code} em {method} {url}\n{detalhe}")


def resolver_termo(tipo, nome):
    """Busca (ou cria) uma categoria/tag pelo nome ou slug. Retorna o ID."""
    achados = req(f"{API}/{tipo}?search={urllib.parse.quote(nome)}&per_page=20")
    for t in achados:
        if t["slug"] == nome.lower() or t["name"].lower() == nome.lower():
            return t["id"]
    novo = req(f"{API}/{tipo}", "POST", {"name": nome}, auth=True)
    print(f"   + criada nova {tipo[:-1]}: {nome}")
    return novo["id"]


# ------------------------------------------------------------------ ações
def gate_conformidade(html_path, meta_path, forcar=False):
    """Bloqueia o envio se o artigo violar as políticas do Google.

    Roda checar_conformidade.py. Erro = publicação abortada. Isso existe para
    que nenhum artigo gerado por IA chegue ao site sem passar pelas travas de
    afiliação sem valor agregado, rel=sponsored e E-E-A-T.
    """
    checker = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "checar_conformidade.py")
    if not os.path.exists(checker):
        print("⚠️  checar_conformidade.py não encontrado — pulando o gate.")
        return True

    cmd = [sys.executable, checker, html_path]
    if meta_path:
        cmd += ["--json", meta_path]
    print("🔒 Rodando trava de conformidade…\n", flush=True)
    r = subprocess.run(cmd)
    if r.returncode == 0:
        return True
    if forcar:
        print("\n⚠️  Erros de conformidade IGNORADOS via --forcar. "
              "Você assume o risco de rebaixamento no Google.")
        return True
    print("\n🚫 Publicação abortada. Corrija os erros acima ou use --forcar.")
    return False


def publicar(html_path, meta_path, agendar=None, publicar_ja=False, forcar=False):
    if not gate_conformidade(html_path, meta_path, forcar):
        sys.exit(1)

    html = open(html_path, encoding="utf-8").read()
    meta = json.load(open(meta_path, encoding="utf-8"))

    print(f"\n📤 Preparando '{meta.get('titulo_seo', meta['nome'])}'…")

    cat_id = resolver_termo("categories", meta["categoria"]) if meta.get("categoria") else None
    tag_ids = [resolver_termo("tags", t) for t in meta.get("tags", [])]

    payload = {
        "title": meta.get("titulo_seo", meta["nome"]),
        "slug": meta.get("slug", ""),
        "content": html,
        "excerpt": meta.get("meta_description", ""),
        "status": "draft",
    }
    if cat_id:
        payload["categories"] = [cat_id]
    if tag_ids:
        payload["tags"] = tag_ids

    if agendar:
        dt = datetime.strptime(agendar, "%Y-%m-%d %H:%M")
        payload["status"] = "future"
        payload["date"] = dt.strftime("%Y-%m-%dT%H:%M:%S")
    elif publicar_ja:
        payload["status"] = "publish"

    novo = req(f"{API}/posts", "POST", payload, auth=True)

    print(f"\n✅ Post criado — ID {novo['id']}  (status: {novo['status']})")
    print(f"   Editar:     {SITE}/wp-admin/post.php?post={novo['id']}&action=edit")
    print(f"   Preview:    {novo.get('link', '')}")
    if novo["status"] == "draft":
        print("\n   ⚠️  Está como RASCUNHO. Revise antes de publicar — nunca publique")
        print("      conteúdo de agente sem leitura humana.")


def listar():
    posts = req(f"{API}/posts?per_page=100&status=any&_fields=id,date,status,title,link")
    print(f"{'ID':>6}  {'DATA':<12} {'STATUS':<9} TÍTULO")
    print("-" * 92)
    for p in posts:
        t = re.sub("<[^>]+>", "", p["title"]["rendered"])[:56]
        print(f"{p['id']:>6}  {p['date'][:10]:<12} {p['status']:<9} {t}")
    print(f"\nTotal: {len(posts)}")


def auditar_links():
    """Varre todos os posts, extrai links de afiliado e testa cada um."""
    print("🔍 Auditando links de afiliado em todos os posts…\n")
    posts = req(f"{API}/posts?per_page=100&_fields=id,title,link,content")
    problemas = []
    total = 0

    for p in posts:
        titulo = re.sub("<[^>]+>", "", p["title"]["rendered"])[:50]
        links = set(
            re.findall(r'href="(https?://(?:link\.amazon|meli\.la|amzn\.to)[^"]*)"',
                       p["content"]["rendered"])
        )
        for l in links:
            total += 1
            try:
                r = urllib.request.Request(
                    l, method="HEAD",
                    headers={"User-Agent": "Mozilla/5.0 (compatible; LinkChecker/1.0)"},
                )
                with urllib.request.urlopen(r, timeout=15) as resp:
                    code = resp.status
            except urllib.error.HTTPError as e:
                code = e.code
            except Exception:
                code = 0

            if code == 0 or code >= 400:
                problemas.append((p["id"], titulo, l, code))
                print(f"  ❌ [{code or 'erro'}] post {p['id']} — {titulo}\n     {l}")

    print(f"\n{'='*70}")
    print(f"Verificados: {total} links  |  Problemas: {len(problemas)}")
    if not problemas:
        print("✅ Todos os links de afiliado respondendo normalmente.")
    else:
        with open("links-quebrados.csv", "w", encoding="utf-8") as f:
            f.write("post_id,titulo,url,http_code\n")
            for row in problemas:
                f.write(f'{row[0]},"{row[1]}",{row[2]},{row[3]}\n')
        print("📄 Detalhes salvos em links-quebrados.csv")


def checar_duplicados():
    """Detecta títulos muito parecidos (canibalização de SEO)."""
    posts = req(f"{API}/posts?per_page=100&_fields=id,title,slug,link")
    print("🔍 Procurando títulos duplicados / canibalização…\n")
    norm = lambda s: re.sub(r"[^a-z0-9 ]", "", re.sub("<[^>]+>", "", s).lower())
    vistos = {}
    for p in posts:
        k = norm(p["title"]["rendered"])
        base = " ".join(k.split()[:5])
        vistos.setdefault(base, []).append(p)
    achou = False
    for base, grupo in vistos.items():
        if len(grupo) > 1:
            achou = True
            print(f"⚠️  Possível duplicata — '{base}…'")
            for p in grupo:
                print(f"     ID {p['id']}  /{p['slug']}")
            print()
    if not achou:
        print("✅ Nenhuma duplicata óbvia encontrada.")


def main():
    ap = argparse.ArgumentParser(description="Publica e audita posts no Curadoria Prime")
    ap.add_argument("html", nargs="?", help="arquivo HTML gerado")
    ap.add_argument("--meta", help="JSON com metadados do produto")
    ap.add_argument("--agendar", help='data/hora "AAAA-MM-DD HH:MM"')
    ap.add_argument("--publicar-ja", action="store_true", help="publica imediatamente (cuidado)")
    ap.add_argument("--listar", action="store_true", help="lista posts existentes")
    ap.add_argument("--auditar-links", action="store_true", help="checa links de afiliado")
    ap.add_argument("--checar-duplicados", action="store_true", help="detecta canibalização")
    ap.add_argument("--forcar", action="store_true",
                    help="publica mesmo com erros de conformidade (não recomendado)")
    a = ap.parse_args()

    if a.listar:
        return listar()
    if a.auditar_links:
        return auditar_links()
    if a.checar_duplicados:
        return checar_duplicados()
    if not a.html or not a.meta:
        ap.print_help()
        sys.exit(1)
    publicar(a.html, a.meta, a.agendar, a.publicar_ja, a.forcar)


if __name__ == "__main__":
    import urllib.parse
    main()
