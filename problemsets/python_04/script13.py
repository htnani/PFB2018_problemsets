#!usr/bin/env

#this script prints position, elements, their lengths

elements = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

count = 0
for element in elements:
  count += 1
  print(count,len(element), '\t', element)
