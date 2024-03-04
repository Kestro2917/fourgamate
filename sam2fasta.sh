samtools view -S -b all_human_20200601.sam > all_human_20200601.bam
samtools sort all_human_20200601.bam -o all_human_20200601_srt.bam
samtools index all_human_20200601_srt.bam
java -jar /home/code/jvarkit/jvarkit/dist/sam4weblogo.jar -r NC_045512.2:1-29903 all_human_20200601_srt.bam > all_human_20200601.fasta