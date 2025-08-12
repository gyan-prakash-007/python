#PYTHON NUMBER GUESSING GAME
import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print('python number guessing game')
print(f"select a number between { lowest_num } and { highest_num } ")

while is_running:
    guess = input("guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if guess < lowest_num or guess > highest_num:
            print(f"your guess is out of range ")
            print(f"please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print(" too low try again")
        elif guess > answer:
            print(" too high try again")
        else:
            print(f"correct! the answer was {answer}")
            print(f"number of guesses :{guesses}")
            is_running = False
    else:
        print("invalid guess")
        print(f"please select a number between { lowest_num } and { highest_num }")
