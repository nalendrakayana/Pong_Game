from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.create_paddle(x_pos, y_pos)
    
    def create_paddle(self, x_pos, y_pos):
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x_pos, y_pos)
    
    def up(self):
        y_cor = self.ycor() + 20
        self.goto(self.xcor(), y_cor)
    
    def down(self):
        y_cor = self.ycor() - 20
        self.goto(self.xcor(), y_cor)
    
    
        