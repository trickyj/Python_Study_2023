# Exponentiation
# Exponentiation is the raising of one number to the power of another.
# This operation is performed using two asterisks **.
# Let's use exponentiation to solve a known problem.
# You are offered a choice of either $1.000.000 or $0.01 (one penny) doubled every day for 30 days (the resulting amount is doubled every day).
# Task:
# Write a program to calculate the amount that will result from the doubling to understand which choice results in a larger amount.
# Hint:
# Let's see how exponentiation can be useful to perform the calculation.
# For example, if we want to calculate how much money we will have on the 5th day, we can use this expression: 0.01*(2**5) = 0.32 dollars (multiply the penny by 2 raised to the power of 5).Problem


# your code goes here

choice1 = 10_000_000
choice2 = 0.01*(2**30)

# compare the numbers.

if choice1 > choice2:
    print("The bigger amount is: ", choice1)
elif choice2 > choice1:
    print("The bigger amoutnt is: ", choice2)
else:
    print("Both amount are equal.")
