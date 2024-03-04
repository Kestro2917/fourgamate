from collections import defaultdict
a=['1','1','1','1','2','2','2','2']
b=['a','b','c','d','e','f','g','h']

d= defaultdict(list)
i=0
e=[]
while i < len(a):
	d[a[i]].append(b[i])
	i += 1
print(d)
