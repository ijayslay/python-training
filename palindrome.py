
def is_palindrome(text):
    # check if string equals its reverse
    return text == text[::-1]

# take user input
word = input("Enter a word: ")

if is_palindrome(word):
    print("Palindrome")
else:
    print("Not a palindrome")
