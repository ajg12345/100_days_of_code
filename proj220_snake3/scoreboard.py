from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.write_score()
    
    def read_high_score(self) -> int:
        with open('high_score.txt', 'r') as f:
            score = f.readline()
        return 0 if not score else int(score)

    def write_high_score(self) -> None:
        with open('high_score.txt', 'w') as f:
            f.write(str(self.score))

    def write_score(self):
        self.clear()
        score_text = f"Score: {self.score} High Score: {self.high_score}"
        self.write(score_text, align='center', font=('Arial', 12, 'bold'))
    
    def score_up(self):
        self.score += 1
        self.write_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.score = 0
        self.write_score()

    #def game_over(self):
        #self.goto(0, 0)
        #score_text = "GAME OVER"
        #self.write(score_text, align='center', font=('Arial', 12, 'bold'))