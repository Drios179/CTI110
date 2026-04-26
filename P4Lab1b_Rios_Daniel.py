#inport to library
import turtle

#Create the turtle window and drawing object
win = turtle.Screen()
pen = turtle.Turtle()

#creating a definition to move without drawing
def jump(x, y):
    pen.penup()
    pen.goto(x, y)
    pen.pendown()


#Set turtle options
pen.pensize(3)
pen.pencolor("purple")
pen.shape("arrow")

#draw initials DR
pen.left(90)
pen.forward(100)
pen.right(60)
#creating hlaf circle for the"D"
pen.circle(-60, 230)
pen.forward(8)
pen.right(70)
pen.forward(100)
pen.right(90)

#Moving pen without drawing
jump(100,0)
#Creating the "R"
pen.left(90)
pen.forward(100)
pen.right(60)
#Creating half circle for the "R"
pen.circle(-20,200)
pen.forward(15)
pen.left(110)
pen.forward(70)


#wait for user to close window
win.mainloop()
