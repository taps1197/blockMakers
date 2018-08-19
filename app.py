#This is the main.py of our project 

from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def RunApp():
    return render_template("patient.html",title='My first app', content='Hello there',site='127.0.0.1:5000')

@app.route('/videochat')
def VideoChat():
    return render_template("videochat.html",title='Video Chat platform')




if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
