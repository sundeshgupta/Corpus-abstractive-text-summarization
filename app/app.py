from flask import Flask, render_template, url_for, jsonify, request
from datasets import datasets
from summarizationModel import extractive

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
	text = data['text']
	summary = extractive.summarize(text)

	return jsonify(text = data['text'], summary = summary)

@app.route('/api/visualize', methods=['POST'])
def visualize():
	dataset = request.get_data().decode()
	return jsonify(datasets[dataset])

if(__name__=='__main__'):
    app.run(port = 8000, debug=True)
