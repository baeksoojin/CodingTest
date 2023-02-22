import turtle
import random

screen = turtle.Screen()
image1 = "/Users/baeksujin/Desktop/codingtest/CodingTest/휴몬랩코딩수업준비/car1.gif"
image2 = "/Users/baeksujin/Desktop/codingtest/CodingTest/휴몬랩코딩수업준비/car2.gif"
screen.addshape(image1)
screen.addshape(image2)

def player(image,no):
    t = turtle.Turtle()
    t.shape(image)
    t.pensize(3)
    t.penup()
    t.goto(-screen.canvwidth , -200*(no-1))
    return t

t1 = player(image1, 1)
t2 = player(image2,2)

t1.pendown()
t2.pendown()

t1.speed(1)
t2.speed(1)

for i in range(50):
    d1 = random.randint(1,60)
    t1.forward(d1)
    d2 = random.randint(1,60)
    t2.forward(d2)

    if(t1.pos()[0] > screen.canvwidth or t2.pos()[0] > screen.canvwidth):
        if(t1.pos()[0] > t2.pos()[0]):
            print("the first runner is the winner")
        else:
            print("the second runner is the winner")
        break

print("race is done")


input()