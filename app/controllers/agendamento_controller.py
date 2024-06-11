from flask import jsonify, request
from ..models import Agendamento, Cliente, Funcionario, Servico
from ..database import db

def criar_agendamento():
    data = request.get_json()
    cliente_id = data.get('cliente_id')
    funcionario_id = data.get('funcionario_id')
    servico_id = data.get('servico_id')
    data_agendamento = data.get('data_agendamento')
    observacoes = data.get('observacoes')

    cliente = Cliente.query.get(cliente_id)
    funcionario = Funcionario.query.get(funcionario_id)
    servico = Servico.query.get(servico_id)

    if not cliente or not funcionario or not servico:
        return jsonify({'error': 'Cliente, funcionário ou serviço não encontrado'}), 404

    agendamento = Agendamento(
        cliente=cliente,
        funcionario=funcionario,
        servico=servico,
        data_agendamento=data_agendamento,
        observacoes=observacoes
    )

    db.session.add(agendamento)
    db.session.commit()

    return jsonify({'message': 'Agendamento criado com sucesso'}), 201

def listar_agendamentos():
    agendamentos = Agendamento.query.all()
    agendamentos_json = [agendamento.to_json() for agendamento in agendamentos]
    return jsonify(agendamentos_json), 200

def obter_agendamento(agendamento_id):
    agendamento = Agendamento.query.get(agendamento_id)
    if not agendamento:
        return jsonify({'error': 'Agendamento não encontrado'}), 404
    return jsonify(agendamento.to_json()), 200

def atualizar_agendamento(agendamento_id):
    agendamento = Agendamento.query.get(agendamento_id)
    if not agendamento:
        return jsonify({'error': 'Agendamento não encontrado'}), 404

    data = request.get_json()
    cliente_id = data.get('cliente_id')
    funcionario_id = data.get('funcionario_id')
    servico_id = data.get('servico_id')
    data_agendamento = data.get('data_agendamento')
    observacoes = data.get('observacoes')

    if cliente_id:
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        agendamento.cliente = cliente
    if funcionario_id:
        funcionario = Funcionario.query.get(funcionario_id)
        if not funcionario:
            return jsonify({'error': 'Funcionário não encontrado'}), 404
        agendamento.funcionario = funcionario
    if servico_id:
        servico = Servico.query.get(servico_id)
        if not servico:
            return jsonify({'error': 'Serviço não encontrado'}), 404
        agendamento.servico = servico
    if data_agendamento:
        agendamento.data_agendamento = data_agendamento
    if observacoes:
        agendamento.observacoes = observacoes

    db.session.commit()
    return jsonify({'message': 'Agendamento atualizado com sucesso'}), 200

def deletar_agendamento(agendamento_id):
    agendamento = Agendamento.query.get(agendamento_id)
    if not agendamento:
        return jsonify({'error': 'Agendamento não encontrado'}), 404
    db.session.delete(agendamento)
    db.session.commit()
    return jsonify({'message': 'Agendamento deletado com sucesso'}), 200