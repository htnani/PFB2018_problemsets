#!usr/bin/env python3

import re 

file = open('Python_07.fasta')

headers = 0

for line in file:
	line = line.rstrip()
	if re.search(r'^>', line):
		for header in re.finditer(r'^(>\S+)\s(.+)$', line):
            		gene_id = header.group(1)
            		desc = header.group(2)  
            		print('Id: {}, seq name: {}'.format(gene_id, desc)) 
#print(headers)

file.close()
