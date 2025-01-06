# What is List? - DONE
# How to define a list with items? - Done
# How to access a list item? - DONE
# How to delete a list item?
# Popping a list item
# How to add an item to a list
# list length

a_list = ['Bobita', 'Razzak', 'Joshim', 1, 5.6, True]
print(a_list)
del a_list[-1]
print(a_list)

a_list.remove(5.6)
print(a_list)

a_list.pop()
print(a_list)

a_list.append('Salman Shah')
print(a_list)

a_list[1] = 'Rajjak'
print(a_list)

# how to insert an item to an existing list
a_list.insert(1, 'Omar Sunny')
print(a_list)

print(len(a_list))

