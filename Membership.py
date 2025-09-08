# Supermarket Billing System

# Enter bill amount
amount = float(input("Enter total bill amount: "))

# Ask for membership type
print("Membership Types: none / gold / platinum")
membership = input("Enter your membership type: ").strip().lower()

# Apply discount
if membership == "gold":
    discount = 0.10 * amount
    final_amount = amount - discount
    print(f"Gold Membership: 10% discount applied.")
elif membership == "platinum":
    discount = 0.20 * amount
    final_amount = amount - discount
    print(f"Platinum Membership: 20% discount applied.")
else:
    discount = 0
    final_amount = amount
    print("No membership discount applied.")

# Show final bill
print(f"Original Amount: ₹{amount:.2f}")
print(f"Discount: ₹{discount:.2f}")
print(f"Final Payable Amount: ₹{final_amount:.2f}")
