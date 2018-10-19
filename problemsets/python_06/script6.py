#!sr/bin/env python3
 # This script makes sets of all_genes, proliferation and pigmentation files     and calculates and calculates the differences. Read is a default option for     open
  
trans_f = open('alpaca_transcriptionFactors.tsv')
prolif = open('alpaca_stemcellproliferation_genes.tsv')

count_tf = 0
num_lines_tf = 0
tf_set = set()
for line in trans_f:
  if count_tf == 0:
    line.rstrip()
    count_tf += 1
  else:
    tf_set.add(line.rstrip())
    num_lines_tf += 1

count_prol = 0
num_lines_prol = 0
prol_genes_set = set()
for line in prolif:
  if count_prol == 0:
    line.rstrip()
    count_prol += 1
  else:
    prol_genes_set.add(line.rstrip())
    num_lines_prol += 1

#print(num_lines_all, num_lines_prol, num_lines_pigm)

prol_plus_tf = len(prol_genes_set & tf_set)

print('Number of alpaca genes that are transcription factors for proliferation genes is: {}'.format(prol_plus_tf))
