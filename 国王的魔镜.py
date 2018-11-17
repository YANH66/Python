s=input()
L=len(s)
l=int(L/2)
flag=0
if L%2==1:
	print(len(s))
elif L%2==0:
	while(True):
		for i in range(0,int(l)):
			if(s[i]!=s[int(L)-i-1]):
				print(len(s[0:L]))
				flag=1
				break
		if flag==1:
			break
		L//=2