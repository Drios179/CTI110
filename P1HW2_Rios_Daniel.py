# Daniel Rios
# 05Apr2026
# P1HW2_Rios_Daniel
# Basic calculations with math

#Display header
print("--------This program calculates and displays travel expenses--------")
print()

#Inital total budget from user
base = int(input("Enter budget: "))

#Intial destination input from user
location = input("Enter your travel destination: ")

# Initial approximat integers for gas, accomidations, and food
num1 = int(input("How much do you think you will spend on gas?: "))
num2 = int(input("Approximately, how much will you need for accomidation/hotel?: "))
num3 = int(input("Last, how much do you need for food?: "))

#Calculate Expenses

#Display header
print("--------Travel Expenses--------")
print()

#Display of all user information inputed
print("Location: ",location)
print("Initial Budget: ",base)
print("Fuel: ",num1)
print("Accomidation: ",num2)
print("Food: ",num3)

#Calculate total expenses
sum_result = num1 + num2 + num3

#Calculate of remaining balance by subtracting expenses from budget
final_result = base - sum_result

#Display of remaining balance
print("Remaining Balance: ",final_result)