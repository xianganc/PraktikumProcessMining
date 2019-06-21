from hadoop import HadoopInteractions
from reducer import Reduce
from mapper import Mapper
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
  return render_template('api.html', name = 'Dagen')

@app.route('/api/mr', methods = ['POST', 'GET'])
def runMr():
  if request.method == 'GET':
    return render_template('mr.html', name = 'Dagen')
  header = request.form['header']
  return render_template('mr.html', name = 'Dagen')

@app.route('/api/alpha', methods = ['POST', 'GET'])
def runAlpha():
  return render_template('alpha.html', name = 'Dagen')

if __name__ == '__main__':
	app.run(debug = True, port = 3000, host='0.0.0.0')
