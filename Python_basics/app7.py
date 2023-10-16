# Lists Day 4

# A list is an order collection of Items.

todo_list = ['Learn Python List', 'How to Manage List Elements']
print(todo_list[-1])
todo_list[1] = 'Hello Python'
print(todo_list)


# Split() method in string splits a string into a list.

myline = "Hello, my name is tom, I am from japan"
x = str(myline.split(","))
print('\n', x)

# basic operations
print("\nBelow example shows what is the lenth of the list using len: ")
list1 = ['Learn Python List', 'How to Manage List Elements']
print(list1)
print('\n The above list leng is: ', len(list1))

# Concatenation

print("\n Lets check list concatination example")

# Method 1 to combile a list.
a = [1, 2, 3]
b = [3, 2, 1]
c = a + b
print("\nThis is my list 1: ", a, "This is my List 2", b)
print("\nNow I joined it using concatenation: ", c)


# Repetation

print("\nLets see example of Repetation example: ")
l1 = ['Welcome to Python', 'Thank you']
result = l1*4
print('\n this is my current list: ', l1)
print('\n this is what it looks when I do repetation x 4: ', result)

# Membership

result = 3 in [1, 2, 3]

print(result)

# iteration Example

for x in [1, 2, 3]:
    print(x)

# Validate
# print("\n Lets see if xyz item is available in my list: ")
# mylist1 = [1, 2, 3, 4]
# userdata = input("\nEnter number to guess: ")
# print("\nYou enterered: ", userdata)
# if int(userdata) in mylist1:
#     print("\nYes, its true available in list")
# else:
#     print("\nno its not there in the list")

# some build in function for tuples

# Tuples are very similar to list,s except that they are immutable(they cannot be changed). Also, they are created using parentheses, rather then square brackets.

li1 = (1, 2, 3)
li2 = (3, 2, 1)

print(li1, li2)


# Exercise 4

print("\n Lets check list concatination example")

# Question 1 : 2 ways to combile the list.

# Method 1 to combine a list.
a = [1, 2, 3]
b = [3, 2, 1]
c = a + b
print("\nThis is my list 1: ", a, "This is my List 2", b)
print("\nNow I joined it using concatenation: ", c)

# Method 2 to combine the list. using the extend built in method.

a = [1, 2, 3]
b = [3, 2, 1]
a.extend(b)
print("combined using extend method: ", a)

# Question 2 : Convert the list good morning sir to good morning.

a = ['good', 'morning', 'sir']

print(a[:2])

# question 3 : create below matrix in list: 3x3 matrix below.
# 1 2 3
# 4 5 6
# 7 8 9

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# convert the matrix into the list.
matrix_list = [matrix]
# display the resulting list of lists.
for row in matrix_list:
    print(row)

# Question 4 : write a code to print the below list in the reversed format.

list = ['a', 'b', 'c', 'd', 'e', 'f', 'g']

list.reverse()

print(list)

# for item in list:
#     print(item)

# Question 5: write a code to remote all occurance of 5 from the below list:

list = [1, 3, 5, 6, 6, 5, 5, 8, 2, 3, 4, 5, 6, 3, 5]

while 5 in list:
    list.remove(5)

print(list)
