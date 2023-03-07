import turtle
import time

def showCircle(n):
    try:
        win = turtle.Screen()
        t = turtle.Turtle()
        angle = 360 / n
        for i in range(n):
            t.forward(10)
            t.left(angle)
        time.sleep(3)
    except:
        print("Error")

showCircle(45)
#showCircle(0)