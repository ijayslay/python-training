# Blood Donation Camp Eligibility Checker

# Take user input
age = int(input("Enter your age: "))
weight = float(input("Enter your weight in kg: "))

# Check conditions
if 18 <= age <= 65:
    if weight >= 50:
        print("You are eligible to donate blood.")
    else:
        print("You are not eligible to donate blood because your weight is below 50 kg.")
else:
    print("You are not eligible to donate blood because your age is not between 18 and 65.")
