# List Comprehension

# power operator: **
# list comprehension

numbers = [1, 2, 3, 4, 5]
squares = []

# for number in numbers:
#     # sq = number ** 2
#     squares.append(number ** 2)

#list comprehension
squares = [i ** 2 for i in numbers]

print(squares)

names = ['bobita', 'razzak', 'shabana', 'joshim']
upper_names = []

# for name in names:
#     upper = name.upper()
#     upper_names.append(upper)

# list comprehension
upper_names = [name.upper() for name in names]
print(upper_names)
upper_names = [name.lower() for name in names]
print(upper_names)
upper_names = [name.title() for name in names]
print(upper_names)


# list comprehension with condition
names_string = "bobita,    Razzzak,Shabana  , joshim"
# using the following functions and list comprehenstion, create a list of names where the names are titleaized and without any extra spaces.
# split(), strip(), title()

names = []
# for name in names_string.split(","):    # split the string by comma
#     names.append(name.strip().title()) # remove extra spaces and titleize the names

names = [name.strip().title() for name in names_string.split(",")]

print(names)