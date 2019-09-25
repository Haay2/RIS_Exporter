# Importing packages used in this code
import sqlite3
import ast
# Connecting to the database
conn = sqlite3.connect('all_documents.sqlite')
cur = conn.cursor()
print('Connected to the database')
# Searching the database for the search terms and loading the data into RAM
search2 = 'SME* OR MSME*'
cur.execute('SELECT * FROM Docs WHERE SearchFi MATCH ?', [search2,] )
results2 = cur.fetchall()
print(str(len(results2)) + ' results found in the database.')

# Iterating through the results and writing them into the string which will become the RIS file
num = 0
RIS = str()
while num < len(results2):
    title = results2[num][1]
    abstract = results2[num][2]
    Link = results2[num][3]
    if Link != None:
        Link = ast.literal_eval(Link)
        LinkRIS = str()
        for Li in Link:
            LinkRIS = LinkRIS + '\n\rUR  - '+Li
    if Link == None:
        LinkRIS = str()
    EldisLink = results2[num][4]
    author = results2[num][6]
    if author =='No Data':
        authorRIS = str()
    elif author != None:
        author = ast.literal_eval(author)
        authorRIS = str()
        for auth in author:
            authorRIS = authorRIS + '\n\rAU  - '+auth
    elif author == None:
        authorRIS = str()
    language = results2[num][7]
    publisher = results2[num][8]
    PubDate = results2[num][9]
    num = num + 1
    RIS = RIS + 'TY  - ABST\n\rAB  - '+ str(abstract)+ authorRIS + '\n\rDB  - Eldis' +'\n\rL1  - '+str(EldisLink) +  '\n\rPB  - '+str(publisher) + '\n\rPY  - '+str(PubDate)+ '\n\rTI  - '+str(title)+LinkRIS+'\n\rER  - \n\r'
print('Results from the database parsed')
# Writing the RIS file into memory
RIS = RIS.encode('ascii', 'replace')
RIS = RIS.decode('utf-8', 'replace')
file = open('RIS Formated Eldis Data.ris', 'w')
file.write(RIS)
file.close()
print('Well done. You have created an RIS file with the results!')
