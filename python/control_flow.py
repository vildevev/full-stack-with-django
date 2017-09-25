# logical operators 
# and 
(1 > 2) and (2 > 3)
# or 
(1 > 2) or (2 > 3)

if 1<2: # colon implies that a code block will occur
	print("Booyah") 
	if 2<1:
		print("Wooow") # identation matters
	elif 3 == 3:
		print("Because we have to call 'else if' something different, for fun!")

else: 
	print("Yup")


# Loops

# for loops:
seq = [1,2,3,4,5,6]

# variable name can be whatever 
for item in seq:
	print(item)

d = {"Sam": 1, "Bob":2}
for k in d:
	print(k) # prints out the keys
	print(d[k]) # to get value 


mypairs = [(1,2),(3,4),(5,6)]
# tuple unpacking
for tup1, tup2 in mypairs: 
	print(tup2)
	print(tup1)


# while loops 
i = 1

while i < 5:
	print("Hell yeah")
	i = i + 1


# range function 
# creates a list with the given range
# third, optional argument is step ex. skip every other (2)
list(range(0,5))

for item in range(10):
	print item 


# List comprehension
x = [1,2,3,4]

out = [num**2 fo num in x]
print(out)