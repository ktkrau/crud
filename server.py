from flask import Flask, render_template, request, redirect
#importando la clase de USUARIO para poder utilizar sus funciones
from users import User

app = Flask(__name__)

@app.route('/')
def index():
    users = User.muestra_usuario()
    return render_template('index.html', usuarios=users)

@app.route('/new')
def new():
    return render_template('new.html')

@app.route('/create', methods=['POST'])
def create():
    #Recibimos el formulario a través de una variable llamada request.form
    #request.form = {"first_name":"Juana", "last_name":"De Arco" etc etc}
    User.guardar(request.form)
    return redirect('/')

@app.route('/delete/<int:id>')
def delete(id):
    formulario = {"id": id} #diccionario que le ponemos formulario como nombre de variable
    User.borrar(formulario)
    return redirect('/')

@app.route('/edit/<int:id>')
def edit(id):
    formulario = {"id":id}
    user = User.mostrar(formulario) #Instancia de usuario basado en el id de la url
    return render_template('edit.html', usuario = user)

@app.route('/update', methods=['POST'])
def update():
    #request.form = diccionario con el formulario de edit.html
    User.actualizar(request.form)
    return redirect('/')




if __name__ =="__main__":
    app.run(debug=True)
