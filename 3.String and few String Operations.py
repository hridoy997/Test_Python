# String and few String Operations


# Introduction to Python String 
# Few operations on String: 
#  * Concatenation
#  * Strip 
#  * Conversion to String

print('Arman Hossain Hridoy') # Single quotes
print("Arman Hossain Hridoy") # Double quotes

# single quotes inside double quotes
print("I'm Arman Hossain Hridoy")
# double quotes inside single quotes
print('my name is "Arman Hossain Hridoy"')

# single and double quotes inside double quotes
print("I'm Arman Hossain Hridoy and my name is \"Arman Hossain Hridoy\"")


first_name = "Arman Hossain"
last_name = "Hridoy"

print(first_name + " " + last_name) # String concatenation

a_long_string = "    This is a long string with lots of ...   "
print(a_long_string) 
print(a_long_string.strip()) # stripping operation
print(a_long_string.lstrip()) # left stripping operation
print(a_long_string.rstrip()) # right stripping operation

age = 25
print("His age is " + str(age)) # conversion to String
