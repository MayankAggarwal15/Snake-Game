from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()

        with open("highscore.txt" , "r") as data :
            self.high_score = int(data.read())

        self.game_score = -1
        self.color("black")
        self.hideturtle()
        self.speed(0)
        self.penup()
        


    def scoreboard(self):
        self.clear()
        self.game_score += 1
        self.highest_score()

        self.goto(0,320)
        self.string1 = f"SCORE : {self.game_score}"
        self.write(self.string1 , False , "center" , ("Calibri" , 30 , "bold"))

        self.goto(500, 320)
        self.string2 = f"HIGH SCORE : {self.high_score}"
        self.write(self.string2 , False , "center" , ("Calibri" , 30 , "bold"))

        with open("../SNAKE GAME/highscore.txt" , "w") as file :
            file.write(f"{self.high_score}")

    def highest_score(self):
        if self.game_score > self.high_score:
            self.high_score = self.game_score

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER" , False , "center" , ("Cambria" , 30 , "bold"))

    def game_logo(self):
        self.goto(-500,0)
        self.write("S N A K E" , False , "center" , ("Algerian" , 50 , "bold"))
        self.goto(500,0)
        self.write("G A M E" , False , "center" , ("Algerian" , 50 , "bold"))

        
            

    
