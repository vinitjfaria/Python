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

#print(di)

for k,v in di.items():
    lst.append((v,k))
#(v,k) becomes tuples and lst((v,k)) is list with v=key and k=value
#Reversed the formation key becomes value and value becomes the key in the dictionary
#The elements v,k in converted to list since list can be easily sorted using sorted command
#print(lst)
lst=sorted(lst,reverse=True)
#sorted the first element of the list and then reversed the order i.e. from big to small
#print('Top 10 are',lst[:10])
for k,v in lst[:10]:
#Printing only the top 10 recurring words from the list
    print(v,k)
