# Introduction to Python List

# Few operations on List:
#  * List Creation
#  * List Access
#  * List Update
#  * List Delete
#  * List Slicing
#  * List Length
#  * List Concatenation
#  * List Repetition
#  * List Membership Test
#  * List Iteration
#  * List Comprehension

# List Creation
a_list = ['Bobita', 'Razzak', 'Joshim', 1, 5.6, True]
print(a_list)
print(len(a_list))
print(a_list[0]) # item starts at index 0
print(a_list[1])

print(a_list[-1])   # Negative indexing
print(a_list[-2])

# List Update
a_list[0] = 'Bobita Khan'
print(a_list)

# List Slicing
print(a_list[0:3]) # slicing from 0 to 3
print(a_list[2:]) # slicing from 2 to end

# List Length
print(len(a_list))

# List Delete
# del a_list[0]
# print(a_list)

# List Concatenation
b_list = ['Shabana', 'Jasim']
print(a_list + b_list)

# List Repetition
print(a_list * 2)

# List Membership Test
print('Bobita' in a_list)
print('Bobita' not in a_list)

# List Iteration
for item in a_list:
    print(item)

# List Comprehension
squares = [i * i for i in range(10)]
print(squares)

# List Comprehension with condition
even_squares = [i * i for i in range(10) if i % 2 == 0]
print(even_squares)

# List Comprehension with condition
odd_squares = [i * i for i in range(10) if i % 2 != 0]
print(odd_squares)
