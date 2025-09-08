# Polling Booth Program

# Taking user input for age
age = int(input("Enter your age: "))

# Check eligibility
if age < 18:
    print(" You are not eligible to vote. Minimum age is 18.")
else:
    # If age is 18 or above, check ID
    has_id = input("Do you have a valid voter ID? (yes/no): ").lower()
    
    if has_id == "yes":
        print("You are eligible to vote. Please proceed.")
    else:
        print("You must have a voter ID to vote.")
