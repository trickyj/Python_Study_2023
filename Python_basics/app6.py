import math
print(10+5)
print(100 % 2)

# Exercise 1:  - which operator is equivalent to mathematical function math.pow(x,y) ?

# In Python, the math.pow function is used to raise a number to a specific power.

print("2 raised to 4 is " + str(math.pow(2, 4)))

print(2 ** 4)

# Exercise 2: Which of the following 'if' condition is correct ?
x = 0
x = 1
if (x == 0 or x == 1):
    print("yes correct")

# Exercise 3: write an if condition using an operator to check if the below list fruits have "apple" in it.


fruits = ['orange', 'banana', 'watermellon']

if "apple" in fruits:
    print("Yes, apple is there in the list")
else:
    print("No there is no apple in the list: ", fruits)


my_str = "python string"
for index, character in enumerate(my_str):
    print(f"Character '{character}' is at index {index}")


for x in "banana":
    print(x)


a = "hello, python!"
print(len(a))

# Slicing example

b = "hello, python!"
print(b[:8])

b = "hello, python!"
print(b[-5:-2])

# Built in methods for string -
# upper() for upper case, strip(), replace(), split()

a = "hello world"
print(a.upper())

a = "     Hello, Python!"
print(a, "woo i got white splace before")
print(a.strip(), "funny i dont have it now, I strip it")

a = "Hello, Python!"
print(a.replace("H", "P"))

a = "Hello, Python"
print(a.split(","))

# some more exaples below.

a = "Good Morning"
b = "GOOD MORNING"
c = "Hello, 你好"

print("\nLowercase string:" + a.lower())
print("Replac String: " + a.replace("Morning", "Evening"))
print("Splitted string: " + str(a.split(" , ")))
print("Case swapped: " + a.swapcase())
print("First char to upper case: " + a.capitalize())
print("Convert to lover case: " + b.casefold())
print("Returned a centered string: " + b.center(10, '*'))
# count the number of times 'o' appears in the below string "Good Morning"
print("number of times a specified value occurs in a string", + a.count('o'))
# encode a string using specified encoding such as UTF-8. It returns a bytes object, which represents the encoded version of the orignal string.
print(c.encode('utf-8'))
# The bytes object contains the encoded characters in a format suitable for storage or transmission, and it can be decoded back into a string when needed. The encode() method is useful when working with character encodings, such as when dealing with text data in different languages or when interfacing with external systems that require specific encodings.
print(c.join(c))
# Trim the below string using built-in functions in strings.
d = "                       I am feeling very sleepy"
print("strip version: " + d.lstrip())
# Get the names in the below string in the form of list using built-in functions in Strings.
e = "John, Riya, Neha, Tiara, Rahul"
print("Returning in list format: " + str(e.split()))
# Covert the string from "The weather today will be hot." to "Weather will be hot" - Using slicing in the strings.
f = "The weather today will be hot"
print("Converting to Weather will be hot. using slicing: " + f[4:11] + f[17:])
# Count the number of times 'W' appears in the below tongue twister using string functions.
g = "How much wood would a woodchuck chuck if a woodchuck could chuck wood As a woodchuck would if a woodcheck could check wood"
print("W appears", + g.count('w'), "times in the above tongue twister")
