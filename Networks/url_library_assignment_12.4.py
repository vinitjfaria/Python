'''The file is a table of names and comment counts. You can ignore most of the data in the file except for lines like the following:

<tr><td>Modu</td><td><span class="comments">90</span></td></tr>
<tr><td>Kenzie</td><td><span class="comments">88</span></td></tr>
<tr><td>Hubert</td><td><span class="comments">87</span></td></tr>

You are to find all the <span> tags in the file and pull out the numbers from the tag and sum the numbers.
Answer should be 2538'''

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl
add=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_68648.html', context=ctx).read()

soup = BeautifulSoup(html, "html.parser")

# Retrieve all from <span> to </span>
tags = soup('span')
for tag in tags:
    comments=tag.contents[0]   #Extracting anything at the position 0
    comments=int(comments)     #Coverting the extracted string to integer
    add=comments+add           #Sequencial Adding
print(add)
