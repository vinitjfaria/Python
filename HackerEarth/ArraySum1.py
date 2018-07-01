N=input()
N=int(N)
num=[]
summ=int()
for i in range(1,N+1):
	num.append(input())
for s in num:
	s=int(s)
	summ+=s
print(summ)