balance = 0
history = []


def deposit():

    global balance

    amount = float(input("Enter deposit amount: "))

    balance += amount

    history.append(f"Deposited: {amount}")

    print("Deposit Successful")


def withdraw():

    global balance

    amount = float(input("Enter withdrawal amount: "))

    if amount <= balance:

        balance -= amount

        history.append(f"Withdrawn: {amount}")

        print("Withdrawal Successful")

    else:

        print("Insufficient Balance")


def check_balance():

    print("Current Balance =", balance)


def transaction_history():

    if len(history) == 0:

        print("No Transactions Yet")

    else:

        print("\nTransaction History")

        for transaction in history:
            print(transaction)


while True:

    print("\nBank Menu")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Transaction History")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        deposit()

    elif choice == 2:
        withdraw()

    elif choice == 3:
        check_balance()

    elif choice == 4:
        transaction_history()

    elif choice == 5:
        print("Thank you for using the Bank App")
        break

    else:
        print("Invalid Choice")