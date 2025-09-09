def find_duplicates(numbers):
    same = []
    duplicates = []
    
    for num in numbers:
        if num in same and num not in duplicates:
            duplicates.append(num)
        else:
            same.append(num)
    return duplicates


# Example usage
nums = [10, 20, 30, 40, 20, 50, 10, 60, 30]
print("Duplicate values are:", find_duplicates(nums))


