 #hang man in python
import random

words = ("apple", "banana", "coconut", "orange","pineapple")

hangman_art = {
        0: """
      +---+
      |   |
          |
          |
          |
          |
    ========
    """,
        1: """
      +---+
      |   |
      O   |
          |
          |
          |
    ========
    """,
        2: """
      +---+
      |   |
      O   |
      |   |
          |
          |
    ========
    """,
        3: """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    ========
    """,
        4: """
      +----+
      |    |
      O    |
     /|\\  |
           |
           |
    ========
    """,
        5: """
      +----+
      |    |
      O    |
     /|\\  |
     /     |
           |
    ========
    """,
        6: """
      +-----+
      |     |
      O     |
     /|\\   |
     / \\   |
            |
    ========
    """
    }


def display_man(wrong_guess):
  print("****************") 
  print(hangman_art[wrong_guess])
  print("****************")


def display_hint(hint):
    print(" ".join(hint))


def display_answer(answer):
    print(" ".join(answer))

def main():
    answer = random.choice(words)
    hint = ["_"]*len(answer)
    wrong_guesses = 0
    guess_letters = set()
    is_running = True


    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("Enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input")
            continue

        if guess in guess_letters:
            print(f"{ guess} is already guessed ")

        guess_letters.add(guess)


        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess

        else :
            wrong_guesses += 1

        if "_" not in hint:
            display_answer(wrong_guesses)
            display_answer(answer)
            print("YOU WIN!!")
            is_running = False

        elif wrong_guesses >= len(hangman_art)-1:
            display_answer(wrong_guesses)
            display_answer(answer)
            print("YOU LOSE!!")
            is_running = False


if __name__ == '__main__':
    main()
