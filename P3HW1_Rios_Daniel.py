# Rios Daniel
# 19/APR/2026
# P3HW1
# Fixing code for the calculation of grades

# Enter grades for six modules
mod_1 = float(input(f"{'Module 1:':15s} "))
mod_2 = float(input(f"{'Module 2:':15s} "))
mod_3 = float(input(f"{'Module 3:':15s} "))
mod_4 = float(input(f"{'Module 4:':15s} "))
mod_5 = float(input(f"{'Module 5:':15s} "))
mod_6 = float(input(f"{'Module 6:':15s} "))
# Add grades to a list
grades = [mod_1, mod_2, mod_3, mod_4, mod_5, mod_6]

# Determine lowest, highest, sum, and average
low = min(grades)
high = max(grades)
total = sum(grades)
avg = total / len(grades)

# Display results
print("----------- Results -----------")
print(f"{'Lowest Grade:':15s} {low}")
print(f"{'Highest Grade:':15s} {high}")
print(f"{'Sum of Grades:':15s} {total}")
print(f"{'Average:':15s} {avg:.2f}")
# Determine letter grade
print("----------- Letter Grade -----------")
if avg >= 90:
    print('Your grade is: A')
elif avg >= 80:
    print('Your grade is: B')
elif avg >= 70:
    print('Your grade is: C')
elif avg >= 60:
    print('Your grade is: D')
else:
    print('Your grade is: F ')
