import urllib.request
from bs4 import BeautifulSoup
import re
import ssl
url = input('Enter - ')
# url = 'http://python-data.dr-chuck.net/known_by_Fikret.html'
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE
for i in range(7):
    html = urllib.request.urlopen(url,context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    url = tags[17].get('href')
lname = re.findall('y_(.+).h',url)
print(lname)
