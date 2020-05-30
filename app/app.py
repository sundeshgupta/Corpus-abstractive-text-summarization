from flask import Flask, render_template, url_for, jsonify, request
from datasets import datasets
from summarizationModel import extractive
import os



app = Flask(__name__)

def extractiv(text):
	summary = extractive.summarize(text)
	return summary

def abstractive(text):
	os.chdir('/home/ubuntu/Software/Corpus-abstractive-text-summarization/app/summarizationModel/')
	file = open('/home/ubuntu/Software/Corpus-abstractive-text-summarization/app/summarizationModel/IO/in.txt', 'w')
	file.write(text)
	file.close()
	os.system('/home/ubuntu/Software/Corpus-abstractive-text-summarization/app/summarizationModel/get_summ_abs.sh')
	file = open('/home/ubuntu/Software/Corpus-abstractive-text-summarization/app/summarizationModel/IO/out.txt')
	summary = file.read()
	file.close()
	return summary


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
	print(data)
	text = data['text']
	typ = data['type']
	if(typ == 'extractive'):
		summary = extractiv(text)
	elif(typ == 'abstractive'):
		summary = abstractive(text)

	return jsonify(text = data['text'], summary = summary)

@app.route('/api/visualize', methods=['POST'])
def visualize():
	dataset = request.get_json()['dataset']
	if(dataset == 'all'):
		return jsonify(datasets)

	return jsonify(datasets[dataset])

@app.route('/download', methods=['GET'])
def download():
	return render_template('download.html', page='download')

if(__name__=='__main__'):
    app.run(port = 8000, debug=True)
