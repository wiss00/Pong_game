from turtle import Turtle, Screen
from paddle import Paddle
from scoreboard import Scoreboard
from ball import Ball
import time
screen = Screen()

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("pong")

screen.tracer(0)

l_paddle = Paddle ((-350, 0))
r_paddle = Paddle((350, 0))
my_ball = Ball()

screen.listen()
screen.onkey(r_paddle.move_up, "Up")
screen.onkey(r_paddle.move_down, "Down")

screen.onkey(l_paddle.move_up, "w")
screen.onkey(l_paddle.move_down, "s")
score=Scoreboard()
game_on = True
speed=0.1
while game_on:
    time.sleep(my_ball.move_speed)
    screen.update()
    my_ball.move()

    #collision with top and bottom walls
    if my_ball.ycor()>280 or my_ball.ycor()<-280:
        my_ball.bounce_y()
    #collision with pallades
    if (my_ball.distance(r_paddle) <50 and my_ball.xcor()>320) or (my_ball.distance(l_paddle) <50 and my_ball.xcor()<-320):
        my_ball.bounce_x()
    #right one misses
    if my_ball.xcor()>350:
        score.l_point()
        my_ball.reset_position()

    #left one misses
    if my_ball.xcor()<-350:
        score.r_point()
        my_ball.reset_position()


screen.exitonclick()
