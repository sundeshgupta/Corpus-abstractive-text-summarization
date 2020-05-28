datasets = {}

cnn = {
	'Number of articles-summary pairs': 287113,
	'Number of distinct words in article': 810883,
	'Number of distinct words in summary': 201694,
	'Number of distinct words common in article and summary': 176408,
	'Mean number of word in summary': 46.88636529868031,
	'Mean number of word in article': 677.4758892840101,
	'Mean number of sentences per article': 3.7898144632949395,
	'Mean compression ratio': 16.012921894895314,
	'Mean extractive fragment coverage': 0.8635503034940778,
	'Mean extractive fragment density': 3.3318217257143927
}

gigaword = {
	'Number of articles-summary pairs': 3803957,
	'Number of distinct words in article': 115519,
	'Number of distinct words in summary': 66843,
	'Number of distinct words common in article and summary': 62343,
	'Mean number of word in summary': 8.039039347710817,
	'Mean number of word in article': 28.61209366982855,
	'Mean number of sentences per article': 1.0,
	'Mean compression ratio': 3.836603152355721,
	'Mean extractive fragment coverage': 0.575584529920481,
	'Mean extractive fragment density': 1.067076520041172
}

dataset1 = {
	'Number of articles-summary pairs': 5386,
	'Number of distinct words in article': 57673,
	'Number of distinct words in summary': 11807,
	'Number of distinct words common in article and summary': 10682,
	'Mean number of word in summary': 11.81414779056814,
	'Mean number of word in article': 161.78908280727813,
	'Mean number of sentences per article': 1.0,
	'Mean compression ratio': 14.626952640907215,
	'Mean extractive fragment coverage': 0.6493958848470976,
	'Mean extractive fragment density': 1.412259883074382
}

dataset2 = {
	'Number of articles-summary pairs': 2196,
	'Number of distinct words in article': 43896,
	'Number of distinct words in summary': 6673,
	'Number of distinct words common in article and summary': 6388,
	'Mean number of word in summary': 11.8816029143898,
	'Mean number of word in article': 437.14071038251365,
	'Mean number of sentences per article': 1.0,
	'Mean compression ratio': 38.75446019461595,
	'Mean extractive fragment coverage': 0.7533885462814058,
	'Mean extractive fragment density': 1.6606111538612436
}

datasets['cnn'] = cnn
datasets['giga'] = gigaword
datasets['free'] = dataset1
datasets['hindustan'] = dataset2