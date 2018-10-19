#!sr/bin/env python3

# This script makes sets of all_genes, proliferation and pigmentation files and calculates and calculates the differences. Read is a default option for open

all_genes = open('alpaca_all_genes.tsv')
prolif = open('alpaca_stemcellproliferation_genes.tsv')
pigm = open('alpaca_pigmentation_genes.tsv')

count_all = 0
num_lines_all = 0
all_genes_set = set()
for line in all_genes:
  if count_all == 0:
    line.rstrip()
    count_all += 1
  else:
    all_genes_set.add(line.rstrip())
    num_lines_all += 1    

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

count_pigm = 0
num_lines_pigm = 0
pigm_genes_set = set()
for line in pigm:
  if count_pigm == 0:
    line.rstrip()
    count_pigm += 1
  else:
    pigm_genes_set.add(line.rstrip())
    num_lines_pigm += 1 

#print(num_lines_all, num_lines_prol, num_lines_pigm)   

not_prol_genes = len(all_genes_set - prol_genes_set)
prol_and_pigm_genes = len(prol_genes_set & pigm_genes_set)

print('Number of alpaca genes which are not cel proliferation genes is: {}.\nNumber of both stem cell proliferation gens and pigment genes is:{}.'.format(not_prol_genes, prol_and_pigm_genes))
