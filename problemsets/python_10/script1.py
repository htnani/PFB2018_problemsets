#!usr/bin/env

# this script creates a DNA sequence class with its seq name and organism

class dna_seq(object):
  def __init__(self, sequence, seq_name, seq_organism):
    self.sequence = sequence
    self.seq_name = seq_name
    self.seq_organism = seq_organism

dna_seq_obj1 = dna_seq('GTTAGAGACCAATGAGA', 'ABC', 'Homo sapiens')
dna_seq_obj2 = dna_seq('GAGATTACCAGATCCCA', 'DEF', 'Homo sapiens')

for d in [dna_seq_obj1, dna_seq_obj2]:
  print('name:', d.seq_name, '\t', 'seq:', d.sequence, '\t', 'organism:', d.seq_organism)  
