# Driving License Eligibility Checker

# Take user input
age = int(input("Enter your age: "))
has_license = input("Do you already have a driving license? (yes/no): ").lower()

# Check conditions
if age > 18:
    if has_license == "yes":
        print("You are eligible to drive.")
    else:
        print("You cannot drive without a valid license.")
else:
    print("You are not eligible to drive because your age is below 18.")
