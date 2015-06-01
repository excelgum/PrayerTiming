#main.py
__author__ = 'Anas'
from bs4 import BeautifulSoup
import urllib.request

page = str(urllib.request.urlopen("http://wiao.org").read())
soup = BeautifulSoup(page)
print("Data Collected from:", soup.title.string,"[http://wiao.org]")
ptable=soup.find_all('table')[2].find_all('td')
#Fajar
for i in range(6):
    print(ptable[3*i].string,end=" "*(15-len(ptable[3*i].string)))
    print(ptable[3*i+1].string)
input()



