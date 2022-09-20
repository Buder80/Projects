x=int(input("How many points get Mark in an Exam form 0-100? "))
y=(x)

if(y>=90):
    print("Mark pass exam Grade: A*")
elif(y>=80):
    print("Mark pass exam for Grade: A")
elif(y>=70):
   print("Mark pass exam for Grade: B")
elif(y>=60):
    print("Mark pass exam for Grade: C")
elif(y>=50):
    print("Mark pass exam for Grade: D")
else:
    print("Mark fail  exam get less then min 60 poit score. Have another go!")
