# finance_calculator.py

# Prompt user for monthly income
income = float(input("Enter your monthly income: "))

# Prompt user for monthly expenses
expenses = float(input("Enter your total monthly expenses: "))

# Calculate monthly savings
monthly_savings = income - expenses

# Annual savings before interest
annual_savings = monthly_savings * 12

# Apply 5% interest to annual savings
projected_savings = annual_savings + (annual_savings * 0.05)

# Output results
print("Your monthly savings are $" + str(monthly_savings) + ".")
print("Projected savings after one year, with interest, is: $" + str(projected_savings) + ".")

