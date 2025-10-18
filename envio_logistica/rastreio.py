"""
rastreio.py
============
Define a classe Rastreio, responsável por armazenar o histórico de eventos de entrega de um envio.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import List, Dict, Optional
import logging

logger = logging.getLogger("envio_module")

@dataclass
class Rastreio:
    """Controla o histórico de eventos associados a um código de rastreamento."""
    codigo_rastreio: str
    historico_status: List[Dict[str, str]] = field(default_factory=list)
    data_ultima_atualizacao: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def registrar_evento(self, status: str, local: Optional[str] = None) -> None:
        evento = {
            "status": status,
            "local": local or "Indefinido",
            "timestamp": datetime.now(timezone.utc).isoformat()
        }
        self.historico_status.append(evento)
        self.data_ultima_atualizacao = datetime.now(timezone.utc)
        logger.info(f"[Rastreio:{self.codigo_rastreio}] Evento registrado: {status}")

    def obter_historico(self) -> List[Dict[str, str]]:
        return list(self.historico_status)

    def ultimo_status(self) -> Optional[str]:
        if not self.historico_status:
            return None
        return self.historico_status[-1]["status"]

    def to_dict(self) -> Dict:
        return {
            "codigo_rastreio": self.codigo_rastreio,
            "historico_status": list(self.historico_status),
            "data_ultima_atualizacao": self.data_ultima_atualizacao.isoformat()
        }
