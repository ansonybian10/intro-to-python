import turtle

screen = turtle.Screen()
screen.title("My Turtle Program")

t = turtle.Turtle()
t.speed(5)
t.color("blue")
t.shape("turtle")

for i in range(4):
    t.forward(100)
    t.right(90)



for i in range(3):
    t.forward(100)
    t.right(120)



t.pensize(3)
t.pencolor("blue")
t.forward(150)
t.right(90)
t.pencolor("red")
t.forward(75)
t.right(90)
t.pencolor("blue")
t.forward(150)
t.right(90)
t.pencolor("red")
t.forward(75)
t.right(90)



for i in range(4):
    t.forward(100)
    t.right(90)



t.pencolor("purple")
for i in range(6):
    t.forward(80)
    t.right(60)



t.pencolor("pink")
for i in range(6):
    t.pendown()
    t.circle(50)
    t.penup()
    t.right(60)

screen.mainloop()