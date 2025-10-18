"""
Pacote envio_logistica
======================

Este pacote implementa o módulo de Envio e Logística do sistema E-Commerce (Integrante 5 -> Thiago A. Paraiso C. Vasconcelos).

Funções principais:
- Gerenciamento de envio de pedidos e integração com transportadoras.
- Registro de eventos de rastreamento (histórico de entrega).
- Simulação de APIs de transportadoras (para testes e QA).

Módulos disponíveis:
--------------------
- envio            → Classe principal `Envio` (gerencia o processo de envio e status)
- transportadora   → Classe `Transportadora` (dados da empresa de entrega)
- rastreio         → Classe `Rastreio` (histórico detalhado de eventos de entrega)
- simulated_api    → Classe `SimulatedCarrierAPI` (API simulada para testes de integração)
- utils            → Funções auxiliares (`gerar_codigo_rastreio`, `probabilidade_ocorre`)
"""

from .envio import Envio
from .transportadora import Transportadora
from .rastreio import Rastreio
from .simulated_api import SimulatedCarrierAPI
from .utils import gerar_codigo_rastreio

__all__ = [
    "Envio",
    "Transportadora",
    "Rastreio",
    "SimulatedCarrierAPI",
    "gerar_codigo_rastreio"
]
