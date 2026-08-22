numbers = [1, 2, 3, 4, 5]

squares = []

for number in numbers:
    squares.append(number * number)

print(squares)
numbers.extend([numbers.copy(), 10, 20, 30, 40, 50, 60, 70])
print(numbers)
print(numbers[5])

squares = [number * number for number in numbers]

print(squares)
