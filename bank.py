
balance = float(input("Enter initial balance: "))
deposit = float(input("Enter deposit amount: "))

balance += deposit
print("Balance after deposit:", balance)

withdraw = float(input("Enter withdrawal amount: "))

if withdraw <= balance:
    balance -= withdraw
    print("Balance after withdrawal:", balance)
else:
    print("Insufficient balance!")