from turtle import Turtle
import random
FOOD_COLORS = ["blue", "red", "yellow", "green", "purple", "orange"]

class Food(Turtle):
    """Food class inherited from Turtle class.
    No need to create a food object from Turtle inside the __init__"""
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color(random.choice(FOOD_COLORS))
        self.speed(0)
        self.new_pos()

    def change_color(self):
        self.color(random.choice(FOOD_COLORS))

    def new_pos(self):
        x_cor = random.randint(-260, 260)
        y_cor = random.randint(-260, 260)
        self.goto(x_cor, y_cor)