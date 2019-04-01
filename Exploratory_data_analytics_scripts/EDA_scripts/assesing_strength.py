import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.corpus import words
from nltk.probability import FreqDist
from matplotlib import pyplot as plt
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator 
import re
from collections import Counter
import string
corpus = open("final_corpus_after_refractions.txt").read()

using freqdist to analize dataset strength refer graph
freqdist = nltk.FreqDist(word.lower() for word in word_tokenize(corpus))
print(word_tokenize(corpus))
var = word_tokenize(corpus)
print(var.count('the'))
print(Counter(var))
#remove occureces of following meaningless words to clean data further: 'the': 28053, 'to': 26748, 'and': 25503, 'of': 20331, 'a': 16905, 'in': 14748, 'you': 11461, '’': 10653, 'emotional': 10423, 'is': 9750, 'that': 8799
updated_tokens = [x for x in var if x != 'the']
list_to_be_removed = ['the','and','you','is','that','your','with','it','for','can','as','are','on','s','or','be','how','their','they','from','when','has','if','also','will','which','them','who','these','than','those','there','was','us','ll','its','into','any','i','youre','1','m','x','am','theyre','im','jr','g','thatll']
updated_tokens = [x for x in var if x not in {'to','of','a','in','an','n','re','-','what','at','her','so','his','by','this','ve','4n','the','and','you','is','that','your','with','it','for','can','as','are','on','s','or','be','how','their','they','from','when','has','if','also','will','which','them','who','these','than','those','there','was','us','ll','its','into','any','i','youre','1','m','x','am','theyre','im','jr','g','thatll','articlexa0highlights','asxa0achievement','evenxa0understanding','thexa0best','2016n','researchxa0has','we','"','t'}]
print("After:",Counter(updated_tokens))
str_one = " ".join(str(x) for x in updated_tokens)	
with open('final_corpus_after_refractions.txt','a') as f:
	f.write(str_one)

freqdist = nltk.FreqDist(word for word in corpus if word.lower() not in stopwords and word.isalpha())
plt.figure(figsize=(16,5))
freqdist.plot(50)
applying wordcloud to visualize the cloud of words in the corpus where words with max font size are most occuring, refer graph for the same
Wordcloud = WordCloud(max_font_size = 60).generate(corpus)
plt.figure(figsize=(16,12))
plt.imshow(Wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
refracted_files = open("final_corpus_after_refractions.txt").read()
freqdist = nltk.FreqDist(word.lower() for word in word_tokenize(refracted_files))
plt.figure(figsize=(16,5))
freqdist.plot(50)
var = word_tokenize(refracted_files)
print(Counter(var))
#clear special chars
text = re.sub('[%s]'%re.escape(string.punctuation),'',refracted_files)
print(text)
