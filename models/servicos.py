from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Servicos(db.Model):
    def to_dict(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'descricao':self.descricao,
            'preco':self.preco,
            'data':self.data,
        }
    
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    descricao = db.Column(db.String(100))
    preco = db.Column(db.Float)
    data = db.Column(db.DateTime)
    

    #cargo = relationship('Cargos', backref='cliente')

    def __init__(self, id ,nome, descricao, preco, data):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.data = data
        