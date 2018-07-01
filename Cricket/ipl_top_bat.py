from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
bat_list=list()
bowl_list=list()
count = 0
num_player=input('Numbers of Players: ')
num_player=int(num_player)

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://stats.espncricinfo.com/ci/engine/records/averages/batting.html?id=12210;type=tournament', context=ctx).read()

soup = BeautifulSoup(html, "html.parser")


# Retrieve the Table Contents
tags = soup.find_all("tbody")

for mytable in tags:
    rows = mytable.find_all('tr')

    for tr in rows:
        cols = tr.find_all('td')
        count=count+1
        for td in cols:
            '''for link in td.find_all('a'):
                l=link.get('href')
                l='http://www.espncricinfo.com'+l
                html = urlopen(l, context=ctx).read()
                soup = BeautifulSoup(html, "html.parser")
                tags = soup.find_all("table")'''



            count=count+1
            if count<=(17*num_player): #no. of player you want to see in the team
                bat_list.append(td.text)

#To See the Whole Team Statistics(Batting an Bowling) remove the
# sign from the print() below
print('Batting Stats', bat_list)
