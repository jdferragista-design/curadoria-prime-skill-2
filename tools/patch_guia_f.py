#!/usr/bin/env python3
"""Patch 25/08/2026 — parte F: alt do hero + renome da imagem hero."""
import sys

F = "articles/html_output/melhores-techs-custo-beneficio-2026.html"
src = open(F, encoding="utf-8").read()

PARES = [
    ("alt=\"Guia volta às aulas tech 2026 com 7 produtos essenciais: mouse, teclado, fone, power bank, roteador, hub e suporte\"",
     "alt=\"Melhores techs custo-benefício 2026 para trabalhar e estudar: mouse, teclado, fone, power bank, roteador, hub e suporte\"", 1),
    ("hero-kit-volta-aulas-2026.jpg", "hero-melhores-techs-custo-beneficio-2026.jpg", 3),
]

erros = 0
for old, new, exp in PARES:
    n = src.count(old)
    if n != exp:
        print(f"ERRO ({n}x, esperado {exp}): {old[:90]}...")
        erros += 1
    else:
        src = src.replace(old, new)

if erros:
    print(f"{erros} substituição(ões) falharam — nada foi gravado.")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(src)
print("OK: parte F aplicada (alt do hero x2, ref da imagem hero x2).")
