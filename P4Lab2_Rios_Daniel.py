#Daniel Rios
#26APR2026
#P4Lab2
#use while loop and for loop together

'''
Get integer from user
Determine if integer is positive or negative
if number is positive, display multiplication table
if number is negative, tell user program cannot accept
Ask user to run again?
If yes, run program
If no, end program
'''

run_again = 'yes'

while run_again != "no":
    
    num = int(input("Enter an integer: "))
    if num >= 0:
        #display ,multiplication for that value and range from (1-12)
        for item in range(1, 12+1):
            print(f"{num} * {item} = {num * item}")
    else:
        print("This program does not handle negative values")

    run_again = input("Would you like to run the program again? ")

#The loop has broken. User has entered 'no'
print("Program is ending . . .")
