#!usr/bin/env python3

numbers = [101,2,15,22,95,33,2,27,72,15,52]
even_num = []
for num in numbers:
  if num%2 == 0:
    even_num.append(num)
print(even_num)
