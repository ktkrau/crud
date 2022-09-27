from flask import Flask, render_template, request, redirect
#importando la clase de USUARIO para poder utilizar sus funciones
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    #Recibimos el formulario a través de una variable llamada request.form
    #request.form = {"first_name":"Juana", "last_name":"De Arco" etc etc}
    User.guardar(request.form)
    return redirect('/')




if __name__ =="__main__":
    app.run(debug=True)
