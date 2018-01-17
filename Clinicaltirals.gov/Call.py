import os
import xml.etree.ElementTree as ET

current_dir = os.getcwd()
#print(current_dir)
folder = current_dir + '\Place Unzipped Data Here\\'
files = os.listdir(folder)

RIS = str()
num = int(0)
for fi in files:
    place = folder + fi
    file = open(place, 'r')
    Data = file.read()
    file.close()
    SData = ET.fromstring(Data)
    x = SData.find
    title = x('official_title').text
    try:
        link = x('required_header')
        link = link.find('url').text
    except: link = ' '
    abstract = SData.find('brief_summary')
    try: abstract = abstract.find('textblock').text
    except: abstract = None
    if abstract == None:
        abstract = SData.find('detailed_description')
        try: abstract = abstract.find('textblock').text
        except: abstract = None
    if abstract == None:
        abstract = 'No Data'
    author = SData.find('overall_official')
    try: author = author.find('last_name').text
    except: author = ' '
    try: date = SData.find('study_first_submitted').text[-4:]
    except: date = ' '
    try:
        sponsor = x('sponsors')
        sponsor = sponsor.find('lead_sponsor')
        sponsor = sponsor.find('agency').text
    except: sponsor = ' '
    RIS = RIS + 'TY  - DBASE\n\rAB  - '+ abstract + '\n\rAU  - '+ str(author) + '\n\rDB  - clinicaltrials.gov' + '\n\rPB  - ' + str(sponsor) + '\n\rPY  - '+ str(date) + '\n\rTI  - ' + str(title) + '\n\rUR  - '+ str(link) + '\n\rER  - \n\r'
    num = num+1
    print(str(num) + ' trials identified in XML files and read into memory')

file = open('RIS Formatted clinicaltrials-gov Data.ris', 'w')
file.write(RIS)
file.close()
print('RIS file written into working directory. Well Done!')
