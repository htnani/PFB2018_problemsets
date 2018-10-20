#!usr/bin/env
 
# this script takes a multi-fasta file and max length of each line from the command line,makes a dictionary of seq_id and sequences and wrap it to this width

import sys
import re 

output = open('output_script4.fa', 'w')


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
       file_dict[seq_id] = file_dict[seq_id] + line.rstrip()
except IndexError:
   print('Please provide a file name:')
 
width = int(sys.argv[2])
 
def seq_width(dna):
   new_dna = ''
   dna_no_n = re.sub(r'\s+','', dna)
   for i in range(0, len(dna_no_n),(width)):
     string = dna_no_n[i:i+(width - 1)]+'\n'
     new_dna = new_dna + string
     #print(len(string))    
   return new_dna
 
for seq_id in file_dict:
  seq = file_dict[seq_id]
  output.write(str(seq_id)+'\n'+str(seq_width(seq)))

