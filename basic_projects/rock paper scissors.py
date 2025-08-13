# rock paper scissors

import random

options = ("rock", "paper", "scissors")

running = True

while running:

    computer = random.choice(options)
    player = None

    while player  not in options :
         player = input(" Enter a choice ( Rock , Paper , Scissors): ").lower()


    print(f"player : {player}")
    print(f"computer : {computer}")

    if player == computer :
        print("It's a tie!")
    elif player == "rock"  and computer == "scissors" :
        print("you win!")
    elif player == "scissor"  and computer == "paper" :
        print("you win!")
    elif player == "paper"  and computer == "rock" :
        print("you win!")
    else:
        print("you lose!")

    if not input("Do you want to play again? (y/n): ").lower() == "y":
            running = False

print("Thank you for playing!")
