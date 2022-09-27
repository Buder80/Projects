#Przemyslaw Budrewicz
#25/09/2022
#Optional task 2
import random


def additional(): #This function draws two numbers between 5-20
    # and adds them together and compares them with the user's result
    num1 = random.randint(5, 20)
    num2 = random.randint(5, 20)
    print("We draw two numbers for you from 5 - 20: ", num1, "and", num2)
    correct_sum = num1 + num2
    print("Please add these two numbers", num1, "with", num2)
    sum = int(input("Enter the result: "))
    print("Your score is:",sum, "correct is:", correct_sum)
    if correct_sum == sum:
        print("Your answer is Correct!!")
    else:
        print("Your answer is Incorrect!! \nThe correct value is:", correct_sum)


def subtraction():#This function draws two numbers between 25-50, 1-25
    # and subtracts them together and compares them with the user's result
    num1 = random.randint(25, 50)
    num2 = random.randint(1, 25)
    print("We draw two numbers for you  first from 5 - 20, and second 1 - 25: ", num1, "and", num2)
    correct_sum = num1 - num2
    print("Please subtract these numbers from each other ", num1, "with", num2)
    sum = int(input("Enter the result: "))
    print("Your score is:", sum, "correct is:", correct_sum)
    if correct_sum == sum:
        print("Your answer is Correct!!")
    else:
        print("Your answer is Incorrect!! \nThe correct value is:", correct_sum)

while True: #this is a loop for selections
    print("*****Welcome to the random numbers*****\n")
    choice = int(input("Would you like to do? \n 1.Addition\n 2.Subtraction\n 3.Exit\n"))

    if choice == 1:
        additional()
    elif choice == 2:
        subtraction()
    elif choice == 3:
        break
    else:
        ("Please enter 1 , 2 or 3")


