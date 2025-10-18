# BFD-SOFTEX-projetoIntegrador-Entrega-Logistica
A partir do projeto de e-commerce hipotético, separado em módulos para desenvolvimento de seu código conforme apresentado abaixo:

1️⃣— Cliente / Autenticação: Criar classes: Cliente, Administrador, Usuário, Autenticacao. • Implementar login, cadastro e autenticação de sessão. • Métodos: login(), logout(), registrador(), autenticar(). •Controlar permissões de acesso (cliente vs admin). 
2️⃣— Catálogo / Carrinho: Criar classes: Produto, Categoria, Carrinho. • Métodos: listar_produtos(), adicionar_ao_carrinho(), remover_do_carrinho(), calcular_total(). • Lidar com persistência de dados dos produtos. 
3️⃣— Pedido e Checkout: Criar classes: Pedido, ItemPedido, Checkout. • Métodos: finalizar_compra(), acompanhar_pedido(), gerar_nota_fiscal(). • Fazer a ponte entre carrinho, pagamento e envio. 
4️⃣— Pagamento: Criar classes: Pagamento, Transação, NotificaçãoPagamento. • Métodos: processar_pagamento(), verificar_status(), notificar_falha(). • Integração simulada com API de pagamento (ex: Stripe, PagSeguro ou PayPal). 
5️⃣— Entrega / Logística: Criar turmas: Transportadora, Envio, Rastreio. • Métodos: enviar_produto(), atualizar_status_entrega(). • Pode simular integração com API de transporte (ex: Correios). 
6️⃣— Administração e Relatórios: Criar classes: Relatorio, GerenciamentoUsuarios, GerenciamentoPedidos, GerenciamentoProdutos. • Métodos: gerar_relatórios(), visualizar_vendas(), gerenciar_cadastros(). • Responsável por funções exclusivas do Administrador.

Apresento neste repositório o código e documentação referente a:

INTEGRANTE 5: Thiago: Sobre a Entrega / Logística Módulo de Envio: •Criar classes: Transportadora, Envio, Rastreio. •Criar Métodos: enviar_produto(), atualizar_status_entrega(). •Integração simulada com API de transporte (ex: Correios).
