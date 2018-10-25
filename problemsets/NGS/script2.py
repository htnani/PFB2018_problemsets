#!usr/bin/env python3

#this script parse FASTQ file into the list of reads and qualities and trims

import sys
  
trimmed_bases = sys.argv[2]
tr_fastq = open('trimmed.fastq','w')
     
try:
  file = sys.argv[1]
  fastq = open(file)
  print("User provided file:" , file)
  count = 0 
  qualities_30 = 0
  qualities_total = 0
  for line in fastq:
    if count == 0:
       tr_fastq.write(line)
       count += 1
    elif count == 1:
       line_tr = line[int(trimmed_bases):len(line)]
       tr_fastq.write(line_tr)
       count += 1
    elif count == 2:
       tr_fastq.write(line)
       count += 1
    elif count == 3:
       line_tr = line.rstrip()
       line_tr = line[int(trimmed_bases):len(line)]
       qualities_total += len(line_tr) 
       tr_fastq.write(line_tr)
       for i in line_tr:
         qual = ord(i) - 33
         if qual > 30:
           qualities_30 += 1
       count = 0
except IndexError:
  print('Please provide a file name')

print('Total qualities:{}, qualities over 30:{}, nucleotides > 30 phred33:{}%.'.format(qualities_total, qualities_30, round((qualities_30/qualities_total)*100,2)))
  
tr_fastq.close()
     
       




''' line.rstrip()
      read = line.rstrip()
      dict_fastq += read
      line.rstrip()
      dict_fastq[read] += line.rstrip() 
file_dict[seq_id]['A'] += line.count('A')
      file_dict[seq_id]['G'] += line.count('G')
      file_dict[seq_id]['C'] += line.count('C')
      file_dict[seq_id]['T'] += line.count('T')
except IndexError:
  print("Please provide a file name")
'''

