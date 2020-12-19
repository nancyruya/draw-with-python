import turtle

ruya = turtle.Turtle()

ruya.begin_fill()
ruya.color("red", "cyan")
ruya.forward(100)
ruya.left(90)
ruya.forward(100)
ruya.left(90)
ruya.forward(100)
ruya.left(90)
ruya.forward(100)

ruya.penup()
ruya.forward(150)
ruya.penend()
ruya.forward(100)
ruya.end_fill()

turtle.done()
