#!usr/bin/env python3

string1 = 'sapiens, erectus, neanderthalensis'
print(string1)
list1 = string1.split(', ')
print(list1)
print(sorted(list1))
print(sorted(list1, key=len)) 
 
