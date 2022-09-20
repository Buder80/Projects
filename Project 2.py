#Przemyslaw Budrewicz
#15/09/22
#Password generator
import random
import string
import sys

password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Number of characters outside the range 0,", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Characters left:", characters_left)

password_length = int(input("How long should be the password? "))

if password_length < 5:
    print("Password must be at least 5 characters long, please try again.")
    sys.exit(0)
else:
    characters_left = password_length

lowercase_letters = int(input("How many lowercase letters should the password have?"))
update_characters_left(lowercase_letters)


uppercase_letters = int(input("How many uppercase letters should the password have?"))
update_characters_left(uppercase_letters)


special_characters = int(input("How many special characters the password should have?"))
update_characters_left(special_characters)

digits = int(input("How many digits the password should have?"))
update_characters_left(digits)

if characters_left > 0:
    print("Not all letters have been used, the password will be filled with lowercase.")
    lowercase_letters +=characters_left

print("Password length:", password_length)
print("Uppercase letter:", uppercase_letters)
print("Lowercase letters:", lowercase_letters)
print("Special characters:", special_characters)
print("Didits:", digits)

for _ in range(password_length):
    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1
    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1
    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -=1
    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)
print("Generated password:", "".join(password))

#quick random password generator

#import random
#import string

# password = "".join([random.choice(string.ascii_letters + string.punctuation + string.digits)]) for _ in range(30)])
# print(password)






