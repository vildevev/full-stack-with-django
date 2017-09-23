# Dictionaries
# does not retain any sort of order
my_stuff = {"key1": "value1", "key2": "value2"}
print(my_stuff['key2']) # grab keys 
# reassignment and appending same as in ruby/js
my_stuff['key1'] = 'boho'

# Booleans 
	true or false 

# Tuples 
t = (1,2,3)
print(t[0])
# like a list, but immutable

# Sets 
# unorderered collections on unique elements 
x = set()
x.add(1)
x.add(1) # no error, but it won't be added 

print(x)

converted = set([1,2,3,4]) # shortcut for getting all the unique elements