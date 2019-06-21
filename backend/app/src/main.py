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

def createMR(dataList):
  with open('/src/src/templates/mr.html','w') as outfile:
    outfile.write("""
    <html>
    <body>
    <p> files </p>
    <table>
    """)
    for entry in dataList:
      outfile.write("<tr>")
      outfile.write("<td>"+entry+"</td>")
      outfile.write("</tr>")
    outfile.write("""
    </table>
    <p>
      Please enter the key, by which you wish to map the selected file
    </p>
    <form action="/api/mr" method="post">
      <p>Header:</p>
      <input type="text" name="header">
      <p>File:</p>
      <input type="text" name="files">
      <input type="submit">
    </form>
    </body>
    </html>
    """)

@app.route('/')
def index():
	return render_template('unauthorized.html', name = 'Dagen')

@app.route('/api')
def showApi():
  return render_template('api.html', name = 'Dagen')

@app.route('/api/mr', methods = ['POST', 'GET'])
def runMr():
  if request.method == 'GET':
    out = had.showData('/')
    createMR(out)
    return render_template('mr.html', name = 'Dagen')
  header = request.form['header']
  files = request.form['files']
  mp = Mapper()
  if files[-3] == 'csv':
    createMR(mp.mapCsv(files,header))
  elif files[-3] == 'xes':
    createMR(mp.mapXes(files,header))
  return render_template('mr.html', name = 'Dagen')

@app.route('/api/alpha', methods = ['POST', 'GET'])
def runAlpha():
  return render_template('alpha.html', name = 'Dagen')

if __name__ == '__main__':
	app.run(debug = True, port = 3000, host='0.0.0.0')
