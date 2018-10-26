#!usr/bin/env

# this script creates a DNA sequence class with its seq name and organism, plus nucleotide composition method, reverse complement

class dna_seq(object):
  def __init__(self, sequence, seq_name, seq_organism):
    self.sequence = sequence
    self.seq_name = seq_name
    self.seq_organism = seq_organism

  def seq_len(self):
    sequence_len = len(self.sequence)
    return sequence_len

  def reverse_compl(self):
    seq_upper = str(self.sequence.upper())
    seq_upper = seq_upper.replace('A', 't')
    seq_upper = seq_upper.replace('G', 'c')
    seq_upper = seq_upper.replace('C', 'g')
    seq_upper = seq_upper.replace('T', 'a')
    reverse_comp = seq_upper[::-1]
    return reverse_comp.upper()

  def nucl_comp(self):
    seq_string = str(self.sequence.upper())
    A = seq_string.count('A')
    G = seq_string.count('G')
    C = seq_string.count('C')
    T = seq_string.count('T')
    comp = 'As:{}, Gs:{}, Cs:{}, Ts:{}'.format(A, G, C, T)
    return comp

dna_seq_obj1 = dna_seq('GTTAGAGACCAATGAGA', 'ABC', 'Homo sapiens')
dna_seq_obj2 = dna_seq('GAGATTACCAGATCCCA', 'DEF', 'Homo sapiens')

for d in [dna_seq_obj1, dna_seq_obj2]:
  print('name:', d.seq_name, '\t', 'seq:', d.sequence, '\t', 'nucleotide composition:', d.nucl_comp(), 'seq_rc:', d.reverse_compl(), '\t' 'length:', int(d.seq_len()), '\t', 'organism:', d.seq_organism)

