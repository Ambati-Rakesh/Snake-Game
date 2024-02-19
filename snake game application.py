import turtle
import time
import random
delay = 0.1
score = 0
high_score = 0
# Creating a window screen
wn = turtle.Screen()
wn.title("ADR Snake Game")
wn.bgcolor("black")
wn.bgpic("border.gif")
wn.addshape('apple.gif')
wn.addshape('snake head.gif')
wn.addshape('download.gif')
# the width and height can be put as user's choice
wn.setup(width=420, height=560)
wn.tracer(0)
# head of the snake
head = turtle.Turtle()
head.shape("snake head.gif")
head.color("red")
head.penup()
head.goto(0, 0)
head.direction = "Stop"
#grid
grid=turtle.Turtle()
grid.shape('download.gif')
grid.penup()
grid.goto(80,0)
#grid 2
grid1=turtle.Turtle()
grid1.shape('download.gif')
grid1.penup()
grid1.goto(-60,-100)
#grid 3
grid2=turtle.Turtle()
grid2.shape('download.gif')
grid2.penup()
grid2.goto(-80,140)

# food in the game
food = turtle.Turtle()
colors = random.choice(['red', 'green', 'blue'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)
pen = turtle.Turtle()
pen.speed(10)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0,200)
pen.write("Score : 0 High Score : 0", align="center",
        font=("candara", 24, "bold"))
# assigning key directions
def group():
    if head.direction != "down":
        head.direction = "up"
def godown():
    if head.direction != "up":
        head.direction = "down"
def goleft():
    if head.direction != "right":
        head.direction = "left"
def goright():
    if head.direction != "left":
        head.direction = "right"
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)
wn.listen()
wn.onkeypress(group, "Up")
wn.onkeypress(godown, "Down")
wn.onkeypress(goleft, "Left")
wn.onkeypress(goright, "Right")

segments = []
# Main Gameplay
while True:
    wn.update()
    if head.xcor() > 170 or head.xcor() < -170 or head.ycor() > 230 or head.ycor() < -240 or (head.xcor() == 80 and head.ycor() == 0) or (head.xcor() == -60 and head.ycor() == -100)  or (head.xcor() == -80 and head.ycor()==140):
        time.sleep(1)
        head.goto(0, 0)
        head.direction = "Stop"
        colors = random.choice(['red', 'blue', 'green'])
        shapes = random.choice(['square', 'circle'])
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        delay = 0.1
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    if head.distance(food) < 20:
        x = random.randint(-170, 170)
        y = random.randint(-170, 170)
        food.goto(x, y)
        # Adding segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("circle")
        new_segment.color("light green") # tail colour
        new_segment.penup()
        segments.append(new_segment)
        delay -= 0.001
        score += 10
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("candara", 24, "bold"))
    # Checking for head collisions with body segments
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0, 0)
            head.direction = "stop"
            colors = random.choice(['red', 'blue', 'green'])
            shapes = random.choice(['square', 'circle'])
            for segment in segments:
                segment.goto(1000, 1000)
            segments.clear()
            score = 0
            delay = 0.1
            pen.clear()
            pen.write(" Score : {} High Score : {} ".format(
                score, high_score), align="center", font=("candara", 24, "bold"))
    time.sleep(delay)
wn.mainloop()
