# calculate_annual_salary()
def calculate_annual_salary(monthly_salary):
    return monthly_salary * 12


# calculate_roi()
def calculate_roi(initial_investment, final_value):
    return ((final_value - initial_investment) / initial_investment) * 100


# calculate_profit()
def calculate_profit(initial_investment, final_value):
    return final_value - initial_investment


# calculate_loss()
def calculate_loss(initial_investment, final_value):
    return initial_investment - final_value


# calculate_percentage()
def calulate_percentage(part, whole):
    return (part / whole) * 100


roi = calculate_roi(10000, 12500)

print(f"ROI: {roi}%")
print(f"profit: {calculate_profit(10000, 12500)}")
print(f"Loss: {calculate_loss(10000, 8000)}")
print(f"Percentage: {calulate_percentage(10,100)}")
