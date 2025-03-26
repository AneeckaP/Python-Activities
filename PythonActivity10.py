import turtle
turtle.Screen().bgcolor("purple")
turtle.Screen().setup(600,700)
Aneecka=turtle.Turtle()

num_sides=8
side_length=65
angle=360.0/num_sides
for i in range (num_sides):
    Aneecka.forward(side_length)
    Aneecka.right(angle)
turtle.done()
