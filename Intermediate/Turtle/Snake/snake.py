from turtle import Turtle
STARTING_POSITIONS = [(0,0) , (-20,0) ,(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
        
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_tail(pos)
            
        
    def move(self):
        for s in range(len(self.snake) - 1 , 0 , -1):
            new_x = self.snake[s-1].xcor()
            new_y = self.snake[s-1].ycor()
            self.snake[s].goto(new_x , new_y)
        self.snake[0].forward(MOVE_DISTANCE)
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    
    def add_tail(self,pos):
            snake_part = Turtle("square")
            snake_part.color("white")
            snake_part.penup()
            snake_part.goto(pos)
            self.snake.append(snake_part)
    
    def extend(self):
        self.add_tail(self.snake[-1].position())
        
    def restart(self):
        self.snake = []
        self.create_snake()
        
    # def del_snake(self):
    #     for s in self.snake:
    #         s.hideturtle()
        
    
    