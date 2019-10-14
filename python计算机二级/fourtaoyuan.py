import turtle
r = 10
dr = 40
head = 90
for i  in range (4):
    turtle.pendown()
    turtle.circle(r)
    r +=  dr
    turtle.penup()
    turtle.seth(-head)
    turtle.fd(dr)
    turtle.seth(0)
