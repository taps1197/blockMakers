#This is the main.py of our project 

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def run_app():
    return render_template("index.html",title='My first app', content='Hello there')


