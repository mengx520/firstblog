from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('home.html')

@app.route('/about')
def about():
    return 'About'

@app.route('/learn')
def recipe():
    return 'Learn'

@app.route('/food')
def food():
    return 'Food'

@app.route('/photo')
def photo():
    return 'Photo'

@app.route('/art')
def art():
    return 'Art'

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', username=name)
