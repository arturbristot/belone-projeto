from ..database import db

class Agendamento(db.Model):
    __tablename__ = 'agendamentos'

    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'), nullable=False)
    funcionario_id = db.Column(db.Integer, db.ForeignKey('funcionarios.id'), nullable=False)
    servico_id = db.Column(db.Integer, db.ForeignKey('servicos.id'), nullable=False)
    data_agendamento = db.Column(db.DateTime, nullable=False)
    observacoes = db.Column(db.Text)

    cliente = db.relationship('Cliente', backref='agendamentos')
    funcionario = db.relationship('Funcionario', backref='agendamentos')
    servico = db.relationship('Servico', backref='agendamentos')

    def __repr__(self):
        return f'<Agendamento {self.id}>'

    def to_json(self):
        return {
            'id': self.id,
            'cliente_id': self.cliente_id,
            'funcionario_id': self.funcionario_id,
            'servico_id': self.servico_id,
            'data_agendamento': self.data_agendamento.isoformat() if self.data_agendamento else None, 
            'observacoes': self.observacoes
        }