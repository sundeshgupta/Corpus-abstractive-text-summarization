#!/usr/bin/env python
# coding: utf-8

# In[6]:


from urllib import request, error
from readability.readability import Document
from bs4 import BeautifulSoup
from collections import deque


# In[53]:


url= 'https://www.freepressjournal.in/entertainment/jennifer-lopez-has-no-plans-of-going-back-on-sets-anytime-soon'
domain = 'https://www.freepressjournal.in/'

http = 'http://'
https = 'https://'

cnt = 0

visited = {domain}

f=open('f1.txt', 'w+')

q = deque()
q.append(url)

while len(q) > 0:
    url = q.popleft()
    
    if ' ' in url:
        continue
    
    req = request.Request(url, headers={'User-Agent': 'XYZ/3.0'})
        
    if url in visited:
        continue
    
    visited.add(url)
    
    print(url)
    
    try: request.urlopen(req)
    except error.URLError as e:
        continue
    
    a = request.urlopen(req).read()
    
    obj = Document(a)
#     para = obj.summary()
#     title = obj.short_title()

    para = BeautifulSoup(para, 'html.parser').get_text()

    soup = BeautifulSoup(a, 'html.parser')

    l=[]

    for i in soup.find_all('a'):
        l.append(i.get('href'))    
    
    time = soup.find('time')
    
    date = ""
    
    if time is not None:
        date = time['datetime']

    head = soup.find('div', attrs = {'class':'story-meta-info-m__headline__1S-aa'})

    title = ""
    
    if head is not None:
        title = head.text.strip()
    
    story = soup.find('div', attrs = {'class':'story-element story-element-text'})
    
    para = ''
    
    if story is not None:
        for i in story.find_all('p'):
            para += i.text.strip()
        
#     print(para)
    
    for i in l:
        if i is None:
            continue
        if domain in i:
            q.append(i)
        if (http not in i) and (https not in i):
            q.append(domain + i)

    print(title)
            
    if title == "":
        continue
    
    title.replace('\n', ' ')
    para.replace('\n', ' ')
    
    cnt += 1
    s="<url id = '" + str(cnt) + "' >"+url+'</url>'
    s+='\n'
    s+="<title id = '" + str(cnt) + "' >"+title+'</title>'
    s+='\n'
    s+="<body id = '" + str(cnt) + "' >"+para+"</body>"
    s+='\n'
    s+="<date id = '"+ str(cnt) + "' >" + date + "</date>"
    s+='\n'
    f.write(s)
    
f.close()


# In[54]:


print(cnt)

