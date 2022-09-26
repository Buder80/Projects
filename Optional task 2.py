#Przemyslaw Budrewicz
#25/09/2022
#Optional task 2
import random

# def random():
def additional():
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print(num1, num2)
    print(num1 + num2)

def subtraction():
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    print(num1, num2)
    print(num1 - num2)

print("*****Welcome to the random numbers*****\n")
choice = int(input("Would you like to do? \n 1.Addition\n 2.Subtraction\n"))
print(choice)
if choice == "1":
    additional()
elif choice == "2":
    subtraction()
else:
    ("Please enter 1 or 2")


# random()