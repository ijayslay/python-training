def sum_all(*numbers):
    return sum(numbers)


# Example 1: passing numbers directly
print("Example 1:", sum_all(1, 2, 3, 4, 5, 6, 30, 40, 50, 60, 100))

# Example 2: passing a list with unpacking
my_list = [10, 20, 30, 40, 50]
print("Example 2:", sum_all(*my_list))

# Example 3: passing a tuple with unpacking
my_tuple = (5, 15, 25, 35, 45)
print("Example 3:", sum_all(*my_tuple))

