

# def numbers():
#     num1 = int(input("Please enter a number "))
#     num2 = int(input("Please enter a second number "))
#     num3 = int(input("Please enter a third number "))
#     num4 = int(input("Please enter a fourth number "))
#
#     sumnum = num1+num2+num3+num4
#     print("The sum of the numbers you entered is", sumnum)
# numbers()

def calculator():
    global num1
    global num2
    print("*****Welcome to the Calculator*****\n")
    choice = input("Would you like to do? \n 1.Addition\n 2.Subtraction\n")

    if choice == "1":
        additional()
    elif choice == "2":
        subtraction()
    else:
        ("Please enter 1 or 2")

def additional():
    answer = num1+num2
    print("The answer is ", answer)

def subtraction():
    answer = num1-num2
    print("The answer is ", answer)

calculator()

# def UserDetails(fname, Sname):
#     print("Hello", fname,  Sname)
#
# UserDetails("Jenny","Davis")
# UserDetails("Joe","Bloggs")
# UserDetails("Donald","Duck")

# def Multiplier(number):
#     print(number, "times 5 =",number*5)
# Multiplier(2)

# def power(num,power):
#     print(num,"to the power of:", power, "=", num**power)
# power(3,2)

# word = "string"
#
# print(len(word))
# print(word.capitalize())
# print(word.upper())
# print(word.lower())
# print(word.title())
# print("Hello World"[7:10])

# name = input("Please enter your name ")
# length = len(name)
# print(length)

# word = input("Enter a word ")
# word = word.upper()
# print(word)

# rhyme = input("Enter the first line of a nursery rhyme :")
# length = len(rhyme)
# print("this has ", length, "letter in it")
# start = int(input("Enter a starting number :"))
# end = int





