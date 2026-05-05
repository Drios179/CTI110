#Daniel Rios
#05MAY2026
#P4HW1
#collecting scores using a loop 


# number of scores you want to enter
count = int(input("How many scores do you want to enter? "))
print()

scores = []

# range of scores 1 at a time
score_number = 1

# number grade entered by user
while score_number <= count:
    score = float(input(f"Enter score #{score_number}: "))

    # score entered is between 0-100 if not it presents an 'error'
    while score < 0 or score > 100:
        print()
        print("INVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        score = float(input(f"Enter score #{score_number} again: "))

    # adds scores 1 by 1 at end of list
    scores.append(score)
    score_number += 1

# Removing lowest score
lowest = min(scores)
scores.remove(lowest)

# Calculates letter grade average
average = sum(scores) / len(scores)

# letter grade average
if average >= 90:
    grade = 'A'
elif average >= 80:
    grade = 'B'
elif average >= 70:
    grade = 'C'
elif average >= 60:
    grade = 'D'
else:
    grade = 'F'

# Displaying results (low, list, avg, and letter grade)
print()
print("-------------Results-------------")
print(f"{'Lowest Score:':15s} {lowest}")
print(f"{'Modified List:':15s} {scores}")
print(f"{'Scores Average:':15s} {average:.2f}")
print(f"{'Grade:':15s} {grade}")
print("---------------------------------")
print()
