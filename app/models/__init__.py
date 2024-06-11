from .agendamento import Agendamento
from .cliente import Cliente
from .funcionario import Funcionario
from .servico import Servico

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

