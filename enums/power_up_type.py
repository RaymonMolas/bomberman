from enum import Enum

class PowerUpType(Enum):
    """
    Enumeración que representa los tipos de power-ups disponibles.

    Valores:
    - BOMB: Tipo de power-up que incrementa el número de bombas disponibles, representado por el valor 0.
    - FIRE: Tipo de power-up que incrementa la potencia explosiva de las bombas, representado por el valor 1.
    """

    BOMB = 0
    FIRE = 1

# Comentarios:

# - La clase PowerUpType hereda de Enum, permitiendo la definición de constantes nombradas.

# - Cada miembro de la enumeración tiene un nombre (BOMB, FIRE) y un valor asociado (0, 1).

# - Los comentarios docstring dentro de la clase describen brevemente cada tipo de power-up y su efecto.

# - Esta enumeración podría ser utilizada para representar diferentes tipos de power-ups que un jugador puede recoger en un juego.

# - El uso de Enum en Python proporciona un código más legible y mantenible al asignar nombres descriptivos a valores específicos.

# - Es una práctica común utilizar enumeraciones para representar opciones discretas y limitadas en un programa.

