'''Using the Python language, have the function LetterChanges(str) take the str parameter being passed and modify it using the 
following algorithm. Replace every letter in the string with the letter following it in the alphabet (ie. c becomes d, z becomes a). 
Then capitalize every vowel in this new string (a, e, i, o, u) and finally return this modified string. '''

'''Input:"hello*3"

Output:"Ifmmp*3"


Input:"fun times!"

Output:"gvO Ujnft!"'''
str="a confusing /:sentence:/[ this is not!!!!!!!~"
str=str.lower()
vowels = ('a', 'e', 'i', 'o', 'u')
val=0
cha=''
char=''
for s in str:
	val=ord(s)
	if val>=97:
		val=val+1
		ch=chr(val)
		cha=cha+ch
	else:
		ch=chr(val)
		cha=cha+ch

for vol in cha:
	if vol in vowels
		vol=vol.upper()
	char=char+vol
print(char)
