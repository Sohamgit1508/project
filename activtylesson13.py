import turtle
turtle.Screen().bgcolor("orange")
turtle.Screen().setup(300,400)
polygon=turtle.Turtle()
numside=6
sizelength=70
angle=360.0/numside
for i in range(numside):
     polygon.forward(sizelength)
     polygon.right(angle)
turtle.done()