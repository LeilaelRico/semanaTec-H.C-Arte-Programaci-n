"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.

"""

from turtle import up, goto, down, color, begin_fill, forward, onscreenclick
from turtle import left, end_fill, clear, shape, stamp, write, done
from turtle import update, ontimer, setup, addshape, hideturtle, tracer
from random import shuffle
from freegames import path

car = path('earth.gif')
tiles = list(range(21)) * 2 #el numero y su multiplicacion (ejemplo cuntos valores del primero van a existir)
state = {'mark': None}
hide = [True] * 42 #tiene que ser igual que la linea 20


def square(x, y):
    "Draw white square with black outline at (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(75)
        left(90)
    end_fill()


def index(x, y):
    "Convert (x, y) coordinates to tiles index."
    return int((x + 263) // 75 + ((y + 225) // 75) * 7) #segundo y cuarto valor tamano del cubo, primer y tercer valor posicion del cubo y ultimo valor es fila y columna
# posicion x entre menos mas a la derecha, es igaul en y

def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % 7) * 75 - 263, (count // 7) * 75 - 225 #segundo y cuarto valor tamano del cubo, tercer y ultimo valor posicion del cubo y primer y cuarto valor es fila y columna


def tap(x, y):
    "Update mark and hidden tiles based on tap."
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None


def draw():
    "Draw image and tiles."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(42): #tiene que ser igual que la linea 20
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(700, 600, 370, 0) #posicion y tamano del canvas
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
