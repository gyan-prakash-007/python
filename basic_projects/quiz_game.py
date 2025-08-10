#python quiz game

questions = ("How many elements are in the periodic table ? :",
            "Which animal has the largest egg ? : ",
            "what is the most abundant gas in Earth's atmosphere? : ",
            "how many bones are in the human body ? :",
            "which planet in the solar system is hottest ? :")

options = (("A.116","B.117","C.118","D.119"),
          ("A.HUMAN","B.CROCODILE","C.ELEPHANT","D.OSTRICH"),
          ("A.NITROGEN","B.OXYGEN","C.CARBON-DIOXIDE","D.HYDROGEN"),
          ("A.206","B.207","C.208","D.209"),
          ("A.MERCURY","B.VENUS","C.EARTH","D.MARS"))

answers = ("C","D","A","A","B")
guesses = []
score = 0
question_num = 0

for question in questions :
    print("___________________________")
    print(question)
    for option in options[question_num] :
        print(option)

    guess = input("enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1


print("___________________________")
print("RESULT")
print("___________________________")

print("answers: ", end=" ")
for answer in answers :
    print(answer,end=" ")
print()

print("guesses", end=" ")
for guess in guesses :
    print(guess,end=" ")
print()

score =  int(score/len(guesses)*100)
print(f"Your score is : {score}%")
