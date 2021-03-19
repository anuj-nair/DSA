import turtle

MAX_LENGTH = 250
INCREMENT = 5


def draw_spiral(a_turtle, line_length):
    if line_length > MAX_LENGTH:
        return
    a_turtle.forward(line_length)
    a_turtle.right(90)
    draw_spiral(a_turtle, line_length+INCREMENT)


ninja = turtle.Turtle(shape='turtle')
ninja.pensize(5)
ninja.color('green')
draw_spiral(ninja, 1)
turtle.done()
