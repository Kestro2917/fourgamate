from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

class twin_mutation:
	def seq_length(self):
		a=[]
		for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
			my_seq=seq_record.seq
			length=len(my_seq)
			a.append(my_seq[0])
		col_len=len(a)
		return length,col_len
	def duplicate_removal(self,i):
		self.a=[]
		self.res=[]
 		#print(i)
		for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
			my_seq=seq_record.seq
			self.a.append(my_seq[i])
	
		for j in self.a:
			if j not in self.res:
				self.res.append(j)
		#print(self.res)
		self.res.remove('-')
		return self.res
			
	def comparision(self,pos,length,col_length):
		a=[]
		i=pos+1
		while i < length:
			counter=0
			for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
				my_seq=seq_record.seq
				if (my_seq[pos] == my_seq[i] or my_seq[pos] == "-" or "-" == my_seq[i]) :
					counter += 1
			i += 1
			if counter == col_length:
				pos1=pos+1
				i1=i
				print(str(pos1)+"\t"+str(i1)+"are twin muation")
		
				

def main():
	#d=twin_mutation()
	#length,col_length = d.seq_length()
	#print(length)
	#print(col_length)
	#a=[]
	#i=0
	#while i < length:
	#	res=[]
	#	res=d.duplicate_removal(i)
	#	if len(res) >= 2:
	#		#print(i)
	#		d.comparision(i,length,col_length)
	#	#print(a)
	#	
	#	i += 1
	

if __name__=="__main__":
	main()
