def greet():
    print("Hello")


greet()


def greet(name):
    print(f"Hello {name}")


greet("Deepak")


def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


annual_salary = calculate_annual_salary(5000)

print(annual_salary)
