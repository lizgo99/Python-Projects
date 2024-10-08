from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.goto(-230, 260)
        self.write(f"Level: {self.level}", align= "center", font= ("Courier", 24, "normal"))
        
    def update_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font= ("Courier", 24, "normal"))
        print("aaaaaaa")
        
        
        
