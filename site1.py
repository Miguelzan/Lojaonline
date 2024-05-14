#importa a biblioteca
from flask import Flask,render_template
from flask_assets import Environment


#cria um site
app = Flask(__name__)

#QUAL LINK VAI FICAR A PAGINA
@app.route("/")

#QUAL SERA A EXIBIÇÃO
def home():
    return render_template('home.html') #importa codigo HTML

#cria um novo link
@app.route('/contato')
def contato():
    return render_template('contato.html')


# qualquer mudança e atualizada automaticamente no site
if __name__ == '__main__':
    app.run(debug=True)