# app/routes/__init__.py
from flask import Blueprint

api = Blueprint('api', __name__)

def init_app(app):
    """Inicializa as rotas da API."""

    from .agendamento import controller as agendamento_controller
    from .cliente import controller as cliente_controller
    from .funcionario import controller as funcionario_controller
    from .servico import controller as servico_controller


    

    # Rotas de Agendamento
    @app.route('/agendamentos', methods=['POST'])
    def criar_agendamento():
        return agendamento_controller.criar_agendamento()

    @app.route('/agendamentos', methods=['GET'])
    def listar_agendamentos():
        return agendamento_controller.listar_agendamentos()

    @app.route('/agendamentos/<int:agendamento_id>', methods=['GET'])
    def obter_agendamento(agendamento_id):
        return agendamento_controller.obter_agendamento(agendamento_id)

    @app.route('/agendamentos/<int:agendamento_id>', methods=['PUT'])
    def atualizar_agendamento(agendamento_id):
        return agendamento_controller.atualizar_agendamento(agendamento_id)

    @app.route('/agendamentos/<int:agendamento_id>', methods=['DELETE'])
    def deletar_agendamento(agendamento_id):
        return agendamento_controller.deletar_agendamento(agendamento_id)

    # Rotas de Cliente
    @app.route('/clientes', methods=['POST'])
    def criar_cliente():
        return cliente_controller.criar_cliente()

    @app.route('/clientes', methods=['GET'])
    def listar_clientes():
        return cliente_controller.listar_clientes()

    @app.route('/clientes/<int:cliente_id>', methods=['GET'])
    def obter_cliente(cliente_id):
        return cliente_controller.obter_cliente(cliente_id)

    @app.route('/clientes/<int:cliente_id>', methods=['PUT'])
    def atualizar_cliente(cliente_id):
        return cliente_controller.atualizar_cliente(cliente_id)

    @app.route('/clientes/<int:cliente_id>', methods=['DELETE'])
    def deletar_cliente(cliente_id):
        return cliente_controller.deletar_cliente(cliente_id)

    # Rotas de Funcionário
    @app.route('/funcionarios', methods=['POST'])
    def criar_funcionario():
        return funcionario_controller.criar_funcionario()

    @app.route('/funcionarios', methods=['GET'])
    def listar_funcionarios():
        return funcionario_controller.listar_funcionarios()

    @app.route('/funcionarios/<int:funcionario_id>', methods=['GET'])
    def obter_funcionario(funcionario_id):
        return funcionario_controller.obter_funcionario(funcionario_id)

    @app.route('/funcionarios/<int:funcionario_id>', methods=['PUT'])
    def atualizar_funcionario(funcionario_id):
        return funcionario_controller.atualizar_funcionario(funcionario_id)

    @app.route('/funcionarios/<int:funcionario_id>', methods=['DELETE'])
    def deletar_funcionario(funcionario_id):
        return funcionario_controller.deletar_funcionario(funcionario_id)

    # Rotas de Serviço
    @app.route('/servicos', methods=['POST'])
    def criar_servico():
        return servico_controller.criar_servico()

    @app.route('/servicos', methods=['GET'])
    def listar_servicos():
        return servico_controller.listar_servicos()

    @app.route('/servicos/<int:servico_id>', methods=['GET'])
    def obter_servico(servico_id):
        return servico_controller.obter_servico(servico_id)

    @app.route('/servicos/<int:servico_id>', methods=['PUT'])
    def atualizar_servico(servico_id):
        return servico_controller.atualizar_servico(servico_id)

    @app.route('/servicos/<int:servico_id>', methods=['DELETE'])
    def deletar_servico(servico_id):
        return servico_controller.deletar_servico(servico_id)
    
    @app.route('/teste')
    def teste():
        return "Olá, esta é uma rota de teste!", 200