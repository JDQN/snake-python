from turtle import Screen
from scoreboard import Scoreboard
from snake import Snake
from food import Food
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

screen.tracer(0)

snake = Snake()


scoreboard  = Scoreboard()
scoreboard.draw_scoreboard()


food = Food()

#Snake movement
screen.listen()
screen.onkey(snake.up,"Up") #accion que se va a ejecuta y tipo de tecla que se va a mover
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


#set game state
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.2)


    snake.move()

    if snake.head.distance(food) < 20:
        snake.add_segment()
        scoreboard.add_score(1)
        food.refresh()

    #Check collision with border
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False


    #Check collision with body
    for segment in snake.segments:
        if segment != snake.head and segment.distance(snake.head) < 20:
            game_is_on = False



while not game_is_on:
    scoreboard.game_over()
