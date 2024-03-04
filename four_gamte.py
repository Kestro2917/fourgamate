class four_gamete:
	f=open("four_gamet.txt","r")
	#f2=open("result.txt","w")
	arr=[]
	d={}
	d1={}
	d2={}
	d3={}
	for line in f:
		arr=line.split("\t")
		d[arr[0]]=arr[1]
		d1[arr[2]]=arr[3]
		d2[arr[4]]=arr[5]
		d3[arr[6]]=arr[7]
	#print(d)
	#print(d['14353'])
	#print(d['2982'])
	a=[]
	f1 =open("four_gamet.txt","r")
	for l in f1:
		a=l.split("\t")
		a1= d1[a[0]] if a[0] in d1.keys() else 0
		a2= d2[a[0]] if a[0] in d2.keys() else 0
		a3= d3[a[0]] if a[0] in d3.keys() else 0
		print(a[0]+"\t"+a[1]+"\t"+str(a1)+"\t"+str(a2)+"\t"+str(a3))
		
def main():
	b=four_gamete()

if __name__ == "__main__":
	main()
