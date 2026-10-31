"""Tic Tac Toe

Ejercicios originales:

1. Dar a la X y a la O un color y tamaño diferentes.
2. ¿Qué pasa cuando alguien toca una casilla ocupada?
3. ¿Cómo detectarías cuando alguien ha ganado?
4. ¿Cómo podrías crear un jugador controlado por la computadora?
"""

from turtle import *

from freegames import line

# Coordenadas de inicio de las 3 columnas/filas del tablero.
# Cada casilla mide 133 px y el tablero va de -200 a 200.
CELLS = (-200, -67, 66)

# Nombre que se muestra en pantalla para cada jugador (0 = X, 1 = O)
NAMES = ['X', 'O']

# Las 8 combinaciones ganadoras: 3 columnas, 3 filas y 2 diagonales
LINES = []
for a in CELLS:
    LINES.append([(a, b) for b in CELLS])  # columna completa
    LINES.append([(b, a) for b in CELLS])  # fila completa
LINES.append([(c, c) for c in CELLS])  # diagonal principal
LINES.append([(CELLS[i], CELLS[2 - i]) for i in range(3)])  # diagonal inversa


def grid():
    """Dibuja la cuadrícula del tablero."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):
    """Dibuja la X del jugador 1."""
    color('blue')  # MODIFICACIÓN 1: X en color azul
    width(8)  # MODIFICACIÓN 1: trazo más grueso
    # La casilla mide 133 px; con márgenes de 25 px la X queda centrada
    line(x + 25, y + 25, x + 108, y + 108)
    line(x + 25, y + 108, x + 108, y + 25)


def drawo(x, y):
    """Dibuja la O del jugador 2."""
    color('red')  # MODIFICACIÓN 1: O en color rojo
    width(8)  # MODIFICACIÓN 1: trazo más grueso
    up()
    # circle() dibuja desde el punto más bajo del círculo, por eso se resta
    # el radio (45) para que el centro quede en el centro de la casilla
    goto(x + 66.5, y + 66.5 - 45)
    down()
    circle(45)
    up()


# 'player': jugador en turno (0 = X, 1 = O)
# 'over': True cuando el juego terminó (ya hay ganador o empate)
state = {'player': 0, 'over': False}
players = [drawx, drawo]

# MODIFICACIÓN 2: registra las casillas ocupadas.
# Guarda {(x, y): jugador} para saber quién ocupó cada casilla.
board = {}


def floor(value):
    """Redondea hacia abajo al inicio de la casilla (cuadros de 133)."""
    return ((value + 200) // 133) * 133 - 200


def winner():
    """Regresa el jugador ganador (0 o 1), o None si aún no hay."""
    for a, b, c in LINES:
        # Las tres casillas deben estar ocupadas por el mismo jugador
        if a in board and b in board and c in board:
            if board[a] == board[b] == board[c]:
                return board[a]
    return None


def show_message(text):
    """Escribe un mensaje arriba del tablero."""
    up()
    goto(0, 205)
    color('black')
    write(text, align='center', font=('Arial', 18, 'bold'))
    update()


def tap(x, y):
    """Dibuja X u O en la casilla donde se hizo clic."""
    # MODIFICACIÓN 3: si el juego ya terminó, se ignoran los clics
    if state['over']:
        return

    x = floor(x)
    y = floor(y)

    # Ignora clics fuera del tablero
    if x not in CELLS or y not in CELLS:
        return

    cell = (x, y)

    # MODIFICACIÓN 2: si la casilla ya está ocupada, no se hace nada
    # y el turno no cambia
    if cell in board:
        return

    player = state['player']
    players[player](x, y)  # dibuja la X o la O según el turno
    board[cell] = player  # marca la casilla como ocupada
    update()

    # MODIFICACIÓN 3: revisa si hay ganador o empate
    result = winner()
    if result is not None:
        show_message(f'¡Ganó {NAMES[result]}!')
        state['over'] = True
    elif len(board) == 9:  # las 9 casillas llenas y sin ganador
        show_message('¡Empate!')
        state['over'] = True
    else:
        state['player'] = int(not player)  # cambia el turno


# Ventana un poco más alta (470) para dejar espacio al mensaje de resultado
setup(420, 470, 370, 0)
hideturtle()
tracer(False)
grid()
update()
onscreenclick(tap)
done()
