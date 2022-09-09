from flask import render_template, request
from app import app

@app.route('/')
def login():
    return render_template('login.html')
@app.route('/',methods = ['POST', 'GET'])
def webLogin():
    return render_template('login.html')

