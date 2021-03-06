from flask import Flask, jsonify, render_template
from functions import *
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/get_random_video/<num>')
def rand_video(num):
	return jsonify(get_random_video(int(num)))

@app.route('/get_random_img/<num>')
def rand_img(num):
	return jsonify(get_random_img(int(num)))

@app.route('/get_random/<num>')
def rand(num):
	return jsonify(get_random(int(num)))

if __name__ == '__main__':
	app.run(debug=True)