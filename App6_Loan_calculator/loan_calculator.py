# Get details of loan
money_owed = float(input('how much money do you owe, in dollars?\n')) #example $50,000
#annual percentage rate value ?
apr = float(input('What is the annual percentage rate of the loan\n')) #example 9%
#How much you will pay each month in dollar?
payment = float(input('How much you will pay each month in dollar?\n')) #Example $1000
#for how many months you want to generate the results for ?
months = int(input('How many months do you want to see the results for?\n')) #example 24 months
monthly_rate = apr/100/12
#At this point, we only calculated the results for one month. So what we need now is to add a for loop that does this for as many months as the user wanted, say 24 months.
for i in range(months):
#calculate interest to pay
    interest_paid = money_owed*monthly_rate
    #add in interest
    money_owed = money_owed + interest_paid
    if (money_owed - payment < 0):
        print('The last layment is', money_owed)
        print('you paid off the loan in', i+1, 'months')
        break
    #make payment
    money_owed = money_owed - payment
    print ('\npaid', payment,'of which', interest_paid, 'was interest', end='')
    print('Now I owe', money_owed, ':)\n')

