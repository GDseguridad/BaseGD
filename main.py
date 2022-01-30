from flask import Flask, app, render_template, request, redirect, url_for, session, flash
from flask_mysqldb import MySQL
import MySQLdb.cursors
import re

app= Flask(__name__)
app.secret_key = 'mysecretkey'

#Conexion a la base SQL
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Admind1lm3'
app.config['MYSQL_DB'] = 'pythonlogin'

#Initialize MySQL
mysql = MySQL(app)


@app.route('/gdapp/', methods=['GET', 'POST'])
def login():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username" and "password" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s AND password = %s', (username, password,))
        # Fetch one record and return result
        account = cursor.fetchone()
        # If account exists in accounts table in out database
        if account:
            # Create session data, we can access this data in other routes
            session['loggedin'] = True
            session['id'] = account['id']
            session['username'] = account['username']
            # Redirect to home page
            return redirect(url_for('home'))
        else:
            # Account doesnt exist or username/password incorrect
            msg = 'Incorrect username/password!'
    # Show the login form with message (if any)
    return render_template('index.html', msg=msg)






# http://localhost:5000/python/logout - this will be the logout page
@app.route('/gdpp/Salir')
def logout():
    # Remove session data, this will log the user out
   session.pop('loggedin', None)
   session.pop('id', None)
   session.pop('username', None)
   # Redirect to login page
   return redirect(url_for('login'))





# http://localhost:5000/pythinlogin/register - this will be the registration page, we need to use both GET and POST requests
@app.route('/gdapp/registro', methods=['GET', 'POST'])
def register():
    # Output message if something goes wrong...
    msg = ''
    # Check if "username", "password" and "email" POST requests exist (user submitted form)
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form and 'email' in request.form:
        # Create variables for easy access
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        # Check if account exists using MySQL
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT * FROM accounts WHERE username = %s', (username,))
        account = cursor.fetchone()
        # If account exists show error and validation checks
        if account:
            msg = 'Account already exists!'
        elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
            msg = 'Invalid email address!'
        elif not re.match(r'[A-Za-z0-9]+', username):
            msg = 'Username must contain only characters and numbers!'
        elif not username or not password or not email:
            msg = 'Please fill out the form!'
        else:
            # Account doesnt exists and the form data is valid, now insert new account into accounts table
            cursor.execute('INSERT INTO accounts VALUES (NULL, %s, %s, %s)', (username, password, email,))
            mysql.connection.commit()
            msg = 'You have successfully registered!'
    elif request.method == 'POST':
        # Form is empty... (no POST data)
        msg = 'Please fill out the form!'
    # Show registration form with message (if any)
    return render_template('register.html', msg=msg)





# http://localhost:5000/gdapp/home - this will be the home page, only accessible for loggedin users
@app.route('/gdapp/home')
def home():
    # Check if user is loggedin
    if 'loggedin' in session:
        # User is loggedin show them the home page
        return render_template('home.html', username = session['username'])
    # User is not loggedin redirect to login page
    return redirect(url_for('login'))

#Ruta para la toma de asistencias
@app.route('/gdapp/asistencia')
def asistencia():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts')
    data = cur.fetchall()
    cur.close()
    return render_template('asistencia.html', contacts = data) 



@app.route('/gdapp/asistencia_add', methods =['POST', 'GET'] )
def asistencia_add():

    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO contacts (fullname, phone, email) VALUES (%s, %s, %s)',
        (fullname, phone, email))
        mysql.connection.commit()
        flash('Se agrego con exito')
        return redirect(url_for('asistencia'))


@app.route('/gdapp/eliminar/<id>', methods = ['GET'])
def eliminar(id):
          cur = mysql.connection.cursor()
          cur.execute('DELETE FROM contacts WHERE id = {0}' . format(id)) 
          mysql.connection.commit()
          flash('Se removio el contacto')
          return redirect(url_for('asistencia'))

@app.route('/gdapp/editar/<id>')
def editar(id):
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM contacts WHERE id = %s', id)
    data = cur.fetchall()
    return render_template('editar.html', contact = data[0])

@app.route('/gdapp/actualizar/<id>', methods = ['POST'])
def actualizar(id):
    if request.method == 'POST':
        fullname = request.form['fullname']
        phone = request.form['phone']
        email = request.form['email']
    cur = mysql.connection.cursor()
    cur.execute("""
    UPDATE contacts
    SET fullname = %s,
        email = %s, 
        phone = %s
    WHERE id = %s
    """, (fullname, email, phone, id))
    mysql.connection.commit()
    flash('Contacto actualizado')
    return redirect(url_for('asistencia'))


if __name__ == '__main__':
    app.run(port=5000, debug=True)