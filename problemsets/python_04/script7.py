#!usr/bin/env python3

num = [101,2,15,22,95,33,2,27,72,15,52]
num_sorted = sorted(num)
even = 0
odd = 0

for num in num_sorted:
  if num%2 == 0:
    even+= num
  else:
    odd+= num
print('Sum of even numbers: {}\nSum of odds: {}'.format(even, odd))
	
  
