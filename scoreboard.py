from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("White")
        self.penup()
        self.goto(0,270)
        self.write(f"Score: {self.score}",align= ALIGNMENT,font= FONT )
        self.hideturtle()
    
    def score_increase(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}",align= ALIGNMENT,font= FONT )
    
    def game_over(self):
        self.goto(0,0)
        self.write(f"Game OVER",align= ALIGNMENT,font= FONT )
