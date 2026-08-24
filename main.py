from turtle import Screen
import time

from ball import Ball
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)  #Non aggiornare automaticamente lo schermo.

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.1) #to see the ball is going slowly
    screen.update()
    ball.move()

screen.exitonclick()
