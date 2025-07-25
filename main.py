from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

def play_game():
    screen_game.clear()
    screen_game.bgcolor("black")
    screen_game.title("My snake game")
    screen_game.tracer(0)

    snake = Snake()
    food = Food()
    score_ = Score()

    screen_game.listen()
    screen_game.onkey(snake.up, 'Up')
    screen_game.onkey(snake.down, 'Down')
    screen_game.onkey(snake.left, 'Left')
    screen_game.onkey(snake.right, 'Right')

    game_on = True
    while game_on:
        screen_game.update()
        time.sleep(0.1)
        snake.move()

        # Detect collision with food
        pos_x = snake.turtle_[0].xcor()
        pos_y = snake.turtle_[0].ycor()
        if abs(pos_x - food.X_cor) < 15 and abs(pos_y - food.Y_cor) < 15:
            food.food_go()
            snake.make_long()
            score_.score_update()

        # Detect collision with wall
        if abs(pos_x) > 280 or abs(pos_y) > 280:
            game_on = False
            score_.game_over()

        # Detect collision with self
        for segment in snake.turtle_[1:]:
            if snake.turtle_[0].distance(segment) < 10:
                game_on = False
                score_.game_over()

# Setup screen once
screen_game = Screen()
screen_game.setup(width=600, height=600)

# Start first game
play_game()

# Restart mechanism
def restart_game():
    screen_game.onkey(None, "Return")  # Disable the key during execution
    play_game()
    screen_game.onkey(restart_game, "Return")  # Re-enable

screen_game.onkey(restart_game, "Return")
screen_game.listen()
screen_game.mainloop()
