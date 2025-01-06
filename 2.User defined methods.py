#User defined methods
    # What is a method?
    # How to define a user-defined method?
    # How to call a method?
    # What does a method return?

print('Arman Hossain Hridoy') 

def greeting():
    print('Hi there!')
greeting()

# greeting method 
def greeting(name):
    print('Hi there! ' + name)
    # by default 'None'

greeting("Bobita")
greeting("Razzak")

def my_sum(x, y):
    return x + y

result = my_sum(5, 10)
print(result)

print(greeting('Ronny'))
# null or None  is returned when a method does not return anything  explicitly


def add(a, b):    # method definition
    return a + b

def subtract(a, b):    # method definition
    return a - b

def multiply(a, b):    # method definition
    return a * b

def divide(a, b):    # method definition
    return a / b

print(add(10, 20))    # method call
print(subtract(10, 20))    # method call
print(multiply(10, 20))    # method call
print(divide(10, 20))    # method call

