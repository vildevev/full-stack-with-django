# Either single or double quotes 
"hello"
'hello'

my_string = 'abcde'
# Supports negative index location
print(my_string[-1])


# slicing
# to the end of the string, starting at index 2
print(my_string[2:])
# grabs all the elements up to, but not including index 3
print(my_string[:3])
# define start and ending point
print(my_string[2:5])
# grabs all, if '2' instead of '1', will skip every other ex. [::2]
print(my_string[::1])

my_string.upper() # to uppercase, '.lower()' fo lowercase

my_string.split() # allows you to split, returns items in list (array in Ruby)

# string interpolation
"Insert string: {} Insert another string: {}".format("Magic man", "Boyah")
# call also give them variable names. More conventional with this approach.
"Hello {x} {y}".format(x="you", y="creep")