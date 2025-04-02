balance = 1000000

while True:
    print(" Welcome ")
    print("1. Check balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is: ", balance)
    elif choice == 2:
        amount = int(input("Enter the amount you want to deposit: "))
        if amount > 0:
            balance = balance + amount 
            print("Your new balance is: ", balance)
        else:
            print("Invalid amount. Try again")
    elif choice == 3:
        amount = int(input("Enter the amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance = balance - amount
            print("Your new balance is: ", balance )
        elif amount <= 0:
            print("Invalid amount")
    else:
        break