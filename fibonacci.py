def fibonacci(n):
    a, b = 0, 1   # first two numbers
    series = []
    
    for _ in range(n):
        series.append(a)   # store current number
        a, b = b, a + b   # update values
    return series


# Example usage
num = int(input("Enter how many terms you want: "))
print("Fibonacci series:", fibonacci(num))
