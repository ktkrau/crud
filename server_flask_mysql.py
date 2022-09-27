#pipenv install flask pymysql
#este server es el que usamos para ver la union con mysql
from flask import Flask, render_template, request, redirect

from mysqlconnection import connectToMySQL

app = Flask(__name__)


@app.route('/')
def index():
    query = "SELECT * FROM users"
    results = connectToMySQL('esquema_usuarios').query_db(query)
    return results

@app.route('/insertar')
def insertar():
    data = {
        "first_name": "Juana",
        "last_name": "De Arco",
        "email": "juana@codingdojo.com"
    }
    #INTERPOLACION: %(LLAVE)s
    query = "INSERT INTO users(first_name, last_name, email) VALUES( %(first_name)s , %(last_name)s, %(email)s )"
    result = connectToMySQL('esquema_usuarios').query_db(query, data)
    return data['first_name']+" registrada"





if __name__== "__main__":
    app.run(debug=True)

