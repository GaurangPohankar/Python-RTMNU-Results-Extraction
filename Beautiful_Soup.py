import urllib
import requests
from bs4 import BeautifulSoup
import os

url = "https://ubuntu.com"

soup = BeautifulSoup(requests.get(url).text, "lxml")

# kill all script and style elements
for script in soup(["script", "style"]):
    script.decompose()    # rip it out

# get text
text = soup.get_text()
file = open("title.txt","w")
file.writelines(soup.title.string)
file.close()

# break into lines and remove leading and trailing space on each
lines = (line.strip() for line in text.splitlines())
# break multi-headlines into a line each
chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
# drop blank lines
text = '\n'.join(chunk for chunk in chunks if chunk)

file = open("text.txt","w")
file.writelines(text)
file.close()

##print(text)
links=[]
for link in soup.find_all('a'):
    #print(link.get('href'))
    links.append(link.get('href')+' '+',')
    print(links)
    
#print(links)
file = open("links.txt","w")
file.writelines(links)
file.close() 
