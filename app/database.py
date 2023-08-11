from flask import g, current_app
import sqlite3
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['SQLALCHEMY_DATABASE_URI'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row
    
    return g.db

def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

def init_db():
    """Inicializa o banco de dados."""
    db.drop_all()
    db.create_all()
    print('Banco de dados inicializado.')

def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)

