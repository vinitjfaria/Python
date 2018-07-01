"""Read through the mbox-short.txt and figure out the distribution by hour of the day for each of the
messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the
string a second time using a colon."""

fname = input("Enter file name: ")
if len(fname) < 1 : fname = "mbox-short.txt"

fh = open(fname)
word=list()
di=dict()
lst=list()
for line in fh:
      line=line.rstrip()
      if line.startswith('From '):
          line=line.split()
          #print(line)
          word=line[5:6]
          #print(word)
          for w in word:
              w=w.split(':')
              w=w[0:1]
              #print(w)
              for words in w:
                  di[words]=di.get(words,0)+1
#print(di)

for k,v in di.items():
    lst.append((k,v))
lst=sorted(lst)
#print(lst)
for k,v in lst:
    print(k,v)
