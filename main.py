class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Your new balance is ${self.balance}.")
        else:
            print("Invalid deposit amount. Please enter a positive amount.")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Your new balance is ${self.balance}.")
        elif amount <= 0:
            print("Invalid withdrawal amount. Please enter a positive amount.")
        else:
            print("Insufficient funds for withdrawal.")

def main():
    account = BankAccount()
    
    while True:
        print("\nChoose an action:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        
        choice = input("Enter the number of your choice: ")
        
        if choice == '1':
            amount = float(input("Enter the deposit amount: $"))
            account.deposit(amount)
        elif choice == '2':
            amount = float(input("Enter the withdrawal amount: $"))
            account.withdraw(amount)
        elif choice == '3':
            print("Exiting the program. Thank you!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
