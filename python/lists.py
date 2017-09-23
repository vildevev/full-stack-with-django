# A simple list 
my_list = [1,3, "hello", ["hello", 2]]
# how you get the length of the list
print(len(my_list))

# lists are mutable 
my_list[0] = "Wow, this is AMAAAZING"
# a ton of built-in operations 
my_list.append("Adding this bad boy to the end")
# extend if you want to extend another list with the original list
my_list.extend([1,4])
# removes last element, returns it. Can take an index as argument.  
my_list.pop()
# sorting and reversing are 'destructive methods', meaning they change the original object without needing to reassign

matrix = [[1,2,3],[4,5,6],[7,8,9]]
matrix[0][0]

# List comprehension:
first_col = [row[0] for row in matrix]
print(first_col)