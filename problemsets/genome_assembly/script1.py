#!usr/bin/env python3

#this script create a fasta parser for pacbio contig output file, with some general stats of the file

from Bio import SeqIO

sequences = []
lengths = []
total_no_contig = 0
genome_size = 0
#seq_dict = {}

for seq_record in SeqIO.parse('ecoli.fasta', 'fasta'):
  print(seq_record)
 # print(type(seq_record))
  #print(seq_record.seq.count('A'))
  #print(seq_record.id)
  ID = seq_record.id #u don'thave to do it, because by default it assigins sec_record to sequence and treats it as a string
  description = seq_record.description
  sequence = seq_record.seq
  seq_string = str(sequence)
 # seq_id = str(ID)
 # seq_dict[seq_id] = {}
 # seq_dict['description'] = '' you only need to intialize this empty string in if esle statement because it has to appear both in if and in else, otherwise you dont need it
 # seq_dict['description'] = str(description) 
  sequences.append(seq_string)
  genome_size += len(seq_string)
  lenght = int(len(seq_string))
  lengths.append(lenght)
  total_no_contig += 1
  
sorted_lengths = sorted(lengths)

L_50_sm = 0
N_50_num = 0
N_50 = []

for i, contig_length in enumerate(sorted_lengths):
  N_50_num += contig_length
  L_50_sm += 1
  if N_50_num >= (genome_size/2):
    N_50.append(sorted_lengths[i])
    break

L_50 = len(lengths) - (L_50_sm - 1)

print('\n 1.The number of contigs in the file: {}\n 2.The shortest contig {}\n 3.The longest contig: {}\n 4.L_50: {}\n 5.N_50: {} nt.'.format(len(lengths),min(sorted_lengths), max(sorted_lengths),L_50, N_50[0]))


