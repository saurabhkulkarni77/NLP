import urllib.request
from bs4 import BeautifulSoup
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
#few are PDFs they are saved according to link number
#check link eight http://mindapples.org/2018/01/30/the-downsides-of-emotional-intelligence/
#link 9 is pdf
#link 12 is pdf
#check link seventeen https://www.trainingzone.co.uk/lead/culture/emotional-intelligence-vital-to-management-cipd-feature
#check link ninteen https://www.lifehack.org/articles/communication/emotional-intelligence-why-important.html
# check link twenty_one https://digital.com/blog/emotional-intelligence/
#check link twenty_six https://medium.com/personal-growth/the-10-qualities-of-an-emotionally-intelligent-person-f595440af4fb
#check link thirty two:https://www.ciphr.com/features/emotional-intelligence/
#check link thirty_three : https://www.atlassian.com/blog/teamwork/emotional-intelligence-articles
#check link thirty_five : https://www.psychologytoday.com/us/basics/emotional-intelligence
def article_crawler():

	user_agent = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.9.0.7) Gecko/2009021910 Firefox/3.0.7'
	headers={'User-Agent':user_agent,} 
	url = "http://mindapples.org/2018/01/30/the-downsides-of-emotional-intelligence/"
	request = urllib.request.Request(url, None, headers) 
	html = urllib.request.urlopen(request).read()
	soup = BeautifulSoup(html,'lxml')

	# kill all script and style elements
	for script in soup(["script", "style"]):
		script.extract()# rip it out

	# get text
	text = soup.get_text()

	# break into lines and remove leading and trailing space on each
	lines = (line.strip() for line in text.splitlines())
	# break multi-headlines into a line each
	chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
	# drop blank lines
	text = '\n'.join(chunk for chunk in chunks if chunk)

	with open('link_seven.txt','w') as content:
		content.write(text)
article_crawler()