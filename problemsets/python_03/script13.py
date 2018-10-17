#!usr/bin/env python3

seq = 'GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCa'

sequence = seq.upper()
#complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}

As = sequence.replace('A','t')
Gs = As.replace('G','c')
Cs = Gs.replace('C','g')
Ts = Cs.replace('T','a')

complement = Ts.upper()

rev_complement = complement[::-1]
print('Original Sequence 5\'{} 3\'\nComplement 5\'{} 3\'\nReverse Complement 5\'{} 3\''.format(sequence, complement, rev_complement))
