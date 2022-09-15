from flask import render_template,redirect
from app import app, userView

conn = userView.connection()
cursor = conn.cursor()


def database():
    cursor.execute("select * from dbo.userDetails where isAdmin=0")
    global data
    data = cursor.fetchall()


@app.route("/manageUsers")
def user_management():
    database()
    return render_template("adminTemplate/manageUsers.html", data=data)


# Performing Delete Function
@app.route("/delete/<num>", methods=['POST', 'GET'])
def userDelete(num):
    cursor.execute("Delete from dbo.userDetails where number='" + num + "'")
    conn.commit()
    database()
    return redirect("manageUsers")



