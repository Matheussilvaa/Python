from flask import Flask

# Criando uma instância da aplicação Flask
app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return 'Bem-vindo ao meu site!'

# Executar a aplicação
if __name__ == '__main__':
    app.run(debug=True)
