from flask import jsonify, request
from models import Servico
from database import db

class ServicoController:

    def criar_servico():
        data = request.get_json()
        nome = data.get('nome')
        descricao = data.get('descricao')
        preco = data.get('preco')
        data = data.get('data')

        if not nome or not descricao or not preco or not data:
            return jsonify({'error': 'Nome, descrição, preço e data são obrigatórios'}), 400

        servico = Servico(nome=nome, descricao=descricao, preco=preco, data=data)
        db.session.add(servico)
        db.session.commit()

        return jsonify({'message': 'Serviço criado com sucesso'}), 201


    def listar_servicos():
        servicos = Servico.query.all()
        servicos_json = [servico.to_json() for servico in servicos]
        return jsonify(servicos_json), 200


    def obter_servico(servico_id):
        servico = Servico.query.get(servico_id)
        if not servico:
            return jsonify({'error': 'Serviço não encontrado'}), 404
        return jsonify(servico.to_json()), 200


    def atualizar_servico(servico_id):
        servico = Servico.query.get(servico_id)
        if not servico:
            return jsonify({'error': 'Serviço não encontrado'}), 404

        data = request.get_json()
        nome = data.get('nome')
        descricao = data.get('descricao')
        preco = data.get('preco')
        data = data.get('data')

        if nome:
            servico.nome = nome
        if descricao:
            servico.descricao = descricao
        if preco:
            servico.preco = preco
        if data:
            servico.data = data

        db.session.commit()
        return jsonify({'message': 'Serviço atualizado com sucesso'}), 200


    def deletar_servico(servico_id):
        servico = Servico.query.get(servico_id)
        if not servico:
            return jsonify({'error': 'Serviço não encontrado'}), 404
        db.session.delete(servico)
        db.session.commit()
        return jsonify({'message': 'Serviço deletado com sucesso'}), 200