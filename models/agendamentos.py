from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Agendamentos(db.Model):
    def to_dict(self):
        return {
            'id':self.id,
            'cliente_id':self.cliente_id,
            'funcionario_id':self.funcionario_id,
            'servico_id':self.servico_id,
            'data_agendamento':self.data_agendamento,
            'observacoes':self.observacoes,
        }
    id = db.Column(db.Integer, primary_key=True)
    #id = db.Column(ForeignKey('cargos.id'))
    
    cliente_id = db.Column(db.Integer, ForeignKey('cliente.id'))
    funcionario_id = db.Column(db.Integer, ForeignKey('funcionario.id'))
    servico_id = db.Column(db.Integer, ForeignKey('servico.id'))
    data_agendamento = db.Column(db.DateTime)
    observacoes = db.Column(db.String(100))
    

    cliente = relationship('cliente', backref='agendamentos')
    funcionarios = relationship('funcionarios', backref='agendamentos')
    servicos = relationship('servicos', backref='agendamentos')

    def __init__(self, id ,cliente_id, funcionario_id, servico_id, data_agendamento, observacoes):
        self.id = id
        self.cliente_id = cliente_id
        self.funcionario_id = funcionario_id
        self.servico_id = servico_id
        self.data_agendamento = data_agendamento
        self.observacoes = observacoes
        