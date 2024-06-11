from database import db

class Servico(db.Model):
    __tablename__ = 'servicos'

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(255), nullable=False)
    descricao = db.Column(db.Text, nullable=False)
    preco = db.Column(db.Float, nullable=False)
    data = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Servico {self.id}>'

    def to_json(self):
        return {
            'id': self.id,
            'nome': self.nome,
            'descricao': self.descricao,
            'preco': self.preco,
            'data': self.data.isoformat() if self.data else None 
        }