import random
import string
from flask import render_template, request, redirect
from app import app
import pyodbc


def connection():
    s = 'guideportfolios.database.windows.net'  # Your server name
    d = 'InvServ_DEV'
    u = 'guideadmin'  # Your login
    p = 'Tbg963369@'  # Your login password
    cstr = 'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + s + ';DATABASE=' + d + ';UID=' + u + ';PWD=' + p
    conn = pyodbc.connect(cstr)
    return conn


@app.route('/')
def login():
    return render_template('login.html')


@app.route('/login', methods=['POST', 'GET'])
def webLogin():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute('''Select * FROM dbo.userDetails WHERE (Name = '?') and (Pass ='?') ''', username, password)
            conn.close()
            return redirect('dashboard')
        except:
            return redirect('login')
    return render_template('login.html')


def databaseTest():
    users = []
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.userDetails")
    for row in cursor.fetchall():
        users.append({"id": row[0], "name": row[1], "number": row[2], "email": row[3], "password": row[4]})
    conn.close()
    return render_template('dashboard.html', users=users)


@app.route('/signup', methods=['POST', 'GET'])
def signUp():
    if request.method == 'POST' and 'username' in request.form and 'email' in request.form:
        if 'number' in request.form and 'password' in request.form:
            try:
                nam = request.form['username']
                ema = request.form['email']
                num = request.form['number']
                pas = request.form['password']
                conn = connection()
                cursor = conn.cursor()
                cursor.execute('''Insert into dbo.userDetails (Name,Number,Email,Password) VALUES(?,?,?,?)''', nam, ema,
                               num, pas)
                conn.commit()
                conn.close()
                return redirect('login')
            except:
                msg = "Please provide different Value."
                return render_template('login.html')

        else:
            return render_template('login.html')


@app.route('/forgotPassword')
def forgot():
    return render_template('forgotPassword.html')


@app.route('/login', methods=['POST', 'GET'])
def forgotPassword():
    if request.method == 'POST' and 'number' in request.form and 'email' in request.form:
        # Create variables for easy access
        number = request.form['number']
        email = request.form['email']
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute('''Select * FROM dbo.userDetails WHERE (Name = '?') and (Pass ='?') ''', number, email)
            success = cursor.fetchone()

            if success:
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                symbols = string.punctuation
                num =string.digits
                all = lower+upper+num+symbols
                temp = random.sample(all)
            else:
                msg = "Invalid Email or Phone Number entered"
            conn.close()
            return redirect('dashboard')
        except:
            return redirect('login')
    return render_template('login.html')