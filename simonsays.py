from random import choice
from time import sleep
from turtle import update, onscreenclick, setup, hideturtle, tracer, done
from freegames import floor, square, vector

pattern = []
tsl = 0.5
guesses = []
tiles = {
    vector(0, 0): ('red', 'dark red'),
    vector(0, -200): ('blue', 'dark blue'),
    vector(-200, 0): ('green', 'dark green'),
    vector(-200, -200): ('yellow', 'khaki'),
    vector(200, 0): ('purple', 'violet'),
    vector(200, -200): ('gray', 'black'),
    # Se agregan 2 nuevas baldosas que se encontrarán
    # al lado derecho de la roja y azul.
}


def grid():
    "Draw grid of tiles."
    square(0, 0, 200, 'dark red')
    square(0, -200, 200, 'dark blue')
    square(-200, 0, 200, 'dark green')
    square(-200, -200, 200, 'khaki')
    # Se agregan los colores de 'apagado' de las nuevas baldosas.
    square(200, 0, 200, 'violet')
    square(200, -200, 200, 'black')
    update()


def flash(tile):
    "Flash tile in grid."
    glow, dark = tiles[tile]
    square(tile.x, tile.y, 200, glow)
    update()
    """
    Con el tiempo, la velocidad en la que saldrán los colores aumentará,
    para que esta no sea abrupta, la velocidad irá cambiando lentamente.
    Se debe de recalcar que, el límite que el programa tendrá será cuando
    el valor de la variable tsl = 0
    """
    sleep(tsl-(len(guesses)*0.01))
    square(tile.x, tile.y, 200, dark)
    update()
    sleep(tsl-(len(guesses)*0.01))


def grow():
    "Grow pattern and flash tiles."
    tile = choice(list(tiles))
    pattern.append(tile)

    for tile in pattern:
        flash(tile)

    print('Pattern length:', len(pattern))
    guesses.clear()


def tap(x, y):
    "Respond to screen tap."
    onscreenclick(None)
    x = floor(x, 200)
    y = floor(y, 200)
    tile = vector(x, y)
    index = len(guesses)

    if tile != pattern[index]:
        exit()

    guesses.append(tile)
    flash(tile)

    if len(guesses) == len(pattern):
        grow()

    onscreenclick(tap)


def start(x, y):
    "Start game."
    grow()
    onscreenclick(tap)


setup(0.60, 0.50, None, None)
hideturtle()
tracer(False)
grid()
onscreenclick(start)
done()
