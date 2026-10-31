"""
Entités et DTOs du Domaine Pur -- Starter Kit MCP Hybride Snorbik.
Couche Domaine Pure (Clean Architecture DPN v4).
"""
from __future__ import annotations

import time
from enum import Enum
from typing import Dict, Any, List, Optional
from pydantic import BaseModel, Field


class OperationStatus(str, Enum):
    SUCCESS = "SUCCESS"
    WARNING = "WARNING"
    FAILED = "FAILED"


class ToolRequestDto(BaseModel):
    """Paramètres d'entrée standardisés pour un cas d'usage."""
    action: str = Field(..., description="Action demandée par l'agent IA.")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Paramètres libres.")
    caller_agent_id: Optional[str] = Field(default=None, description="Identifiant optionnel de l'agent appelant.")


class ToolResponseDto(BaseModel):
    """Résultat métier certifié retourné par le cas d'usage."""
    operation_id: str
    action: str
    status: OperationStatus
    payload: Dict[str, Any] = Field(default_factory=dict)
    execution_duration_ms: float
    timestamp: float = Field(default_factory=time.time)
    error_message: Optional[str] = None
