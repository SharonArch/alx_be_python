# finance_calculator.py

# Prompt user for monthly income
monthly_income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
monthly_expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = monthly_income - monthly_expenses

# Annual savings before interest
annual_savings = monthly_savings * 12

# Apply 5% interest to annual savings
projected_savings = annual_savings + (annual_savings * 0.05)

# Output results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")
