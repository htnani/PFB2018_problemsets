#!usr/bin/env )python3

#this script processes fastq file (arg1) into kmers (length form the command line, arg 2) and displays the top x kmers and their count (arg 3), 1st step of Trinity - inchworm

from Bio import SeqIO
import sys

filename = sys.argv[1]
kmer_length = sys.argv[2]
kmer_length_int = int(kmer_length)
num_top_kmers = sys.argv[3]
kmers = {} 

for seq_record in SeqIO.parse(filename, 'fastq'):
  seq = str(seq_record.seq)
  for i in range(0, len(seq)):
      kmer_end = i + kmer_length_int
      if kmer_end > (len(seq)-1):
        break
      kmer = seq[i:kmer_end]
      if kmer in kmers:
        kmers[kmer] += 1
      else:
        kmers[kmer] = 1

sorted_kmers = sorted(kmers.keys(), key = lambda x: kmers[x], reverse=True)

counter = 0

for kmer in sorted_kmers:
  count = kmers[kmer]
  counter += 1
  print('{}\t{}'.format(kmer, count))
  if counter >= int(num_top_kmers):
    break 
