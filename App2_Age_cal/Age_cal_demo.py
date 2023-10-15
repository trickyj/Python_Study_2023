age = int(input("\nhow old you are?\n"))

#Python has a special operator for whole number division or integer division, which is two back slashes. 

decades = age // 10

#we want to get the remainder after the whole number division 
#Python also has an operator for that, which is the % sign. It's also called modulus. 

years = age % 10

print("\nYou are " + str(decades) + 
    " decades and " + str(years) + " years old.\n")
