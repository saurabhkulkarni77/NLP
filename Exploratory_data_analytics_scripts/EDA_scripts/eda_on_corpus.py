#import spacy
#nlp = spacy.load('en')
import pandas as pd 
import re
import string
#import spacy
import nltk
nltk.download('stopwords')
nltk.download('punkt')
def clean_text():
	'''make text in lowercase'''
	text = open('giant_corpus.txt').read()
	text = text.lower()
	print("original_corpus:",len(list(text)))
	#remove all punctuation marks
	text = re.sub('[%s]'%re.escape(string.punctuation),'',text)
	print("after cleaning:",len(list(text)))
	nltk_stopwords = nltk.corpus.stopwords.words('english')
	print('Number of stop words: %d' % len(nltk_stopwords))
	tokens = nltk.tokenize.word_tokenize(text)
	print("length of tokens of words",len(tokens))
	tokens = [token for token in tokens if not token in nltk_stopwords]
	print("after removing stop words",len(tokens))
	return text
clean_text()