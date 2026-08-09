# This code checks whether a given input is a palindrome

def is_palindrome(text):
    text = text.lower()
    return text[::-1] == text

user_input = input("Enter a string or number: ")

if user_input.isdigit():
    print("The given number is a palindrome:", is_palindrome(user_input))
elif user_input.isalpha():
    print("The given string is a palindrome:", is_palindrome(user_input))
else:
    print("The given input is not a plain string or number")