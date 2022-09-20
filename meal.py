

question1= input("What is your favorite meal? ")
print("So your main course will be",question1)

question2=input("What would You like im meantime for starter? ")
print("Great choice",question2, " excellent!!")

question3=input("Would You like any dessert?")
if question3=="yes":
    print("We have banana, ice cream and pudding.")
    question4=input("What is Your choice?")
    print("Your like",question4,"the best choice!!")
    question5=input("What is Your favorite drink?")
    print("So your favorite meal is",question1,"and You like", question5, "Nice I will remember for next time!!")

elif question3=="no":
    print("So maybe something do drink? ")
    question5=input("What is Your favorite drink?")
    print("So your favorite meal is",question1,"and You like", question5, "Nice I will remember for next time!!")
else:
    print("No rush I can wait")


