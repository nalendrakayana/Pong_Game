import turtle as t
from paddle import Paddle
from ball import Ball
from score import Score
import time

screen = t.Screen()

screen.listen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()
score = Score()

screen.onkeypress(r_paddle.up, "Up")
screen.onkeypress(r_paddle.down, "Down")
screen.onkeypress(l_paddle.up, "w")
screen.onkeypress(l_paddle.down, "s")

game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)  
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.y_bounce()
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.x_bounce()
    if ball.xcor() > 380: 
        ball.ball_reset()
        score.l_point()
    if ball.xcor() < -380:
        ball.ball_reset()
        score.r_point()
    































screen.exitonclick()