from flask import Flask
from flask_cors import CORS
from database import db
from routes import api

class App:
    def __init__(self):
        self.app = Flask(__name__)
        self.configure_app()
        self.register_blueprints()
        self.create_tables()

    def configure_app(self):
        CORS(self.app)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/barbearia'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        db.init_app(self.app)

    def register_blueprints(self):
        self.app.register_blueprint(api)

    def create_tables(self):
        with self.app.app_context():
            db.create_all()

    def run(self):
        self.app.run(debug=True)

if __name__ == '__main__':
    app = App()
    app.run()