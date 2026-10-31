"""
Exercises

1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""

from turtle import *

from freegames import line


def grid():
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Draw X player."""
    color('blue')
    width(8)
    line(x, y, x + 133, y + 133)
    line(x, y + 133, x + 133, y)


def drawo(x, y):
    """Draw O player."""
    color('red')
    width(8)
    up()
    goto(x + 66.5, y +66.5 - 45)
    down()
    circle(45)


def floor(value):
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]
board = {}  # casilla (x, y) -> jugador que la ocupa


def tap(x, y):
    """Draw X or O in grid box."""
    x = floor(x)
    y = floor(y)
    cell = (x, y)

    if cell in board:  # casilla ocupada: ignorar el click
        return

    player = state['player']
    draw = players[player]
    draw(x, y)
    board[cell] = player
    update()
    state['player'] = not player
players = [drawx, drawo]



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
