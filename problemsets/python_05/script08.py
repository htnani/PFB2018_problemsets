#!usr/bin/env python3

fav_things = {}

fav_things['music'] = 'dancehall'
fav_things['food'] = 'pizza'
fav_things['movie'] = 'chocolate'

print(fav_things)
fav_thing = input('My favourite:')
fav_things[fav_thing] = input('is:')
print(fav_things)

