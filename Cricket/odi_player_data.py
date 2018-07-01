from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?class=2;current=2;id=6;type=team', context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all from <span> to </span>
tags = soup.find_all(class_="data-link")

for tag in tags:
    links=tag.get('href')
    link='http://www.espncricinfo.com'+links
    #print(link)
    html1 = urlopen(link, context=ctx).read()
    soups = BeautifulSoup(html1, "html.parser")
    table = soups.find_all("table")
    for mytable in table:
             table_body = mytable.find('tbody')
             try:
                 rows = table_body.find_all('tr')
                 for tr in rows:
                     cols = tr.find_all('td')
                     for td in cols:
                         print(td.text)
                 type(td)
             except:
                 print("no tbody")


'''comments=int(comments)     #Coverting the extracted string to integer
add=comments+add           #Sequencial Adding
print(add)'''
