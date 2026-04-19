#Daniel Rios
#04/12/2026
#P2Lab2
#Using dictionaries

cars = {'Camaro':18.21, 'Prius':52.36, 'Model S':110, 'Silverado':26}

#get keys from dict
cars_keys = cars.keys()

print(cars_keys)

print(*cars_keys, sep = ", ")

#get a car from user

car_name = input("Enter a car: ")

#get mpg for the given car
car_mpg = cars[car_name]
print(f"The {car_name} gets {car_mpg} miles per gallon. ")

#get miles from user
miles_driven = float(input(f"How miles will you drive the {car_name}? "))

#Calculate
gallons_needed = miles_driven/car_mpg

#display results
print(f"{gallons_needed:.2f} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")
