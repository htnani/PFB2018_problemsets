#!usr/bin/env python3

ecoI = 'GAATTC'

dna = 'CATGAATTCCCATGGACAGAATTCAA'

start_position = dna.find(ecoI)
end_position = start_position + len(ecoI) 
print('EcoI startPos:{} endPos:{}'.format(start_position+1, end_position+1))

#not working
#i = 0
#while ecoI in dna:
#  start_position = dna.find(ecoI)
#  end_position = start_position + len(ecoI) 
#  print('EcoI startPos:{} endPos:{}'.format(start_position+1, end_position+1))
#  i = i+1
 

#istart_positions = []
#i = 0
#for i in range(len(dna)):
#  if ecoI in dna:
#    start_positions.append(i)
#    i = i + 1
#print(start_positions)

