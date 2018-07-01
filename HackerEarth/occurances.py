
# perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT
zero=0
one=0
two=0
three=0
four=0
five=0
six=0
seven=0
eight=0
nine=0

# Write your code here
for s in name:
	if s=='0':
		zero=zero+1
	if s=='1':
		one=one+1
	if s=='2':
		two=two+1
	if s=='3':
	    three=three+1
	if s=='4':
	    four=four+1
	if s=='5':
	    five=five+1
	if s=='6':
	    six=six+1
	if s=='7':
	    seven=seven+1
	if s=='8':
	    eight=eight+1
	if s=='9':
	    nine=nine+1

print('0', '  ', zero)
print('1', '  ', one)
print('2', '  ', two)
print('3', '  ', three)
print('4', '  ', four)
print('5', '  ', five)
print('6', '  ', six)
print('7', '  ', seven)
print('8', '  ', eight)
print('9', '  ', nine)
