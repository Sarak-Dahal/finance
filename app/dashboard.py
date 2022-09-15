from flask import render_template
from app import app, userView


@app.route('/home')
def home():
    print(userView.session['loggedIn'])
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/home.html')

@app.route('/dataAnalytics')
def dataAnalytics():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/dataAnalytics.html')


@app.route('/portfolioSessions')
def portfolioSessions():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/portfolioSessions.html')


@app.route('/createSession')
def createSession():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/createSession.html')

@app.route('/monteCarlo')
def monteCarlo():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/monteCarlo.html')


@app.route('/regimeChanging')
def regimeChanging():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/regimeChanging.html')


@app.route('/portfolioReview')
def portfolioReview():
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/portfolioReview.html')


@app.route('/user')
def dashboardUser():
    if userView.session['loggedIn'] == False:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/user.html')
