from urllib.request import urlopen
import ssl
import json
add=0
count=0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urlopen('http://py4e-data.dr-chuck.net/comments_68651.json', context=ctx).read()

info = json.loads(html)
lst=info["comments"]

for item in lst:
    numbers=item['count']
    numbers=int(numbers)
    add=numbers+add
    count=count+1

print('Count:', count)
print('Sum:', add)
