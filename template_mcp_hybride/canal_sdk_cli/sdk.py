"""
SDK In-Process -- Starter Kit MCP Hybride Snorbik.
Porte 3 : Accès ultra-rapide in-memory sans latence de processus.
"""
from __future__ import annotations

import sys
from pathlib import Path
from typing import Dict, Any, Optional

_ROOT = Path(__file__).resolve().parents[1]
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))

from core.domain.entities import ToolRequestDto, ToolResponseDto
from core.application.usecases import ExecuteActionUseCase
from core.infrastructure.adapter import ConcreteOperationalAdapter


class HybridMcpStarterSDK:
    """Façade in-process pour intégration directe dans FastAPI, scripts ou workers."""

    def __init__(self):
        self.adapter = ConcreteOperationalAdapter()
        self.usecase = ExecuteActionUseCase(adapter=self.adapter)

    def execute(self, action: str, parameters: Optional[Dict[str, Any]] = None) -> ToolResponseDto:
        req = ToolRequestDto(action=action, parameters=parameters or {})
        return self.usecase.execute(req)

    def ping(self) -> Dict[str, Any]:
        return self.execute("ping").payload
