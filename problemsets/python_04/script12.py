#!usr/bin/env

#this script generates list of tuples 

elements = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

#all code below also works, an alternative
#tuples = []
#for element in elements:
 # tuple = (element, len(element))
 # tuples.append(tuple)
#print(tuples)

tuples = [(element, len(element)) for element in elements]
print(tuples)
