from turtle import Screen, Turtle
from Pong_Paddle import Paddle
from Pong_Ball import Ball
from Pong_Scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width= 800, height= 600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

l_paddle = Paddle((-350,0))
r_paddle = Paddle((350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(r_paddle.go_up , "Up")
screen.onkeypress(r_paddle.go_down , "Down")
screen.onkeypress(l_paddle.go_up , "w")
screen.onkeypress(l_paddle.go_down , "s")

# screen.onkeyrelease(restart_game , "c")

game_is_on = True    
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
               
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    


screen.exitonclick()