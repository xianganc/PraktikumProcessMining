from flask import Flask, render_template
from flask.views import MethodView
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


@app.route('/templates/dashboard.html')
def dashboard2():
	return render_template('dashboard.html', name = "Dagen")

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