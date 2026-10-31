"""
Cas d'Usage Métier -- Starter Kit MCP Hybride Snorbik.
Couche Application (Clean Architecture DPN v4).
"""
from __future__ import annotations

import time
import uuid
from typing import Dict, Any, Optional

from ..domain.entities import ToolRequestDto, ToolResponseDto, OperationStatus
from ..domain.ports import IOperationalAdapter, IMemoryRecorder


class ExecuteActionUseCase:
    """Orchestre l'exécution d'une action métier avec audit et capture d'erreurs."""

    def __init__(self, adapter: IOperationalAdapter, memory: Optional[IMemoryRecorder] = None):
        self.adapter = adapter
        self.memory = memory

    def execute(self, request: ToolRequestDto) -> ToolResponseDto:
        start_time = time.time()
        op_id = f"op-{uuid.uuid4().hex[:8]}"

        try:
            # Exécution déléguée à l'adaptateur d'infrastructure
            raw_result = self.adapter.execute_operation(request.action, request.parameters)
            duration = round((time.time() - start_time) * 1000, 2)

            response = ToolResponseDto(
                operation_id=op_id,
                action=request.action,
                status=OperationStatus.SUCCESS,
                payload=raw_result,
                execution_duration_ms=duration
            )

            # Consignation mémoire optionnelle
            if self.memory:
                try:
                    self.memory.record_turn(
                        goal=f"Exécution action {request.action}",
                        actions=[f"Appel adapter.{request.action}"],
                        summary=f"Succès en {duration} ms"
                    )
                except Exception:
                    pass

            return response

        except Exception as e:
            duration = round((time.time() - start_time) * 1000, 2)
            return ToolResponseDto(
                operation_id=op_id,
                action=request.action,
                status=OperationStatus.FAILED,
                payload={},
                execution_duration_ms=duration,
                error_message=str(e)
            )
