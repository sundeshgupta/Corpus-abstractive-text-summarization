from summa import summarizer

with open('./IO/in.txt', 'r') as f:
	text = f.read()

with open('./IO/out.txt', 'w') as f:
	f.write(summarizer.summarize(text, words = 50))