from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://stats.espncricinfo.com/ci/engine/records/team/match_results.html?class=2;id=2017;type=year', context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
#print(soup)
tags = soup.find_all("table")
#print(tags)
# Retrieve all from <span> to </span>
#tags = soup.find_all(class_="data-link")
for mytable in tags:
     table_body = mytable.find('tbody')
     try:
         rows = table_body.find_all('tr')
         for tr in rows:
             cols = tr.find_all('td')
            # print(cols)
             for td in cols:
                 tag=td.find_all('a')
                 tag=tag.rstrip()
                 links=tag.get('href')
                 print(links)
                 #print(tag)
                 #for link in tag:

     except:
         print("no tbody")
