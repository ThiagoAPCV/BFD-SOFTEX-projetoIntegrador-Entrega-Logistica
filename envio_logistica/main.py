"""
main.py
========
Script principal de demonstração do módulo de envio_logistica_vfinal.

Ele mostra o ciclo completo de um envio:
1. Criação de uma transportadora (Correios, Jadlog, etc.);
2. Criação de um envio associado a um pedido;
3. Envio do produto (mudança de status);
4. Consultas simuladas de rastreamento;
5. Exibição do histórico completo de eventos de entrega.

"""
# Ajuste de caminho para execução direta no VS Code.
# Adiciona o diretório pai ao sys.path para permitir que o pacote
# 'envio_logistica_vfinal' seja importado quando esse script for executado com `python main.py`.
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


# ---------------------------------------------------------------------------
# IMPORTAÇÃO DOS MÓDULOS para funcionar no VS Code
# ---------------------------------------------------------------------------
import os
import sys
import logging

# Adiciona o diretório "pai" ao caminho de busca do Python. Isso garante que o pacote envio_logistica 
# seja encontrado, mesmo que o main.py esteja sendo executado de dentro da pasta.

sys.path.append(os.path.dirname(__file__))

# Agora importar os módulos do pacote
# Importando módulos do pacote local 'envio_logistica_vfinal'
from envio_logistica_vfinal.transportadora import Transportadora
# Importando módulos do pacote local 'envio_logistica_vfinal'
from envio_logistica_vfinal.envio import Envio
# Importando módulos do pacote local 'envio_logistica_vfinal'
from envio_logistica_vfinal.simulated_api import SimulatedCarrierAPI

# ---------------------------------------------------------------------------
# CONFIGURAÇÃO DE LOGS
# ---------------------------------------------------------------------------
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("envio_module")

# ---------------------------------------------------------------------------
# FUNÇÃO PRINCIPAL DE DEMONSTRAÇÃO
# ---------------------------------------------------------------------------
def demonstracao_simples():
    """
    Demonstra o funcionamento completo do módulo Envio/Logística.
    Inclui a criação da transportadora, envio e simulação da API.
    """

    # Criação da transportadora
    t = Transportadora(
        nome="Correios",
        codigo="C001",
        prazo_entrega="5 dias úteis",
        taxa_envio=20.0
    )

    # Criação do envio vinculado ao pedido 123
    envio = Envio(pedido_id=123, transportadora=t)

    # Produto é “enviado” (primeiro status do rastreio)
    envio.enviar_produto()

    # Criação da API simulada
    api = SimulatedCarrierAPI(seed=42)

    # Consulta o status várias vezes e exibe resultados
    for i in range(6):
        status_externo = envio.consultar_status_externo(api)
        print(f"[Demonstração] Consulta {i + 1} retornou: {status_externo}")

    # Exibe o histórico completo de rastreamento
    print("\nHistórico de rastreio:")
    for ev in envio.rastreio.obter_historico():
        print(ev)

# ---------------------------------------------------------------------------
# PONTO DE ENTRADA DO SCRIPT
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    logger.info("Iniciando simulação de envio_logistica_vfinal...")
    demonstracao_simples()
    logger.info("Simulação finalizada com sucesso.")
