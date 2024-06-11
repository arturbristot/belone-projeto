from ..database import db

class Funcionario(db.Model):
    __tablename__ = 'funcionarios'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    especialidade = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)
    salario = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Funcionario {self.id}>'

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'especialidade': self.especialidade,
            'telefone': self.telefone,
            'email': self.email,
            'salario': self.salario
        }