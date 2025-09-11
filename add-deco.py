def add_decorator(func):
    def wrapper(a, b):
        print("== Before Addition ==")
        result = func(a, b)      # call the original function
        print("== After Addition ==")
        return result
    return wrapper

@add_decorator
def add(a, b):
    return a + b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

print("Result:", add(num1, num2))
