#AKA List Comprehension
fname=input('File Name:')
if len(fname)<1 or fname == "romeo.txt":
    fname=fname
    handle=open(fname)
else:
    print('incorret name')
di=dict()
for line in handle:
    line=line.rstrip()
    word=line.split()
    for w in word:
        di[w]=di.get(w,1)+1
#Extracted the words from the file 'romeo.txt' and the counting and placed them in dictionary 'di'

print(sorted([(v,k) for k,v in di.items()]))
"""for k,v in di.items():
    lst.append((v,k))
lst=sorted(lst,reverse=True)
print(sorted([(v,k) for k,v in di.items()])) - includes all the above operations"""

print('The Top 10 Common Words are:',)
