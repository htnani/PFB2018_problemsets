#!usr/bin/env

#this script opens, reads and uppercases a file python_06.txt

file = open('Python_06.txt')

for line in file:
  line = line.rstrip()
  line_up = line.upper()
  print(line_up)
