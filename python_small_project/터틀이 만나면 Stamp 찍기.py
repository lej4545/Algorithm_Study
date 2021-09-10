import turtle as t
import random
import keyboard
t.setup(width=600,height=600)
t.screensize(600,600)
t1 = t.Turtle()
t1.shape('turtle')
t1.color('red')
t1.turtlesize(2)
t1.penup()
t1.goto(-100,-100)
t1.speed('fastest')
t2 = t.Turtle()
t2.shape('turtle')
t2.color('green')
t2.turtlesize(2)
t2.penup()
t2.goto(0,0)
t2.speed('fastest')
t3 = t.Turtle()
t3.shape('turtle')
t3.color('blue')
t3.turtlesize(2)
t3.penup()
t3.goto(100,100)
t3.speed('fastest')
while True:
    random_move = [[random.randint(0,50), random.randint(0,360)] for r in range(3)]
    t1.forward(random_move[0][0])
    t2.forward(random_move[1][0])
    t3.forward(random_move[2][0])
    t1.right(random_move[0][1])
    t2.right(random_move[1][1])
    t3.right(random_move[2][1])
    print(t1.xcor())
    if t1.distance(t2.pos()) <= 30:
        t1.stamp()
        t2.stamp()
        continue
    if t1.distance(t3.pos()) <= 30:
        t1.stamp()
        t3.stamp()
    if t2.distance(t3.pos()) <= 30:
        t2.stamp()
        t3.stamp()
    if (t1.xcor() < -300 or t1.xcor() > 300) or (t1.ycor() < -300 or t1.ycor() > 300):
        t1.goto(-100,-100)
    if (t2.xcor() < -300 or t2.xcor() > 300) or (t2.ycor() < -300 or t2.ycor() > 300):
        t2.goto(0,0)
    if (t3.xcor() < -300 or t3.xcor() > 300) or (t3.ycor() < -300 or t3.ycor() > 300):
        t3.goto(100,100)
    if keyboard.is_pressed('q'):
        break