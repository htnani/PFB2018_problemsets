#!usr/bin/env
   
# (followed by Jesen review session) this script takes a multi-fasta file fr    om the command line, makes its reverse complement and writes it to a file
  
import sys
import re 

dna_str= 'ggAtaGAGGATGAGGAgagtacaccatagga'
  
output = open('output_script6.fa', 'w')
def rev_compl(dna):
  dna_lower = dna.lower()
  dna_lower = dna_lower.replace('a','T')
  dna_lower = dna_lower.replace('t','A')
  dna_lower = dna_lower.replace('g','C')
  dna_lower = dna_lower.replace('c','G')
  dna_rc = dna_lower[::-1]
  return(dna_rc)

print(rev_compl(dna_str))
