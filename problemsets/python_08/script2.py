#!usr/bin/env

# this script takes a multi-fasta file and calculate the nt composition of each sequence

import sys

file_dict = {}


try:
  file = sys.argv[1]
  fasta = open(file)
  print("User provided file:" , file)
  for line in fasta:
    if line.startswith('>'):
      seq_id = line.rstrip()
      file_dict[seq_id] = ''
    else:
      file_dict[seq_id] = file_dict[seq_id] + (line.rstrip())
      #sequences  = ''.join(file_dic)
      #file_dict[seq_id] = seq 
except IndexError:
  print("Please provide a file name")
print(file_dict)

for seq_id in file_dict:
  nt_comp = {'A' : '', 'G' : '', 'C' : '', 'T' : '' }
  nt_comp['A']= file_dict[seq_id].count('A')
  nt_comp['G'] = file_dict[seq_id].count('G')
  nt_comp['C'] = file_dict[seq_id].count('C')
  nt_comp['T'] = file_dict[seq_id].count('T')   
  print(nt_comp)



