# python.exe -m venv .venv
# cd .venv/Scripts
# activate.bat
# py -m ensurepip --upgrade
# pip install -r requirements.txt

from flask import Flask

from flask import render_template
from flask import request
from flask import jsonify, make_response

import mysql.connector

import datetime
import pytz

from flask_cors import CORS, cross_origin

con = mysql.connector.connect(
    host="82.197.82.90",
    database="u861594054_jsHTF",
    user="u861594054_m33Rt",
    password="cY!5R/r?LJ9"
)

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return render_template("index.html")

@app.route("/app")
def app2():
    if not con.is_connected():
        con.reconnect()

    con.close()

    return "<h5>Hola, soy la view app</h5>"

@app.route("/decoraciones")
def decoraciones():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """
    SELECT idDecoracion,
           nombreMaterial

    FROM decoraciones

    """

    cursor.execute(sql)
    registros = cursor.fetchall()
    print(registros)
    return render_template("decoraciones.html", decoraciones=registros)

@app.route("/paquetes")
def paquetes():
    if not con.is_connected():
        con.reconnect()

    cursor = con.cursor(dictionary=True)
    sql    = """
    SELECT idPaquete,
           Clave,
           idDecoracion,
           Cantidad,
           Precio,
           INNER JOIN  decoraciones ON decoraciones.idDecoracion = paquetes.idDecoracion

    FROM paquetes

    """

    cursor.execute(sql)
    registros = cursor.fetchall()
    print(registros)
    return render_template("paquetes.html", paquetes=registros)
