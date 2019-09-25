from bravado.client import SwaggerClient
import datetime

search = 'Malaria AND Senegal'

OPENTRIALS_API_SPEC = 'http://api.opentrials.net/v1/swagger.yaml'
config = {'use_models': False}
client = SwaggerClient.from_url(OPENTRIALS_API_SPEC, config=config)
#print(dir(client))

result = client.trials.searchTrials(q=search, per_page=100).result()
#print(list(result.keys()))
print(str(result['total_count']) + ' articles retrieved from OpenTrials')

#print(len(result['items']))
#print(result['items'][0])
RIS = str()
for item in result['items']:
    title = item['public_title']
    abstract = item['brief_summary']
    url = item['records'][0]
    url = url['source_url']
    try:
        author = list()
        for auth in item['persons']:
            author.append(auth['name'])
    except:
        author = ' '
        pass
    date = item['registration_date']
    if date != None: date = date.year
    Pub = str()
    indi = 0
    for rec in item['records']:
        Pubi = rec['source_id']
        if indi ==0:
            Pub = Pub + str(Pubi)
            indi = indi +1
        else:
            Pub = Pub + ' , ' + str(Pubi)
    location = item['locations']
    countries = str()
    indi = 0
    for loc in location:
        if loc['type']=='country':
            country = loc['name']
            if indi == 0:
                counries = countries + str(country)
                indi = indi+1
            else:
                countries = countries + ' , ' + str(country)
    #print(countries, Pub)
    authli = str()
    for aut in author:
        authli = authli + '\n\rAU  - '+str(aut)
    RIS = RIS + 'TY  - DBASE\n\rAB  - '+ str(abstract) + authli + '\n\rCY  - '+str(countries)+ '\n\rDB  - OpenTrials' + '\n\rPB  - ' + str(Pub) + '\n\rPY  - '+ str(date) + '\n\rTI  - ' + str(title) + '\n\rUR  - '+ str(url) + '\n\rER  - \n\r'
#print(RIS)
RIS = RIS.encode('ascii', 'replace')
RIS = RIS.decode('utf-8', 'replace')
file = open('RIS Formatted OpenTrials Data.ris', 'w')
file.write(RIS)
file.close()
print('RIS file written into working directory. Well Done!')
#    if Pub != None:
#        print(Pub)
#print([obj['public_title'] for obj in result['items']])
