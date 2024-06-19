
from turtle import Screen,bgpic
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
score_board = Scoreboard()
bgpic("bg.gif")

# -------TODO :-------------  ADD THE BRICK BACKGORUND   -------------------------------
# screen.setup(width=600,height=600)
# -----------------------------  This makes it fullscreen   -------------------------------
screen.screensize()
screen.setup(width = 1.0, height = 1.0)
canvas = screen.getcanvas()
root = canvas.winfo_toplevel()
root.overrideredirect(1)
#------------------------------------------------------------------------------------------

screen.bgcolor("#03002b")
screen.title("The Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.05)
    snake.move()

    # Collision with food
    if snake.head.distance(food) <16:
        food.refresh()
        snake.grow()
        score_board.increase_score()
        
    score_board.update_score()

    # Collision with wall
    if snake.head.xcor() > 840 or snake.head.xcor() <-840 or snake.head.ycor() > 520 or snake.head.ycor() <-520:
        score_board.reset()
        snake.reset()
    # Collision of head with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score_board.reset()
            snake.reset()   
            

screen.exitonclick()







