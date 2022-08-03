from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("Black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

score = Score()
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        score.score_increase()
    if snake.head.xcor()>295 or snake.head.xcor()< -295 or snake.head.ycor()>295 or snake.head.ycor()<-295:
        game_is_on = False
        score.game_over()
    
    for segments in snake.segments[1:]:
        if snake.head.distance(segments)<10:
            game_is_on = False
            score.game_over()






















screen.exitonclick()