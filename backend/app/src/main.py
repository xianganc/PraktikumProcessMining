from hadoop import HadoopInteractions
from reducer import Reduce
from mapper import Mapper
from flask import Flask, render_template, request, redirect, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename
import time
import os
import json

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
      <p>Event:</p>
      <input type="text" name="event">
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

@app.route('/api/upload')
def up():
  for (dirpath, dirnames, filenames) in os.walk('/data'):
    for filename in filenames:
      if os.path.splitext(filename)[1] in ['.png']:
        continue
      had.pushData(os.path.join(dirpath,filename),'/'+dirpath)


@app.route('/api/mr', methods = ['POST', 'GET'])
def runMr():
  had.data()
  if request.method == 'GET':
    out = had.showData('/')
    createMR(out)
    return render_template('mr.html', name = 'Dagen')
  files = request.form['files']
  mp = Mapper()
  rp = Reduce()
  if files[:-3] == 'csv':
    ma, tl = mp.map1Csv(files)
    tmp, ti, to, tl = rp.reduce1(ma, tl)
    res = rp.reduce2(tmp, ti, to, tl)
  elif files[:-3] == 'xes':
    ma, tl = mp.map1Xes(files)
    tmp, ti, to, tl = rp.reduce1(ma, tl)
    res = rp.reduce2(tmp, ti, to, tl)
  with open('/tmp/out.json', "w") as reducedLog:
    json.dump(res,reducedLog)
  return "success"

@app.route('/api/alpha')
def runAlpha():
  os.system("python3 /src/src/alphaAlgo.py /tmp/out.json")
  return "success: True"

if __name__ == '__main__':
  up()
  app.run(debug = True, port = 3000, host='0.0.0.0')
