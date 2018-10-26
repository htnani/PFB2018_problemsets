#!usr/bin/env python3

#this script create a fasta parser and extracts codons for each sequence

import sys
from Bio import SeqIO

file = sys.argv[1]
seq_dict = {}
output = open('Python_08.codons-frame-1.nt', 'w')


for seq_record in SeqIO.parse(file , 'fasta'):
  ID = seq_record.id
  seq_dict[ID] = {}
  description = seq_record.description
  seq_dict[ID]['description'] = description
  sequence = str(seq_record.seq)
  seq_dict[ID]['sequence'] = sequence
  seq_dict[ID]['codons'] = []
  for key in seq_dict:
    for subkey in seq_dict[key]:
      if subkey == 'sequence':
        seq = seq_dict[key][subkey]
        for i in range (0, len(seq),3):
           if len(seq[i:i+3]) != 3:
             break
           codon = seq[i:i+3]
           seq_dict[key]['codons'].append(codon)
  output.write(ID + '-frame-1-codons' + '\n' + str(seq_dict[ID]['codons']) + '\n')

output.close()           
