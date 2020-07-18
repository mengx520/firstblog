from flask import Flask
from flask import render_template


app = Flask(__name__)
body = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
@app.route('/')
def home_page():
    return render_template('base.html', title='Home', content=body)

@app.route('/about')
def about():
    return render_template('base.html', title='About', content=body)

@app.route('/learn')
def recipe():
    return render_template('base.html', title='Learn', content=body)

@app.route('/food')
def food():
    return render_template('base.html', title='Food', content=body)

@app.route('/photo')
def photo():
    return render_template('base.html', title='Photo', content=body)

@app.route('/art')
def art():
    return render_template('home.html', title='Art', content=body)

@app.route('/hello/<name>')
def hello(name):
    return render_template('hello.html', username=name)
