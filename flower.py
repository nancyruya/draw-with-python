import turtle

ruya = turtle.Turtle()
ruya.color("red", "yellow")
ruya.speed(10)

ruya.begin_fill()
for i in range(50):
    ruya.forward(300)
    ruya.left(168.5)
ruya.end_fill()

turtle.done()
