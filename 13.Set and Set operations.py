# Set and Set operations


# Empty set
mySet = set()
print(mySet)

# Are sets unordered?
setA = {1, 2, 3, 4, 5}
setB = {2, 1, 4, 3, 5}
print(setA == setB)

# Immutable objects? Can tuples be in the set? What about Lists?
setC = {(1, 3), (2, 4)}
print(setC)

##setLists = {[1, 2], [3, 4]}
##print(setLists)

# 0 is False and 1 is True in Python, really?
set_zero = set()
set_zero.add(0)
print(set_zero)
set_zero.add(False)
print(set_zero)
set_zero.add(True)
print(set_zero)
set_zero.add(1)
print(set_zero)


# Set operations using symbols
set_one = {1, 2, 3, 4, 5}
set_two = {3, 4, 5, 6, 7}
set_three = {3, 4, 5}
print(set_one | set_two) # Union
print(set_one & set_two) # Intersection
print(set_one - set_two) # Difference
print(set_one <= set_two) # subset
print(set_one >= set_two) # superset
print(set_three <= set_two) # subset

print(set_one ^ set_two) # mutual exclusion

#Set operations using functions
print(set_one.union(set_two)) # union
print(set_one.intersection(set_two)) # interection
# I leave rest for you to try


# converting a list into a set
# membership using the 'in' keyword
# len function to find the size

my_list = [1, 2, 3, 1, 2, 3, 4, 5]
mySet = set(my_list)
print(mySet)

print(2 in mySet)
print(len(mySet))