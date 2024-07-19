from enum import Enum

class Algorithm(Enum):
    """
    Enumeración que representa diferentes algoritmos.

    Valores:
    - DFS: Algoritmo de búsqueda en profundidad, representado por el valor 0.
    - DIJKSTRA: Algoritmo de Dijkstra, representado por el valor 1.
    - PLAYER: Algoritmo asociado al jugador, representado por el valor 2.
    - NONE: Valor nulo o sin algoritmo específico, representado por el valor 3.
    """

    DFS = 0
    DIJKSTRA = 1
    PLAYER = 2
    NONE = 3

# Comentarios:

# - La clase Algorithm hereda de Enum, permitiendo la definición de un conjunto de constantes nombradas.

# - Cada miembro de la enumeración tiene un nombre (DFS, DIJKSTRA, PLAYER, NONE) y un valor asociado (0, 1, 2, 3).

# - Los nombres y valores están definidos explícitamente para proporcionar claridad y consistencia en el código.

# - Los comentarios docstring dentro de la clase describen brevemente cada valor de la enumeración y su significado.

# - Esta enumeración podría ser utilizada para representar diferentes tipos de algoritmos en un contexto específico de la aplicación o juego.

# - El uso de Enum en Python permite un código más legible y mantenible al asignar nombres descriptivos a valores específicos.

# - Es una buena práctica en Python utilizar enumeraciones para representar conjuntos de opciones discretas y limitadas.

