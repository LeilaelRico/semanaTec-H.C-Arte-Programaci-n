import turtle
"""
 cambiar la aceleracion de la bola
 First to 5 
"""
def pong(name1, score_a, name2, score_b):
    # Canvas
    win = turtle.Screen()
    win.title("Pong")
    win.bgcolor("black")
    win.setup(width=800, height=600)
    win.tracer(0)
    rootwindow = win.getcanvas().winfo_toplevel()
    rootwindow.call('wm', 'attributes', '.', '-topmost', '1')
    rootwindow.call('wm', 'attributes', '.', '-topmost', '0')
    score_a = 0
    score_b = 0
    square_size = 20
    linea_posicion = 0
    turtle.color("gray")
    turtle.shape("square")
    turtle.shapesize(stretch_wid=3, stretch_len=1)
    turtle.penup()
    for i in range(6):
        turtle.setpos(linea_posicion, (250-(i*square_size*5)))
        turtle.stamp()

    # Barra Izquierda
    barra_Izq = turtle.Turtle()
    barra_Izq.speed(0)
    barra_Izq.shape("square")
    barra_Izq.color("white")
    barra_Izq.shapesize(stretch_wid=5, stretch_len=1)
    barra_Izq.penup()
    barra_Izq.goto(-350, 0)

    # Barra Derecha
    barra_Der = turtle.Turtle()
    barra_Der.speed(0)
    barra_Der.shape("square")
    barra_Der.color("white")
    barra_Der.shapesize(stretch_wid=5, stretch_len=1)
    barra_Der.penup()
    barra_Der.goto(350, 0)

    # Bola
    bola = turtle.Turtle()
    bola.speed(0)
    bola.shape("circle")
    bola.color("white")
    bola.penup()
    bola.goto(0, 0)
    bola.dx = 0.9
    bola.dy = 0.9


    # Score
    Dscore = turtle.Turtle()

    Dscore.color("white")
    Dscore.penup()
    Dscore.hideturtle()
    Dscore.goto(0, 250)
    Dscore.write("{}: 0           {}: 0".format(name1, name2), align="center", font=("Arial", 24, "normal"))
    # Intrucciones
    Tutorial = turtle.Turtle()
    Tutorial.color("gray")
    Tutorial.penup()
    Tutorial.hideturtle()
    Tutorial.goto(0, -250)
    Tutorial.write("Player A: 'w' 's'                Player B: '↑' '↓'", align="center", font=("Arial", 16, "normal"))
    esc = turtle.Turtle()
    esc.color("gray")
    esc.penup()
    esc.hideturtle()
    esc.goto(-350, -290)
    esc.write("Press esc to quit")

    # Funciones
    def barra_Izq_up():
        y = barra_Izq.ycor()
        y += 40
        barra_Izq.sety(y)

    def barra_Izq_down():
        y = barra_Izq.ycor()
        y -= 40
        barra_Izq.sety(y)

    def barra_Der_up():
        y = barra_Der.ycor()
        y += 40
        barra_Der.sety(y)

    def barra_Der_down():
        y = barra_Der.ycor()
        y -= 40
        barra_Der.sety(y)

    # Keyboard bindings
    win.listen()
    win.onkeypress(barra_Izq_up, "w") or win.onkeypress(barra_Izq_up, "W")
    win.onkeypress(barra_Izq_down, "s") or win.onkeypress(barra_Izq_down, "S")
    win.onkeypress(barra_Der_up, "Up")
    win.onkeypress(barra_Der_down, "Down")

    # Game loop
    continua = True
    while continua:
        win.update()

        # Movimiento bola
        bola.setx(bola.xcor()+bola.dx)
        bola.sety(bola.ycor()+bola.dy)
        win.listen()
        win.onkey(salir, "Escape")
        # Canvas Border
        if bola.ycor() > 290:
            bola.sety(290)
            bola.dy *= -1

        elif bola.ycor() < -290:
            bola.sety(-290)
            bola.dy *= -1

        elif bola.xcor() > 390:
            bola.goto(0, 0)
            bola.dx *= -1
            score_a += 1
            Dscore.clear()
            Dscore.write("{}: {}           {}: {}".format(name1, score_a, name2, score_b), align="center", font=("Arial", 24, "normal"))

        elif bola.xcor() < -390:
            bola.goto(0, 0)
            bola.dx *= -1
            score_b += 1
            Dscore.clear()
            Dscore.write("{}: {}           {}: {}".format(name1, score_a, name2, score_b), align="center", font=("Arial", 24, "normal"))

        # Colisiones
        elif bola.xcor() > 340 and (bola.ycor() < barra_Der.ycor() + 40 and bola.ycor() > barra_Der.ycor() - 40):
            bola.setx(340)
            bola.dx *= -1

        elif bola.xcor() < -340 and (bola.ycor() < barra_Izq.ycor() + 40 and bola.ycor() > barra_Izq.ycor() - 40):
            bola.setx(-340)
            bola.dx *= -1

        elif score_a >= 5:
            turtle.clearscreen()
            WinA = turtle.Turtle()

            WinA.color("black")
            WinA.penup()
            WinA.hideturtle()
            WinA.goto(0, 0)
            WinA.write("{} WINS!".format(name1), align="center", font=("Arial", 24, "normal"))

        elif score_b >= 5:
            turtle.clearscreen()
            WinB = turtle.Turtle()

            WinB.color("black")
            WinB.penup()
            WinB.hideturtle()
            WinB.goto(0, 0)
            WinB.write("{} WINS!".format(name2), align="center", font=("Arial", 24, "normal"))


def crea_matriz(name1, score_a, name2, score_b):
    matriz = [[name1, score_a], [name2, score_b]]
    return matriz


def imprime_matriz(matriz):
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            print(matriz[i][j], end="    ")
        print()


def salir():
    turtle.bye()



def main():
    continua = True
    while continua:
        name1 = str(input("First player name: "))
        name2 = str(input("Second player name: "))
        score_a = 0
        score_b = 0
        m = crea_matriz(name1, score_a, name2, score_b)
        imprime_matriz(m)
        pong(name1, score_a, name2, score_b)


main()
