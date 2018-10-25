#!usr/bin/env python3

#this script parse FASTA file into the dictionary, calculates the number of nt and GC content

import sys
  
file_dict = {}
  
  
try:
  file = sys.argv[1]
  fasta = open(file)
  print("User provided file:" , file)
  for line in fasta:
    if line.startswith('>'):
      line = line.lstrip('>')
      seq_id = line.rstrip()
      file_dict[seq_id] = {'A' : 0, 'G' : 0, 'C' : 0, 'T' : 0}
    else:
      file_dict[seq_id]['A'] += line.count('A')
      file_dict[seq_id]['G'] += line.count('G')
      file_dict[seq_id]['C'] += line.count('C')
      file_dict[seq_id]['T'] += line.count('T')
except IndexError:
  print("Please provide a file name")

Atotal = 0
Gtotal = 0
Ttotal = 0
Ctotal = 0


for seq_id in file_dict:
  Atotal += file_dict[seq_id]['A']  
  Gtotal += file_dict[seq_id]['G']  
  Ctotal += file_dict[seq_id]['C']  
  Ttotal += file_dict[seq_id]['T']  
  length_total = Atotal + Gtotal + Ttotal + Ctotal
  length = file_dict[seq_id]['A'] + file_dict[seq_id]['G'] + file_dict[seq_id]['C'] + file_dict[seq_id]['T']  
  GC_cont = round((file_dict[seq_id]['G']+file_dict[seq_id]['C'])/length ,2)
  print(seq_id, ('\t'), GC_cont)  


print('The total frequency of A is:{}, G:{}, C:{},T:{}'.format(round(Atotal/length_total,2), round(Gtotal/length_total,2), round(Ctotal/length_total,2), round(Ttotal/length_total,2)))
