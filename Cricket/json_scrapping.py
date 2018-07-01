import pandas as pd
import requests
from bs4 import BeautifulSoup
 
res = requests.get("http://stats.espncricinfo.com/ci/engine/records/averages/bowling.html?id=12210;type=tournament")
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')
df = pd.read_html(str(table))
#print(df[0].to_json(orient='records'))
players = df['Player'].tolist()
wickets = df['Wkts'].tolist()
print(players)