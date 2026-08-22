for number in range(1, 11):
    print(number)

# Print even numbers from 1–20.
print("Print even numbers from 1–20")
for number in range(2, 21, 2):
    print(number)


def sum_series_formula(n):
    return n * (n + 1) // 2


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)


# Calculate the sum of 1–100.
print("Sum:", sum_series_formula(100))

# Calculate the factorial of 5.
print("Calculate the factorial of 5.")
print(factorial(5))
