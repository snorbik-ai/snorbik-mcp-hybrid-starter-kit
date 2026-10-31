"""
Ports et Interfaces (DIP) -- Starter Kit MCP Hybride Snorbik.
Couche Domaine Pure.
"""
from __future__ import annotations

from typing import Protocol, Dict, Any, Optional
from .entities import ToolRequestDto, ToolResponseDto


class IOperationalAdapter(Protocol):
    """Port vers le système externe, base de données ou service technique."""
    def execute_operation(self, action: str, params: Dict[str, Any]) -> Dict[str, Any]: ...
    def check_health(self) -> bool: ...


class IMemoryRecorder(Protocol):
    """Port vers le gestionnaire de mémoire contextuelle (ContextHistoryManager)."""
    def record_turn(self, goal: str, actions: list, summary: str) -> Dict[str, Any]: ...
