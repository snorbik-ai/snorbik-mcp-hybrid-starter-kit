#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Serveur MCP Officiel JSON-RPC 2.0 / stdio -- Starter Kit MCP Hybride Snorbik.
Porte 1 : Connexion universelle IDE IA (Cursor, Antigravity, Claude Desktop).
"""
from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Dict, Any

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from core.domain.entities import ToolRequestDto
from core.application.usecases import ExecuteActionUseCase
from core.infrastructure.adapter import ConcreteOperationalAdapter

# Injection de dépendances
adapter = ConcreteOperationalAdapter()
usecase = ExecuteActionUseCase(adapter=adapter)

TOOLS_METADATA = [
    {
        "name": "template_execute_action",
        "description": "Point d'entrée principal du MCP : exécute une action certifiée ('ping', 'status', etc.) avec retour structuré et gestion d'erreurs intégrée.",
        "inputSchema": {
            "type": "object",
            "properties": {
                "action": {
                    "type": "string",
                    "description": "Action métier à exécuter (ex: 'ping', 'status').",
                    "default": "ping"
                },
                "parameters": {
                    "type": "object",
                    "description": "Paramètres optionnels de l'action.",
                    "default": {}
                }
            },
            "required": ["action"]
        }
    },
    {
        "name": "template_ping",
        "description": "Vérifie la réactivité et la disponibilité immédiate du serveur MCP.",
        "inputSchema": {
            "type": "object",
            "properties": {}
        }
    }
]


def handle_tool_call(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
    if tool_name == "template_ping":
        req = ToolRequestDto(action="ping", parameters={})
        res = usecase.execute(req)
        return res.model_dump()

    elif tool_name == "template_execute_action":
        action = arguments.get("action", "ping")
        params = arguments.get("parameters", {})
        req = ToolRequestDto(action=action, parameters=params)
        res = usecase.execute(req)
        return res.model_dump()

    else:
        raise ValueError(f"Outil MCP inconnu: {tool_name}")


def run_stdio_server():
    """Boucle principale JSON-RPC 2.0 sur stdin / stdout conforme au protocole MCP."""
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            req = json.loads(line)
            req_id = req.get("id")
            method = req.get("method", "")

            # Notification JSON-RPC (sans id ou méthode notifications/*) : AUCUNE réponse autorisée
            if req_id is None or method.startswith("notifications/"):
                continue

            if method == "initialize":
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "protocolVersion": "2024-11-05",
                        "capabilities": {"tools": {}},
                        "serverInfo": {"name": "snorbik-mcp-hybrid-starter-kit", "version": "1.0.0"}
                    }
                }
            elif method == "ping":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {}}
            elif method == "tools/list":
                resp = {"jsonrpc": "2.0", "id": req_id, "result": {"tools": TOOLS_METADATA}}
            elif method == "tools/call":
                params = req.get("params", {})
                name = params.get("name")
                args = params.get("arguments", {})
                result = handle_tool_call(name, args)
                resp = {
                    "jsonrpc": "2.0",
                    "id": req_id,
                    "result": {
                        "content": [{"type": "text", "text": json.dumps(result, indent=2, ensure_ascii=False)}]
                    }
                }
            else:
                resp = {"jsonrpc": "2.0", "id": req_id, "error": {"code": -32601, "message": f"Method not found: {method}"}}

            sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
            sys.stdout.flush()
        except Exception as e:
            if req.get("id") is not None:
                err_resp = {"jsonrpc": "2.0", "id": req.get("id"), "error": {"code": -32603, "message": str(e)}}
                sys.stdout.write(json.dumps(err_resp, ensure_ascii=False) + "\n")
                sys.stdout.flush()


if __name__ == "__main__":
    run_stdio_server()
