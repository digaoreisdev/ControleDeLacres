from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import click
from flask.cli import with_appcontext
from app.database import db, init_db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# Registrar o comando na aplicação Flask
@click.command('init-db')
@with_appcontext
def init_db_command():
    init_db()
    click.echo('Banco de dados inicializado.')

# Adicionar o comando à aplicação Flask
app.cli.add_command(init_db_command)

# Importar e registrar rotas após a criação da aplicação
from app.routes import *

if __name__ == '__main__':
    app.run(debug=True)