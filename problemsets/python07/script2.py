#!usr/bin/env python3

#this script find all ocurrences of word Nobody in file Python_07_nobody.txt and replaces it with Pepino

import re

file = open('Python_07_nobody.txt')

for line in file:
  line = line.rstrip()
  new_line =  re.sub(r'Nobody', 'Pepino', line)
  print(new_line)

file.close()
