customer_name = "John smith Doe"
company_name = "Excellent Corp"
print(customer_name)
print(len(customer_name))

print(customer_name[0:4])  # John
print(customer_name[5:])  # Doe
print(customer_name[:4])  # John
print(customer_name[-3:])  # Doe
print(customer_name[:-4])  # John
print(customer_name[::-1])  # eoD nhoJ
print(customer_name.rsplit(" ", 1)[-2])  # John smith
print(customer_name.rsplit(" ", 1)[-1])  # Doe
print(customer_name.rsplit(" ", 1)[0])  # John smith
print(customer_name.rsplit(" ", 1)[1])  # Doe


print(
    "This is the company name {} and the employee name is {}".format(
        company_name, customer_name
    )
) #This is the company name Excellent Corp and the employee name is John smith Doe
