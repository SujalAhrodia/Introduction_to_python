import turtle

#length = side of bigger triangle, depth = levels of the fractal design
def fractal(length,depth):
    if depth==0:
        for i in range(0,3):
            bond.forward(length)
            bond.left(120)
    else:
        fractal(length/2,depth-1)
        bond.forward(length/2)
        fractal(length/2,depth-1)
        bond.backward(length/2)
        bond.left(60)
        bond.forward(length/2)
        bond.right(60)
        fractal(length/2,depth-1)
        bond.left(60)
        bond.backward(length/2)
        bond.right(60)

canvas = turtle.Screen()
canvas.bgcolor("black")
bond = turtle
bond.color("white")
bond.shape("turtle")
bond.speed(20)
bond.goto(-100,0)
fractal(200,2)
canvas.exitonclick()

