import re
count=0
hand = open('mbox-short.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    stuff=re.findall('^X-DSPAM-Confidence: ([0-9.]+)',line)
    print(stuff)
    if len(stuff)!=1:
        continue
        count=count+1
#    num = float(stuff[0])
#    numlist.append(num)
#print('Maximum:',max(numlist))'''
print('count',count)
