n=int(input('请输入一个数：'))
m=n
def func(n):
	for i in range(2,n+1):
		if (n%i==0):
			print(i,end='')
			n/=i
			if n!=1:
				print('*',end='')
				return func(int(n))
func(m)