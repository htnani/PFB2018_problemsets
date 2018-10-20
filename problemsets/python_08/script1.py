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
      file_dict[seq_id] = {'A' : 0, 'G' : 0, 'C' : 0, 'T' : 0}
    else:
      file_dict[seq_id]['A'] += line.count('A')
      file_dict[seq_id]['G'] += line.count('G')
      file_dict[seq_id]['C'] += line.count('C')
      file_dict[seq_id]['T'] += line.count('T')      
except IndexError:
  print("Please provide a file name")
print(file_dict)
   
#if you want to do it with a list instead of the string, we should create an empyt list outside and then clear it up (make it empty again insdie the if statement, use commented lines)
