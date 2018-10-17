Python 3.7.0 (default, Jun 28 2018, 07:39:16) 
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> fav_things = ['1','2','3','4','5']
>>> print(fav_things)
['1', '2', '3', '4', '5']
>>> fav_things[2]
'3'
>>> fav_things[2]='0'
>>> fav_things[2]='0'
>>> print(fav_things)
['1', '2', '0', '4', '5']
>>> fav_things.append('6')
>>> print(fav_things)
['1', '2', '0', '4', '5', '6']
>>> fav_things.insert(0,'7')
>>> print(fav_things)
['7', '1', '2', '0', '4', '5', '6']
>>> fav_things.pop()
'6'
>>> fav_things.pop(0)
'7'
>>> print(fav_things)
['1', '2', '0', '4', '5']
>>> fav_things.remove(5)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> fav_things.remove('5')
>>> print(fav_things)
['1', '2', '0', '4']
>>> fav_things.pop(4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: pop index out of range
>>> fav_things.pop(3)
'4'
>>> print(fav_things)
['1', '2', '0']
>>> 
