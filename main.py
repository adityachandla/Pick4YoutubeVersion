from bs4 import BeautifulSoup
from urllib.request import urlopen
from random import shuffle
import re

start_url = "https://www.youtube.com" ##please do not include / in the end
url = start_url

print("Enter the number of steps: ")

for i in range(int(input())):
	t = urlopen(url)
	bsobj = BeautifulSoup(t,features="html5lib")
	l = bsobj.findAll("a",href=re.compile("/watch?"))
	finalList = list()
	for i in l:
	    if "title" in i.attrs and re.match("^[a-zA-Z0-9-\.,| ]*$",i["title"]):
	        finalList.append(i)
	shuffle(finalList)
	count = 1
	for i in finalList[:10]:
	    print(count,i["title"])
	    count += 1
	print("Enter which video you want to go to next ")
	p = int(input())
	url = start_url+finalList[p-1]["href"]

