#!usr/bin/env python3

#this script opens Python_06.fastq file and reports number of lines, characters and av line length

file = open('Python_06.fastq')

num_lines = 0
total_char = 0
for line in file:
  new_line = line.rstrip()
  num_lines += 1
  total_char += len(new_line)

av_length = round(total_char/num_lines,2)
print('Totatl number of lines is: {}, total number of characters is: {}, average line length is:{}'.format(num_lines,total_char,av_length))
