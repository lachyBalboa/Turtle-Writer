
import patterns
import turtle
import data
import sys

patterns.start(data.speed)

if sys.argv:
    patterns.draw_text(sys.argv[1])
    turtle.exitonclick()

