# app/models/__init__.py
from .agendamento import Agendamento
from .cliente import Cliente
from .funcionario import Funcionario
from .servico import Servico

# app/database/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

