#  this is the code for fizzbuzz word
def fizz_buzz(number):
    for i in range(1, number+1):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

input_number = input("Enter the last number : ")

if not input_number.isdigit():
    print("Please enter a valid number.")
else:
    fizz_buzz(int(input_number))
