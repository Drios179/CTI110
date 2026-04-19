#Daniel Rios
#04/12/2026
#P2HW2
#display grades and averages with f strings

#Display header space
print()



# Initial input grades for modules
num1 = float(input(f"{'Module 1:':15s} "))
num2 = float(input(f"{'Module 2:':15s} "))
num3 = float(input(f"{'Module 3:':15s} "))
num4 = float(input(f"{'Module 4:':15s} "))
num5 = float(input(f"{'Module 5:':15s} "))
num6 = float(input(f"{'Module 6:':15s} "))


#key for f string grades, averages, max, min, and total
grades = {num1, num2, num3, num4, num5, num6}

#calculates min
lowest = min(grades)
#calculates max
highest = max(grades)
#calculates total
total = sum(grades)
#calculates avg using lenght function for the grade key
average = total / len(grades)

#Display header
print("------------Results------------")

#Display of input grades seperated
print(f"{'Lowest Grade:':15s} {lowest}")
print(f"{'Highest Grade:':15s} {highest}")
print(f"{'Sum of Grades:':15s} {total}")
print(f"{'Average:':15s} {average:.2f}")
print("--------------------------------")
