import turtle
colors = ["red", "blue", "green", "yellow"]

t = turtle.Turtle()
t.speed(0) 
turtle.bgcolor("black")

for i in range(100):
    t.color(colors[i % len(colors)])
    t.forward(i * 5)
    t.right(59)

turtle.done()
