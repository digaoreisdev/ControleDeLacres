import sqlite3
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Configuração do banco de dados
DATABASE = 'temp_database.db'

# Variável global para armazenar o email do usuário logado
global_email = None

# Rota da página de login
@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    global global_email  # Acessa a variável global
    error_message = ""
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        # Conectar-se ao banco de dados
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        
        # Buscar informações do usuário no banco de dados
        cursor.execute("SELECT senha, nivel_permissoes, email FROM usuarios WHERE nome=?", (username,))
        user_data = cursor.fetchone()
        
        if user_data and user_data[0] == password:
            nivel = user_data[1]
            global_email = user_data[2]  # Armazena o email na variável global
            return redirect(url_for('dashboard', nivel=nivel))
        else:
            error_message = "Verifique usuário e senha e tente novamente"
        
        conn.close()
        
    return render_template('login.html', error_message=error_message)

# Rota da página de dashboard
@app.route('/dashboard/<nivel>')
def dashboard(nivel):
    return render_template('dashboard.html', nivel=nivel, email=global_email)  # Passa o email para a página

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

@app.route('/cadastro_lojas', methods=['GET', 'POST'])
def cadastro_lojas():
    # Lógica para cadastrar lojas
    # ...
    return render_template('cadastroLojas.html')

@app.route('/cadastro_veiculos', methods=['GET', 'POST'])
def cadastro_veiculos():
    # Lógica para cadastrar veiculos
    # ...
    return render_template('cadastroVeiculos.html')

@app.route('/cadastro_conferentes', methods=['GET', 'POST'])
def cadastro_conferentes():
    # Lógica para cadastrar conferentes
    # ...
    return render_template('cadastroConferentes.html')

if __name__ == '__main__':
    app.run(debug=True)
