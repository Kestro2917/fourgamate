fopen = open("/alina-data1/Bikram/Final_Host_protein_data.txt","r")

a = []
j=1
for line in fopen:
	#print(line)
	a = line.split("\t")
	print(">"+a[0]+str(j))
	i=1
	seq=""
	while(i<len(a)):
		seq = seq+a[i]
		#rint(a[i])	
		i=i+1
	print(seq)
	j = j+1
