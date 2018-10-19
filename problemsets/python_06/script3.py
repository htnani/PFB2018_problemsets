#!usr/bin/env

#this script opens and print reverse complement from Python_06.seq.txt

file = open('Python_06.seq.txt', 'r')

for line in file:
  line = line.rstrip()
  name, seq = line.split()
  seq_up = seq.upper()
  As = seq_up.replace('A','t')
  Gs = As.replace('G','c')
  Cs = Gs.replace('C','g')
  Ts = Cs.replace('T','a')
  seq_complement = Ts.upper()
  rev_complement = seq_complement[::-1]
  #print('>'+name, 'reverse complement' '\n', seq )
  print('>{}_reverse_complement\n{}'.format(name,seq))
file.close()
