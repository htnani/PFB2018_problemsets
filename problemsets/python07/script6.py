#!ussarry.bin/env python3

# this script finds all occurences of ApoI restriction sites in Python_07_ApoI.fasta

import re

seq = open('Python_07_ApoI.fasta')

new_seq = ''
counts = 0
for line in seq:
  if counts == 0:
    line.rstrip()  
    counts += 1
  else:
    new_line = line.rstrip()
    new_seq += new_line

#printing match is not necesarry

for match in re.finditer('(.{5}[AG])(AATT[CT].{5})', new_seq):
  up = match.group(1)
  down = match.group(2) 
  print(match, up,'^',down, '\n')

