### Steven Morgan
### Scraping state government press releases into .txt

# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2, re, requests, bs4, os

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (gov.alaska....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 98):
	x = "https://gov.alaska.gov/newsroom/category/press-releases/page/" + str(i) + "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://gov.alaska.gov/newsroom/[\d]', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

os.makedirs('alaska_press_releases')
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	alaska = open('AK_' + link[40:-1] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		alaska.write(pElems[i].getText().encode("utf-8"))
		alaska.write("\n")

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.alabama....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 11):
	x = "https://governor.alabama.gov/newsroom/press-releases/page" + str(i) + "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://governor.alabama.gov/press-releases/', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

os.makedirs('alabama_press_releases')
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	alabama = open('AL_' + link[44:-1] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		alabama.write(pElems[i].getText().encode("utf-8"))
		alabama.write("\n")

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.arkansas....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 59):
	x = "https://governor.arkansas.gov/press-releases/P" + str(i*10-10) #+ "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://governor.arkansas.gov/press-releases/detail/', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

os.makedirs('arkansas_press_releases')
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	arkansas = open('AR_' + link[52:-1] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		arkansas.write(pElems[i].getText().encode("utf-8"))
		arkansas.write("\n")

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.delaware....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 2):
	print "Booyah"
	x = "https://governor.delaware.gov/newsroom/"# + str(i*10-10) #+ "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		print str(link)
		if re.search('https://news.delaware.gov/', str(link)):
			print link['href']
			links = links + [link['href']]
			
links = list(set(links))
print len(links)

#os.makedirs('delaware_press_releases')
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	delaware = open('DE_' + link[52:-1] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		delaware.write(pElems[i].getText().encode("utf-8"))
		delaware.write("\n")

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.georgia....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list

for j in range(2011, 2019):
	for i in range(0, 25):
		x = "https://gov.georgia.gov/press-releases/" + str(j) + "?page=" + str(i) #+ "/"
		resp = urllib2.urlopen(x)
		soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
		for link in soup.find_all('a', href=True):
			#print link
			if re.search('press-releases/\d\d\d\d-\d\d-', str(link)):
				print link['href']
				links = links + [link['href']] #list('https://gov.georgia.gov/' + str([link['href']]))

	links = list(set(links))
	print len(links)

#for i in range(0, 22):
#	x = "https://gov.georgia.gov/press-releases/2016?page=" + str(i) #+ "/"
#	resp = urllib2.urlopen(x)
#	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
#	for link in soup.find_all('a', href=True):
#		#print link
#		if re.search('press-releases/\d\d\d\d-\d\d-', str(link)):
#			print link['href']
#			links = links + [link['href']] #list('https://gov.georgia.gov/' + str([link['href']]))

#links = list(set(links))
#print len(links)

#os.makedirs('georgia_press_releases')
for link in links:
	link = "https://gov.georgia.gov/" + link
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	georgia = open('GA_' + link[51:] + '.txt', 'w')
	#print georgia
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		georgia.write(pElems[i].getText().encode("utf-8"))
		georgia.write("\n")

# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.hawaii....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 91):
	x = "https://governor.hawaii.gov/category/newsroom/press-releases/page/" + str(i) + "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://governor.hawaii.gov/newsroom/', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

os.makedirs('hawaii_press_releases')
for link in links:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	hawaii = open('HI_' + link[52:-1] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		hawaii.write(pElems[i].getText().encode("utf-8"))
		hawaii.write("\n")

		
# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.kansas....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 35):
	x = "https://governor.kansas.gov/newsroom/media-releases/page/" + str(i) + "/"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		if re.search('https://governor.kansas.gov/', str(link)):
			print link['href']
			links = links + [link['href']]

links = list(set(links))
print len(links)

#os.makedirs('kansas_press_releases')
for link in links[348:]:
	res = requests.get(link)
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	kansas = open('KS_' + re.sub('/', '_', link)[28:] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		kansas.write(pElems[i].getText().encode("utf-8"))
		kansas.write("\n")

		
# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.kansas....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
x = "http://governor.ky.gov/news-media/news/"
resp = urllib2.urlopen(x)
soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
for link in soup.find_all('a', href=True):
	#print link
	if re.search('http://kentucky.gov/Pages/Activity-stream', str(link)):
		print link['href']
		links = links + [link['href']]

links = list(set(links))
print len(links)

#os.makedirs('kentucky_press_releases')
for link in links:
	try:
		#headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.10; rv:39.0)'}
		#res = requests.get(link, headers=headers).raise_for_status()
		res = requests.get(link)
	except:
		print("Connection refused by the server...")
		time.sleep(50)
		print "Was a nice sleep, now let me continue..."
		continue
	#res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	kentucky = open('KY_' + re.sub('/', '_', link)[-3:] + '.txt', 'w')
	print kentucky
	for i in range(len(pElems)):
		print pElems[i].getText().encode("utf-8")
		kentucky.write(pElems[i].getText().encode("utf-8"))
		kentucky.write("\n")

		
# Create empty list to store press release urls
links = []
		
# Iterate through pages of press release links
# The url for each page follows a set pattern (governor.louisianna....../press-releases/page/3/)
# therefore each iteration changes the page of press release links
# Appends all press releases URLs (ending with .../newsroom/"some digit") to a list
for i in range(1, 53):
	x = "http://gov.louisiana.gov/index.cfm/newsroom/category/9?si=0" + str(i-1) + "1"
	resp = urllib2.urlopen(x)
	soup = BeautifulSoup(resp, from_encoding=resp.info().getparam('charset'))
	for link in soup.find_all('a', href=True):
		#if re.search('http://gov.louisiana.gov/', str(link)):
		print link['href']
		links = links + [link['href']]

links = list(set(links))
print len(links)

#os.makedirs('louisianna_press_releases')
for link in links:
	try:
		res = requests.get('http://gov.louisiana.gov' + link)
	except:
		print("Connection refused by the server...")
		time.sleep(50)
		print "Was a nice sleep, now let me continue..."
		continue
	res.raise_for_status()
	noStarchSoup = bs4.BeautifulSoup(res.text, 'html5lib')

	#print type(noStarchSoup)
	pElems = noStarchSoup.select('p')
	louisianna = open('LA_' + re.sub('/|=|\?', '_', link)[18:] + '.txt', 'w')
	for i in range(len(pElems)):
		#print pElems[i].getText().encode("utf-8")
		louisianna.write(pElems[i].getText().encode("utf-8"))
		louisianna.write("\n")
