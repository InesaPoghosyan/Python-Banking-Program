# Python Banking Program

def show_balance(balance):
    print(f'Balance is {balance:.2f}$')

def deposit():
    amount = float(input('Enter amount to deposit: '))

    if amount <= 0:
        print('Amount must be positive')
        return  0
    else:
        return  amount

def withdraw(balance):
    amount = float(input('Enter amount to withdraw: '))

    if amount <= 0:
        print('Amount must be positive')
        return 0
    elif amount > balance:
        print('Insufficient funds')
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True

    while is_running:
        print("Welcome to Bank Program")
        print("Please choose an option:")
        print("1. Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            show_balance(balance)
        elif choice == '2':
            balance += deposit()
        elif choice == '3':
            balance -= withdraw(balance)
        elif choice == '0':
            is_running = False
        else:
            print("Invalid choice")

if __name__ == '__main__':
    main()
