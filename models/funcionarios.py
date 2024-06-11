from database.db import db
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

class Funcionarios(db.Model):
    def to_dict(self):
        return {
            'id':self.id,
            'nome':self.nome,
            'especialidade':self.especialidade,
            'telefone':self.telefone,
            'email':self.email,
            'salario':self.salario,
        }
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100))
    especialidade = db.Column(db.String(100))
    telefone = db.Column(db.String(100))
    email = db.Column(db.String(100))
    salario = db.Column(db.Float)
    

    #cargo = relationship('Cargos', backref='cliente')

    def __init__(self, id ,nome, especialidade, telefone, email, salario):
        self.id = id
        self.nome = nome
        self.especialidade = especialidade
        self.telefone = telefone
        self.email = email
        self.salario = salario
        