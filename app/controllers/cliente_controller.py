from flask import jsonify, request
from models import Cliente
from database import db

class ClienteController:
    def criar_cliente():
        data = request.get_json()
        nome = data.get('nome')
        telefone = data.get('telefone')
        email = data.get('email')

        if not nome or not telefone or not email:
            return jsonify({'error': 'Nome, telefone e email são obrigatórios'}), 400

        cliente = Cliente(nome=nome, telefone=telefone, email=email)
        db.session.add(cliente)
        db.session.commit()

        return jsonify({'message': 'Cliente criado com sucesso'}), 201

    def listar_clientes():
        clientes = Cliente.query.all()
        clientes_json = [cliente.to_json() for cliente in clientes]
        return jsonify(clientes_json), 200

    def obter_cliente(cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        return jsonify(cliente.to_json()), 200

    def atualizar_cliente(cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente não encontrado'}), 404

        data = request.get_json()
        nome = data.get('nome')
        telefone = data.get('telefone')
        email = data.get('email')

        if nome:
            cliente.nome = nome
        if telefone:
            cliente.telefone = telefone
        if email:
            cliente.email = email

        db.session.commit()
        return jsonify({'message': 'Cliente atualizado com sucesso'}), 200

    def deletar_cliente(cliente_id):
        cliente = Cliente.query.get(cliente_id)
        if not cliente:
            return jsonify({'error': 'Cliente não encontrado'}), 404
        db.session.delete(cliente)
        db.session.commit()
        return jsonify({'message': 'Cliente deletado com sucesso'}), 200