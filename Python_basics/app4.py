import math
# boolean example

# example 1
print(10 > 9)

# example 2
a = 20
b = 33
if b > a:
    print("B is grater than a")
else:
    print("b is not grater than a")

# example 3 this below example will print what type of value it is. Is it int or string.

rate = '100'  # string
print(type(int(rate)))  # <class 'int'>

print(type(rate))  # <class 'str'>

print(type(10 > 9))  # <class 'bool'>

print(type(10/3))  # <class 'float'>

# Exercise Python Day 2

# question 1 - Create a variable of type float and assign the value of Mathematical pi to it.

mypi = math.pi
print(mypi)
print(type(mypi))

# Question 2 - Write a python code to get the value of Squareroot of 6^3  using mathematical functions.

mynumbers = math.pow(6, 3)
squrt = math.sqrt(mynumbers)
print(squrt)

# or we can directly do this operation.

result = math.sqrt(6 ** 3)
print(result)

# Question 3 - Convert the variable num in below code to integer type and print the type num = 88.4

number = int(88.4)
print(number)
print(type(number))
