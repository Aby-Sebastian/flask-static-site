from flask import Flask, render_template, request, url_for
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)

CORS(app)

#database connection
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  
)
print('localhost connected')
print(mydb) 
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS opnlabs")
mycursor.execute("USE opnlabs")
print('database connected')

#data insertion
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		data = request.form['id_email'] #data collects from html form 
		mycursor.execute("CREATE TABLE IF NOT EXISTS UserEmails(id INT PRIMARY KEY NOT NULL auto_increment, emails VARCHAR(50) NOT NULL)")
		mycursor.execute("INSERT INTO UserEmails(emails) VALUES (%s)",(data,)) # collected data gets inserted
		mydb.commit()
		return render_template('Opnlabs.html')
	return render_template('Opnlabs.html')

#page redirecting links
@app.route('/home',methods=['POST','GET'])
def home():
	if request.method == 'POST':
		data = request.form['id_email'] #data collects from html form 
		mycursor.execute("INSERT INTO UserEmails(emails) VALUES (%s)",(data,)) # collected data gets inserted
		mydb.commit()
		return render_template('Opnlabs.html')
	return render_template('Opnlabs.html')

@app.route('/services')
def services():
	return render_template('services.html')

@app.route('/research')
def research():
	mycursor.execute("SELECT * FROM UserEmails")
	data = mycursor.fetchall()
	return render_template('research.html', data=data)

@app.route('/resources')
def resources():
	return render_template('resources.html')

@app.route('/contact')
def contact():
	return render_template('contactus.html')

@app.route('/about')
def about():
	return render_template('aboutus.html')

if __name__ == '__main__':
	app.run()
