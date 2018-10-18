#!usr/bin/env python3

fav_things = {}

fav_things['music'] = 'dancehall'
fav_things['food'] = 'pizza'
fav_things['movie'] = 'chocolate'

print(fav_things.keys())
fav_thing = input('Choose the category of favourite objects from the above:')
print(fav_things[fav_thing])

