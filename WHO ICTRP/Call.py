import xml.etree.ElementTree as ET

file = open('ICTRP-Results.xml', 'r')
Data = file.read()
SData = ET.fromstring(Data)

RIS = str()

num = 0

for Trial in SData:
    try:
        first = Trial.find('Contact_Firstname').text
        if first==None:
            first = ' '
    except: first = ' '
    try:
        last = Trial.find('Contact_Lastname').text
        if last == None:
            last = ' '
    except: last = ' '
    author = first + ' ' + last
    title = Trial.find('Public_title').text
    date = Trial.find('Date_registration').text[-4:]
    link = Trial.find('web_address').text
    agemin = Trial.find('Inclusion_agemin').text
    agemax = Trial.find('Inclusion_agemax').text
    gender = Trial.find('Inclusion_gender').text
    SType = Trial.find('Study_type').text
    design = Trial.find('Study_design').text
    try: countries = Trial.find('Countries').text
    except: countries = 'No Data'
    try: inclusion = Trial.find('Inclusion_Criteria').text
    except: inclusion = 'No Data'
    try: condition = Trial.find('Condition').text
    except: condition = 'No Data'
    try: intervention = Trial.find('Intervention').text
    except: intervention = 'No Data'
    try: primary = Trial.find('Primary_outcome').text
    except: primary = 'No Data'
    try:
        secondary = Trial.find('Secondary_outcome').text
    except:
        secondary = 'No Data'
    try: afil = Trial.find('Contact_Affiliation').text
    except: afil = 'No Data'
    sponsor = Trial.find('Primary_sponsor').text
    abstract = 'Study type: ' + str(SType) + '\nStudy design: ' + str(design) + '\nCountries: ' +str(countries) + '\nInclusion Criteria: \nMinimum Age: ' + str(agemin) + '\nMaximum Age: ' + str(agemax) + '\nGender: ' + str(gender) + '\nOther Inclusion criteria: \n' + str(inclusion) + '\nCondition: ' + str(condition) + '\nIntervention: ' + str(intervention) + '\nPrimary Outcomes: ' + str(primary) + '\nSecondary Outcomes: ' + str(secondary) + '\nSponsor: ' + str(sponsor)
    abstract = abstract.replace('<br>','\n' )
    abstract = abstract.replace('<\br>','\n' )
    RIS = RIS + 'TY  - DBASE\n\rAB  - '+ abstract + '\n\rAU  - '+ author + '\n\rDB  - WHO ICTRP' + '\n\rPB  - ' + str(afil) + '\n\rPY  - '+ str(date) + '\n\rTI  - ' + str(title) + '\n\rUR  - '+ str(link) + '\n\rER  - \n\r'
    num = num + 1
    print(str(num) + ' trials identified in XML file and read into memory')

RIS = RIS.encode('ascii', 'replace')
RIS = RIS.decode('utf-8', 'replace')
file.close()
file = open('RIS Formated WHO ICTRP Data.ris', 'w')
file.write(RIS)
file.close()

print('RIS file written into working directory. Well Done!')
