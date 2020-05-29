from urllib import request,error
from bs4 import BeautifulSoup 
from collections import deque
import emoji
import re

# Gets rid of unnecessary characters(unicode characters)
def remove_unwanted(inputString): 
    return inputString.encode('ascii', 'ignore').decode('ascii')

# Returns summary, content and date of article
def get_summary_article_date(soup):

    summary = ""

    # Extracts summary
    table = soup.find( 'h1')
    if table is None:
        return None, None, None

    summary = table.text.strip()

    # Removes tags
    summary=summary.replace('<','')
    summary=summary.replace('>','')
    summary=summary.replace('&','')

    # Removes small length summaries to improve dataset
    if len(summary)<25:
        return None, None, None
    
    print(summary)

    article=""

    # Extracts article content
    for row in table.find_all_next('p'):
        text = row.text
        article += text.strip() +" "

        # Removes tags
        article=article.replace('<','')
        article=article.replace('>','')
        article=article.replace('&','')

    # Fixed minimum length to improve dataset
    if len(article)<200:
        return None, None, None

    if table is None:
        return None, None, None
    
    table = soup.find('span', attrs = {'class':'text-dt'})

    # Extracts date
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
cnt = 0 # No of articles stored

f=open('it123.xml','w')

q = deque()
q.append(URL)

# Appling BFS to visit links
while len(q)>0:
    
    URL=q.popleft()
    req=request.Request(URL,headers = {"User-Agent": "Mozilla/5.0"})
    
    if cnt>10000:
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
        # Helps filter unnecessary urls
        if len(i)<65:
            continue

        #Makes the process many times faster and filters unnecessary urls
        blist=['twitter.com','facebook.com','linkedin.com','reddit.com','bollywood','regional-movies','music','television','login']   
        illegal=0

        for w in blist:
            if w in i:
                illegal=1

        if illegal==1:
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
    # Improves dataset
    if len(s)<400:
        continue
    cnt+=1
    s=s.replace('&','')
    remove_unwanted(s)

    # Writing s to xml file
    f.write(s)
  
f.close()
