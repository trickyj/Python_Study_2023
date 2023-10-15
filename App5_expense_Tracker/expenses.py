expenses = [100, 30, 50, 150, 400, 200, 10, 5]

# we need to add each expense to this variable below. We need for loop for that.
# sum = 0

# #we are creating for loop here.
# for  x in expenses:
#     sum = sum + x

#we can also solve the above forloop using the built in function called sum.

# total = sum(expenses)

# print('\nYou spent', total,'Rupees\n') 

#another example below with Adding input to the expenses calculator.

total = 0
expenses = []
num_expenses = int(input("Enter # of expenses: "))
for i in range(num_expenses):
    expenses.append(float(input("Enter an expenses: ")))

total = sum(expenses)

print("you spent $", total, sep='')
