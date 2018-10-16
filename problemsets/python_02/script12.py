#!/usr/bin/env python3

value = 61

if value > 0:
  print('positive')
  if value < 50:
    print('smaller than 50')
    if value%2 == 0:
      print('it is an even number that is smaller than 50')
  else:
    if value%3 == 0:
      print('bigger than 50 and divisible by 3')
elif value < 0:
  print('negative')
elif value == 0:
  print('0')


