# Rios Daniel
# 04/12/2026
#P2Lab1
#the program will calculate the diameter, circumference, and area of a circle

#import math module to us the constant, math.pi
import math

#get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

#display diameter with 1 decimal point
print(f"The diameter of the circle is {diameter:.1f}\n")

#calculate circumference
circumference = 2 * math.pi * radius

#display circumference with 2 decimal places
print(f"The circumference of the circle is {circumference:.2f}\n")

#calculate the area
area = math.pi * radius**2

#display area with 3 decimal places

print(f"The area of the circle is {area:.3f}\n")

