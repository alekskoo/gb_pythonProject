import turtle
import time


def make_red(sec):
    turtle.TurtleScreen._RUNNING = True
    turtle.reset()
    turtle.ht()
    turtle.speed(0)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.fillcolor("red")
    turtle.end_fill()
    turtle.pu()
    turtle.sety(-80)
    turtle.pd()
    turtle.circle(30)
    turtle.pu()
    turtle.sety(-160)
    turtle.pd()
    turtle.circle(30)
    time.sleep(sec)
    turtle.bye()


def make_yellow(sec):
    turtle.TurtleScreen._RUNNING = True
    turtle.reset()
    turtle.ht()
    turtle.speed(0)
    turtle.pendown()
    turtle.circle(30)
    turtle.pu()
    turtle.sety(-80)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.fillcolor("yellow")
    turtle.end_fill()
    turtle.pu()
    turtle.sety(-160)
    turtle.pd()
    turtle.circle(30)
    time.sleep(sec)
    turtle.bye()


def make_green(sec):
    turtle.TurtleScreen._RUNNING = True
    turtle.reset()
    turtle.ht()
    turtle.speed(0)
    turtle.pendown()
    turtle.circle(30)
    turtle.pu()
    turtle.sety(-80)
    turtle.pd()
    turtle.circle(30)
    turtle.pu()
    turtle.sety(-160)
    turtle.pd()
    turtle.begin_fill()
    turtle.circle(30)
    turtle.fillcolor("green")
    turtle.end_fill()
    time.sleep(sec)
    turtle.bye()


