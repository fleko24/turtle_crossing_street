from turtle import Turtle

STEP = 20
INITIAL_Y_POSITION = -240

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.setheading(90)
        self.color("green")
        self.goto(0, INITIAL_Y_POSITION)

    def move_forward(self):
        new_y = self.ycor() + STEP
        self.goto(self.xcor(), new_y)

    def move_back(self):
        if self.ycor() >= INITIAL_Y_POSITION:
            new_y = self.ycor() - STEP
            self.goto(self.xcor(), new_y)

    def back_to_initial_position(self):
        self.goto(0, INITIAL_Y_POSITION)

