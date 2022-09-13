import random
import string
from flask import render_template, request, redirect
from app import app
import pyodbc
import smtplib
from email.message import EmailMessage


def connection():
    s = 'guideportfolios.database.windows.net'  # Your server name
    d = 'InvServ_DEV' # Database Name
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
            cursor.execute("Select * from dbo.userDetails WHERE name = '" + username + "' AND password = '" + password + "'")
            data = cursor.fetchone()
            conn.close()
            if data:
                print('Login Successful')
                return render_template('userTemplate/user.html')
            else:
                print('Database Error')
                return redirect('/')
        except:
            print('Login Failed')
            return redirect('/')
    return render_template('login.html')


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
                print('User created Successfully')
                return render_template('login.html')
            except:
                print('User not created')
                msg = "Please provide different Value."
                return render_template('login.html')

        else:
            return render_template('login.html')


@app.route('/forgotPassword')
def forgot():
    return render_template('forgotPassword.html')


@app.route('/forgotPassword', methods=['POST', 'GET'])
def forgotPassword():
    if request.method == 'POST' and 'number' in request.form and 'email' in request.form:
        # Create variables for easy access
        number = request.form['number']
        email = request.form['email']
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("Select * from dbo.userDetails WHERE number = '" + number + "' AND email = '" + email + "'")
            success = cursor.fetchone()

            if success:
                lower = string.ascii_lowercase
                upper = string.ascii_uppercase
                symbols = string.punctuation
                num = string.digits
                all = lower + upper + num + symbols
                temp = random.sample(all)
                msg = EmailMessage()
                try:
                    conn = connection()
                    cursor = conn.cursor()
                    cursor.execute("Update dbo.userDetails set password = '" + temp + "' where email = '" + email + "'")
                    conn.commit()
                    forgot = cursor.fetchone()
                    conn.close()
                    if forgot:
                        msg.set_content(
                            "Your new Password is: " + temp + "\n Do not share this password with anyone else. If you "
                                                              "need additional help you may mail to youremail@gmail.com")
                        msg['Subject'] = 'Nepse Master Password Reset'
                        msg['From'] = "nepsemaster@gmail.com"
                        msg['To'] = email
                        # send secret key to mail
                        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
                        server.login("nepsemaster@gmail.com", "$h!$h!r9861")
                        server.send_message(msg)
                        server.send
                        server.quit()
                        print('Database connection done')
                        return render_template('login.html')
                    else:
                        print('Database connection could not be made.')
                        return render_template('forgotPassword.html')
                except:
                    print('Database connection could not be made.')
                    return render_template('forgotPassword.html')
            else:
                msg = "Invalid Email or Phone Number entered"
                print('Invalid credentials')
                return render_template('login.html')
        except:
            return render_template('login.html')
    return render_template('login.html')
# def databaseTest():
#     users = []
#     conn = connection()
#     cursor = conn.cursor()
#     cursor.execute("SELECT * FROM dbo.userDetails")
#     for row in cursor.fetchall():
#         users.append({"id": row[0], "name": row[1], "number": row[2], "email": row[3], "password": row[4]})
#     conn.close()
#     return render_template('dashboard.html', users=users)
#



# Select [Date],
# Price,
# [Name],
# Instrument,
# CASE
# WHEN LAG(Instrument, 1) over (order by Instrument, [Date]) <> Instrument THEN Null
# ELSE (Price/100)/(Lag(Price/100, 1) over (order by Instrument, [Date])) -1 END as [Returns]
#
#
#
# from [dbo].[FACT_PRICE_DATA]
# where DimIndexKey in (44, 34, 18)
