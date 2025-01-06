# range(); list enumeration, slicing; simple statistics

# range() function
# list enumeration
# list slicing

# print 0 - 10 numbers, each in a new line 
# for x in range(11, 1, -1):
  # print(x)

movie_stars = ['Bobita', 'Razzak', 'Shabana', 'Joshim']
print(movie_stars)

# list enumeration: give the index as well as the item
for i, name in enumerate(movie_stars):
  print(f'{i+1}. {name}')

# list slicing
# print the first 3 items
print(movie_stars[:3])
print(movie_stars[2:])
print(movie_stars[:3])
print(movie_stars[:])


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(numbers))
print(max(numbers))
print(sum(numbers))