#!usr/bin/env python3

file_dict = {'ht':'gatagaca', 'hu':'gagatacacg'}


for seq_id in file_dict:
  A = file_dict[seq_id].count('A')
  G = file_dict[seq_id].count('G')
  C = file_dict[seq_id].count('C')
  T = file_dict[seq_id].count('T')   
  print(A, G) 
 
