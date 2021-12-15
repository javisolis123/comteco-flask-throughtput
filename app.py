from flask import Flask, render_template, redirect, url_for, request, jsonify, make_response
from routes.routes import rutas
from flask_sqlalchemy import SQLAlchemy



app = Flask(__name__)

app.secret_key = "Frida12"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://admin:javiersolis@localhost/comteco'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
SQLAlchemy(app)
app.register_blueprint(rutas)



