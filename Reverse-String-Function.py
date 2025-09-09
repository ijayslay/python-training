def reverse_string(text):
    reversed_text = ""
    for ch in text:
        reversed_text = ch + reversed_text   # add each character in front
    return reversed_text


# Taking input from user
user_input = input("Enter a string: ")
print("Reversed string:", reverse_string(user_input))
