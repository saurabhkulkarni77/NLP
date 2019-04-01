import os
import glob
path = "./*.txt"
files = glob.glob(path)
concat = " "
for file in files:
	read_all_content = open(file).readlines()
	concat += str(read_all_content)
	with open('giant_corpus.txt','a') as giant_corpus:
		giant_corpus.write(concat)
