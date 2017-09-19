from flask import Flask, render_template, request, redirect
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
print mysql.query_db("SELECT * FROM data")

@app.route('/')
def index():
    query = "SELECT name, age, DATE_FORMAT(created_at, '%b-%D-%Y') as friends_since FROM data"
    friends = mysql.query_db(query)
    return render_template('index.html',full_friends=friends)

@app.route('/add', methods=['post'])
def add_friend():
    name = request.form['name']
    age = request.form['age']
    query = "INSERT INTO data (name, age, created_at) VALUES ('" + name + "'," + age + ",NOW());"
    mysql.query_db(query)
    return redirect('/')

app.run(debug=True)
