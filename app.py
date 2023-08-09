from flask import Flask, render_template

app = Flask(__name__)

# Rota da página de login
@app.route('/')
@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)