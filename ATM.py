# Simple ATM Machine Simulation with Multiples of 100

# Initial balance in ATM
balance = 50000  

print("=== Welcome to Python ATM ===")
print(f"Available Balance: ₹{balance}")

# Ask user for withdrawal amount
amount = int(input("Enter the amount you want to withdraw: "))

# First check if amount is in multiples of 100
if amount % 100 != 0:
    print("Invalid amount! Please enter in multiples of ₹100.")
else:
    # Then check if sufficient balance is available
    if amount <= balance:
        balance -= amount  # Deduct the amount
        print(f"Withdrawal successful! You withdrew ₹{amount}")
        print(f"Remaining Balance: ₹{balance}")
    else:
        print("Insufficient Balance! Please try a smaller amount.")

print("=== Thank You for Using Python ATM ===")
