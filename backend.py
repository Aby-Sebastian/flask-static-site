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
  database='opnlabs'
)
print('database connected')
print(mydb) 
mycursor = mydb.cursor()

#data insertion
@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':
		data = request.form['id_email'] #data collects from html form 
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
	return render_template('research.html')

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