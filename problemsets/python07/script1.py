#!usr/bin/env python3

#this script find all ocurrences of word nobody in file Python_07_nobody.txt

import re

file = open('Python_07_nobody.txt')

for line in file:
  line = line.rstrip()
  match = re.search(r'Nobody', line)
  print(match)
#finditer (match.start)

#print(new_file)

#occurences = re.findall(r'Nobody', new_file)

#print(occurences)
file.close()
