# variable names
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# assign multiple values
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

# One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

# Unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# ouput variables
x = "Python is awesome"
print(x)

# global variables
x = "awesome"

def myfunc():
  print("Python is " + x)

myfunc()

# The global Keyword

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)