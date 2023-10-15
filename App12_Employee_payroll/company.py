# the lowercase employee is the file name and the upper case Employee is the class name.
from employee import Employee


class Company:
    def __init__(self):
        # this emptry list is for storing the employee object for the company.
        self.employees = []
# We want to know the way to add the employee to that list. We create new function below and then append new employees to employee lis properties.

    def add_employee(self, new_employee):
        self.employees.append(new_employee)

    def display_employees(self):
        print('Current Employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('________________________')

    def pay_employees(self):
        print('Paying Employees: ')
        for i in self.employees:
            print('Paycheck for:', i.fname, i.lname)
            print(f'Amount: ${i.calculate_paycheck():,.2f}')
            print('________________________')

# main problem starts from here


def main():
    my_company = Company()
    employee1 = Employee('Sarha', 'player', 50000)
    my_company.add_employee(employee1)
    employee2 = Employee('Jet', 'lee', 150000)
    my_company.add_employee(employee2)
    employee3 = Employee('Anny', 'homes', 250000)
    my_company.add_employee(employee3)
    my_company.display_employees()
    my_company.pay_employees()


main()
