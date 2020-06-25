from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home_page():
	return render_template('home.html')

@app.route('/about')
def about():
	return 'About'

@app.route('/recipe')
def recipe():
	return 'Recipe'

@app.route('/hello/<name>')
def hello(name):
	return render_template('hello.html', username=name)
