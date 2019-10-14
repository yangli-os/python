from turtle import *
from random import *
# 绘制随机雪花
def DrawSnow(snow):
    x = randrange(-750, 750)
    y = randrange(-50, 400)
    snowcolor = (randrange(0, 255), randrange(0, 255), randrange(0, 255))
    snowsize = randrange(10, 20)
    snowstyle = choice([30, 45])
    snow.penup()
    snow.setpos(x, y)
    snow.pendown()
    colormode(255)
    snow.pencolor(snowcolor)
    for i in range(int(360/snowstyle)):
        if snowsize < 11:
            snowstyle = 90
        snow.forward(snowsize)
        snow.backward(snowsize)
        snow.right(snowstyle)
#绘制上半部分雪花
def InitSnow(n):
    snow = Turtle()
    for i in range(n):
        DrawSnow(snow)
#绘制下半部分雪地
def InitField():
    field = Turtle()
    colormode(255)
    for i in range(300):
        x = randrange(-850, 850)
        y = randrange(-400, 0)
        width = randrange(50, 200)
        length = randrange(3, 8)
        field.penup()
        field.setpos(x, y)
        field.pendown()
        tempcolor = int(-255 * y/400)
        print(tempcolor)
        fieldcolor = (tempcolor, tempcolor, tempcolor)
        field.color(fieldcolor, fieldcolor)
        field.begin_fill()
        field.fd(width)
        field.circle(length, 180)
        field.fd(width)
        field.circle(length, 180)
        field.end_fill()
 
def main():
    bgcolor("black")
    tracer(False)
    InitField()
    InitSnow(200)
    tracer(True)
    mainloop()
 
if __name__ == '__main__':
    main()
