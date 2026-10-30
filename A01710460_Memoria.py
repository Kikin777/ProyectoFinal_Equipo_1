"""Memory, puzzle game of number pairs.

Exercises:

1. Count and print how many taps occur.
2. Decrease the number of tiles to a 4x4 grid.
3. Detect when all tiles are revealed.
4. Center single-digit tile.
5. Use letters instead of tiles.
"""

from random import *
from turtle import *

from freegames import path

car = path('car.gif')

# Geometria del tablero: SIDE x SIDE casillas de SIZE pixeles cada una
SIDE = 6
SIZE = 60
OFFSET = SIDE * SIZE // 2
COUNT = SIDE * SIDE

tiles = list(range(COUNT // 2)) * 2
state = {'mark': None, 'pairs': 0}
hide = [True] * COUNT


def square(x, y):
    "Draw white square with black outline at (x, y)."
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
    "Convert (x, y) coordinates to tiles index."
    return int((x + OFFSET) // SIZE + ((y + OFFSET) // SIZE) * SIDE)


def xy(count):
    "Convert tiles count to (x, y) coordinates."
    return (count % SIDE) * SIZE - OFFSET, (count // SIDE) * SIZE - OFFSET


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
        state['pairs'] += 1  # se acaba de descubrir un par


def draw():
    "Draw image and tiles."
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
    goto(-OFFSET, OFFSET + 10)
    color('black')
    write('Pares: {} de {}'.format(state['pairs'], COUNT // 2),
          font=('Arial', 14, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
