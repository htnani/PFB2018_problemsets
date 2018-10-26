#!usr/bin/env

# this script creates a DNA sequence class with its seq name and organism, plus seq length ,method

class dna_seq(object):
  def __init__(self, sequence, seq_name, seq_organism):
    self.sequence = sequence
    self.seq_name = seq_name
    self.seq_organism = seq_organism

  def seq_len(self):
    sequence_len = len(self.sequence)
    return sequence_len

dna_seq_obj1 = dna_seq('GTTAGAGACCAATGAGA', 'ABC', 'Homo sapiens')
dna_seq_obj2 = dna_seq('GAGATTACCAGATCCCA', 'DEF', 'Homo sapiens')

for d in [dna_seq_obj1, dna_seq_obj2]:
  print('name:', d.seq_name, '\t', 'seq:', d.sequence, '\t', 'length:', int(d.seq_len()), '\t', 'organism:', d.seq_organism)

