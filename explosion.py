from enums.power_up_type import PowerUpType
from power_up import PowerUp

class Explosion:
    
    bomber = None  # Variable estática para almacenar al jugador que colocó la bomba

    def __init__(self, x, y, r):
        """
        Inicializa una explosión en una posición específica con un rango dado.

        Args:
            x (int): Posición x de la explosión.
            y (int): Posición y de la explosión.
            r (int): Rango de la explosión.
        """
        self.sourceX = x  # Posición x de origen de la explosión
        self.sourceY = y  # Posición y de origen de la explosión
        self.range = r    # Rango de la explosión
        self.time = 300   # Tiempo de vida de la explosión
        self.frame = 0    # Frame actual de la explosión
        self.sectors = []  # Sectores afectados por la explosión

    def explode(self, map, bombs, b, power_ups):
        """
        Realiza la explosión en el mapa y gestiona sus efectos.

        Args:
            map (list): Matriz que representa el mapa del juego.
            bombs (list): Lista de bombas en el juego.
            b (Bomb): Bomba que explota.
            power_ups (list): Lista de power-ups en el juego.
        """
        self.bomber = b.bomber  # Establece al jugador que colocó la bomba como bomber
        self.sectors.extend(b.sectors)  # Extiende los sectores afectados por la explosión con los de la bomba b
        bombs.remove(b)  # Elimina la bomba b de la lista de bombas
        self.bomb_chain(bombs, map, power_ups)  # Inicia la reacción en cadena de explosiones

    def bomb_chain(self, bombs, map, power_ups):
        """
        Realiza la reacción en cadena de explosiones a partir de los sectores afectados por la explosión.

        Args:
            bombs (list): Lista de bombas en el juego.
            map (list): Matriz que representa el mapa del juego.
            power_ups (list): Lista de power-ups en el juego.
        """
        for s in self.sectors:
            for x in power_ups:
                if x.pos_x == s[0] and x.pos_y == s[1]:
                    power_ups.remove(x)  # Elimina el power-up si está en el mismo sector que la explosión

            for x in bombs:
                if x.pos_x == s[0] and x.pos_y == s[1]:
                    map[x.pos_x][x.pos_y] = 0  # Elimina la bomba del mapa
                    x.bomber.bomb_limit += 1  # Incrementa el límite de bombas del jugador que colocó la bomba
                    self.explode(map, bombs, x, power_ups)  # Realiza una nueva explosión en la bomba x

    def clear_sectors(self, map, random, power_ups):
        """
        Limpia los sectores afectados por la explosión en el mapa y genera posibles power-ups.

        Args:
            map (list): Matriz que representa el mapa del juego.
            random (module): Módulo random para generar números aleatorios.
            power_ups (list): Lista de power-ups en el juego.
        """
        for i in self.sectors:
            if map[i[0]][i[1]] == 2:  # Si el sector es de tipo caja
                r = random.randint(0, 9)  # Genera un número aleatorio entre 0 y 9
                if r == 0:
                    power_ups.append(PowerUp(i[0], i[1], PowerUpType.BOMB))  # Añade un power-up de bomba
                elif r == 1:
                    power_ups.append(PowerUp(i[0], i[1], PowerUpType.FIRE))  # Añade un power-up de fuego

            map[i[0]][i[1]] = 0  # Limpia el sector en el mapa

    def update(self, dt):
        """
        Actualiza el tiempo restante de vida de la explosión y ajusta el frame de la animación.

        Args:
            dt (int): Delta de tiempo desde la última actualización.
        """
        self.time = self.time - dt  # Actualiza el tiempo restante de la explosión

        if self.time < 100:
            self.frame = 2  # Si queda menos de 100ms, establece el frame 2 (última fase de la explosión)
        elif self.time < 200:
            self.frame = 1  # Si queda menos de 200ms, establece el frame 1 (segunda fase de la explosión)
