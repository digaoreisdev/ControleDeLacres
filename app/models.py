from app import db

class Usuario(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    nivel_permissoes = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    chave_id_loja = db.Column(db.Integer, db.ForeignKey('loja.id'))

class Loja(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    endereco = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    usuarios = db.relationship('Usuario', backref='loja')

class Veiculo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    placa = db.Column(db.String(10), nullable=False)
    # Outros campos do veículo

class Conferente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    # Outros campos do conferente

# Adicione outras classes de modelos conforme necessário
