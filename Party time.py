#Przemyslaw Budrewicz
#25/09/2022
#Party Time
party = int(input("How many people do you want to join? "))

print("Will be ", party, "persons")

party_names = []

def names(): #this function writes to a list
    name = input("Enter party member name: ")
    party_names.append(name)
    print("Person added to party list.")
    print(party_names)

for party in range(0,party):
    if party < 10:
         names()

    if party >= 10:
        print("Too many people.")










