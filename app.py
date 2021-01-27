
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL,MySQLdb
import bcrypt
from modules import img, comb

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'flaskdb'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'
mysql = MySQL(app)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login',methods=["GET","POST"])
def login():
    try:
        if request.method == 'POST':
            email = request.form['email']
            password = request.form['password'].encode('utf-8')

            curl = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
            curl.execute("SELECT * FROM users WHERE email=%s",(email,))
            user = curl.fetchone()
            curl.close()

            if len(user) > 0:
                if bcrypt.hashpw(password, user["password"].encode('utf-8')) == user["password"].encode('utf-8'):
                    session['name'] = user['name']
                    session['email'] = user['email']
                    return render_template("pass_check.html")
                else:
                    return "Error password and email not match"
            else:
                return "Error user not found"
        else:
            return render_template("login.html")
    except:
        return render_template("login.html") 



@app.route('/logout', methods=["GET", "POST"])
def logout():
    session.clear()
    return render_template("soon.html")



@app.route('/register', methods=["GET", "POST"])
def register():
    try:
        if request.method == 'GET':
            return render_template("register.html")
        else:
            name = request.form['name']
            email = request.form['email']
            password = request.form['password'].encode('utf-8')

            # Hashing the password
            hash_password = bcrypt.hashpw(password, bcrypt.gensalt())

            # Image creation
            rec = img.create_image(email)
            
            if rec == 1:
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users (name, email, password) VALUES (%s,%s,%s)",(name,email,hash_password,))
                mysql.connection.commit()
                return render_template("msg.html")
            else:
                return render_template("unmsg.html")
    except:
        return render_template("register.html")



if __name__ == '__main__':
    app.secret_key = "^A%DJAJU^JJ123"
    app.run(debug=True)