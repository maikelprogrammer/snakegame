from turtle import Turtle,Screen
import random
import time

screen=Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("THE SNAKE GAME")
screen.tracer(0)

from turtle import Turtle
POSITIONS=[(0,0),(-20,0),(-40,0)]
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:

    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self):
        for position in POSITIONS:
            self.add_segment(position)

    def add_segment(self,position):
            tim=Turtle("square")
            tim.color("red")
            tim.penup()
            tim.goto(position)
            self.segments.append(tim)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for num_seg in range(len(self.segments)-1,0,-1):
            new_x=self.segments[num_seg-1].xcor()
            new_y = self.segments[num_seg - 1].ycor()
            self.segments[num_seg].goto(new_x,new_y)
        self.head.forward(20)

    def move_up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading()!=UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.penup()
        self.move_random()

    def move_random(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(-230,260)
        self.increase_score()

    def increase_score(self):
        self.clear()
        self.write(f"score:{self.score}", align="center", font=("courier", 20, "normal"))

    def add_score(self):
        self.score+=1
        self.increase_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("courier", 20, "normal"))

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(snake.move_up,"Up")
screen.onkey(snake.move_down,"Down")
screen.onkey(snake.move_left,"Left")
screen.onkey(snake.move_right,"Right")


game_is_on=True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    snake.move()

    if snake.head.distance(food)<15:
        food.move_random()
        snake.extend()
        score.add_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        game_is_on=False
        score.game_over()

    for num_seg in snake.segments:
        if num_seg==snake.head:
            pass
        elif snake.head.distance(num_seg)<10:
            game_is_on=False
            score.game_over()

screen.exitonclick()

