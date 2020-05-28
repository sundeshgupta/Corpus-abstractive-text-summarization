from summa import summarizer

def summarize(text, file=False, output_file=None):
	summary = ''
	if(file == True):
		f = open(text).read()
		summary = summarizer.summarize(f, words = 50)
	else:
		summary = summarizer.summarize(text, words = 50)

	if(output_file is not None):
		f = open(output_file, 'w')
		f.write(summary)
		f.close()

	return summary
