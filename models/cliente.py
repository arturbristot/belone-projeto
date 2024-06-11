from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Cliente(db.Model):
    def to_dict(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'telefone':self.telefone,
            'email':self.email,
        }
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    

    #cargo = relationship('Cargos', backref='cliente')

    def __init__(self, id ,nome, telefone, email):
        self.id = id
        self.nome = nome
        self.telefone = telefone
        self.email = email

        