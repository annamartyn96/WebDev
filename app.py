#Viewing all, filtering and adding a record to and from database
from flask import Flask, render_template, request, redirect, url_for, session
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app = Flask(__name__)
app.secret_key = 'mysecretkey'

#For Workbench use 'localhost' 
#For editor.computing use 'student.computing.dcu.ie'
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='Anna.is.Smart'
app.config['MYSQL_DB']='members'

mysql = MySQL(app)




 #This function will retrieve all data from database
@app.route('/', methods=['GET', 'POST'])
def all():
    cur = mysql.connection.cursor()
    query1 = "SELECT * FROM members.project"
    cur.execute(query1)
    output = cur.fetchall()
    mysql.connection.commit()
    cur.close()

    return render_template('all.html', data=output)




#@app.route('/login', methods =['GET', 'POST'])
#def login():
    #msg = ''
    #if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
       # email = request.form['email']
       # password = request.form['password']
        #cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        #cursor.execute('SELECT * FROM members.project WHERE email = % s AND password = % s', (email, password, ))
        #account = cursor.fetchone()
       # if account:
            #session['loggedin'] = True
           # session['password'] = account['password']
            #session['email'] = account['email']
            #return render_template('profile.html', msg = msg)
       # else:
           # msg = 'Incorrect username / password !'
 #   return render_template('login.html', msg = msg)





@app.route('/signup', methods=['GET', 'POST'])
def signup():
    msg = ''
    
    if request.method == 'POST':
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        query1 = "INSERT INTO members.project (firstname, lastname, email, password) VALUES (%s, %s, %s, %s)" 
        cur.execute(query1, (firstname, lastname, email, password))
        mysql.connection.commit()
        cur.close()
        return render_template('success.html',)
        
    
    return render_template('signup.html',)




@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        cur = mysql.connection.cursor()
        query1 = "SELECT * FROM members.project WHERE email=%s AND password=%s"
        cur.execute(query1, (email, password))
        output = cur.fetchall()
        mysql.connection.commit()
        cur.close()
        return render_template('profile.html', data=output)
    
    return render_template('login.html')




#Use if in localhost environment
if __name__=='__main__':
    app.run(debug=True)

#Use in editor.computing.dcu.ie environment
#if __name__=='__main__':   
    #app.run(host='0.0.0.0', port='8080', debug=True)