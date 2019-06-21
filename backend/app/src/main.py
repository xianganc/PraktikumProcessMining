from hadoop import HadoopInteractions
from flask import Flask, render_template, request, redirect, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename
import time
import os

app = Flask(__name__)
had = HadoopInteractions()

@app.route('/')
def index():
	return render_template('unauthorized.html', name = 'Dagen')

@app.route('/api')
def showApi():
  return render_template('unauthorized.html', name = 'Dagen')

@app.route('/api/mr', methods = ['POST', 'GET'])
def runMr():
  had.runMR('{}')
  return False

@app.route('/api/alpha', methods = ['POST', 'GET'])
def runAlpha():
  had.runAlpha('{}')
  return False

if __name__ == '__main__':
	app.run(debug = True, port = 3210, host='0.0.0.0')
