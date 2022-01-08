#wymaga instalacji flaska za pomocą polecenia "pip install flask"
from flask import Flask, render_template, url_for, request, flash
import pymysql

admin_login = "admin"
admin_password = "P4ssvv0rd!"

app = Flask(__name__)
connection = pymysql.connect(host="czytnik-rfid.mysql.database.azure.com",
                             user="_Root_2022@czytnik-rfid", password="Qwerty^%4321", database="mysql",
                             charset="utf8mb4",
                             cursorclass=pymysql.cursors.DictCursor)


@app.route("/", methods=['GET', 'POST'])
def main_page():
    return render_template("start.html")


@app.route("/database", methods=['POST', 'GET'])
def db_control_panel():
    login = request.form['login']
    password = request.form['password']
    if login.__eq__(admin_login) and password.__eq__(admin_password):
        return render_template("index.html")
    else:
        flash("Credential error!!!")
        return render_template("start.html")


@app.route("/add-rfid-card")
def add_rfid():
    return render_template("add_rfid.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
