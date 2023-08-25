from turtle import *
import time
import random

score= 0
executionDelay = 0.1
root = Screen() #object of screen class
root.title('Snake Game')
root.setup(width=600,height=600)
root.bgcolor('black')
root.bgpic('border.gif')
root.tracer(False)
root.addshape('upmouth.gif')
root.addshape('downmouth.gif')
root.addshape('rightmouth.gif')
root.addshape('leftmouth.gif')
root.addshape('body.gif')
root.addshape('food.gif')
head = Turtle()
head.shape('upmouth.gif')
head.penup()
head.goto(0,0)
head.direction = 'stop'

food = Turtle()
food.penup()
food.goto(0,100)
food.shape('food.gif')

text = Turtle()
text.penup()
text.goto(0,268)
text.color('white')
text.write('Score:0',font=('courier',25,'bold'),align='center')
text.hideturtle()

lost = Turtle()
lost.color('white')
lost.penup()
lost.hideturtle()


def move_snake():
    if head.direction=='up':
        y=head.ycor()
        y=y+20
        head.sety(y)

    if head.direction == 'down':
        y=head.ycor()
        y=y-20
        head.sety(y)
    if head.direction == 'right':
        x=head.xcor()
        x=x+20
        head.setx(x)

    if head.direction == 'left':
        x=head.xcor()
        x=x-20
        head.setx(x)

def goUp():
    if head.direction!='down':
        head.direction = 'up'
        head.shape('upmouth.gif')

def goDown():
    if head.direction!='up':
        head.direction = 'down'
        head.shape('downmouth.gif')

def goRight():
    if head.direction!='left':
        head.direction = 'right'
        head.shape('rightmouth.gif')

def goLeft():
    if head.direction != 'right':
        head.direction = 'left'
        head.shape('leftmouth.gif')

root.listen()

root.onkeypress(goUp,'Up')
root.onkeypress(goDown,'Down')
root.onkeypress(goRight,'Right')
root.onkeypress(goLeft,'Left')

segments=[]

while True:
    root.update()
    if head.xcor()>260 or head.xcor()<-260 or head.ycor()>260 or head.ycor()<-260:
        lost.write('Game Lost',align='center',font=('courier',34,'bold'))
        time.sleep(1)
        lost.clear()
        time.sleep(1)
        head.goto(0,0)
        head.direction = 'stop'
        for bodies in segments:
            bodies.goto(1000,1000)

        score = 0
        executionDelay = 0.1
        segments.clear()
        text.clear()
        text.write('Score:0',align='center',font=('courier',25,'bold'))

    if head.distance(food)<20:
        x = random.randint(-255,255)
        y = random.randint(-255,255)
        food.goto(x,y)
        executionDelay=executionDelay-0.003

        body = Turtle()
        body.penup()
        body.shape('body.gif')
        segments.append(body)
        score=score+10
        text.clear()
        text.write(f'Score:{score}',font=('courier',25,'bold'),align='center')

    for i in range(len(segments)-1,0,-1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x,y)

    if len(segments)>0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)

    move_snake()

    for bodies in segments:
        if bodies.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = 'stop'

            for bodies in segments:
                bodies.goto(1000,1000)

            segments.clear()
            score = 0
            executionDelay = 0.1
            lost.write('Game Lost',align='center',font = ('courier',34,'bold'))
            time.sleep(1)
            lost.clear()

            text.clear()
            text.write('Score:0',align='center',font=('courier',25,'bold'))

    time.sleep(executionDelay)

