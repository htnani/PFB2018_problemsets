#!usr/bin/env python3

#this script create a fasta parser with some general stats of the file

from Bio import SeqIO

GC_content = []
sequences = []
total_seq = 0
total_nt = 0

for seq_record in SeqIO.parse('1.fasta', 'fasta'):
  ID = seq_record.id
  description = seq_record.description
  sequence = seq_record.seq
  seq_string = str(sequence)
  sequences.append(seq_string)
  num_nt = len(seq_string)
  total_nt += num_nt
  G = sequence.count('G')
  C = sequence.count('C')
  GC_cont = round((G+C)/num_nt,2)
  GC_content.append(GC_cont)
  total_seq += 1
  print(ID, sequence)

total_GC = float(sum(GC_content[:]))
print(total_GC)

print('\nsequence count:\t{}\n total number of nucleotides:\t{}\n avg len:\t{}\n shortest len:\t{}\n longest len:\t{}\n avg GC content: \t{}\n lowest GC content:\t{}\n highest GC content:\t{}'.format(total_seq, total_nt, round((total_nt/total_seq),2), len(min(sequences)), len(max(sequences)), round(total_GC/total_seq,2), min(GC_content), max(GC_content)))   
