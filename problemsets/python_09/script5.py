#!usr/bin/env

#this script calculates the gc content from an user  input sequence

import sys

dna_seq = input('Insert DNA sequence:')

def gc_content(dna):
  dna = dna.upper()
  G = dna.count('G')
  C = dna.count('C')
  gc_cont = round((G+C)/len(dna),2)
  return gc_cont

print(gc_content(dna_seq))

