#Daniel Rios
#04/12/2026
#P2HW1
#alinging with f strings

#Display header
print("This program calculates and displays travel expenses")
print()

#Inital total budget from user
base = int(input("Enter budget: "))

#Intial destination input from user
location = input("Enter your travel destination: ")

# Initial approximat integers for gas, accomidations, and food
num1 = int(input("How much do you think you will spend on gas? "))
num2 = int(input("Approximately, how much will you need for accomidation/hotel? "))
num3 = int(input("Last, how much do you need for food? "))

#Calculate Expenses

#Display header
print()
print("--------Travel Expenses--------")
print()

#Display of all user information inputed



print(f'{"Location:":<15s} {location:>}')
print(f'{"Initial Budget:":<15s} ${base:.2f}')
print(f'{"Fuel:":<15s} ${num1:.2f}')
print(f'{"Accomidation:":<15s} ${num2:.2f}')
print(f'{"Food:":<15s} ${num3:.2f}')


#Calculate total expenses
sum_result = num1 + num2 + num3

#Calculate of remaining balance by subtracting expenses from budget
final_result = base - sum_result

#Display of remaining balance
print("-" *34)
print()
print(f'{"Remaining Balance:":<15s} ${final_result:>.2f}')
