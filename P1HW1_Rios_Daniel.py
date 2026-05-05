# Daniel Rios
# 05Apr2026
# P1HW1_Rios_Daniel
# Calculating exponents and addition and subtraction

#calculate exponents

print("--------Exponents--------")
print()

base = int(input("Enter a base number: "))
exponent = int(input("Enter a exponent: "))
result = base ** exponent
print(base, "rasised to the power of", exponent, "is", result, "!!")

# calculate addition and subtraction
print("--------Addition and Subtraction--------")
print()

num1 = int(input("Enter a starting integer: "))
num2 = int(input("Enter a integer to add: "))
num3 = int(input("Enter a integer to subtract: "))

sum_result = num1 + num2
final_result = sum_result - num3

print(num1, "+", num2, "-", num3, "is equal to", final_result, "!!")