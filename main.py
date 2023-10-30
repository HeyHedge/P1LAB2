#Travel expenses
#9-4-23
#CTI-110 P1HW2 - Travel Expenses
# Tyrique Lawrence
####################
budget = float(input("Enter your budget: "))
destination = input("Enter your travel destination: ")
gas_expenses = float(input("Enter the amount you will spend on gas: "))
accommodation_expenses = float(input("Enter the amount you will spend on accommodation: "))
food_expenses = float(input("Enter the amount you will spend on food: "))

total_expenses = gas_expenses + accommodation_expenses + food_expenses
remaining_budget = budget - total_expenses

print("Results")
print("Destination:", destination)
print("Total Expenses:", total_expenses)
print("Remaining Budget:", remaining_budget)