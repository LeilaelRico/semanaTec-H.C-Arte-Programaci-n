from turtle import update, clear, ontimer, setup, hideturtle, done
from turtle import tracer, listen, onkey
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
color = ['black', 'green', 'orange', 'blue', 'yellow', 'pink']
snakeColor = color[randrange(0, 5)]
fruitColor = color[randrange(0, 5)]


if fruitColor == snakeColor:
    fruitColor = color[randrange(0, 5)]


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, snakeColor)

    square(food.x, food.y, 9, fruitColor)
    update()
    "Changed to make the snake move faster"
    ontimer(move, 100-(10+len(snake)))


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(5, 0), 'Right')
onkey(lambda: change(-5, 0), 'Left')
onkey(lambda: change(0, 5), 'Up')
onkey(lambda: change(0, -5), 'Down')
move()
done()
