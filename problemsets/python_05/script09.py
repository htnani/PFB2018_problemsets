#!usr/bin/env python3

fav_things = {}

fav_things['music'] = 'dancehall'
fav_things['food'] = 'pizza'
fav_things['movie'] = 'chocolate'

print(fav_things)
fav_thing = input('My favourite:')
fav_things[fav_thing] = input('is:')

for category in fav_things:
  fav_spec = fav_things[category]
  print(category, fav_spec)

