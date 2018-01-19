# Importing ALL the packages that we will need in this script
import urllib.request, urllib.parse, urllib.error
from urllib.request import Request, urlopen
import urllib.parse
import http
import sqlite3
import json
import time
import ssl
import sys
from bs4 import BeautifulSoup

# Defining the function that later extracts results and writes them into a database
def ADD_DB(results):
    indi = 0
    for line in results:
        try:
            author = line['author']
            author = str(author)
        except:
            author = 'No Data'
            pass
        try:
            Abstract = line ['description']
            soup = BeautifulSoup(Abstract, 'html.parser')
            soupy = soup.find_all(['p', 'li'])
            AB = str()
            for sp in soupy:
                sq = sp.getText()
                AB = AB + sq + '\n'
        except:
            AB = 'No Data'
            pass
        try:
            country = line['country_focus']
            country = str(country)
        except:
            country = 'No Data'
            pass
        try:
            url = line['urls']
            url = str(url)
        except:
            url = 'No Data'
            pass
        try:
            Language = line['language_name']
            Language = str(Language)
        except:
            Language = 'No Data'
            pass
        try:
            Publisher = line['publisher']
            Publisher = str(Publisher)
        except:
            Publisher = 'No Data'
            pass
        try:
            PubDate = line['publication_year']
            PubDate = str(PubDate)
        except:
            PubDate = 'No Data'
            pass
        try:
            title = line['title']
            title = str(title)
        except:
            title = 'No Data'
            pass
        try:
            EldisURL = line['website_url']
            EldisURL = str(EldisURL)
        except:
            EldisURL = 'No Data'
            pass
        try:
            SField = title + ' ' + AB
        except:
            SField = 'No Data'
            pass
        cur.execute('INSERT OR REPLACE INTO Docs (Tit, Abst, Liink, ELiink, SearchFi, author, lang, publ, PubDate) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (title, AB, url, EldisURL, SField, author, Language, Publisher, PubDate))
        conn.commit()
        indi = indi +1


# Making the Database
conn = sqlite3.connect('all_documents.sqlite')
cur = conn.cursor()
cur.execute('DROP TABLE IF EXISTS Docs')
cur.execute('CREATE VIRTUAL TABLE Docs USING fts3 (id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE, Tit TEXT UNIQUE, Abst TEXT, Liink TEXT, ELiink TEXT UNIQUE, SearchFi TEXT, author TEXT, lang TEXT, publ TEXT, PubDate TEXT)')

# Some internet security code
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# API key and Search Data
api_key = 'YOUR_API_KEY_HERE'
InitSearch= ['firm*', 'enterpr*', 'busines*']

# Finding the initial pages
InitPages = list()

for term in InitSearch:
    termi = urllib.parse.quote_plus(term)
    SURL = 'http://api.ids.ac.uk/openapi/eldis/search/documents/full?q='+termi+'&num_results=500'
    URL = Request(SURL, headers={'Token-Guid' : api_key})
    uh = urlopen(URL, context=ctx).read()
    js = json.loads(uh)
    meta = js['metadata']
    numhits = meta['total_results']
    numPages = int(((numhits-(numhits%500))/500)+1)
    print(termi+' finds '+str(numhits)+' documents, which means ' + str(numPages) + ' pages of results')
    if numPages <= 4:
        InitPages.append(SURL)
    if numPages > 4:
        InitPages.append(SURL)
        numInits = (numPages-(numPages%4))/4+1
        alla = 2
        offs = int(0)
        while alla <= numInits:
            offs = offs+2000
            IURL =  'http://api.ids.ac.uk/openapi/eldis/search/documents/full?q='+termi+'&num_results=500'+'&start_offset='+str(offs)
            InitPages.append(IURL)
            alla = alla + 1
print('The Initial Pages are: '+str(InitPages))

# Calling the initial pages, downloading their data and add it to the database with the ADD_DB function
for InitPage in InitPages:
        URL = Request(InitPage, headers={'Token-Guid' : api_key})
        uh = urlopen(URL, context=ctx).read()
        js = json.loads(uh)
        meta = js['metadata']
        offset = meta['start_offset']
        numhits = meta['total_results']
        numPages = int(((numhits-(numhits%500))/500)+1)-(offset/500)
        result = js['results']
        ADD_DB(result)
        #print(meta)
        pagi = int(2)
        print('page 1 of a total of '+str(numPages) + ' from the initial Page '+str(InitPage)+' read into the database')
        if numPages>1:
            while pagi <= 4:
                np = meta['next_page']
                if pagi >= numPages: pagi = 5
                URL = Request(np, headers={'Token-Guid' : api_key})
                uh = urlopen(URL, context=ctx).read()
                js = json.loads(uh)
                meta = js['metadata']
                result = js['results']
                ADD_DB(result)
                print(meta)
                if pagi <=4: print('page '+str(pagi)+' of a total of '+str(numPages) + ' from the initial Page '+str(InitPage)+' read into the database')
                if pagi ==5: print('page '+str(numPages)+' of a total of '+str(numPages) + ' from the initial Page '+str(InitPage)+' read into the database')
                pagi = pagi+1

print('All entries added to the database. Well done!')
