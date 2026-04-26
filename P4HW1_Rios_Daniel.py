#Daniel Rios
#26APR2026
#P4HW1
#Using loop to display score averages



def valid_score(score_number):
    # asks until the user enters a valid value
    while True:
        score = float(input(f"Enter score #{score_number}: "))
        #determining range/value of user number input
        if 0 <= score <= 100:
            return score
        #printing based off invalid input
        else:
            print("INVALID Score entered!!!!")
            print("Score should be between 0 and 100")


#deteremining letter grade by input
def letter_grade(average):
    if average >= 90:
        return "A"
    elif average >= 80:
        return "B"
    elif average >= 70:
        return "C"
    elif average >= 60:
        return "D"
    else:
        return "F"


#program container
def main():
    # Asking how many scores from the user
    count = int(input("How many scores do you want to enter? "))

    scores = []

    # range of scores one at a time
    for i in range(1, count + 1):
        score = valid_score(i)
        scores.append(score)

    # entries determine to remove the lowest score
    lowest = min(scores)
    scores.remove(lowest)

    # Calculate average
    average = sum(scores) / len(scores)

    # letter grade
    grade = letter_grade(average)

    # Display results
    print("-------------Results-------------")
    print(f"{'Lowest Score:':15s} {lowest}")
    print(f"{'Modified List:':15s} {scores}")
    print(f"{'Scores Average:':15s} {average:.2f}")
    print(f"{'Grade:':15s} {grade}")
    print("---------------------------------")


# end of program container
main()
