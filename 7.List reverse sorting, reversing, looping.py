#List reverse sorting, reversing, looping

#list creation
#sorted() method is use temporary sorting and reverse=True is use temporary reverse
list = [9, 8, 5, 4, 7, 8, 3, 6, 10, 1]
temp_sortedList = sorted(list)
reverseList = sorted(list, reverse=True)
print("Sorted List: ", temp_sortedList)
print("Reverse Sorted List: ", reverseList)
print("Original List: ", list)

# sort() method is use permanent sorting and reverse() method is use permanent reverse
# list.sort()
# list.reverse() or
list.sort(reverse=True)
print("Sorted List: ", list)

#new list creation
list2 = [9, 8, 5, 4, 7, 8, 3, 6, 10, 1]
print("Original List: ", list2)
list2.reverse()
print("Reversed List: ", list2)

movie_stars = ['Bobita', 'Razzak', 'Shabana', 'Joshim']
for name in movie_stars:
    print(f"{name} is a movie star.")

print('This will be printed everytime')