from turtle import Turtle
# ALIGNMENT = "center"
# FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.best_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-75, 270)
        self.write(f"Score: {self.score}", align= "center", font= ("Arial", 24, "normal"))
        self.goto(75, 270)
        self.write(f"Best Score: {self.best_score}", align= "center", font= ("Arial", 24, "normal"))
        
    
    def add_point(self):
        self.score += 1
        self.update_scoreboard()
        
    def game_over(self): 
        self.update_scoreboard()
        self.goto(0,0)
        self.write("GAME OVER", align= "center", font= ("Arial", 24, "normal"))
        self.goto(0,-30)
        self.write("Start again?", align= "center", font= ("Arial", 24, "normal"))
        self.goto(0,-50)
        self.write("press c ", align= "center", font= ("Arial", 24, "normal"))
        
    def restart(self): 
        self.score = 0
        self.update_scoreboard()
        
    def best_score_update(self):
        if self.score > self.best_score:
            self.best_score = self.score
        
        
        
        
        