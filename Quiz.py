#Przemyslaw Budrewicz
#16/09/22
#Quiz
import json

points = 0

def show_question(question):
    global points

    print(question["pytanie"])
    print("a", question["a"])
    print("b", question["b"])
    print("c", question["c"])
    print("d", question["d"])
    print()

    answer = input("Ktora odpowiedz wybierzesz? ")

    if answer == question["prawidlowa_odpowiedz"]:
        points += 1
        print("To prawidłowa odpowiedz, brawo! Masz juz",points, "punktow.")
    else:
        print("Niestety to zla odpowiedz, prawidlowa odpowiedz to "+ question["prawidlowa_odpowiedz"]+".")

with open("quiz.json") as json_file:
    questions = json.load(json_file)

    for i in range(0, len(questions)):
        show_question(questions[i])

print()
print("To koniec gry, zdobyta liczba punktow to "+ str(points)+".")
