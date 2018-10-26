#!usr/bin/env python3

# this script calculates the number of reads per one gene froma .sam file

import sys
import re

filename = sys.argv[1]
file_sam = open(filename, 'r')

gene_dict = {}
for line in file_sam:
   line_list = (line.split('\t'))
   transcript_name = line_list[2]
   gene = re.search(r'(.+)\^(.+)', transcript_name)
   gene_name = gene.group(1)
   if gene_name in gene_dict:
     gene_dict[gene_name].add(line_list[0])
   else:
     gene_dict[gene_name] = {line_list[0]}
    # either one line like above or two lines below
    # gene_dict[gene_name] = set()
    # gene_dict[gene_name].add(line_list[0])

sorted_gene_dict = sorted(gene_dict.keys(), key = lambda x: len(gene_dict[x]), reverse=True) 
for gene_name in sorted_gene_dict:
  print(gene_name,'\t', len(gene_dict[gene_name]))
   
