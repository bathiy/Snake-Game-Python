from turtle import Turtle

position_list = [0, -20, -40]


class Snake:
    def __init__(self):
        self.turtle_ = []
        self.snake_initiate()

    def snake_initiate(self):
        for position in position_list:
            segmant = Turtle()
            segmant.color("white")
            segmant.penup()
            segmant.shape("square")
            segmant.setposition(x=position, y=0)
            self.turtle_.append(segmant)

    def move(self):
        for number in range(len(self.turtle_)-1, 0, -1):
            self.turtle_[number].goto(self.turtle_[number - 1].position())
        self.turtle_[0].forward(20)

    def up(self):
        if self.turtle_[0].heading() != 270:
            self.turtle_[0].setheading(90)

    def down(self):
        if self.turtle_[0].heading() != 90:
            self.turtle_[0].setheading(270)

    def right(self):
        if self.turtle_[0].heading() != 180:
            self.turtle_[0].setheading(0)

    def left(self):
        if self.turtle_[0].heading() != 0:
            self.turtle_[0].setheading(180)

    def make_long(self):
        segmant = Turtle()
        segmant.color("white")
        segmant.penup()
        segmant.shape("square")
        segmant.setposition(x=self.turtle_[-1].position()[0], y=self.turtle_[-1].position()[1])
        self.move()
        self.turtle_.append(segmant)