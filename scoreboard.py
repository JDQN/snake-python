import turtle


class Scoreboard:
    def __init__(self):
        self.score = 0
        self.lives = 3
        self.level = 1

    def add_score(self, points):
        self.score += points
        self.update_scoreboard()

    def add_life(self):
        self.lives += 1

    def remove_life(self):
        self.lives -= 1

    def next_level(self):
        self.level += 1

    def get_score(self):
        return self.score

    def get_lives(self):
        return self.lives

    def get_level(self):
        return self.level

    def reset_score(self):
        self.score = 0
        self.update_scoreboard()

    #draw scoreboard using turtle
    def draw_scoreboard(self):
        #create scoreboard
        self.score_turtle = turtle.Turtle()
        self.score_turtle.hideturtle()
        self.score_turtle.speed(0)
        self.score_turtle.color("white")
        self.score_turtle.penup()
        self.score_turtle.setposition(-290, 280)
        self.score_turtle.write("Score: 0  Lives: 3  Level: 1", False, align="left", font=("Arial", 14, "normal"))

    def update_scoreboard(self):
        self.score_turtle.clear()
        self.score_turtle.write("Score: {}  Lives: {}  Level: {}".format(self.score, self.lives, self.level), False, align="left", font=("Arial", 14, "normal"))

    def game_over(self):
        self.score_turtle.clear()
        self.score_turtle.setposition(0, 0)
        self.score_turtle.write("Game Over", False, align="center", font=("Arial", 30, "normal"))