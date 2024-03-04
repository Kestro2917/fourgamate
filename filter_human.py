from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

def main():
	a=[]
	key = []
	f=open("metadata_20200801.txt","r")
	f1=open("all_human.fasta","w")
	for line in f:
		a= line.split("\t")
		key.append(a[0])
	res =key[:1] + [j for i,j in zip(key,key[1:]) if i or j]
	print(res)
		
	arr= []
	dict_seq = {}
	for seq_record in SeqIO.parse("sequences.fasta","fasta"):
		my_id = seq_record.id
		my_seq = seq_record.seq
		arr = list(my_seq)
		#if 'N' in arr:
   			#arr.remove('N')
		#if 'n' in arr:
			#arr.remove('n')
		dict_seq[my_id] = arr

	for k,v in dict_seq.items():
		if k in res:
			s = ''.join(v)
			s1=s.upper()
			s2=s1.replace('N','')
			s3=s2.replace('X','')
			s4=s3.replace('-','')
			#f1.write(">"+k+"\n"+s4+"\n")

if __name__ == "__main__":
	main()
