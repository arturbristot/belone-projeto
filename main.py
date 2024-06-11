from flask import Flask, render_template, request

from models.servicos import Servicos, db


class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@localhost/barbearia'
        db.init_app(self.app)
        self.defaults_routes() #Pedindo para iniciar as rotas quando abrir
    
    def home (self):
        return render_template('index.html', title = 'Home') #renderizando o template index.html
    
    def servicos_marcados(self):
        servicos = Servicos.query.all()  # Obtendo todos os serviços
        return render_template('servicos_marcados.html', title='Serviços Marcados', servicos=servicos)

    def defaults_routes(self):
        self.app.route('/')(self.home)
        self.app.route('/servicos_marcados', methods=['GET'])(self.servicos_marcados)

    def run(self):
        return self.app.run(port = 3000, host = 'localhost', debug = 'True')
                        
app = App()
app.run()