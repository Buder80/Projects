
party_members_count = int(input("How many people do you want to join? "))

print("Will be ", party_members_count, "persons")


party_members_names = []


def names():  # this function writes to a list
    name = input("Enter party member name: ")
    party_members_names.append(name)


    print(f"{name} added to party list.")


def get_names_of_guests(members_count):
    if members_count >= 10:
        print("Too many people.")

        return
    else:
        for i in range(0, members_count):
            names()


get_names_of_guests(party_members_count)