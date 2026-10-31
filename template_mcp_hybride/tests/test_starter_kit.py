"""
Tests unitaires pour le Starter Kit MCP Hybride Snorbik.
Preuve L4 d'exécutabilité immédiate par processus isolés.
"""
import sys
import json
import subprocess
from pathlib import Path
import pytest

KIT_ROOT = Path(__file__).resolve().parents[1]


def test_starter_kit_cli_ping():
    """Valide l'interface CLI terminal (Porte 2)."""
    cli_path = KIT_ROOT / "canal_sdk_cli" / "cli.py"

    proc = subprocess.run(
        [sys.executable, str(cli_path), "--action", "ping", "--params", json.dumps({"test": "cli"})],
        capture_output=True,
        text=True,
        check=False
    )

    assert proc.returncode == 0
    data = json.loads(proc.stdout)
    assert data["status"] == "SUCCESS"
    assert data["payload"]["reply"] == "pong"
    assert data["payload"]["echo"]["test"] == "cli"


def test_starter_kit_error_handling_resilience():
    """Valide que les erreurs sont interceptées proprement sans crasher."""
    cli_path = KIT_ROOT / "canal_sdk_cli" / "cli.py"

    proc = subprocess.run(
        [sys.executable, str(cli_path), "--action", "fail_demo"],
        capture_output=True,
        text=True,
        check=False
    )

    assert proc.returncode == 0
    data = json.loads(proc.stdout)
    assert data["status"] == "FAILED"
    assert "Démonstration d'interception d'erreur" in data["error_message"]


def test_starter_kit_mcp_stdio_server():
    """Valide le canal MCP JSON-RPC 2.0 stdio universel (Porte 1)."""
    server_path = KIT_ROOT / "canal_mcp" / "mcp_server.py"

    proc = subprocess.Popen(
        [sys.executable, str(server_path)],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        text=True,
        encoding="utf-8"
    )

    req = json.dumps({
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "template_execute_action",
            "arguments": {"action": "status"}
        }
    }) + "\n"

    stdout, _ = proc.communicate(input=req, timeout=5)
    resp = json.loads(stdout.strip())

    assert "result" in resp
    content = json.loads(resp["result"]["content"][0]["text"])
    assert content["status"] == "SUCCESS"
    assert content["payload"]["healthy"] is True
