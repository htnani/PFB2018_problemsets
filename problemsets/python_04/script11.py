#!usr/bin/env

#this script prints elements and their lengths

elements = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for element in elements:
  print(len(element), '\t', element)
