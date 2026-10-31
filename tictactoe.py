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


state = {'player': 0, 'over': False}
players = [drawx, drawo]
board = {}  # casilla (x, y) -> jugador que la ocupa

CELLS = (-200, -67, 66)  # coordenadas de las 3 columnas/filas
NAMES = ['X', 'O']

# Las 8 combinaciones ganadoras
LINES = []
for a in CELLS:
    LINES.append([(a, b) for b in CELLS])  # columnas
    LINES.append([(b, a) for b in CELLS])  # filas
LINES.append([(c, c) for c in CELLS])  # diagonal
LINES.append([(CELLS[i], CELLS[2 - i]) for i in range(3)])  # otra diagonal


def winner():
    """Return winning player (0 or 1) or None."""
    for a, b, c in LINES:
        if a in board and b in board and c in board:
            if board[a] == board[b] == board[c]:
                return board[a]
    return None


def show_message(text):
    """Write message above the board."""
    up()
    goto(0, 205)
    color('black')
    write(text, align='center', font=('Arial', 18, 'bold'))
    update()


def tap(x, y):
    """Draw X or O in grid box."""
    if state['over']:  # juego terminado: ignorar clicks
        return

    x = floor(x)
    y = floor(y)

    if x not in CELLS or y not in CELLS:  # click fuera del tablero
        return

    cell = (x, y)
    if cell in board:
        return

    player = state['player']
    players[player](x, y)
    board[cell] = player
    update()

    result = winner()
    if result is not None:
        show_message(f'¡Ganó {NAMES[result]}!')
        state['over'] = True
    elif len(board) == 9:
        show_message('¡Empate!')
        state['over'] = True
    else:
        state['player'] = int(not player)
players = [drawx, drawo]



setup(420, 420, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
