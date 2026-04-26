#Daniel Rios
#26APR2026
#P4Lab1a
#drawing with turle and loops


#inport to library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()


#Set turtle options
pen.pensize(3)
pen.pencolor("purple")
pen.shape("arrow")

#code to draw shapes
for side in range(4):
    pen.forward(100)
    pen.left(90)

#while loop that executes 3 times
sides = 3
while sides > 0:
    pen.forward(100)
    pen.right(120)
    sides = sides - 1


#wait for user to close window
win.mainloop()
