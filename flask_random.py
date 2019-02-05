from flask import Flask, request
app = Flask(__name__)

from random import randint

Number = randint(0,100)

@app.route('/')
def inicio():
    return str(Number) + "<body style='top: 0; left: 0; margin: auto; display: table; background-color: red; text-align: center;'><form action='result' method='post'><h3>Introdueix un numero</h3><input type='num' name='Number'></input><input type='submit' value='Enviar'/></form></body>"

@app.route('/result', methods= ['POST'])
def result():
	error = None
	if request.method == 'POST':
		if request.form['Number'] != str(Number):
    			return "<img src='https://art.pixilart.com/879b72409e998f6.gif' style='display: block; width: 99%; height: 97%;'>"
		else:
    			return "<img src='https://media.giphy.com/media/ZcUGu59vhBGgbBhh0n/giphy.gif' style='display: block; width: 99%; height: 97%;'>"