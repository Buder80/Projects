#Przemyslaw Budrewicz
#25/09/2022
#Fair Diner Bill

def sum(): #function to divide the bill into the number of people
    sum = float(total / persons)
    return sum

total = float(input("I would like the total value of the bill 💷, what is the total amount 💰 ??"))
print("Total amount is: ", total, "£")

persons = int(input("How many poeple ordered? "))
print("We divide the bills fairly into", persons, "persons.")
print("It will be:", sum(), "£ per person.")






