from flask import Flask
from flask_cors import CORS
from .database import db

def create_app():
    app = Flask(__name__)
    CORS(app)

    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/barbearia'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    with app.app_context():
        db.create_all()

    # Importa o blueprint e inicializa as rotas
    from .routes import api, init_app 
    app.register_blueprint(api)
    init_app(app) 

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)