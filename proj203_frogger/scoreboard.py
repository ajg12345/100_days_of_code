from turtle import Turtle

from constants import FONT, FINISH_LINE_Y, SCREEN_SIZE_WIDE_MIN


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(SCREEN_SIZE_WIDE_MIN + 30, FINISH_LINE_Y - 20)
        self.hideturtle()
        self.write_score()

    def write_score(self):
        score_text = f"Level: {self.level}"
        self.write(score_text, font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.write_score()

    def game_over(self):
        self.goto(0, 0)
        game_over_text = "GAME OVER"
        self.write(game_over_text, align='center', font=FONT)

