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

def createAlpha(dataList):
  with open('/src/src/templates/alpha.html','w') as outfile:
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
      <p>Event:</p>
      <input type="text" name="event">
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
  had.data()
  if request.method == 'GET':
    out = had.showData('/')
    createMR(out)
    return render_template('mr.html', name = 'Dagen')
  header = request.form['header']
  files = request.form['files']
  event = request.form['event']
  mp = Mapper()
  if files[-3] == 'csv':
    ma = mp.mapCsv(files,header)
  elif files[-3] == 'xes':
    ma = mp.mapXes(files,header)
  with open("/src/src/templates/res.html") as out:
    out.write("""<html>
    <body>
    <table>""")
    for entry in ma:
      out.write("<tr>")
      out.write("<td>"+entry+"</td>")
      out.write("</tr>")
    out.write("""</table>
    </body>
    </html>
    """)
  return render_template('res.html', name = 'Dagen')

@app.route('/api/alpha', methods = ['POST', 'GET'])
def runAlpha():
  had.data()
  if request.method == 'GET':
    out = had.showData('/')
    createAlpha(out)
    return render_template('alpha.html', name = 'Dagen')
  header = request.form['header']
  files = request.form['files']
  mp = Mapper()
  if files[-3] == 'csv':
    ma = mp.mapCsv(files,header)
  elif files[-3] == 'xes':
    ma = mp.mapXes(files,header)
  return render_template('alpha.html', name = 'Dagen')

if __name__ == '__main__':
	app.run(debug = True, port = 3000, host='0.0.0.0')
