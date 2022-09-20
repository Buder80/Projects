#Przemyslaw Budrewicz
#15/09/22
#Ticking Boomb!!

from time import sleep

# print(10)
# sleep(1)
# print(9)
# sleep(1)
# print(8)
# sleep(1)
# print(7)
# sleep(1)
# print(6)
# sleep(1)
# print(5)
# sleep(1)
# print(4)
# sleep(1)
# print(3)
# sleep(1)
# print(2)
# sleep(2)
# print(1)
# sleep(2)
# print(0)
# print("KAAAaaBooOOOmmMMM!!!")

#########

for bomb in [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]:
    print(bomb)
    if bomb >=3:
        sleep(1)
    if bomb < 3:
        sleep(2)

print("KAAAaaBooOOOmmMMM!!!")
