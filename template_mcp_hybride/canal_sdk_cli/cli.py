#!/usr/bin/env python3
"""
Interface CLI Terminal -- Starter Kit MCP Hybride Snorbik.
Permet d'exécuter des actions directement en ligne de commande.
"""
from __future__ import annotations

import sys
import json
import argparse
from pathlib import Path

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from canal_sdk_cli.sdk import HybridMcpStarterSDK


def main():
    parser = argparse.ArgumentParser(description="CLI Starter Kit MCP Hybride Snorbik")
    parser.add_argument("--action", default="ping", help="Action à exécuter (défaut: ping)")
    parser.add_argument("--params", default="{}", help="Paramètres JSON (défaut: {})")
    args = parser.parse_args()

    sdk = HybridMcpStarterSDK()
    try:
        parameters = json.loads(args.params)
    except Exception as e:
        print(f"Erreur JSON dans --params : {e}")
        sys.exit(1)

    response = sdk.execute(args.action, parameters)
    print(json.dumps(response.model_dump(), indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
