#Przemyslaw Budrewicz
#25/09/2022
#Age check

num = 0 #loop one try is not nice :)

while num < 5:

    age = int(input("How old You are?"))
    print("You have", age, "years old.")

    if age >= 18:
        print("You can vote.")
    elif age == 17:
        print("You can learn to drive.")
    elif age == 16:
        print("You van buy lottery ticket.")
    elif age < 16:
        print("You can go trick or treating.")
    num = num +1

print("Game Over!")
