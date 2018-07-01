from urllib.request import urlopen
import ssl
import xml.etree.ElementTree as ET
add=0
count=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_68650.xml', context=ctx).read()
tree=ET.fromstring(html)
lst=tree.findall('comments/comment')
for item in lst:
     number=item.find('count').text
     number=int(number)
     add=number+add
     count=count+1

print('Sum:',add)
print('Count',count)
