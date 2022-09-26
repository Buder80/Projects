#Przemyslaw Budrewicz
#25/09/2022
#Ten colours

colour_list = ["white", "black", "blue", "green", "yellow", "red", "pink", "purple", "brown", "fiolet"]

i = 0
print("You have 5 attempts to choose different colors,"
      "\nthe 1st time you choose from 0 - 4,"
      "\nand the second time from 5 - 9."
      "\nThe program will show you a list of colors that you have chosen from the list.")
print()

while i < 6:
    num1 = int(input("Select numbers from 0 to 4: "))
    if num1 > 4:
        print("Choice if from 0 to 4!!")
        num1 = int(input("Select numbers from 0 to 4: "))
    num2 = int(input("Select numbers from 5 to 9: "))
    if num2 < 5 or num2 > 9:
        print("Choice number from 5 to 9!!")
        num2 = int(input("Select numbers from 5 to 9: "))
    print(colour_list[num1: num2])
    i = i +1

