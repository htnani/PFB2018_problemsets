#!usr/bin/env

#this script opens, read, uppercases a file python_06.txt and writes it to a file new_python_06.txt

file = open('Python_06.txt', 'r')
new_file = open('new_python_06.txt', 'w')

for line in file:
  line = line.rstrip()
  line_up = line.upper()
  new_file.write(line_up + '\n')

print('File is saved to \'new_python_06.txt')

file.close()
new_file.close()
