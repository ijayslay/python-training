# Function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Call the function for 5
num = 5
print(f"Factorial of {num} is: {factorial(num)}")

