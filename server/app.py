from flask import Flask
from functions import *

app = Flask(__name__)

@app.route('/')
def home():
	return '<h1>Hello World!</h1>'

@app.route('/get_random_video/<num>')
def rand_video(num):
	return str((get_random_video(int(num))))

@app.route('/get_random_img/<num>')
def rand_img(num):
	return str((get_random_img(int(num))))

@app.route('/get_random_quote/<num>')
def rand_quote(num):
	return get_random_quote()

@app.route('/get_random/<num>')
def rand(num):
	return get_random()

if __name__ == '__main__':
	app.run(debug=True)