a = ['1','1','1','1','2','2','2','2']
b = ['a','b','c','d','e','f','g','h']

d = {}

for index, item in enumerate(a):
	print(str(index)+"\t"+str(item))
	if item in d:
		d[item].append(b[index])	
	else:
		d[item] = [b[index]]
	#d[a[i]].append(b[i]).value()
	#i += 1

print(d)
	
