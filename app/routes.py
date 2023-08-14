from flask import render_template, request, redirect, url_for
from app import app
from app.database import db
from app.models import Usuario, Loja
import sqlite3

DATABASE = 'temp_database.db'


# Rota da página de login
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Buscar informações do usuário no banco de dados
        cursor.execute("SELECT senha, nivel_permissoes FROM usuarios WHERE nome=?", (username,))
        user_data = cursor.fetchone()
        
        if user_data and user_data[0] == password:
            nivel = user_data[1]
            return redirect(url_for('dashboard', nivel=nivel))
        else:
            error_message = "Verifique usuário e senha e tente novamente"
        
        conn.close()
        
    return render_template('login.html', error_message=error_message)

# Rota da página de dashboard
@app.route('/dashboard/<nivel>')
def dashboard(nivel):
    return render_template('dashboard.html', nivel=nivel)

# Rota para cadastrar usuários
@app.route('/cadastro_usuarios', methods=['GET', 'POST'])
def cadastro_usuarios():
    if request.method == 'POST':
        nome = request.form['nome']
        senha = request.form['senha']
        nivel = request.form['nivel_permissoes']
        email = request.form['email']
        
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Inserir o novo usuário na tabela de usuários
        cursor.execute("INSERT INTO usuarios (nome, senha, nivel_permissoes, email) VALUES (?, ?, ?, ?)",
                       (nome, senha, nivel, email))
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        conn.close()
        
        return redirect(url_for('login'))
    
    return render_template('cadastroUsuarios.html')

# Rota para cadastrar lojas
@app.route('/cadastro_lojas', methods=['GET', 'POST'])
def cadastro_lojas():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        email = request.form['email']
        
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Inserir a nova loja na tabela de lojas
        cursor.execute("INSERT INTO lojas (nome, endereco, email) VALUES (?, ?, ?)",
                       (nome, endereco, email))
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        conn.close()
        
        return redirect(url_for('dashboard', nivel='administrador'))  # Redirecionar para o dashboard

    return render_template('cadastroLojas.html')

# Rota para cadastrar veiculos
@app.route('/cadastro_veiculos', methods=['GET', 'POST'])
def cadastro_veiculos():
    if request.method == 'POST':
        placa = request.form['placa']
        modelo = request.form['modelo']
                
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Inserir a novo veiculo na tabela de veiculos
        cursor.execute("INSERT INTO veiculos (placa, modelo) VALUES (?, ?)",
                       (placa, modelo))
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        conn.close()
        
        return redirect(url_for('dashboard', nivel='administrador'))  # Redirecionar para o dashboard

    return render_template('cadastroVeiculos.html')

# Rota para cadastrar conferentes
@app.route('/cadastro_conferentes', methods=['GET', 'POST'])
def cadastro_conferentes():
    if request.method == 'POST':
        placa = request.form['placa']
        modelo = request.form['modelo']
                
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Inserir a novo veiculo na tabela de veiculos
        cursor.execute("INSERT INTO veiculos (placa, modelo) VALUES (?, ?)",
                       (placa, modelo))
        
        # Confirmar a inserção e fechar a conexão
        conn.commit()
        conn.close()
        
        return redirect(url_for('dashboard', nivel='administrador'))  # Redirecionar para o dashboard

    return render_template('cadastroVeiculos.html')

# Adicione outras rotas e lógica conforme necessário

if __name__ == '__main__':
    app.run(debug=True)
