from turtle import Screen, Turtle, position


# Create a screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title('Programate snake')

position = [(0, 0), (-20, 0), (-40, 0)]

snake = Turtle("square")
snake.color("white")

for coor in position:
    snake.goto(coor)
    snake.stamp()


screen.exitonclick()
