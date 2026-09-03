#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
openrouter.py — Integração com a API do OpenRouter para modelos de linguagem.

O OpenRouter é um gateway unificado que fornece acesso a diversos modelos de LLM
(GPT, Claude, Llama, etc.) via uma API compatível com a OpenAI.

Endpoint: https://openrouter.ai/api/v1
Referência: https://openrouter.ai/docs

Configuração:
  export OPENROUTER_API_KEY="sua_api_key_aqui"

Uso (CLI):
  # Eniar um prompt simples
  python3 openrouter.py chat --model openai/gpt-4o --prompt "Qual a capital do Brasil?"

  # Usar com Claude
  python3 openrouter.py chat --model anthropic/claude-3-5-sonnet-20241022 --prompt "Explique brevemente o que são headers HTTP"

  # Listar modelos disponíveis
  python3 openrouter.py modelos

  # Enivar conversa com histórico (arquivo JSON)
  python3 openrouter.py chat --model openai/gpt-4o-mini --arquivo roteiro_conversa.json

Uso (Python — importação como módulo):
  from openrouter import chat

  resposta = chat(
    "Explique a diferença entre HTTP e HTTPS",
    model="openai/gpt-4o-mini",
    temperature=0.7,
    max_tokens=500,
  )
  print(resposta)
