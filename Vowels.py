def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    
    for ch in text:
        if ch in vowels:
            count += 1
    return count


# Taking input from user
user_input = input("Enter a string: ")
print("Number of vowels:", count_vowels(user_input))
