#Daniel Rios
#10May2026
#P5LAB
#Using a randon float to calculate total owed for the purchase

#Random module imported
import random

# Generate random total owed
total_owed = round(random.uniform(0.01, 100.00), 2)
print(f"You owe ${total_owed}")

# Get user total payment
payment = float(input("How much cash will you put in the self-checkout? "))

# Calculate change
change = payment - total_owed
change = round(change, 2)

print(f"Change is: ${change}")

# Rounding the amount
change = round(change * 100)

# Determine amount needed
num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickles = change // 5
change = change - (num_nickles * 5)

num_pennies = change

# Display results
if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} Dollar")
    else:
        print(f"{num_dollars} Dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} Quarter")
    else:
        print(f"{num_quarters} Quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} Dime")
    else:
        print(f"{num_dimes} Dimes")

if num_nickles > 0:
    if num_nickles == 1:
        print(f"{num_nickles} Nickle")
    else:
        print(f"{num_nickles} Nickles")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} Penny")
    else:
        print(f"{num_pennies} Pennies")
