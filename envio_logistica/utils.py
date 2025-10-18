"""
utils.py
=========
Módulo com funções auxiliares utilizadas em todo o sistema de envio e logística.

Ele fornece pequenas rotinas reutilizáveis, como:
- geração de código de rastreio;
- cálculo de probabilidades (para simular eventos aleatórios nas APIs).
"""

import random
import string

def gerar_codigo_rastreio(prefix: str = "BR") -> str:
    """Gera um código de rastreio aleatório (simulado)."""
    random_part = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    return f"{prefix}{random_part}"

def probabilidade_ocorre(valor: float) -> bool:
    """Verifica se um evento ocorre com a probabilidade informada."""
    if not (0.0 <= valor <= 1.0):
        raise ValueError("O valor deve estar entre 0.0 e 1.0")
    return random.random() < valor
