from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40,0)]# (-60,0), (-80,0), (-100,0), (-120,0), (-140,0), (-160,0)]
MOVE_DISTANCE = 20
RIGHT = 0
UP = 90
LEFT = 180
DOWN = 270

class Snake():
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_snake_body(position)
            

#add a new segment to the snake
    def add_snake_body(self,position):
        turtle = Turtle(shape = "square")
        turtle.color("white")
        turtle.penup()
        turtle.goto(position)
        self.snake_body.append(turtle)

    def extend(self):
        self.add_snake_body(self.snake_body[-1].position())

#my try at it
        # turtle = Turtle(shape = "square")
        # turtle.hideturtle()
        # turtle.color("yellow")
        # turtle.penup()
        # self.snake_body.append(turtle)
    
    def move(self):
        for turtle in self.snake_body:
            turtle.showturtle()
        for segment_num in range(len(self.snake_body) - 1,0,-1):
            new_x = self.snake_body[segment_num - 1].xcor()
            new_y = self.snake_body[segment_num - 1].ycor()
            self.snake_body[segment_num].goto(new_x, new_y)    
        self.snake_body[0].forward(MOVE_DISTANCE)
        #print(self.head.heading())

    def right(self):
        if not self.head.heading() == LEFT:
            self.head.setheading(RIGHT)
        else: 
            print("Cannot go in reverse")

    def up(self):
        if not self.head.heading() == DOWN:
            self.head.setheading(UP)
        else: 
            print("Cannot go in reverse")

    def left(self):
        if not self.head.heading() == RIGHT:
            self.head.setheading(LEFT)
        else: 
            print("Cannot go in reverse")

    def down(self):
        if not self.head.heading() == UP:
            self.head.setheading(DOWN)
        else: 
            print("Cannot go in reverse")
