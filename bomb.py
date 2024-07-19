class Bomb:
    frame = 0  # Marco de la animación de la bomba

    def __init__(self, r, x, y, map, bomber):
        self.range = r  # Alcance de la bomba
        self.pos_x = x  # Posición x de la bomba en el mapa
        self.pos_y = y  # Posición y de la bomba en el mapa
        self.time = 3000  # Tiempo restante antes de que la bomba explote (en milisegundos)
        self.bomber = bomber  # Jugador que colocó la bomba
        self.sectors = []  # Lista de sectores afectados por la explosión
        self.get_range(map)  # Calcular los sectores afectados por la explosión según el mapa proporcionado

    def update(self, dt):
        # Método para actualizar el estado de la bomba con el paso del tiempo

        self.time = self.time - dt  # Restar el tiempo transcurrido desde la última actualización

        # Cambiar el marco de la animación dependiendo del tiempo restante
        if self.time < 1000:
            self.frame = 2
        elif self.time < 2000:
            self.frame = 1

    def get_range(self, map):
        # Método para determinar los sectores afectados por la explosión de la bomba

        self.sectors.append([self.pos_x, self.pos_y])  # Agregar la posición actual de la bomba a los sectores afectados

        # Comprobar los sectores en dirección horizontal hacia la derecha
        for x in range(1, self.range):
            if map[self.pos_x + x][self.pos_y] == 1:  # Si encuentra un obstáculo sólido, detenerse
                break
            elif map[self.pos_x + x][self.pos_y] == 0 or map[self.pos_x + x][self.pos_y] == 3:
                self.sectors.append([self.pos_x + x, self.pos_y])  # Agregar sector si es espacio vacío o un objeto que puede destruirse
            elif map[self.pos_x + x][self.pos_y] == 2:  # Si encuentra un obstáculo indestructible, detenerse
                self.sectors.append([self.pos_x + x, self.pos_y])
                break

        # Comprobar los sectores en dirección horizontal hacia la izquierda
        for x in range(1, self.range):
            if map[self.pos_x - x][self.pos_y] == 1:
                break
            elif map[self.pos_x - x][self.pos_y] == 0 or map[self.pos_x - x][self.pos_y] == 3:
                self.sectors.append([self.pos_x - x, self.pos_y])
            elif map[self.pos_x - x][self.pos_y] == 2:
                self.sectors.append([self.pos_x - x, self.pos_y])
                break

        # Comprobar los sectores en dirección vertical hacia arriba
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y + x] == 1:
                break
            elif map[self.pos_x][self.pos_y + x] == 0 or map[self.pos_x][self.pos_y + x] == 3:
                self.sectors.append([self.pos_x, self.pos_y + x])
            elif map[self.pos_x][self.pos_y + x] == 2:
                self.sectors.append([self.pos_x, self.pos_y + x])
                break

        # Comprobar los sectores en dirección vertical hacia abajo
        for x in range(1, self.range):
            if map[self.pos_x][self.pos_y - x] == 1:
                break
            elif map[self.pos_x][self.pos_y - x] == 0 or map[self.pos_x][self.pos_y - x] == 3:
                self.sectors.append([self.pos_x, self.pos_y - x])
            elif map[self.pos_x][self.pos_y - x] == 2:
                self.sectors.append([self.pos_x, self.pos_y - x])
                break
