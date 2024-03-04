from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC
import random

f = open("mutated_20%.fasta","w")


d = {"A":"N","R":"Y","N":"F","C":"A","D":"I","E":"H","F":"A","G":"K","H":"T","Q":"V","I":"D","L":"G","K":"A","M":"N","P":"I","S":"E","T":"E","W":"M","Y":"L","V":"R"}

record=SeqIO.read("s_protein.fasta","fasta")


seq = str(record.seq)


count = 1
for i in range(100000):
	array = random.sample(range(0,1272),255)

	#print(array)
	
	for n in array:
		if seq[n] in d.keys():
			my_seq = seq.replace(seq[n],d[seq[n]],n+1)
	f.write(">"+str(count)+"\n")
	f.write(my_seq+"\n")
	count += 1
		
