print("Hello")
print('Hello')

# slicing strings

b = "Hello, World!"
print(b[2:5])

b = "Hello, World!"
print(b[:5])


# modify string
# upper case
a = "Hello, World!"
print(a.upper())

# lower case
a = "Hello, World!"
print(a.lower())

# remove whitespace
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# String Concatenation
a = "Hello"
b = "World"
c = a + " " + b
print(c)


# String Format
# f strings
age = 36
txt = f"My name is John, I am {age}"
print(txt)

# place holders
price = 59
txt = f"The price is {price} dollars"
print(txt)


# escape characters
txt = "We are the so-called \"Vikings\" from the north."

# string methods
