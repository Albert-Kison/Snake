from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup screen
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

# Initialize game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.update()

# Listen to the key press
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
score = 0
speed = 0.3     # speed of the snake moving

# main game loop
while game_is_on:
    screen.update()
    time.sleep(speed)

    snake.move()

    # if the snake eats the food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        speed -= 0.01

    # if the snake collides with the borders
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        speed = 0.3

    # if the snake collides with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()










screen.exitonclick()
