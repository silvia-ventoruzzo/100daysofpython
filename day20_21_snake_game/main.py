from turtle import Turtle, Screen
import time
from day20_21_snake_game.snake import Snake
from day20_21_snake_game.food import Food
from day20_21_snake_game.scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)

# Step 1: Create the snake body
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
    
screen.update()
    
# Part 3: Control the snake
screen.onkeypress(fun=snake.up, key='Up')
screen.onkeypress(fun=snake.down, key='Down')
screen.onkeypress(fun=snake.right, key='Right')
screen.onkeypress(fun=snake.left, key='Left')

# Step 2: Move the snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
# Part 4: Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
# Part 5: Create a scoreboard
        scoreboard.increase()

# Part 6: Detect a collision with the wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

screen.exitonclick()
