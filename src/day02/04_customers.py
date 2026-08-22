customers = [
    {"id": 1, "name": "John", "balance": 5000},
    {"id": 2, "name": "Sarah", "balance": 12000},
    {"id": 3, "name": "Michael", "balance": 7500},
]

print(customers)
print(customers[1]["name"])  # Accessing the name of the second customer
print(customers[2]["balance"])  # Accessing the balance of the third customer
print(customers[1])
customers.append(
    {"id": 4, "name": "Emily", "balance": 90000}
)  # Adding a new customer to the list

customers.remove(
    {"id": 1, "name": "John", "balance": 5000}
)  # Removing a customer from the list


def add_customer(customers, new_customer):
    customers.append(new_customer)
    return customers


def remove_customer(customers, customer_id):
    return [c for c in customers if c["id"] != customer_id]


customers = add_customer(customers, {"id": 4, "name": "Emma", "balance": 9000})
customers = remove_customer(customers, 2)  # removes Sarah
print(customers)

for customer in customers:
    if customer["balance"] > 10000:
        print(f"{customer['name']} has a high balance.")
    elif customer["balance"] < 6000:
        print(f"{customer['name']} has a low balance.")
    else:
        print(f"{customer['name']} has a moderate balance.")

total_balance = 0

for customer in customers:
    total_balance += customer["balance"]

print(total_balance)

print(customers)


def highest_balance(customers):
    if not customers:
        return None
    top_customer = max(customers, key=lambda c: c["balance"])
    print(
        f"Highest balance customer:\nName: {top_customer['name']}, Balance: {top_customer['balance']}"
    )
    return top_customer


highest_balance(customers)
