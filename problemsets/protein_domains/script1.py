#!usr/bin/env python3

#this script calculates the score of alingment for two sequences(a,b)

a =input('Please provide sequence a:')
b = input ('Please provide sequence b:')

rc = input('Please specify if \'reverse_complement_both\', \'reverse_complement_a\', \'reverse_complement_b\' or \'not\':')

if len(a) != len(b):
  print('Please provide sequences of the same size')

def rc_seq(seq):
     seq_upper = seq.upper()
     seq_upper = seq_upper.replace('A', 't')
     seq_upper = seq_upper.replace('G', 'c')
     seq_upper = seq_upper.replace('C', 'g')
     seq_upper = seq_upper.replace('T', 'a')
     reverse_comp = seq_upper[::-1]
     return reverse_comp.upper()

sequences = []
 
if rc == 'reverse_complement_both':
  a_rc = rc_seq(a)
  b_rc = rc_seq(b)
  sequences.append(a_rc)
  sequences.append(b_rc)
elif rc == 'reverse_complement_a':
  a_rc = rc_seq(a)
  sequences.append(a_rc)
  sequences.append(b)
elif rc == 'reverse_complement_b':
  b_rc = rc_seq(b)
  sequences.append(a)
  sequences.append(b_rc)
elif rc == 'not':
  sequences.append(a)
  sequences.append(b)

score = 0
match = 2
mismatch = -2

for i in range(0,len(sequences[0])):
  if sequences[0][i] == sequences[1][i]:
    score += match
  else:
    score += mismatch
print ('The score for sequence a and b is:{}'.format(score))
#alternatively before i in range, yu can make an external loop for sequence in sequences:

