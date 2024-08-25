from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as file:
            data = int(file.read())
            self.high_score = data
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    #def game_over(self):
    #    self.goto(0, 0)
    #    self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        #self.clear()
        self.score += 1
        self.update_scoreboard()