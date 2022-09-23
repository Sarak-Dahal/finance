from flask import render_template, request
from app import app, userView

conn = userView.connection()
cursor = conn.cursor()


def database():
    global data
    # cursor.execute("select Top 100 * from dbo.dim_manager")
    cursor.execute("select * from dbo.dim_manager where recordstatus='open' and currentindicator =1")
    data = cursor.fetchall()

def databaseDataTable():
    global dataTable
    cursor.execute(
        "select * from dbo.dim_manager where Domicile='New Zealand' and AssetType='Equity' and GeographyFocus='Global'")
    dataTable = cursor.fetchall()


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
        database()
        databaseDataTable()
        return render_template('userTemplate/createSession.html', data=data,dataTable=dataTable)


@app.route('/createSession', methods=['GET', 'POST'])
def filterTable():
    database()

    domicle = request.form.get('domicle')
    assetsType = request.form.get('assetsType')
    geoFocus = request.form.get('geoFocus')
    lipperGlobal = request.form.get('lipperGlobal')

    print(domicle)
    print(assetsType)
    print(geoFocus)
    print(lipperGlobal)
    cursor.execute("select * from dbo.dim_manager where Domicile='"+domicle+"' and AssetType='"+assetsType+"' and GeographyFocus='"+geoFocus+"' and LipperGlobalClassification='"+lipperGlobal+"'")
    dataTable = cursor.fetchall()

    return render_template('userTemplate/createSession.html', data=data, dataTable=dataTable)


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
    if not userView.session['loggedIn']:
        msg = "You Must Login to access the Page"
        color = 'red'
        return render_template("login.html", msg=msg, color=color)
    else:
        return render_template('userTemplate/user.html')
