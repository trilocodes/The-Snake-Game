from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0,480)
        self.write(f"Score: {self.score} High Score: {self.score}",align="center", font=("Impact", 24, "normal"))
        self.hideturtle()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode = "a") as file:
                file.truncate(0)
                file.write(str(self.high_score))
        self.score = 0
        self.update_score()

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER",align="center", font=("Impact", 50, "normal"))

    def update_score(self):
        self.clear() 
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.write(f"Score: {self.score} High Score: {self.high_score}",align="center", font=("Impact", 24, "normal"))
    
    def increase_score(self):
        self.score += 1
