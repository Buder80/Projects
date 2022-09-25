#Przemyslaw Budrewicz
#25/09/2022
#Time for Holiday

def hour():      #function to count the hours of the day
    hours = 24
    #sum = int(hours / 1)
    return hours

def minut():
    """
    The function calculates the number of minutes during the day
    """
    day = 24
    minutes = 60
    sum = int(day * minutes)
    return sum

def second():     #function to count seconds in a day
    day = 24
    minutes = 60
    seconds = 60
    sum = int(day * minutes) * seconds
    return sum

holiday = int(input("How many days to holiday left? "))
print("To holiday left:", holiday, "days.")
print("This will be:",hour() * holiday, "hours.")
print("This will be:",minut() * holiday, "minuts.")
print("This will be:",second() * holiday, "secounds.")
