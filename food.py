from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.penup()
        self.speed("fastest")
        self.color("blue")
        self.X_cor = random.randint(-280, 280)
        self.Y_cor = random.randint(-280, 250)
        self.goto(self.X_cor, self.Y_cor)

    def food_go(self):
        self.X_cor = random.randint(-280, 280)
        self.Y_cor = random.randint(-280, 250)
        self.goto(self.X_cor, self.Y_cor)