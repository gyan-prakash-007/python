# python banking program

def show_balance(balance):
    print(f"Your balance is: ${balance: .2f}")


def deposit():
     amount = float(input("Enter amount to deposit: "))

     if amount < 0:
         print("That's not a valid input")
         return 0
     else:
         return amount


def withdraw(balance):
     amount = float(input("enter amount to withdraw: "))
     if amount > balance:
         print("Insufficient balance")
         return 00
     elif amount < 0:
         print("Amount must be greater than 0")
         return 0
     else:
         return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("************************")
        print("     Banking program")
        print("************************")
        print("1.Show balance")
        print("2.Deposit")
        print("3.Withdraw")
        print("4.Exit")
        print("************************")

        choice = input("Enter your choice:(1-4) ")


        if choice == "1":
            show_balance(balance)

        elif choice == "2":
            balance +=deposit()

        elif choice == "3":
            balance -= withdraw(balance)

        elif choice == "4":
            is_running = False

        else:
            print("Invalid choice")


    print("Thank you ! Have a nice day ")

if __name__ == "__main__":
    main()
