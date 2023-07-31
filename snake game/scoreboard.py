from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Calibri", 18, "normal")
class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("snake game\game_data.txt") as file:
                self.highscore = int(file.read())
        except FileNotFoundError:
            file_create = open("snake game\game_data.txt", "a") 
            file_create.write("0")
            file_create.close()
        # self.highscore = 0
        self.penup()
        self.goto(0,270)
        self.color("white")
        self.hideturtle()
        self.update_score()
        
    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align = ALIGNMENT, font = FONT)

    def point_scored(self):
        self.score += 1
        self.clear()
        self.update_score()

    # def game_over(self):
    #     self.hideturtle()
    #     self.goto(0,0)
    #     self.write("GAME OVER", font=FONT, align= ALIGNMENT)

    def reset_game(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("snake game\game_data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_score()