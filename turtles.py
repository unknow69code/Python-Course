import turtle

colors=["white", "red"]
sketch = turtle.pen()
turtle.bgcolor("black")
for i in range(1000):
    sketch.pencolor(colors[i%2])
    sketch.width(i/100+1)
    sketch.forward(i)
    sketch.left(20)
    sketch.turtlesize()