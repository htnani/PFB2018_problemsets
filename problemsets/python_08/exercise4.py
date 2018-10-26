#!usr/bin/env python3
 
#this script create a fasta parser and extracts codons for each sequence

import sys
from Bio import SeqIO

file = sys.argv[1]
seq_dict = {}
output = open('Python_08.codons-frame-2.nt', 'w')

for seq_record in SeqIO.parse(file , 'fasta'):
  ID = seq_record.id
  seq_dict[ID] = {}
  description = seq_record.description
  seq_dict[ID]['description'] = description
  sequence = str(seq_record.seq)
  seq_dict[ID]['sequence'] = sequence
  seq_dict[ID]['codons1'] = []
  seq_dict[ID]['codons2'] = []
  seq_dict[ID]['codons3'] = []
  for key in seq_dict: #key = ID
    for subkey in seq_dict[key]: #key is either sequence, description or codons1/2/3
      if subkey == 'sequence':
        seq = seq_dict[key][subkey]
        for orf in range(0,3):
          if orf == 0:
            for i in range (orf, len(seq),3):
              if len(seq[i:i+3]) != 3:
                break
              codon1 = seq[i:i+3]
              seq_dict[key]['codons1'].append(codon1)
          elif orf == 1:
            for i in range (orf, len(seq),3):
              if len(seq[i:i+3]) != 3:
                break
              codon2 = seq[i:i+3]
              seq_dict[key]['codons2'].append(codon2)
          elif orf == 2:
            for i in range (orf, len(seq),3):
              if len(seq[i:i+3]) != 3:
                break
              codon3 = seq[i:i+3]
              seq_dict[key]['codons3'].append(codon3)        
  output.write(ID + '-frame-1-codons' + '\n' + str(seq_dict[ID]['codons1']) + '\n' + '\n' + ID + '-frame-2-codons' + '\n' + str(seq_dict[ID]['codons2']) + '\n' + '\n' + ID + '-frame-3-codons' + '\n' + str(seq_dict[ID]['codons3']) +'\n' + '\n')

output.close()
                  
