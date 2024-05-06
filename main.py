from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0) #Turns the animation off --> Refresh screen on While Loop

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()


screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.velocity)
    screen.update()  # Refreshes the screen / Animation
    ball.move()

    # Wall Collision
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.reverse_y()

    # paddle collision detection
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320
            or ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.reverse_x()

    # Detect Out of Bounds and reset for Right player, point +1
    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    # Detect OOB and reset for Left Player, +1 point
    if ball.xcor() < -380:
        ball.reset_position()
        score.right_point()







screen.exitonclick()