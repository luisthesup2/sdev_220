def atm():
    """
    Simulate the behavior of an ATM-machine
    :return: None
    """

    balance = 0.00

    while True:
        print("\nWhat would you like to do?")
        action = int(input("(1 - Check balance), (2 - Deposit), (3 - Withdraw), (4 - Quit) <<== "))
        if action == 1:
            print(f"You have ${balance}")
        elif action == 2:
            deposit = float(input("\nHow much would you like to deposit?: "))
            balance += deposit
            print(f"Your new balance is: ${balance}")
        elif action == 3:
            withdraw = float(input("\nHow much would you like to withdraw?: "))
            balance -= withdraw
            print(f"Your new balance is: ${balance}")
        elif action == 4:
            print("\nHave a great day!")
            quit()
        else:
            print("Invalid action")

atm()