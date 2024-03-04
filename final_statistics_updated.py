from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def number(j,comp):
	i=j
	a=[]
	for my_seq in comp:
		a.append(my_seq[i])
	return a
def length(comp):
	for my_seq in comp:
		n=len(my_seq)
	return(n)

def main():
	f1=open("my_final_stats.txt","w+")
	comp=[]
	arr=[]
	for seq_record in SeqIO.parse("april_30th_gaps_filled.fasta","fasta"):
		my_seq=seq_record.seq
		arr=list(my_seq)
		comp.append(arr)	
	n1=length(comp)
	#f1.write(str(n1))
	print(n1)
	i=0
	while i<=n1: 	
		a=[]
		a1=[]
		a=number(i,comp)
		a1=a
		#print(a1)
		#print(a)
		res=[]
		for j in a:
			if j not in res:	
				res.append(j)
		#res.remove('-')
		if len(res) == 1:
			count=a1.count(res[0])
			print(str(len(res))+"\t"+res[0]+"\t"+str(count))
		if len(res) == 2:
			count1=a1.count(res[0])
			count2=a1.count(res[1])
			if count1 > count2:
				print(str(len(res))+"\t"+res[0]+"\t"+str(count1)+"\t"+res[1]+"\t"+str(count2))
			else:	
				print(str(len(res))+"\t"+res[1]+"\t"+str(count2)+"\t"+res[0]+"\t"+str(count1))
		d={}
		if len(res) == 3:
			for e in res:
				d[e]=a1.count(e)
			sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
			print(str(len(res))+"\t"+str(sort_d))
			#print(sort_d)

		d1={}
		if len(res) == 4:
			for y in res:
				d1[y]=a1.count(y)
			sort_d1 = sorted(d1.items(), key=lambda x: x[1], reverse=True)
			print(str(len(res))+"\t"+str(sort_d1))
		i=i+1

if __name__ == "__main__":
	main()