"""

import json
import os
import sys
import argparse
import urllib.request
import urllib.parse
import urllib.error

API_BASE = "https://openrouter.ai/api/v1"
API_KEY = os.environ.get("OPENROUTER_API_KEY")

# Modelos testados/qualificados que você recomenda no fluxo editorial.
# Ver: https://openrouter.ai/models
MODELOS_PADRAO = {
    "gpt-4o": "openai/gpt-4o",
    "gpt-4o-mini": "openai/gpt-4o-mini",
    "gpt-4-turbo": "openai/gpt-4-turbo",
    "claude-3-5-sonnet": "anthropic/claude-3-5-sonnet-20241022",
    "claude-3-5-haiku": "anthropic/claude-3-5-haiku-20241022",
    "o1-preview": "openai/o1-preview",
}


# ───────────────────────────────────────── helpers

def _require_key():
    if not API_KEY:
        sys.exit(
            "❌ OPENROUTER_API_KEY não definida.\n"
            "   Obtenha em https://openrouter.ai/ (cadastro gratuito) e rode:\n"
            "   export OPENROUTER_API_KEY=\"sk-or-...\""
        )
    return API_KEY


def _headers(referer=None):
    h = {
        "Authorization": f"Bearer {_require_key()}",
        "Content-Type": "application/json",
        "HTTP-Referer": referer or "https://curadoriaprime.com",
        "X-Title": "Curadoria Prime",
        "User-Agent": "CuradoriaPrime-Agent/1.0",
    }
    return h


def _post(url, payload):
    req = urllib.request.Request(
        url, data=json.dumps(payload).encode(), headers=_headers(), method="POST"
    )
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:800]
        sys.exit(f"❌ HTTP {e.code} em {url}\n{body}")


def _get(url, params=None):
    if params:
        url = url + "?" + urllib.parse.urlencode(params)
    req = urllib.request.Request(url, headers=_headers(), method="GET")
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:500]
        sys.exit(f"❌ HTTP {e.code} em {url}\n{body}")


# ───────────────────────────────────────── funções principais

def chat(mensagens, model=None, temperature=0.7, max_tokens=1000,
         top_p=1.0, presence_penalty=0, frequency_penalty=0, stream=False):
    """Envia mensagens para um modelo via OpenRouter e retorna a resposta.

    Args:
        mensagens: lista de dicts [{"role": "user"|"assistant"|"system", "content": "..."}]
                   ou uma string simples (tratada como mensagem única de usuário).
        model: ID do modelo (ex: "openai/gpt-4o-mini"). Default: gpt-4o-mini.
        temperature: 0–2 (0 = mais determinístico, 2 = mais criativo).
        max_tokens: limite de tokens na resposta.
        top_p: nucleus sampling (0–1).
        stream: se True, retorna o generator de chunks.

    Returns:
        str com o conteúdo da resposta (ou generator se stream=True).
    """
    if model is None:
        model = MODELOS_PADRAO["gpt-4o-mini"]

    if isinstance(mensagens, str):
        mensagens = [{"role": "user", "content": mensagens}]

    payload = {
        "model": model,
        "messages": mensagens,
        "temperature": temperature,
        "max_tokens": max_tokens,
        "top_p": top_p,
        "presence_penalty": presence_penalty,
        "frequency_penalty": frequency_penalty,
    }

    if stream:
        return _stream(payload)

    data = _post(f"{API_BASE}/chat/completions", payload)
    choices = data.get("choices", [])
    if not choices:
        return ""
    return choices[0].get("message", {}).get("content", "")


def _stream(payload):
    """Versão streaming: yield de chunks de texto conforme chegam."""
    import io
    boundary = None

    req = urllib.request.Request(
        f"{API_BASE}/chat/completions",
        data=json.dumps(payload).encode(),
        headers={**_headers(), "Accept": "text/event-stream"},
        method="POST",
    )

    try:
        with urllib.request.urlopen(req, timeout=120) as resp:
            for line in resp:
                line = line.decode("utf-8").strip()
                if not line or line.startswith(":"):
                    continue
                if line.startswith("data:"):
                    data_str = line[5:].strip()
                    if data_str == "[DONE]":
                        break
                    try:
                        chunk = json.loads(data_str)
                        delta = chunk.get("choices", [{}])[0].get("delta", {})
                        if "content" in delta:
                            yield delta["content"]
                    except json.JSONDecodeError:
                        continue
    except urllib.error.HTTPError as e:
        body = e.read().decode()[:800]
        sys.exit(f"❌ HTTP {e.code} no stream\n{body}")


def modelos(limit=20):
    """Lista modelos disponíveis no OpenRouter."""
    params = {"limit": limit}
    data = _get(f"{API_BASE}/models", params)
    return data.get("data", [])


def modelo_info(model_id):
    """Retorna detalhes de um modelo específico."""
    data = _get(f"{API_BASE}/models/{model_id}")
    return data


def chat_simples(prompt, model=None, system_prompt=None, **kwargs):
    """Conveniência: envia um prompt com system opcional.

    Args:
        prompt: string com o conteúdo do usuário.
        model: ID do modelo. Default: gpt-4o-mini.
        system_prompt: instrução de sistema opcional.

    Returns:
        str com a resposta do modelo.
    """
    msgs = []
    if system_prompt:
        msgs.append({"role": "system", "content": system_prompt})
    msgs.append({"role": "user", "content": prompt})
    return chat(msgs, model=model, **kwargs)


# ───────────────────────────────────────── CLI

def _cmd_chat(args):
    if args.arquivo:
        with open(args.arquivo, encoding="utf-8") as f:
            dados = json.load(f)
        mensagens = dados.get("mensagens", []) if isinstance(dados, dict) else dados
        prompt = None
    else:
        prompt = args.prompt
        mensagens = None

    model = args.model or MODELOS_PADRAO["gpt-4o-mini"]

    print(f"  Modelo: {model}")
    print(f"  Temp:   {args.temperature} | Max tokens: {args.max_tokens}")
    print(f"  Stream: {'sim' if args.stream else 'não'}\n")

    if args.stream:
        for chunk in chat(
            mensagens if mensagens else prompt,
            model=model,
            temperature=args.temperature,
            max_tokens=args.max_tokens,
            stream=True,
        ):
            print(chunk, end="", flush=True)
        print()
    else:
        if args.system:
            # Usa chat_simples para incluir o system prompt
            resposta = chat_simples(
                prompt if prompt else "",
                model=model,
                system_prompt=args.system,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
            )
        else:
            resposta = chat(
                mensagens if mensagens else prompt,
                model=model,
                temperature=args.temperature,
                max_tokens=args.max_tokens,
            )
        print(resposta)

    return 0


def _cmd_modelos(args):
    modelos_lista = modelos(limit=args.limit)
    if not modelos_lista:
        print("  ⚠️  Nenhum modelo retornado.")
        return 1

    print(f"  Modelos disponíveis ({len(modelos_lista)}):\n")
    for m in modelos_lista:
        mid = m.get("id", "?")
        ctx = m.get("context_limit", "?")
        per = m.get("per_request_input_tokens", "?")
        print(f"  {mid}")
        print(f"      contexto: {ctx} tokens | limite per-request: {per}")
        # Preço se disponível
        precos = m.get("pricing", {})
        if precos:
            prompt_p = precos.get("prompt", "?")
            completion_p = precos.get("completion", "?")
            print(f"      preço: prompt ${prompt_p} / completion ${completion_p}")
        print()
    return 0


def main():
    ap = argparse.ArgumentParser(
        description="Integração OpenRouter para modelos de linguagem (LLM). "
                    "Python puro — sem dependências externas.",
    )
    ap.add_argument("--key", help="API key (alternativa à env OPENROUTER_API_KEY)")
    sub = ap.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("chat", help="enviar um prompt para um modelo")
    c.add_argument("--model", default=None,
                   help=f"modelo (default: {MODELOS_PADRAO['gpt-4o-mini']})")
    c.add_argument("--prompt", help="texto do prompt do usuário")
    c.add_argument("--arquivo", help="arquivo JSON com lista de mensagens")
    c.add_argument("--system", help="prompt de sistema (instruções)")
    c.add_argument("--temperature", type=float, default=0.7, help="0-2")
    c.add_argument("--max-tokens", type=int, default=1000)
    c.add_argument("--stream", action="store_true", help="mostra resposta em tempo real")
    c.set_defaults(func=_cmd_chat)

    m = sub.add_parser("modelos", help="listar modelos disponíveis")
    m.add_argument("--limit", type=int, default=20)
    m.set_defaults(func=_cmd_modelos)

    args = ap.parse_args()

    # --key na CLI sobrescreve a env
    if args.key:
        global API_KEY
        API_KEY = args.key

    if args.cmd == "chat" and not args.prompt and not args.arquivo:
        ap.print_help()
        sys.exit(1)

    sys.exit(args.func(args) or 0)


if __name__ == "__main__":
    main()
