#!usr/bin/env
 
# (followed by Jesen review session) this script takes a multi-fasta file from the command line, makes its reverse complement and writes it to a file

import sys
import re 

output = open('output_script6.fa', 'w')

def rev_compl(dna):
  dna_lower = dna.lower()
  dna_lower = dna_lower.replace('a','T')
  dna_lower = dna_lower.replace('t','A')
  dna_lower = dna_lower.replace('g','C')
  dna_lower = dna_lower.replace('c','G')
  dna_rc = dna_lower[::-1]
  return(dna_rc)
  
file = sys.argv[1]
fasta = open(file)

seq_name = ''
seq_desc = ''
seq_string = ''
    
for line in fasta:
  line = line.strip()
  if line.startswith('>'):
    if len(seq_string) > 0:
      rc_string = rev_compl(seq_string)
      output.write('>{}{}\n{}\n'.format(seq_name,seq_desc,rc_string))
      seq_string = ''
    line = line.lstrip('>')
    seq_name, seq_desc = line.split(maxsplit = 1)
  else:
     line = line.rstrip()
     seq_string += line

if len(seq_string) > 0:
  rc_string = rev_compl(seq_string)
  output.write('>{}{}\n{}\n'.format(seq_name,seq_desc,rc_string))

print('File written to output_script6.fa')


