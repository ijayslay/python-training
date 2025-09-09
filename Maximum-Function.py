#def find_max(numbers):
    # assume first element is max
#    max_num = numbers[0]
    
    # loop in the list
#    for num in numbers:
#       if num > max_num:
#          max_num = num
# return max_num


# Example usage
#nums = [10, 45, 67, 23, 89, 2, 100, 56]
#print("The maximum number is:", find_max(nums))

def two_max(numbers):
    first = second = float('-inf')
    
    for num in numbers:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    
    if second == float('-inf'):
        return first, None  # if no second max exists
    return first, second


# Example usage
nums = [10, 45, 67, 23, 89, 2, 100, 56]
maximum, second_maximum = two_max(nums)

print("Maximum number:", maximum)
print("Second maximum number:", second_maximum)
