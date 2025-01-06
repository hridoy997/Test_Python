# Variable naming
# Variable names are case-sensitive
# Variable names must start with a letter or an underscore
# Variable names cannot start with a number
# Variable names can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names cannot contain spaces
# Variable names should be descriptive of what the variable represents
# Variable names should be in lowercase with underscores separating words
# Variable names should not be the same as Python keywords
# Variable names should not be the same as built-in functions or classes in Python
# Variable names should not be the same as built-in modules


# Variable assignment
name = "John"
age = 25
print(name)
print(age)

# Oparater precedence
# Operator precedence determines the order of operations in expressions.
# This affects how an expression is evaluated.
# For example, multiplication has a higher precedence than addition.
# Thus, the expression 1 + 2 x 3 is evaluated as 1 + (2 x 3) = 7, and not as (1 + 2) x 3 = 9.

# Operator precedence in Python
# ** Exponentiation
# ~ + - Complement, unary plus and minus (method names for the last two are +@ and -@)
# * / % // Multiply, divide, modulo and floor division
# + - Addition and subtraction
# >> << Right and left bitwise shift
# & Bitwise 'AND'
# ^ | Bitwise exclusive `OR' and regular `OR'
# <= < > >= Comparison operators
# <> == != Equality operators
# = %= /= //= -= += *= **= Assignment operators
# is is not Identity operators
# in not in Membership operators
# not or and Logical operators



# Assigning a value to a variable
a = 10
b = 20
c = a + b
print(c)

name = "John"
print(name)
age = 25
print(age)

# adding two numbers
a = 10
b = 20
c = a + b
print(c)

# adding two strings
name = "John"
surname = "Doe"
full_name = name + " " + surname
print(full_name)

#subtraction of two numbers
a = 10
b = 20
c = a - b
print(c)

# division of two numbers
a = 10
b = 20
c = a / b
print(c)

# floor division of two numbers
a = 10
b = 20
c = a // b
print(c)


# multiplication of two numbers
a = 10
b = 20
c = a * b
print(c)

# Global variables
# Variables that are created outside of a function are known as global variables.
# Global variables can be used by everyone, both inside of functions and outside.


def my_function():
    print("Inside function")
    print(name)
    print(age)


my_function()
print("Outside function")
print(name)
print(age)

# Local variables
# Variables that are created inside a function are known as local variables.
# Local variables can only be used inside the function where they are created.
# Local variables are created when the function has started execution and is destroyed once the function has completed execution.



# Multiple variables can be assigned with the same value
x = y = z = 10
print(x)
print(y)
print(z)

# Multiple variables can be assigned with different values
name, age = "John", 25
print(name)
print(age)

# Constants
# Constants are usually defined on a module level and written in all capital letters with underscores separating words.
# Constants are put into Python modules and meant not be changed.
PI = 3.14
GRAVITY = 9.8
print(PI)
print(GRAVITY)

# Assigning multiple values to multiple variables
a, b, c = 5, 3.2, "Hello"
print(a)
print(b)
print(c)
