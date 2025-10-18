"""
simulated_api.py
================
Simula o funcionamento de uma API de transportadora.
"""

import random
from typing import Dict, Optional
from .utils import probabilidade_ocorre

class SimulatedCarrierAPI:
    """API simulada que fornece status aleatórios de entrega."""
    STATUS_FLOW = [
        "Objeto postado na origem",
        "Em trânsito para unidade de destino",
        "Em trânsito para centro de distribuição",
        "Saiu para entrega",
        "Entregue"
    ]

    def __init__(self, seed: Optional[int] = None):
        self._rng = random.Random(seed)

    def consultar(self, codigo_rastreio: str) -> Dict[str, str]:
        if probabilidade_ocorre(0.05):
            return {"codigo_rastreio": codigo_rastreio, "status": "Objeto extraviado", "local": "Desconhecido"}
        status = self._rng.choice(self.STATUS_FLOW)
        local = self._rng.choice(["Unidade de origem", "Centro de distribuição", "Filial local", "Rua do destinatário"])
        return {"codigo_rastreio": codigo_rastreio, "status": status, "local": local}
