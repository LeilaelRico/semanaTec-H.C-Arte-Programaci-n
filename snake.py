from turtle import update, clear, ontimer, setup, hideturtle, done
from turtle import tracer, listen, onkey
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
# Se añade vector que cambiará el color de la serpiente y
# fruta en cada nueva partida.
color = ['black', 'green', 'orange', 'blue', 'yellow', 'pink']
# Las funciones se encargarán de que los colores sean aleatorios.
snakeColor = color[randrange(0, 5)]
fruitColor = color[randrange(0, 5)]


if fruitColor == snakeColor:
    """
    Para evitar que el color se repita en la serpiente
    y fruta, se hace uso de esta condición.
    """
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
    """
    La serpiente se irá moviendo más rápido
    conforme esta aumente su tamaño, esto se logra
    haciendo que al valor del ontimer se le reste el
    dato que posee en longitud.
    """
    ontimer(move, 100-(10+len(snake)))
    # El límite del juego se encuentra cuando este valor llegue a 0.


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
