from Bio import SeqIO
from Bio.Seq import Seq
from Bio.Alphabet import IUPAC

class fourgamet:
	def length(self):
		for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
			my_seq=seq_record.seq
			length=len(my_seq)
		return length

	def position(self, num):
		self.a = []
		for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
			my_seq=seq_record.seq
			self.a.append(my_seq[num])
		return self.a	
	def duplicate_removal(self, array):
		self.array = []
		self.array = array
		self.res = []
		for j in self.array:
			if j not in self.res:
				self.res.append(j)
		self.res.remove('-')
		return self.res 
	def four_gamet(self,pos,res,length):
		i = pos+1
		#print(i)
		#print(res[0]+"\t"+res[1])
		while i < length:
			d = {}
			for seq_record in SeqIO.parse("aln_human.fasta","fasta"):
				my_seq=seq_record.seq
				if my_seq[pos] in d:
					d[my_seq[pos]].append(my_seq[i])
				else:
					d[my_seq[pos]] = [my_seq[i]]
			i += 1	
			if (res[0] in d[res[0]] and res[1] in d[res[0]] and res[0] in d[res[1]] and res[1] in d[res[1]]):
				pos1=pos+1
				i1=i+1
				print(str(pos1)+"\t"+str(i1))
			#print(d)
			
		 
				
def main():
	b = fourgamet()
	length = b.length()
	print(length)
	i =0
	while i <= length:
		a = []
		a = b.position(i)
		res = []
		res = b.duplicate_removal(a)
		if len(res) == 2:
			b.four_gamet(i,res,length)
			#print(res)
		d={}
		res1=[]
		if len(res) > 2:
			for e in res:
				d[e]=a.count(e)
			sort_d = sorted(d.items(), key=lambda x: x[1], reverse=True)
			res1.append(sort_d[0][0])
			res1.append(sort_d[1][0])
			b.four_gamet(i,res1,length)					
		i += 1
	

if __name__ == "__main__":
	main()
		
