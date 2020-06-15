from flask import Flask 
app = Flask(__name__)

@app.route('/')
def home_page():
	return 'Home Page'

@app.route('/about')
def about():
	return 'About'

@app.route('/recipe')
def recipe():
	return 'Recipe'

@app.route('/hello/<name>')
def hello(name):
	return 'Hello ' + name
