from Bio.Align.Applications import ClustalwCommandline
in_file = "/alina-data1/Bikram/spike.fasta"
cline = ClustalwCommandline("clustalw", infile=in_file)

print(cline)
import os
stdout, stderr = cline()
print(cline)
#clustalw_cline = 

