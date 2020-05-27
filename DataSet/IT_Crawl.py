from urllib import request,error
from bs4 import BeautifulSoup 
from collections import deque
import emoji
import re

def remove_unwanted(inputString):
    return inputString.encode('ascii', 'ignore').decode('ascii')

def get_summary_article_date(soup):

    summary = ""
    # table = soup.find( 'h1',attrs = {'class':'K55Ut'})
    table = soup.find( 'h1')
    if table is None:
        return None, None, None

    summary = table.text.strip()
    summary=summary.replace('<','')
    summary=summary.replace('>','')
    summary=summary.replace('&','')
    if len(summary)<25:
        return None, None, None
    print(summary)

    article=""
    for row in table.find_all_next('p'):
        text = row.text
        article += text.strip() +" "
        article=article.replace('<','')
        article=article.replace('>','')
        article=article.replace('&','')
    if len(article)<200:
        return None, None, None

    if table is None:
        return None, None, None
    
    table = soup.find('span', attrs = {'class':'text-dt'})

    date = ""
    if table is not None:
        date = table.text.strip()
        print(date)
    return summary, article, date

URL = "https://www.hindustantimes.com/business-news/now-microsoft-eyes-stake-in-jio/story-AFLHYwozmBPB0L6Y3ffzyI.html"
domain = "https://www.hindustantimes.com/"

http = 'http://'
https = 'https://'
visited = set()
cnt = 0

f=open('it123.xml','w')

q = deque()
q.append(URL)

while len(q)>0:
    
    URL=q.popleft()
    req=request.Request(URL,headers = {"User-Agent": "Mozilla/5.0"})
    
    if cnt>2000:
        break

    if URL in visited:
        continue

    visited.add(URL)
    
    print(cnt)
    print(URL)

    req_s=0;
    try: request.urlopen(req)
    except error.URLError as e:
        
        continue

    a=request.urlopen(req).read()
    soup = BeautifulSoup(a, 'html.parser')

    l=[]

    for i in soup.find_all('a'):
        l.append(i.get('href'))    

    for i in l:
        if i is None:
            continue
        if len(i)<65:
            continue
        if domain in i:
            q.append(i)
        if (http not in i) and (https not in i):
            q.append(domain + i)
            
            

    summary, article, date = get_summary_article_date(soup)
    if summary is None or article is None :
        continue 

    s=("<url >"+URL+"</url>")
    s+='\n'
    s+=("<title>"+summary+'</title>')
    s+='\n'
    s+=("<body >"+article+"</body>")
    s+='\n'
    s+=("<date >"+date+"</date>")
    s+='\n'
    if len(s)<400:
        continue
    cnt+=1
    s=s.replace('&','')
    remove_unwanted(s)
    f.write(s)
  
f.close()
