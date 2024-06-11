from flask import jsonify, request
from ..models import Funcionario
from ..database import db

def criar_funcionario():
    data = request.get_json()
    nome = data.get('nome')
    especialidade = data.get('especialidade')
    telefone = data.get('telefone')
    email = data.get('email')
    salario = data.get('salario')

    if not nome or not especialidade or not telefone or not email or not salario:
        return jsonify({'error': 'Nome, especialidade, telefone, email e salário são obrigatórios'}), 400

    funcionario = Funcionario(nome=nome, especialidade=especialidade, telefone=telefone, email=email, salario=salario)
    db.session.add(funcionario)
    db.session.commit()

    return jsonify({'message': 'Funcionário criado com sucesso'}), 201

def listar_funcionarios():
    funcionarios = Funcionario.query.all()
    funcionarios_json = [funcionario.to_json() for funcionario in funcionarios]
    return jsonify(funcionarios_json), 200

def obter_funcionario(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
    if not funcionario:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    return jsonify(funcionario.to_json()), 200

def atualizar_funcionario(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
    if not funcionario:
        return jsonify({'error': 'Funcionário não encontrado'}), 404

    data = request.get_json()
    nome = data.get('nome')
    especialidade = data.get('especialidade')
    telefone = data.get('telefone')
    email = data.get('email')
    salario = data.get('salario')

    if nome:
        funcionario.nome = nome
    if especialidade:
        funcionario.especialidade = especialidade
    if telefone:
        funcionario.telefone = telefone
    if email:
        funcionario.email = email
    if salario:
        funcionario.salario = salario

    db.session.commit()
    return jsonify({'message': 'Funcionário atualizado com sucesso'}), 200

def deletar_funcionario(funcionario_id):
    funcionario = Funcionario.query.get(funcionario_id)
    if not funcionario:
        return jsonify({'error': 'Funcionário não encontrado'}), 404
    db.session.delete(funcionario)
    db.session.commit()
    return jsonify({'message': 'Funcionário deletado com sucesso'}), 200