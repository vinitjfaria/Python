fname = raw_input("Enter file name: ")
if len(fname) == 0:
    fname = 'romeo.txt'
fh = open(fname)
lst = list()

for line in fh:

    for i in line.split():

        if not i in lst:

            lst.append(i)

lst.sort()
print (lst)
