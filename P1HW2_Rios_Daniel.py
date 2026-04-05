# Daniel Rios
# 05Apr2026
# P1HW2_Rios_Daniel
# Basic calculations with math

print("--------This program calculates and displays travel expenses--------")
print()

base = int(input("Enter budget: "))
location = input("Enter your travel destination: ")
num1 = int(input("How much do you think you will spend on gas?: "))
num2 = int(input("Approximately, how much will you need for accomidation/hotel?: "))
num3 = int(input("Last, how much do you need for food?: "))

#Calculate Expenses
print("--------Travel Expenses--------")
print()

print("Location: ",location)
print("Initial Budget: ",base)
print("Fuel: ",num1)
print("Accomidation: ",num2)
print("Food: ",num3)

sum_result = num1 + num2 + num3
final_result = base - sum_result

print("Remaining Balance: ",final_result)