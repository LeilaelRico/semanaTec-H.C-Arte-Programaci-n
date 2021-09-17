"""
Tamanos
Win condition
Dificulad y niveles
Cambio de imagenes
menu
"""

from turtle import up, goto, down, color, begin_fill, forward, onscreenclick
from turtle import left, end_fill, clear, shape, stamp, write, done
from turtle import update, ontimer, setup, addshape, hideturtle, tracer
from random import shuffle
from freegames import path


def baby():
    car = path('pamomitas.gif')
    # el numero y su multiplicacion (1 tiene 2 2 tiene 2)
    tiles = list(range(3)) * 4
    state = {'mark': None}
    # tiene que ser igual que la linea 20
    hide = [True] * 12

    def square(x, y):
        "Draw white square with black outline at (x, y)."
        up()
        goto(x, y)
        down()
        color('black', 'white')
        begin_fill()
        for count in range(4):
            forward(60)
            left(90)
        end_fill()

    def index(x, y):
        "Convert (x, y) coordinates to tiles index."
        return int((x + 120) // 60 + ((y + 90) // 60) * 4)
    # segundo y cuarto valor tamano del cubo, primer y tercer valor posicion
    #  del cubo y ultimo valor es fila y columna
    # posicion x entre menos mas a la derecha, es igaul en y

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 4) * 60 - 120, (count // 4) * 60 - 90
    # segundo y cuarto valor tamano del cubo, tercer y
    # ultimo valor posicion del cubo
    # y primer y cuarto valor es fila y columna

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if spot == 11:
                print("You Win")
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

    # tiene que ser igual que la linea 20
        for count in range(12):
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
    # posicion y tamano del canvas
    setup(280, 230, 770, 300)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()


def easy():
    car = path('TrashPanda.gif')
    # el numero y su multiplicacion (1 tiene 2 2 tiene 2)
    tiles = list(range(12)) * 2
    state = {'mark': None}
    # tiene que ser igual que la linea 20
    hide = [True] * 24

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
        return int((x + 145) // 75 + ((y + 200) // 65) * 4)
    # segundo y cuarto valor tamano del cubo, primer y tercer valor posicion
    #  del cubo y ultimo valor es fila y columna
    # posicion x entre menos mas a la derecha, es igaul en y

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 4) * 75 - 145, (count // 4) * 65 - 200
    # segundo y cuarto valor tamano del cubo, tercer y
    # ultimo valor posicion del cubo
    # y primer y cuarto valor es fila y columna

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if spot == 23:
                print("You Win")
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

    # tiene que ser igual que la linea 20
        for count in range(24):
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
    # posicion y tamano del canvas
    setup(355, 440, 570, 200)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()


def medium():
    car = path('earth.gif')
    # el numero y su multiplicacion (1 tiene 2 2 tiene 2)
    tiles = list(range(21)) * 2
    state = {'mark': None}
    # tiene que ser igual que la linea 20
    hide = [True] * 42

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
        return int((x + 263) // 75 + ((y + 225) // 75) * 7)
    # segundo y cuarto valor tamano del cubo, primer y tercer valor posicion
    #  del cubo y ultimo valor es fila y columna
    # posicion x entre menos mas a la derecha, es igaul en y

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 7) * 75 - 263, (count // 7) * 75 - 225
    # segundo y cuarto valor tamano del cubo, tercer y
    # ultimo valor posicion del cubo
    # y primer y cuarto valor es fila y columna

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if spot == 41:
                print("You Win")
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

    # tiene que ser igual que la linea 20
        for count in range(42):
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
    # posicion y tamano del canvas
    setup(550, 480, 370, 0)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()


def hard():
    car = path('mario.gif')
    # el numero y su multiplicacion (1 tiene 2 2 tiene 2)
    tiles = list(range(40)) * 2
    state = {'mark': None}
    # tiene que ser igual que la linea 20
    hide = [True] * 80

    def square(x, y):
        "Draw white square with black outline at (x, y)."
        up()
        goto(x, y)
        down()
        color('black', 'white')
        begin_fill()
        for count in range(4):
            forward(47)
            left(90)
        end_fill()

    def index(x, y):
        "Convert (x, y) coordinates to tiles index."
        return int((x + 235) // 47 + ((y + 180) // 45) * 10)
    # segundo y cuarto valor tamano del cubo, primer y tercer valor posicion
    #  del cubo y ultimo valor es fila y columna
    # posicion x entre menos mas a la derecha, es igaul en y

    def xy(count):
        "Convert tiles count to (x, y) coordinates."
        return (count % 10) * 47 - 235, (count // 10) * 45 - 180
    # segundo y cuarto valor tamano del cubo, tercer y
    # ultimo valor posicion del cubo
    # y primer y cuarto valor es fila y columna

    def tap(x, y):
        "Update mark and hidden tiles based on tap."
        spot = index(x, y)
        mark = state['mark']

        if mark is None or mark == spot or tiles[mark] != tiles[spot]:
            state['mark'] = spot
            if spot == 79:
                print("You Win")
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

    # tiene que ser igual que la linea 20
        for count in range(80):
            if hide[count]:
                x, y = xy(count)
                square(x, y)

        mark = state['mark']

        if mark is not None and hide[mark]:
            x, y = xy(mark)
            up()
            goto(x + 2, y)
            color('black')
            write(tiles[mark], font=('Arial', 22, 'normal'))

        update()
        ontimer(draw, 100)

    shuffle(tiles)
    # posicion y tamano del canvas
    setup(500, 380, 370, 0)
    addshape(car)
    hideturtle()
    tracer(False)
    onscreenclick(tap)
    draw()
    done()


def menu():
    print("1. Baby Puzzle")
    print("2. Easy Puzzle")
    print("3. Medium Puzzle")
    print("4. Hard Puzzle")
    print("5. Exit")


def main():
    continua = True
    while continua:
        menu()
        opcion = int(input("Introduce una opcion: "))
        if opcion == 1:
            baby()
        elif opcion == 2:
            easy()
        elif opcion == 3:
            medium()
        elif opcion == 4:
            hard()
        elif opcion == 5:
            print("Adios")
            continua = False
        else:
            print("Opcion_invalida")


main()
