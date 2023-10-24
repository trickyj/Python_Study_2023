from datetime import date
sum = 1 + 2
print(sum)

# variables example. (To Get anywhere with coding, you need to undertstand that you're operating on data. As your program is working on data, you might need to remember a certain value throughout the program's execution. For that, you use variables.)
sum = 1 + 2
product = sum * 2
print(product)

# data types
# numeric type - int, float, complex, no = 3
# Text type - str = "a literal string"
# Boolean type " contune = true "
# int, pluto used to be the 9th planet, but its too small.

planet_in_solar_system = 8
distance_to_alpha_centauri = 4.367  # float, lightyears.
can_liftoff = True  # boolean
Shuttl_landed_on_the_moon = "Chandrayan 2"  # string

print(type(distance_to_alpha_centauri))
print(type(planet_in_solar_system))
print(type(can_liftoff))
print(type(Shuttl_landed_on_the_moon))

# operators (Operators let you perform various operations on variables and their values.
# The General Idea is that you have a left side and a right side and an operator in the middle.)

# <left side> <operator> <right side>

# example of a code :

left_side = 10
right_side = 5
operator = left_side / right_side
print(operator)

# Python uses two types of operators: arithmetic and assignment.
# Arithmetic Operators: +, -, /, * (Addition, Subtraction, Division, Multiplication.)
# Assignment Operators: =, +=, -=, /=, *=
# (x=2 means x now contains2),
# (x +=2 means x incremented by 2. If it contained 2 before, it now has a value of 4),
# (x -= 2 means x decremented by 2. If it contained 2 before, it now has value of 0),
# (x /= 2 means x divided by 2. If it contained 2 before, it now has a value of 1),
# (x *=2 means x multiplied by 2. If it contained 2 before, it now has a value of 4).

# Dates: When you're building programs, you're likely to interact with dates. A date in a program usually means both the calendar date and the time.

# you can use a date in various applications, like these examples:

# 1 Backup file: Using a date as part of a backup file's name is a good way to indicate whe a backup was made and when it needs to be made again.

# 2 Condition: you might want to carry a specific logic when there's a creation date.

# 3 Metric: Dates are used to check performance on code to (For example) mesure the time it takes to execute a function.

# example program : First we need to import the date module.


# You can then call the functions that you want to work with. To get today's date, you can call the today() function:
Todaysdate = date.today()

print(Todaysdate)

# Data type conversion

# you want to use a date with something, usually a string. If you, for example , want to show today's date on the console, you might run into a problem:

# print("Todays's date is: " + Todaysdate) #The will throw error. We need to convert the date into a string.

print("Today's date is: " + str(Todaysdate))
