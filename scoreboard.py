from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Times New Roman', 20, 'normal')

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.goto(0,270)
        self.pencolor("white")
        self.show_score()
        

    def show_score(self):
        self.write(arg=f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)
    
    def add_point(self):
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        self.goto(0,0)
        self.write(arg=f"    GAME OVER\nYOU KINDA SUCK", move=False, align=ALIGNMENT, font=FONT)