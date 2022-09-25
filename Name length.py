#Przemyslaw Budrewicz
#25/09/2022
#Name length

name = input("Please enter your first name: ")
length = len(name)  #number of characters in the name

if length < 5:
    print("Give me your surname.")
    sur = input("Please enter your surname: ")
    print(name.upper(), sur.upper())
elif length >= 5:
    print(name.lower())
