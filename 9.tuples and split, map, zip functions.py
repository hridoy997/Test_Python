# tuples and split, map, zip functions

# tuple
# split function
# map function
# zip function 

tuple1 = (1, 2, 3)
print(tuple1[2])
print(tuple1[0])

# tuple1[0] = 10

names = "Bobita,Razzak,Joshim"
scores = "96,89,98"

# split function
students_name = names.split(",")
students_scores = scores.split(",")
print(students_name)
print(students_scores)

# map function
students_scores = list(map(int, students_scores))
print(students_scores)

# zip function
students = list(zip(students_name, students_scores))
print(students)

# zip sorted
# Sorewd by name
students_sorted = sorted(students)
# Sorewd by score/Number
students_sorted = sorted(students, key=lambda x: x[1])
print(students_sorted)

student_name = students[-1][0]
print(student_name)

student_score = students[-1][1]
print(student_score)

