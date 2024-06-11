from database import db

class Cliente(db.Model):
    __tablename__ = 'clientes'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    telefone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f'<Cliente {self.id}>'

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'telefone': self.telefone,
            'email': self.email
        }