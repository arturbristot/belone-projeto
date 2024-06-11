from flask import Blueprint
from controllers import (
    agendamento_controller as agendamento_controller,
    cliente_controller as cliente_controller,
    funcionario_controller as funcionario_controller,
    servico_controller as servico_controller,
)

api = Blueprint('api', __name__)

#agendamentos
@api.route('/agendamentos', methods=['POST'])
def criar_agendamento():
    return agendamento_controller.AgendamentoController.criar_agendamento()

@api.route('/agendamentos', methods=['GET'])
def listar_agendamentos():
    return agendamento_controller.AgendamentoController.listar_agendamentos()

@api.route('/agendamentos/<int:agendamento_id>', methods=['GET'])
def obter_agendamento(agendamento_id):
    return agendamento_controller.AgendamentoController.obter_agendamento(agendamento_id)

@api.route('/agendamentos/<int:agendamento_id>', methods=['PUT'])
def atualizar_agendamento(agendamento_id):
    return agendamento_controller.AgendamentoController.atualizar_agendamento(agendamento_id)

@api.route('/agendamentos/<int:agendamento_id>', methods=['DELETE'])
def deletar_agendamento(agendamento_id):
    return agendamento_controller.AgendamentoController.deletar_agendamento(agendamento_id)

#clientes
@api.route('/clientes', methods=['POST'])
def criar_cliente():
    return cliente_controller.ClienteController.criar_cliente()

@api.route('/clientes', methods=['GET'])
def listar_cliente():
    return cliente_controller.ClienteController.listar_clientes()

@api.route('/clientes/<int:cliente_id>', methods=['GET'])
def obter_cliente(cliente_id):
    return cliente_controller.ClienteController.obter_cliente(cliente_id)

@api.route('/clientes/<int:cliente_id>', methods=['PUT'])
def atualizar_cliente(agendamento_id):
    return cliente_controller.ClienteController.atualizar_cliente(agendamento_id)

@api.route('/clientes/<int:cliente_id>', methods=['DELETE'])
def deletar_cliente(agendamento_id):
    return cliente_controller.ClienteController.deletar_cliente(agendamento_id)

#servicos
@api.route('/funcionarios', methods=['POST'])
def criar_funcionario():
    return funcionario_controller.FuncionarioController.criar_funcionario()

@api.route('/funcionarios', methods=['GET'])
def listar_funcionario():
    return funcionario_controller.FuncionarioController.listar_funcionarios()

@api.route('/funcionarios/<int:funcionario_id>', methods=['GET'])
def obter_funcionario(funcionario_id):
    return funcionario_controller.FuncionarioController.obter_funcionario(funcionario_id)

@api.route('/funcionarios/<int:funcionario_id>', methods=['PUT'])
def atualizar_funcionario(funcionario_id):
    return funcionario_controller.FuncionarioController.atualizar_funcionario(funcionario_id)

@api.route('/funcionarios/<int:funcionario_id>', methods=['DELETE'])
def deletar_funcionario(funcionario_id):
    return funcionario_controller.FuncionarioController.deletar_funcionario(funcionario_id)

#servicos
@api.route('/servicos', methods=['POST'])
def criar_servico():
    return servico_controller.ServicoController.criar_servico()

@api.route('/servicos', methods=['GET'])
def listar_servico():
    return servico_controller.ServicoController.listar_servicos()

@api.route('/servicos/<int:servico_id>', methods=['GET'])
def obter_servico(servico_id):
    return servico_controller.ServicoController.obter_servico(servico_id)

@api.route('/servicos/<int:servico_id>', methods=['PUT'])
def atualizar_servico(servico_id):
    return servico_controller.ServicoController.atualizar_servico(servico_id)

@api.route('/servicos/<int:servico_id>', methods=['DELETE'])
def deletar_servico(servico_id):
    return servico_controller.ServicoController.deletar_servico(servico_id)