# A Simple banking application:
balance = 0
kyc_documents = {}

def check_balance():
    print("Your current balance is: $", balance)

def deposit(amount):
    global balance
    if amount <= 0:
        print("Deposit amount must be positive.")
        return
    balance += amount
    print("Your current balance is: $", balance)

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient funds. Your current balance is: $", balance)
    elif amount <= 0:
        print("Withdrawal amount must be positive.")
    else:
        balance -= amount
    print("Your current balance is: $", balance)

def update_kyc(**documents):
    global kyc_documents
    kyc_documents.update(documents)
    print("KYC documents updated:", kyc_documents)

def check_kyc():
    required_docs = ['ID Proof', 'Address Proof']
    for doc in required_docs:
        if doc not in kyc_documents:
            print(f"KYC incomplete. Missing: {doc}")
            return False
    print("KYC is complete.")
    return True

while True:
    print("\nWelcome to the Simple Banking Application")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check KYC")
    print("5. Update KYC")
    print("6. Exit")

    choice = input("Please select an option (1-6): ")

    if choice == '1':
        check_balance()
    elif choice == '2':
        amount = float(input("Enter amount to deposit: "))
        deposit(amount)
    elif choice == '3':
        amount = float(input("Enter amount to withdraw: "))
        withdraw(amount)
    elif choice == '4':
        check_kyc()
    elif choice == '5':
        id_proof = input("Enter ID Proof document name: ")
        address_proof = input("Enter Address Proof document name: ")
        update_kyc(**{'ID Proof': id_proof, 'Address Proof': address_proof})
    elif choice == '6':
        print("Thank you for using the Simple Banking Application. Goodbye!")
        break
    else:
        print("Invalid option. Please try again.")