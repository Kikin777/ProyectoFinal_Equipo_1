# ProyectoFinal_Equipo_1
Proyecto Final en equipo: Enrique Rios Rosas, Annie Michelle van Zijl Astorga A01710941, Paris Medina Rivera

Pacman:
cambios...

Memoria:
## Enrique Rios Rosas — A01710460

**Juego modificado:** Memoria (`A01710460_Memoria.py`)
**Rama de trabajo:** `A01710460_Memoria`

### Descripción del juego

Juego de memoria en el que se destapan casillas por pares. Al hacer clic sobre
una casilla se revela su número; si el siguiente clic descubre un número igual,
ambas casillas quedan destapadas y muestran parte de la imagen de fondo. Si no
coinciden, se vuelven a ocultar.

### Modificaciones realizadas

1. **Contador de pares descubiertos.** Se agregó la llave `pairs` al diccionario
   de estado del juego, que se incrementa cada vez que dos casillas coinciden.
   El total se dibuja como marcador en la parte superior del tablero con el
   formato `Pares: X de Y`.

2. **Detección del fin de la partida.** En cada ciclo de dibujado se revisa si
   queda alguna casilla oculta. Cuando ya no hay ninguna, se muestra el mensaje
   de victoria al centro de la pantalla y se detiene el ciclo de `ontimer` con
   un `return`, de modo que el mensaje permanece fijo.

3. **Cambio del número de casillas.** El tablero original de 8x8 casillas de
   50 px estaba escrito con valores fijos repartidos en varias funciones. Se
   sustituyeron por las constantes `SIDE`, `SIZE`, `OFFSET` y `COUNT`, con lo
   que el tablero quedó en una cuadrícula de 6x6 y su tamaño ahora se controla
   desde un solo lugar.

4. **Traducción de comentarios.** Los docstrings y comentarios del código
   original se tradujeron al español para unificar el idioma del archivo.

### Proceso seguido

Se clonó el repositorio y se creó la rama `A01710460_Memoria` a partir de
`main`. El juego se descargó con `python3 -m freegames copy memory` y se renombró
el archivo. Cada modificación se trabajó y registró en un commit independiente
siguiendo el formato Conventional Commits. Al terminar, la rama se fusionó a
`main` mediante merge.

### Ejecución

```
python3 -m venv .venv
source .venv/bin/activate
pip install freegames
python A01710460_Memoria.py
```

Ticatactoe:
cambios...
