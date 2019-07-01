from flask import Flask, render_template, request, redirect, url_for
from flask.views import MethodView
from werkzeug.utils import secure_filename
import os
import subprocess

app = Flask(__name__)

@app.route('/')

def index():
	return render_template('login.html')

# if __name__ == '__main__':
# 	app.run(host='0.0.0.0', port = 8080, debug = True)

@app.route('/hello')
def hello():
	return render_template('index.html', name = 'Dagen')


@app.route('/login')
def login():
	return render_template('login.html', name = 'Dagen')

@app.route('/dashboard')
def dashboard():
	return render_template('dashboard.html', name = "Dagen")

@app.route('/result')
def result():
	return render_template('result.html', name = "Dagen")

# @app.route('/templates/dashboard.html')
# def dashboard2():
#     	return render_template('dashboard.html', name = "Dagen")


@app.route('/templates/dashboard.html', methods = ['POST', 'GET'])
def upload():
	if request.method == 'POST':
		f = request.files['file']
		basepath = os.path.dirname(__file__)
		upload_path = os.path.join(basepath, '../../data', secure_filename(f.filename))
		f.save(upload_path)
		subprocess.check_output(['curl','-s','172.18.0.1:3000/api/upload'])
		return redirect(url_for('upload'))
	return render_template('dashboard.html')


def return_img_stream(img_local_path):
    import base64
    img_stream = ''
    with open(img_local_path, 'r') as img_f:
        img_stream = img_f.read()
        img_stream = base64.b64encode(img_stream)
    return img_stream

@app.route('/result')
def show():
    img_path = '../../output.png'
    img_stream = return_img_stream(img_path)
    return render_template('result.html',img_stream=img_stream)

if __name__ == '__main__':
	app.run(debug = True, port = 8080, host='0.0.0.0')

# def greet():
#     	user = {'username': 'Dagen', 'age': "20"}
# 	return '''
# <html>

# 	<head>
# 		<title> Template
# 	</head>

# 	<body>
# 		<h1>Hello, ''' + user['username'] + '''!, you are ''' + user['age'] + ''' years old.</h1>
# 	</body>
# </html>'''

# class IndexHandler(MethodView):

# 	def __init__(self, name):
# 		print(name)

# 	def get(self):
# 		return 'It is a GET request.'

# 	def post(self):
# 		return 'It is a POST request.'

# if __name__ == '__main__':
# 	app.add_url_rule('/', view_func=IndexHandler.as_view('index'))
# 	app.run(port = 8080, host = '0.0.0.0', debug = True)