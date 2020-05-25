#!/usr/bin/env python
# coding: utf-8

# In[1]:


import requests 
from bs4 import BeautifulSoup 
from collections import deque
import pickle
from pickle import dump, load


# In[2]:


def get_summary_article_date(soup):
    summary = ""
    table = soup.find('div', attrs = {'class':'article-item__teaser-text'}) 
    if table is None:
        return None, None, None
    summary = table.text.strip()
    table = soup.find('div', attrs = {'class':'article__body'}) 
    if table is None:
        return None, None, None
    article = ""
    for row in table.find_all_next('p'):
        if row.span is not None and row.span.text=="Nature":
            break
        text = row.text
        article += text.strip() + " "
    table = soup.find('div', attrs = {'class':'article__date'})
    date = ""
    if table is not None:
        date = table.text.strip()
    return summary, article, date


# In[14]:


try:
    extracted_url = load(open("extracted_url.pkl", "rb"))
except FileNotFoundError:
    extracted_url = set()
try:
    id = load(open("id.pkl", "rb"))
except FileNotFoundError:
    id = int(0)
print(id)
print(extracted_url)


# In[17]:


URL = "https://www.nature.com/"
domain = 'https://nature.com'
article_domain = '/articles'
http = 'http://'
https = 'https://'
visited = set()
cnt = 0

f=open('nature.xml', 'a')

q = deque()
num_iterations = 3
while(num_iterations > 0):
    num_iterations -= 1
    q.append(URL)
    req_success = 0
    if len(q)==0:
        break
    URL = q.popleft()
    try:
        req = requests.get(URL)
        req_success = 1
    except requests.exceptions.RequestException as e:  # This is the correct syntax
        print('Could not get URL ' + str(URL))
    
    if not req_success:
        continue

    if URL in visited:
        continue

    visited.add(URL)

    print(URL)

    soup = BeautifulSoup(req.content, 'html5lib')

    l=[]

    for i in soup.find_all('a'):
        l.append(i.get('href'))    

    for i in l:
        if i is None:
            continue
        if domain in i:
            q.append(i)
        if (http not in i) and (https not in i) and (article_domain in i):
            q.append(domain + i)

    if article_domain in URL:
        summary, article, date = get_summary_article_date(soup)
        if summary is None or article is None or URL in extracted_url:
            continue 
        s=("<url id = \'{id}\'>"+URL+"</url>").format(id = id)
        s+='\n'
        s+=("<title id = \'{id}\'>"+summary+'</title>').format(id = id)
        s+='\n'
        s+=("<body id = \'{id}\'>"+article+"</body>").format(id = id)
        s+='\n'
        s+=("<date id = \'{id}\'>"+date+"</date>").format(id = id)
        s+='\n'
        f.write(s)
        extracted_url.add(URL)
        id += 1

f.close()


# In[16]:


with open("extracted_url.pkl", "wb") as pickle_file:
    pickle.dump(extracted_url, pickle_file)
with open("id.pkl", "wb") as pickle_file:
    pickle.dump(id, pickle_file)
print(id)
print(len(q))


# In[ ]:




