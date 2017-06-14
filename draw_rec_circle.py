
import turtle

def draw():
    canvas = turtle.Screen()
    canvas.bgcolor("black")
    bond=turtle.Turtle()
    bond.shape("turtle")
    bond.color("yellow")
    bond.speed(20)

    for j in range (0,36):
        for i in range(0,4):
            bond.forward(100)
            bond.right(90)
        bond.right(10)
    bond.right(90)
    bond.forward(300)
    canvas.exitonclick()

draw()

