#  This program is to count the vowels in a sring with or without spaces


def count_vowels(string):
    vowels = "aeiouAEIOU"
    count = 0
    for char in string:
        if char in vowels:
            count += 1
    return count


user_input = input("Enter a string : ")

if not user_input.isdigit():
    print("The given string has", count_vowels(user_input), "vowels.")
else:
    print("The given input is not a plain string")
