import turtle
t=turtle.Turtle()
for i in range(100,110):
    t.circle(i)
t.penup()
t.fd(100)
t.pendown()
for i in range(100,110):
    t.circle(i)
t.penup()
t.lt(90)
t.fd(30)
t.lt(90)
t.fd(50)
t.pendown()
for i in range(100,110):
    t.circle(i)
t.penup()
t.rt(90)
t.fd(200)
t.pendown()
t.fd(20)



