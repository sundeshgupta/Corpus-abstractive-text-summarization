from flask import Flask, render_template, url_for, jsonify, request
from datasets import datasets

app = Flask(__name__)

@app.route('/', methods=['GET'])
@app.route('/intro', methods=['GET'])
def main():
	return render_template('intro.html', page='intro')

@app.route('/visualize', methods=['GET'])
def visual():
	return render_template("visualize.html", page='visual')

@app.route('/evaluate', methods=['GET'])
def evaluate():
	return render_template('evaluate.html', page='evaluate')

@app.route('/api/summarize', methods=['POST'])
def summarize():
	data = request.get_json()
	return jsonify(text = data['text'], summary = data['text'])

@app.route('/api/visualize', methods=['POST'])
def visualize():
	dataset = str(request.get_data().decode())
	return jsonify(datasets[dataset])

app.run(port = 8000, debug=True)