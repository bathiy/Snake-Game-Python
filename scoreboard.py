from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setposition(0, 270)
        self.color("white")
        self.penup()
        self.write(f"Score : {self.score}", move=False, align='center', font=('Arial', 13, 'normal'))
        self.hideturtle()

    def score_update(self):
        self.score += 1
        self.clear()
        self.write(f"Score : {self.score}", move=False, align='center', font=('Arial', 13, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over! Press Enter to restart", align="center", font=("Arial", 20, "bold"))