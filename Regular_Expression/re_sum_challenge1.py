import re
total=0
count=0
hand = open('actual_regex_sum.txt')
numlist=list()
for line in hand:
    line=line.rstrip()
    #print(line)
    stuff=re.findall('([0-9]+[^a-zA-Z /]*)',line)
    #print(stuff)
    for st in stuff:
        #print(st)
        st=int(st)
        total=total+st
        count=count+1
print('total',total)
print('count: ',count)
