import turtle

screen = turtle.Screen()
screen.title("Turtle Screen")

t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.shape("turtle")

t.penup()
t.goto(-100, 0)
t.pendown()

t.write("67", font=("Arial", 60, "bold"))

screen.mainloop()