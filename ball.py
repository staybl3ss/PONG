from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setpos((0, 0))
        self.x_change = 10
        self.y_change = 10
        self.velocity = 0.1

    def move(self):
        self.setx(self.xcor() + self.x_change)
        self.sety(self.ycor() + self.y_change)

    def reverse_y(self):
        self.y_change *= -1

    def reverse_x(self):
        self.x_change *= -1
        self.velocity *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.velocity = 0.1
        self.reverse_x()

