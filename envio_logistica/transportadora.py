"""
transportadora.py
=================
Define a classe Transportadora, que representa uma empresa responsável por realizar as entregas.
"""

from dataclasses import dataclass, asdict
from typing import Dict, Optional

@dataclass
class Transportadora:
    """Representa uma empresa de transporte (Correios, FedEx, Jadlog etc.)."""
    nome: str
    codigo: str
    prazo_entrega: str
    taxa_envio: float
    contato: Optional[Dict[str, str]] = None

    def to_dict(self) -> Dict:
        """Converte a transportadora em dicionário (útil para APIs e JSON)."""
        return asdict(self)
