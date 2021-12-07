from logging import debug
from os import stat, stat_result
from flask import Flask, render_template, request, flash
from flask.wrappers import Request
from flask_sqlalchemy import SQLAlchemy
import psycopg2

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres:itcj@localhost/tiendas_api"
db = SQLAlchemy(app)


class Tiendas(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))
    direccion = db.Column(db.String(120))
    city = db.Column(db.String(120))
    state = db.Column(db.String(80))
    phone = db.Column(db.Integer())

    def __init__(self, name, direccion, city, state, phone):
        self.name = name
        self.direccion = direccion
        self.city = city
        self.state = state
        self.phone = phone

connection = psycopg2.connect(database="tiendas_api", user="postgres", password="itcj")  

@app.route('/')
def home():
    cursor=connection.cursor()
    cursor.execute('SELECT * FROM public.tiendas')
    data = cursor.fetchall()
    return render_template("index.html", tiendas = data)


@app.route("/datosC", methods = ['GET'])
def datos():
    curC = connection.cursor()
    curC.execute("SELECT * FROM public.tiendas WHERE state = 'Chihuahua'")
    data = curC.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/datosS", methods = ['GET'])
def datosSonora():
    curS = connection.cursor()
    curS.execute("SELECT * FROM public.tiendas WHERE state = 'Sonora'")
    data = curS.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/datosT", methods = ['GET'])
def datosTabasco():
    curT = connection.cursor()
    curT.execute("SELECT * FROM public.tiendas WHERE state = 'Tabasco'")
    data = curT.fetchall()
    return render_template("index.html", tiendas = data)

@app.route("/datosN", methods = ['GET'])
def datosNuevo():
    curN = connection.cursor()
    curN.execute("SELECT * FROM public.tiendas WHERE state = 'Nuevo Leon'")
    data = curN.fetchall()
    return render_template("index.html", tiendas = data)
    

if __name__ == '__main__':
    app.run(debug = True)