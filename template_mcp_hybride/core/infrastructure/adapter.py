"""
Adaptateur d'Infrastructure Exemple -- Starter Kit MCP Hybride Snorbik.
Couche Infrastructure (Clean Architecture DPN v4).
"""
from __future__ import annotations

import time
from typing import Dict, Any


class ConcreteOperationalAdapter:
    """Implémentation concrète d'exemple (peut être un client DB, API distante, etc.)."""

    def execute_operation(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]:
        if action == "ping":
            return {"reply": "pong", "echo": params, "server_time": time.time()}

        if action == "status":
            return {"healthy": True, "version": "1.0.0", "active_connections": 1}

        if action == "fail_demo":
            raise ValueError("Démonstration d'interception d'erreur contrôlée.")

        return {
            "action_executed": action,
            "params_received": params,
            "message": f"Action '{action}' exécutée avec succès par l'infrastructure."
        }

    def check_health(self) -> bool:
        return True
