from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(n=0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        snake.extend()
        food.place_food()
        scoreboard.add_point()

    #Detect collision with wall
    if snake.head.xcor() > 295 or snake.head.xcor() < -295 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        game_is_on = False
        scoreboard.game_over()

#detect collision with the tail
    for body in snake.snake_body[1:]:
        # if body == snake.head:
        #     pass
        if snake.head.distance(body) < 10:
            game_is_on = False
            scoreboard.game_over()
#MY ATTEMPT AT IT
    # for segment in range(1, len(snake.snake_body)-1):
    #     if snake.snake_body[0].pos() == snake.snake_body[segment].pos():
    #         scoreboard.game_over()
    #         game_is_on = False
    
screen.exitonclick()