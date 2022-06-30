a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
a.sort
b.sort
for i in range(len(a)):
	print("("+str(a[i])+","+")",end=', ')
	if(i!=len(a)-1):
