testcase=int(input())
#def countBits(n):
#	n=int(n)
#	count = 0
#	while (n):
#		count += 1
#		n>>=1
#	return count

def division(dividend):
	dividend=int(dividend)
	divisor=1
	x=0
	while(1):
		quotion=dividend/divisor
		#print(divisor,'',quotion)
		#quotion=int(quotion)
		divisor=divisor+1
		#q=countBits(quotion)
		#d=countBits(divisor)
		x=x+1
		if dividend==divisor:
			break
	print(x)
	return x

for t in range(1,testcase+1):
	division(input())

