
from urllib import request,error
from bs4 import BeautifulSoup 
from collections import deque

def get_summary_article_date(soup):

    summary = ""
    table = soup.find( 'h3',attrs = {'class':'mkdf-post-title'})

    if table is None:
        return None, None, None

    summary = table.text.strip()
    print(summary)

    article=""
    for row in table.find_all_next('p'):
        text = row.text
        article += text.strip() +" "

    if table is None:
        return None, None, None
    
    table = soup.find('span', attrs = {'class':'mkdf-blog-date'})

    date = ""
    if table is not None:
        date = table.text.strip()
        print(date)
    return summary, article, date

URL = "https://www.articlecity.com/blog/why-dont-people-believe-in-climate-change-a-discussion-about-deniers/"
domain = "https://www.articlecity.com/"

http = 'http://'
https = 'https://'
visited = set()
cnt = 0

f=open('oe.xml','a')

q = deque()
q.append(URL)

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
        if domain in i:
            q.append(i)
        if (http not in i) and (https not in i):
            q.append(domain + i)
            
            

    summary, article, date = get_summary_article_date(soup)
    if summary is None or article is None :
        continue 
    cnt+=1
    s=("<url >"+URL+"</url>")
    s+='\n'
    s+=("<title>"+summary+'</title>')
    s+='\n'
    s+=("<body >"+article+"</body>")
    s+='\n'
    s+=("<date >"+date+"</date>")
    s+='\n'
    f.write(s)
  
f.close()







