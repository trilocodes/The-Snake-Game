if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False