import requests, sys, bs4
from pymongo import MongoClient
client = MongoClient('localhost:27017')
db = client.WebData

x=input("Enter the no. of Search results u require(0<x<=10):")
print('Hunting.......')
# Download the search page
res = requests.get("https://google.co.in/search?q=" + ''.join(sys.argv[1:]))
res.raise_for_status()
# Pull data out from the html
soup = bs4.BeautifulSoup(res.text)

# Select all the search links
linkElems = soup.select('.r a')
f=open("search.txt","w+")
# Store and print the top x google search results
for i in range(x):
    link = linkElems[i].get('href')
    print ('\n')
    f.write(link)
    f.write("\r\n")
    print (link)
    print('\n')
    db.Websites.insert_one(
        {
            'link':link
        }
    )
#f.close()
print('Data is Inserted to file successfully.\n')
# Dispalys the stored data from the database on command line
webcom = db.Websites.find()
print("complete data from database:\n")
for web in webcom:
    print(web)
