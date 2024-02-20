from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = {"left": 0, "right": 0}
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()
    
    def write_score(self):
        score_text = f"{self.score['left']}   {self.score['right']}"
        self.write(score_text, align='center', font=('Arial', 20, 'bold'))
    
    def score_up(self, side: str):
        self.score[side] += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        score_text = "GAME OVER"
        self.write(score_text, align='center', font=('Arial', 12, 'bold'))