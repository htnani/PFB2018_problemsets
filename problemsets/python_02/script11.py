#!/usr/bin/env python3

value = 50

if value > 0:
	print('positive')
	if value < 50:
		if value%2 == 0:
			print('it is an even number that is smaller than 50')
		else:
			print('smaller than 50')
elif value < 0:
	print('negative')
elif value == 0:
	print('0')
