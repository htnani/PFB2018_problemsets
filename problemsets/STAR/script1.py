#! usr/bin/env python3i

import re


log = open('Log.out', 'r')
log_final = open('Log.final.out', 'r')


for line in log:
  line = line.rstrip()
  line = line.lstrip()
  if r'--genomeDir' in line:
     genome = re.findall(r'\w+/', line)
     genome_str = genome[6]
     genome_final = (genome_str.rstrip('/'))
     break

unmapped = 0

for line in log_final:
  line = line.rstrip()
  line = line.lstrip()
  if r'Uniquely mapped reads %' in line:
     reads_un = re.findall(r'\d.*%', line)
     read_un_str = reads_un[0]
  elif r'Mismatch rate per base, %' in line:
    mismatch = re.findall(r'\d.*%', line)
    mismatch_str = mismatch[0]
  elif r'% of reads mapped to multiple loci' in line:
    mult_loci = re.findall(r'\d.*%', line)
    mult_loci_str = mult_loci[0]
  elif r'% of reads unmapped: too many mismatches' in line:
    mism1 = re.findall(r'\d.*%', line)
    mism1_str = mism1[0]
    unmapped += float(mism1_str.rstrip('%'))
  elif r'% of reads unmapped: too short' in line:
    mism2 = re.findall(r'\d.*%', line)
    mism2_str = mism2[0]
    mism2_n = mism2_str.rstrip('%')
    unmapped += float(mism2_n)
  elif r'% of reads unmapped: other' in line:
    mism3 = re.findall(r'\d.*%', line)
    mism3_str = mism3[0]
    mism3_n = mism3_str.rstrip('%')
    unmapped += float(mism3_n)
  elif r'Number of splices: GT/AG' in line:
    GT_AG = re.findall(r'\d+', line)
    GT_AG_str = GT_AG[0]
  elif r'Number of splices: GC/AG' in line:
    GC_AG = re.findall(r'\d+', line)
    GC_AG_str = GC_AG[0]
  elif r'Number of splices: AT/AC' in line:
    AT_AC = re.findall(r'\d+', line)
    AT_AC_str = AT_AC[0]
  elif r'Number of splices: Non-canonical' in line:
    non_can = re.findall(r'\d+', line)
    non_can_str = non_can[0]

print('Reference genome\t{}'.format(genome_final))
print('Reads uniquely mapped\t{}'.format(read_un_str))
print('Mismatch rate per base\t{}'.format(mismatch_str))

# notfinished, only 3 first print(GT_AG_str, GC_AG_str, AT_AC_str,non_can_str, read_un_str, mismatch_str, mult_loci_str, unmapped)
    

