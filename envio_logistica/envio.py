"""
envio.py
========
Define as classes relacionadas ao processo de envio de pedidos.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Dict, Optional
import random
import logging
from abc import ABC, abstractmethod

from .rastreio import Rastreio
from .transportadora import Transportadora
from .utils import gerar_codigo_rastreio

logger = logging.getLogger("envio_module")

class EnvioBase(ABC):
    """Classe abstrata que define a estrutura comum de todos os tipos de envio."""

    @abstractmethod
    def enviar_produto(self) -> None:
        pass

    @abstractmethod
    def consultar_status_externo(self, api_client) -> Optional[str]:
        pass

@dataclass
class Envio(EnvioBase):
    """Implementação concreta de um envio nacional."""
    pedido_id: int
    transportadora: Transportadora
    id_envio: int = field(default_factory=lambda: random.randint(1000, 9999))
    codigo_rastreio: str = field(default_factory=gerar_codigo_rastreio)
    _status: str = field(default="Preparando envio", repr=False)
    rastreio: Rastreio = field(init=False)
    criado_em: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    atualizado_em: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    def __post_init__(self):
        self.rastreio = Rastreio(self.codigo_rastreio)
        logger.info(f"[Envio:{self.id_envio}] Criado para pedido {self.pedido_id} com código {self.codigo_rastreio}")

    @property
    def status(self) -> str:
        return self._status

    def enviar_produto(self) -> None:
        self._status = "Enviado"
        self.atualizado_em = datetime.now(timezone.utc)
        self.rastreio.registrar_evento("Objeto postado na origem")
        logger.info(f"[Envio:{self.id_envio}] Pedido {self.pedido_id} enviado via {self.transportadora.nome}")

    def atualizar_status_entrega(self, novo_status: str, local: Optional[str] = None) -> None:
        self._status = novo_status
        self.atualizado_em = datetime.now(timezone.utc)
        self.rastreio.registrar_evento(novo_status, local=local)
        logger.info(f"[Envio:{self.id_envio}] Status atualizado para: {novo_status}")

    def consultar_status_externo(self, api_client) -> Optional[str]:
        resposta = api_client.consultar(self.codigo_rastreio)
        status_externo = resposta.get("status")
        local = resposta.get("local")
        if status_externo and status_externo != self._status:
            self.atualizar_status_entrega(status_externo, local=local)
        return status_externo

    def to_dict(self) -> Dict:
        return {
            "id_envio": self.id_envio,
            "pedido_id": self.pedido_id,
            "transportadora": self.transportadora.to_dict(),
            "codigo_rastreio": self.codigo_rastreio,
            "status": self._status,
            "rastreio": self.rastreio.to_dict(),
            "criado_em": self.criado_em.isoformat(),
            "atualizado_em": self.atualizado_em.isoformat()
        }
