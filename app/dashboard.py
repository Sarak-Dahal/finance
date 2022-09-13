from flask import render_template
from app import app


@app.route('/home')
def home():
    return render_template('userTemplate/home.html')

@app.route('/dataAnalytics')
def dataAnalytics():
    return render_template('userTemplate/dataAnalytics.html')


@app.route('/portfolioSessions')
def portfolioSessions():
    return render_template('userTemplate/portfolioSessions.html')


@app.route('/createSession')
def createSession():
    return render_template('userTemplate/createSession.html')

@app.route('/monteCarlo')
def monteCarlo():
    return render_template('userTemplate/monteCarlo.html')


@app.route('/regimeChanging')
def regimeChanging():
    return render_template('userTemplate/regimeChanging.html')


@app.route('/portfolioReview')
def portfolioReview():
    return render_template('userTemplate/portfolioReview.html')


@app.route('/user')
def dashboardUser():
    return render_template('userTemplate/user.html')


@app.route('/logout')
def logout():
    return render_template('login.html')

