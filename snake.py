from turtle import Turtle
from venv import create

# Creación del cuerpo de la serpiente
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]  # Almacenando posiciones
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
# Clase con sus caracteristicas


class Snake:

    # Funcion constructor SELF:sirve para llamar atributos dentro de la misma clase.
    def __init__(self):
        self.segments = []  # Atributo
        self.create_snake()  # Metodo
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:  # Por cada posicion en position se va a ejecutar el recorrido de positions
            snake_segment = Turtle("square")
            snake_segment.color("white")
            snake_segment.penup()
            snake_segment.goto(position)
            self.segments.append(snake_segment)

    def move(self):
        # Movimiento de la serpiente
        # Quiero que me almacene todas las nuevas posiciones
        for seg_num in range(len(self.segments) - 1, 0, - 1):
            # cor = coordenada x coordenada y
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            # movimiento segun las coordenadas que tengo, y aquí debo indicarle donde debe hacer el movimiento, por ende necesita saber la posicion de los cuadritos.
            self.segments[seg_num].goto(new_x, new_y)

        self.head.forward(20)
        # segments[0].left(90)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())

        self.segments.append(new_segment)
