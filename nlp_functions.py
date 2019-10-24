#NLP-Functions contains a variety of functions we'll be using in text processing.

#Lexical Diversity - The average number of times each word appears in a text data
def lexical_diversity(text):
	lex_div = len(text) / len(set(text))
	print(lex_div)
	
#Percentage - how often a word occurs in a text. computing the percentage of the text 
#taken up by a specific word.
def percentage(count, total):
	percent = 100 * count / total
	print(percent)
	
