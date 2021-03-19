import turtle

SPEED = 5
BG_COLOR = "black"
PEN_COLOR = "yellow"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
DRAWING_WIDTH = 700
DRAWING_HEIGHT = 700
PEN_WIDTH = 5
TITLE = "H-Tree Fractal"
FRACTAL_DEPTH = 6


def draw_line(ninja, pos1, pos2):
    # print("Drawing from", pos1,"to",pos2)
    ninja.penup()
    ninja.goto(pos1[0], pos1[1])
    ninja.pendown()
    ninja.goto(pos2[0], pos2[1])


def recursive_draw(ninja, x, y, width, height, count):
    draw_line(
        ninja,
        [x + width * 0.25, y + height // 2],
        [x + width * 0.75, y + height // 2],
    )

    draw_line(
        ninja,
        [x + width * 0.25, y + (height * 0.5) // 2],
        [x + width * 0.25, y + (height * 1.5) // 2],
    )

    draw_line(
        ninja,
        [x + width * 0.75, y + (height * 0.5) // 2],
        [x + width * 0.75, y + (height * 1.5) // 2],
    )

    if count <= 0:
        # Base Case
        return
    else:
        # Recursive Case
        count -= 1
        # Top left
        recursive_draw(ninja, x, y, width//2, height//2, count)
        # Top right
        recursive_draw(ninja, x+width//2, y, width//2, height//2, count)
        # Bottom left
        recursive_draw(ninja, x, y+width//2, width//2, height//2, count)
        # Bottom right
        recursive_draw(ninja, x+width//2, y+width //
                       2, width//2, height//2, count)


if __name__ == "__main__":
    # Screen Setup
    screen = turtle.Screen()
    screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
    screen.title(TITLE)
    screen.bgcolor(BG_COLOR)

    # Turtle Setup
    ninja = turtle.Turtle()
    ninja.hideturtle()
    ninja.pensize(PEN_WIDTH)
    ninja.color(PEN_COLOR)
    ninja.speed(SPEED)

    # Initial call to recursive_draw function
    recursive_draw(ninja, - DRAWING_WIDTH/2, -DRAWING_HEIGHT/2,
                   DRAWING_WIDTH, DRAWING_HEIGHT, FRACTAL_DEPTH)

    turtle.done()
