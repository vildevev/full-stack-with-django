# colon implies that the function is 'starting'
def my_function(param1='default'):
	"""
	Whatever is in this 'docstring' will appear when typing the function name
	"""
	print("a function bro")


# n 'end' keyword. Whatever falls inside of the indentation is part of the function
my_function()


# Lambda Expression (anonymous function)

# Filter 
mylist = [1,2,3,4,5,6,7,8]

# finds all even numbers
filter(lambda num:num%2 == 0, mylist)

# returns a boolean
print(4 in mylist)


# Given a list of integers, return True if the sequence of numbers 1,2,3 appears in the list somewhere.

def arrayCheck(nums):
	