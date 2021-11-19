from turtle import Turtle, Screen

screen = Screen()
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self, x_pos, y_pos):
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.snake_body = []
        self.build_snake(3)

    def build_snake(self, size):
        x_coord = self.x_pos
        for i in range(size):
            snake_segment = Turtle("square")
            snake_segment.penup()
            snake_segment.setx(x_coord)
            snake_segment.color("white")
            x_coord -= 20
            self.snake_body.append(snake_segment)
        screen.update()

    def left(self):
        if self.snake_body[0].heading() != RIGHT:
            self.snake_body[0].setheading(LEFT)

    def right(self):
        if self.snake_body[0].heading() != LEFT:
            self.snake_body[0].setheading(RIGHT)

    def up(self):
        if self.snake_body[0].heading() != DOWN:
            self.snake_body[0].setheading(UP)

    def down(self):
        if self.snake_body[0].heading() != UP:
            self.snake_body[0].setheading(DOWN)

    def move(self):
        for segment in range(len(self.snake_body)-1, 0, -1):
            x = self.snake_body[segment - 1].xcor()
            y = self.snake_body[segment - 1].ycor()
            self.snake_body[segment].goto(x, y)
        self.snake_body[0].forward(20)