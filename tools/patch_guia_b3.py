#!/usr/bin/env python3
"""Patch 24/08/2026 — parte B3: ofertas e FAQ no JSON-LD."""
import sys

F = "articles/html_output/guia-volta-as-aulas-tech-2026-7-itens.html"
src = open(F, encoding="utf-8").read()

PARES = [
    ("\"name\": \"Mouse Logitech M185\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Logitech\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"67.19\"",
     "\"name\": \"Mouse Logitech M185\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Logitech\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"68.90\""),
    ("\"name\": \"Teclado Logitech Pebble Keys 2 K380\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Logitech\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"192.05\"",
     "\"name\": \"Teclado Logitech Pebble Keys 2 K380s\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Logitech\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"197.99\""),
    ("\"name\": \"JBL Wave Buds 2\", \"brand\": { \"@type\": \"Brand\", \"name\": \"JBL\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"235.00\"",
     "\"name\": \"JBL Wave Buds 2\", \"brand\": { \"@type\": \"Brand\", \"name\": \"JBL\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"232.00\""),
    ("\"name\": \"Anker 737 Power Bank\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Anker\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"636.64\"",
     "\"name\": \"Anker 737 Power Bank\", \"brand\": { \"@type\": \"Brand\", \"name\": \"Anker\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"639.00\""),
    ("\"name\": \"Roteador TP-Link Archer AX12\", \"brand\": { \"@type\": \"Brand\", \"name\": \"TP-Link\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"179.10\"",
     "\"name\": \"Roteador TP-Link Archer AX12 (EX1500)\", \"brand\": { \"@type\": \"Brand\", \"name\": \"TP-Link\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"169.15\""),
    ("\"name\": \"Hub USB-C UGREEN 5 em 1\", \"brand\": { \"@type\": \"Brand\", \"name\": \"UGREEN\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"89.00\"",
     "\"name\": \"Hub USB-C UGREEN 5 em 1\", \"brand\": { \"@type\": \"Brand\", \"name\": \"UGREEN\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"99.00\""),
    ("\"name\": \"Suporte Notebook PRINCASE\", \"brand\": { \"@type\": \"Brand\", \"name\": \"PRINCASE\" }, \"offers\": { \"@type\": \"Offer\", \"price\": \"170.05\"",
     "\"name\": \"Suporte de Notebook Giratório 360° com Ventoinha\", \"offers\": { \"@type\": \"Offer\", \"price\": \"157.93\""),
    ("\"text\": \"O kit completo com os 7 produtos soma R$ 1.569,03 (menores preços de 05/08/2026).\"",
     "\"text\": \"O kit completo com os 7 produtos soma R$ 1.563,97 (menores preços de 24/08/2026).\""),
]

erros = 0
for old, new in PARES:
    n = src.count(old)
    if n != 1:
        print(f"ERRO ({n}x): {old[:80]}...")
        erros += 1
    else:
        src = src.replace(old, new)

if erros:
    print(f"{erros} substituição(ões) falharam — nada foi gravado.")
    sys.exit(1)

open(F, "w", encoding="utf-8").write(src)
print(f"OK: {len(PARES)} substituições aplicadas (parte B3).")
