print("how many Fibonacci numbers do you want ?")
nums = int(input())
a=0
b=1
while nums > 0:
	print(a)
	c=a+b
	a=b
	b=c
	nums=nums-1
