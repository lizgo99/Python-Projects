from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()

screen.setup(width= 600, height= 600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

screen.listen()

start_snake = Snake()
star_food = Food()
scoreboard = Scoreboard()

def game(snake, food):
    
    screen.onkeypress(snake.up , "Up")
    screen.onkeypress(snake.down , "Down")
    screen.onkeypress(snake.left , "Left")
    screen.onkeypress(snake.right , "Right")
    screen.onkeyrelease(restart_game , "c")
    
    game_is_on = True
    
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        snake.move()
        
        if snake.head.distance(food) < 15 : 
            food.refresh()
            scoreboard.add_point()
            snake.extend()
            
        if snake.head.xcor() > 280 or snake.head.xcor() < -290 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
            game_is_on = False
            scoreboard.best_score_update()
            scoreboard.game_over()
            
        for s in snake.snake[1:]:
            if snake.head.distance(s) < 10:
                game_is_on = False
                scoreboard.best_score_update()
                scoreboard.game_over()
        
                
def restart_game():
    screen.clear()
    screen.bgcolor("black")
    screen.title("SNAKE GAME")
    screen.tracer(0)
    scoreboard.restart()
    new_snake = Snake()
    new_food = Food()
    game(new_snake, new_food)
                
game(start_snake, star_food)

screen.exitonclick()
