from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Server Works!'

@app.route('/great')
def say_hello():
    return 'Hello from server'
