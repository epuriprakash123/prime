n=int(input())
m=int(n/2)
flag=0
for i in range(m):
	if((n%(i+2))==0):
		flag=1
		break
if(flag==1):
	print("no")
else :
	print("yes")
	
