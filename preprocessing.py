from urllib import request
from readability.readability import Document
from bs4 import BeautifulSoup

url=input()
a=request.urlopen(url).read()
obj=Document(a)
para=obj.summary()
title=obj.short_title()
para=BeautifulSoup(para, 'html.parser').get_text()

soup=BeautifulSoup(a, 'html.parser')

l=[]

for i in soup.find_all('a'):
	l.append(i.get('href'))

for i in l:
	print(i)

f=open('f1.txt', 'w')
s="<url>"+url+'</url>'
s+='\n'
s+="<title>"+title+'</title>'
s+='\n'
s+="<body>"+para+"</body>"
f.write(s)
f.close()
