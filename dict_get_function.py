fname=input('File Name:')
if len(fname)<1 or fname == "romeo.txt":
    fname=fname
    handle=open(fname)
else:
    print('incorret name')
di=dict()
for line in handle:
    w=line.split()
    #print(w)
    for word in w:
        print(word)
        di[word]=di.get(word,1)+1
"""if the key is not there then the count is 1, if the key reoccurs then add 1 to the previous value of that key"""

""" The get function is basically a combination of if and else statements
if word in di:
       di[w]=di[w]+1

else:
    di[w]=1
This is the expantion of how get function works"""
"""When get() is called, python checks if the specified key i.e. word exists in the dictionary
i.e. di. If it does then get() returns the value i.e. 1 but if the key does not exist in the dictionary
di then get() returns the value that is already specified """
print(di)
