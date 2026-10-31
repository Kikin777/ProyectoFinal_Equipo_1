"""Memoria, juego de pares de numeros.

Modificaciones realizadas:

1. Contador de pares descubiertos en pantalla.
2. Deteccion del fin de la partida.
3. Tablero reducido a una cuadricula de 6x6.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Geometria del tablero: SIDE x SIDE casillas de SIZE pixeles cada una.
# SIDE * SIZE debe cubrir los 400 px de la imagen para que no se asome.
SIDE = 6
SIZE = 66
OFFSET = SIDE * SIZE // 2
COUNT = SIDE * SIDE

tiles = list(range(COUNT // 2)) * 2
state = {'mark': None, 'pairs': 0}
hide = [True] * COUNT


def square(x, y):
    "Dibuja un cuadro blanco con borde negro en (x, y)."
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(SIZE)
        left(90)
    end_fill()


def index(x, y):
    "Convierte coordenadas (x, y) al indice de la casilla."
    return int((x + OFFSET) // SIZE + ((y + OFFSET) // SIZE) * SIDE)


def xy(count):
    "Convierte el indice de una casilla a coordenadas (x, y)."
    return (count % SIDE) * SIZE - OFFSET, (count // SIDE) * SIZE - OFFSET


def tap(x, y):
    "Actualiza la marca y las casillas ocultas segun el clic."
    # Los clics fuera del tablero se ignoran
    if not (-OFFSET <= x < OFFSET and -OFFSET <= y < OFFSET):
        return

    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        state['pairs'] += 1  # se acaba de descubrir un par


def draw():
    "Dibuja la imagen, las casillas y el marcador."
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(COUNT):
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

    # Marcador arriba del tablero con los pares descubiertos
    up()
    goto(-OFFSET, OFFSET + 8)
    color('black')
    write('Pares: {} de {}'.format(state['pairs'], COUNT // 2),
          font=('Arial', 14, 'normal'))

    # La partida termina cuando ya no queda ninguna casilla oculta
    if not any(hide):
        up()
        goto(OFFSET, OFFSET + 8)
        color('red')
        write('Ganaste!', align='right', font=('Arial', 16, 'bold'))
        update()
        return

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(440, 470, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
