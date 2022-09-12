from flask import render_template
from app import app


@app.route('/home')
def home():
    return render_template('userTemplate/home.html')


@app.route('/user')
def dashboardUser():
    return render_template('userTemplate/user.html')



@app.route('/logout')
def logout():
    return render_template('login.html')