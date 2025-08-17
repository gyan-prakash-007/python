#python slot machine
import random

def spin_row():
    symbols = ['🍬','🍒','🍓','🍌', '🍑']

    results=[]
    for symbol in range(3):
        results.append(random.choice(symbols))
    return results

def print_row(row):
   print("*************")
   print(" | ".join(row))
   print("*************")


def get_payout(row , bet):
    if row[0] == row[1] == row[2]:
        if row[0] == "🍒":
            return bet*3
        elif row[0] == "🍬" :
            return bet*2
        elif row[0] == "🍓" :
            return bet*4
        elif row[0] == "🍌":
            return bet * 5
        elif row[0] == "🍑":
            return bet * 6

    return 0

def main():
    balance = 100

    print("******************************")
    print("welcome to python slot machine")
    print("symbols:🍬 🍒 🍓 🍌 🍑 ")
    print("******************************")

    while balance > 0:
        print(f" current balance: ${balance}")


        bet = input("place your bet amount: ")

        if not bet.isdigit():
            print("please enter a valid amount")
            continue

        bet = int(bet)

        if bet>balance:
            print("Insufficient balance")

        if bet<=0:
            print("Bet must be greater than 0")
            continue


        balance -= bet

        row = spin_row()
        print("spinning.....\n")
        print_row(row)

        payout = get_payout(row, bet)

        if payout>0:
            print(f"you won${payout}")
        else:
            print(f"you lost this round")

        balance += payout

        play_again = input("Do you want to continue?(Y/N)").upper()

        if play_again != 'Y':
            break

    print("*******************************************")
    print(f"Game over your final balance is ${balance}")
    print("*******************************************")

if __name__ == '__main__':
    main()
