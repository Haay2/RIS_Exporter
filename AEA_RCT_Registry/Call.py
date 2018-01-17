import request
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup
import ssl
import urllib.parse
import time
from random import *
import re

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

search = '(labor AND firm) AND SME'
search = urllib.parse.quote_plus(search)
url = 'https://www.socialscienceregistry.org/trials/search?utf8=%E2%9C%93&commit=Search&query=' + search

req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
site = urlopen(req, context=ctx).read()
soup = BeautifulSoup(site, 'html.parser')

print('STATUS: Inital search page retrieved')

# Finding the number of pages:
hits = soup.find('div', class_='count')
hits = hits.find('p').getText()
hits = int(hits.rstrip(' Trials Found'))
if hits%10 ==0:
    numpage= hits/10
else:
    numpage = hits/10 - (hits%10)/10 + 1
numpage = int(numpage)
#print(numpage)

print('STATUS: '+str(numpage)+' index pages found')
# making a list of index sites
SiteLi = list()
SiteLi.append(url)
if numpage >=2:
    num = 2
    while num <= numpage:
        url2 = 'https://www.socialscienceregistry.org/trials/search?commit=Search&page='+ str(num)+'&query='+search+'&utf8=%E2%9C%93'
        SiteLi.append(url2)
        num = num+1
#Calling the Index Sites
MainSoups = list()

for ste in SiteLi:
    try:
        req = Request(ste, headers={'User-Agent': 'Mozilla/5.0'})
        site = urlopen(req, context=ctx).read()
        soup = BeautifulSoup(site, 'html.parser')
        MainSoups.append(soup)
    except: pass

print('STATUS: '+str(len(MainSoups))+' index pages retrieved')
# Getting the links to the document sites
LinkLi=list()
for soupy in MainSoups:
    trials = soupy.find_all('div', class_='trial')
    for trial in trials:
        LinkLi.append('https://www.socialscienceregistry.org'+trial.find('a').get('href', None))

print('STATUS: '+str(len(LinkLi))+' document pages found')
# Calling the document Sites
DocSoups = list()

ind = 1
for doc in LinkLi:
    req = Request(doc, headers={'User-Agent': 'Mozilla/5.0'})
    site = urlopen(req, context=ctx).read()
    soup = BeautifulSoup(site, 'html.parser')
    DocSoups.append(soup)
    print(ind)
    ind = ind + 1
    time.sleep(2+randint(-1,1))

print('STATUS: '+str(len(DocSoups))+' document pages retrieved')
# Extracting the data from the document sites and writing them into the RIS string
RIS = str()
for suppy in DocSoups:
    FieldLabs = list()
    Fields = list()
    FieldLabLi = suppy.find_all('div', class_='field-label')
    for arg in FieldLabLi:
        FieldLabs.append(arg.getText())
    FieldLi = suppy.find_all('div', class_='field')
    for arg in FieldLi:
        Fields.append(arg.getText())
    bla = 0
    again = 0
    while bla <= len(Fields)-1:
        if FieldLabs[bla]=='Title':
            title = Fields[bla]
        if (FieldLabs[bla]=='Name' and again==0):
            again =1
            author = Fields[bla]
        if FieldLabs[bla]=='Abstract':
            abstract = suppy.find('div', class_='row abstract').getText()
        if FieldLabs[bla]=='Affiliation':
            publisher = Fields[bla]
        if FieldLabs[bla]=='Initial registration date':
            PubDate = Fields[bla]
        if FieldLabs[bla]=='RCT ID':
            ID = Fields[bla]
            #print(Fields[bla])
        bla = bla+1
    abstract = abstract.lstrip('Abstract\n')
    abstract = abstract.rstrip()
    PubDate = PubDate[-4:]
    ID = re.findall('[1-9]*', ID)
    ID = ID[-2]
    print(title, author, abstract, publisher, PubDate, ID)
    if title != '':
        RIS = RIS + '\n\rTY  - DBASE\n\rA1  - '+author+'\n\rAB  - '+abstract+'\n\rDB  - APA RCT Registry\n\rLA  - English\n\rPB  - '+publisher+'\n\rPY  - '+PubDate+'\n\rTI  - '+title+'\n\rUR  - https://www.socialscienceregistry.org/trials/'+ID+'\n\rER  - '

# Exporting the RIS string into an RIS file
RIS = RIS.encode('ascii', 'replace')
RIS = RIS.decode('utf-8', 'replace')

file = open('AEAcrawl.ris', 'w')
file.write(RIS)
file.close()

print('STATUS: End of code. Well done!')
# tag div class=trial
# then first tag a
