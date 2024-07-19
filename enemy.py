import pygame
import random
from bomb import Bomb  # Importación de la clase Bomb desde el módulo bomb
from node import Node  # Importación de la clase Node desde el módulo node
from enums.algorithm import Algorithm  # Importación del enum Algorithm desde enums

class Enemy:

    dire = [[1, 0, 1], [0, 1, 0], [-1, 0, 3], [0, -1, 2]]  # Direcciones: abajo, derecha, arriba, izquierda

    TILE_SIZE = 4  # Tamaño del tile

    def __init__(self, x, y, alg):
        self.life = True  # Vida del enemigo
        self.path = []  # Ruta planificada
        self.movement_path = []  # Ruta de movimiento actual
        self.pos_x = x * Enemy.TILE_SIZE  # Posición X en píxeles
        self.pos_y = y * Enemy.TILE_SIZE  # Posición Y en píxeles
        self.direction = 0  # Dirección de movimiento
        self.frame = 0  # Marco de animación actual
        self.animation = []  # Animaciones disponibles
        self.range = 3  # Alcance del enemigo
        self.bomb_limit = 1  # Límite de bombas que puede colocar
        self.plant = False  # Indicador de si va a plantar una bomba
        self.algorithm = alg  # Algoritmo de movimiento

    def move(self, map, bombs, explosions, enemy):
        # Método para mover al enemigo

        # Realiza el movimiento en la dirección actual
        if self.direction == 0:
            self.pos_y += 1
        elif self.direction == 1:
            self.pos_x += 1
        elif self.direction == 2:
            self.pos_y -= 1
        elif self.direction == 3:
            self.pos_x -= 1

        # Verifica si ha llegado a un nuevo tile completo
        if self.pos_x % Enemy.TILE_SIZE == 0 and self.pos_y % Enemy.TILE_SIZE == 0:
            self.movement_path.pop(0)
            self.path.pop(0)
            # Si todavía hay más nodos en la ruta planificada, verifica el siguiente nodo
            if len(self.path) > 1:
                grid = self.create_grid(map, bombs, explosions, enemy)
                next = self.path[1]
                if grid[next[0]][next[1]] > 1:
                    self.movement_path.clear()
                    self.path.clear()

        # Gestiona el cambio de marco de animación
        if self.frame == 2:
            self.frame = 0
        else:
            self.frame += 1

    def make_move(self, map, bombs, explosions, enemy):
        # Método para ejecutar el movimiento del enemigo

        if not self.life:
            return
        
        # Si no hay camino de movimiento actual, determina uno nuevo
        if len(self.movement_path) == 0:
            if self.plant:
                bombs.append(self.plant_bomb(map))
                self.plant = False
                map[int(self.pos_x / Enemy.TILE_SIZE)][int(self.pos_y / Enemy.TILE_SIZE)] = 3
            if self.algorithm is Algorithm.DFS:
                self.dfs(self.create_grid(map, bombs, explosions, enemy))
            else:
                self.dijkstra(self.create_grid_dijkstra(map, bombs, explosions, enemy))

        else:
            # Si hay un camino de movimiento, mueve al enemigo en esa dirección
            self.direction = self.movement_path[0]
            self.move(map, bombs, explosions, enemy)

    def plant_bomb(self, map):
        # Método para plantar una bomba en la posición actual del enemigo

        b = Bomb(self.range, round(self.pos_x / Enemy.TILE_SIZE), round(self.pos_y / Enemy.TILE_SIZE), map, self)
        self.bomb_limit -= 1
        return b

    def check_death(self, exp):
        # Método para verificar si el enemigo está en una posición de una explosión y morir

        for e in exp:
            for s in e.sectors:
                if int(self.pos_x / Enemy.TILE_SIZE) == s[0] and int(self.pos_y / Enemy.TILE_SIZE) == s[1]:
                    self.life = False
                    return

    def dfs(self, grid):
        # Método de búsqueda en profundidad (Depth-First Search) para determinar la ruta de movimiento

        new_path = [[int(self.pos_x / Enemy.TILE_SIZE), int(self.pos_y / Enemy.TILE_SIZE)]]
        depth = 0
        if self.bomb_limit == 0:
            self.dfs_rec(grid, 0, new_path, depth)
        else:
            self.dfs_rec(grid, 2, new_path, depth)

        self.path = new_path

    def dfs_rec(self, grid, end, path, depth):
        # Función recursiva para la búsqueda en profundidad

        last = path[-1]
        if depth > 200:
            return
        
        # Manejo de los diferentes tipos de casillas en el grid
        if grid[last[0]][last[1]] == 0 and end == 0:
            return
        elif end == 2:
            if grid[last[0] + 1][last[1]] == end or grid[last[0] - 1][last[1]] == end \
                    or grid[last[0]][last[1] + 1] == end \
                    or grid[last[0]][last[1] - 1] == end:
                if len(path) == 1 and end == 2:
                    self.plant = True
                return

        grid[last[0]][last[1]] = 9

        random.shuffle(self.dire)

        # Evalúa las direcciones posibles de movimiento y las agrega a la ruta
        for direction in self.dire:
            if grid[last[0] + direction[0]][last[1] + direction[1]] == 0:
                path.append([last[0] + direction[0], last[1] + direction[1]])
                self.movement_path.append(direction[2])

        # Si ninguna dirección es segura, elimina el último nodo de la ruta
        if len(self.movement_path) > 0:
            path.pop(0)
            self.movement_path.pop(0)

        depth += 1
        self.dfs_rec(grid, end, path, depth)

    def dijkstra(self, grid):
        # Método de búsqueda de Dijkstra para determinar la ruta de movimiento

        end = 1
        if self.bomb_limit == 0:
            end = 0

        visited = []
        open_list = []
        current = grid[int(self.pos_x / Enemy.TILE_SIZE)][int(self.pos_y / Enemy.TILE_SIZE)]
        current.weight = current.base_weight
        new_path = []
        
        while True:
            visited.append(current)
            random.shuffle(self.dire)
            
            # Condiciones de salida para Dijkstra
            if (current.value == end and end == 0) or\
                    (end == 1 and (grid[current.x+1][current.y].value == 1 or grid[current.x-1][current.y].value == 1 or
                grid[current.x][current.y+1].value == 1 or grid[current.x][current.y-1].value == 1)):
                new_path.append([current.x, current.y])
                while True:
                    if current.parent is None:
                        break
                    current = current.parent
                    new_path.append([current.x, current.y])
                new_path.reverse()
                for xd in range(len(new_path)):
                    if new_path[xd] is not new_path[-1]:
                        if new_path[xd][0] - new_path[xd+1][0] == -1:
                            self.movement_path.append(1)
                        elif new_path[xd][0] - new_path[xd + 1][0] == 1:
                            self.movement_path.append(3)
                        elif new_path[xd][1] - new_path[xd + 1][1] == -1:
                            self.movement_path.append(0)
                        elif new_path[xd][1] - new_path[xd + 1][1] == 1:
                            self.movement_path.append(2)
                if len(new_path) == 1 and end == 1:
                    self.plant = True
                self.path = new_path
                return

            # Explora las celdas adyacentes para determinar el siguiente nodo
            for i in range(len(self.dire)):
                if current.x + self.dire[i][0] < len(grid) and current.y + self.dire[i][1] < len(grid):
                    if grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].reach \
                            and grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]] not in visited:
                        if grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]] in open_list:
                            if grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].weight >\
                                    grid[current.x][current.y].weight \
                                    + grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].base_weight:
                                grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].parent = current
                                grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].weight = current.weight + grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].base_weight
                                grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].direction = self.dire[i][2]

                        else:
                            grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].parent = current
                            grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].weight =\
                                current.weight + grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].base_weight
                            grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]].direction = self.dire[i][2]
                            open_list.append(grid[current.x + self.dire[i][0]][current.y + self.dire[i][1]])

            # Si no quedan nodos en la lista abierta, establece la posición actual como el único nodo en el camino
            if len(open_list) == 0:
                self.path = [[int(self.pos_x / Enemy.TILE_SIZE), int(self.pos_y / Enemy.TILE_SIZE)]]
                return

            # Elige el siguiente nodo con el menor peso como nodo actual
            next_node = open_list[0]
            for n in open_list:
                if n.weight < next_node.weight:
                    next_node = n
            open_list.remove(next_node)
            current = next_node

    def create_grid(self, map, bombs, explosions, enemys):
        # Método para crear el grid de navegación para el algoritmo DFS

        grid = [[0] * len(map) for r in range(len(map))]

        # 0 - seguro
        # 1 - inseguro
        # 2 - destruible
        # 3 - inaccesible

        # Marca las casillas según los elementos del mapa, bombas, explosiones y otros enemigos
        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]] = 1
            grid[b.pos_x][b.pos_y] = 3

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]] = 3

        for i in range(len(map)):
            for j in range(len(map[i])):
                if map[i][j] == 1:
                    grid[i][j] = 3
                elif map[i][j] == 2:
                    grid[i][j] = 2

        for x in enemys:
            if x == self:
                continue
            elif not x.life:
                continue
            else:
                grid[int(x.pos_x / Enemy.TILE_SIZE)][int(x.pos_y / Enemy.TILE_SIZE)] = 2

        return grid

    def create_grid_dijkstra(self, map, bombs, explosions, enemys):
        # Método para crear el grid de navegación para el algoritmo de Dijkstra

        grid = [[None] * len(map) for r in range(len(map))]

        # 0 - seguro
        # 1 - destruible
        # 2 - inaccesible
        # 3 - inseguro

        # Inicializa el grid con objetos Node según el tipo de casilla en el mapa
        for i in range(len(map)):
            for j in range(len(map)):
                if map[i][j] == 0:
                    grid[i][j] = Node(i, j, True, 1, 0)
                elif map[i][j] == 2:
                    grid[i][j] = Node(i, j, False, 999, 1)
                elif map[i][j] == 1:
                    grid[i][j] = Node(i, j, False, 999, 2)
                elif map[i][j] == 3:
                    grid[i][j] = Node(i, j, False, 999, 2)

        # Marca las casillas afectadas por bombas y explosiones como inaccesibles
        for b in bombs:
            b.get_range(map)
            for x in b.sectors:
                grid[x[0]][x[1]].weight = 5
                grid[x[0]][x[1]].value = 3
            grid[b.pos_x][b.pos_y].reach = False

        for e in explosions:
            for s in e.sectors:
                grid[s[0]][s[1]].reach = False

        # Marca las posiciones de otros enemigos como inaccesibles
        for x in enemys:
            if x == self:
                continue
            elif not x.life:
                continue
            else:
                grid[int(x.pos_x / Enemy.TILE_SIZE)][int(x.pos_y / Enemy.TILE_SIZE)].reach = False
                grid[int(x.pos_x / Enemy.TILE_SIZE)][int(x.pos_y / Enemy.TILE_SIZE)].value = 1

        return grid

    def load_animations(self, en, scale):
        # Método para cargar las animaciones del enemigo

        front = []
        back = []
        left = []
        right = []
        resize_width = scale
        resize_height = scale

        # Carga de imágenes para cada dirección y animación
        image_path = 'images/enemy/e'
        if en == '':
            image_path = 'images/hero/p'

        f1 = pygame.image.load(image_path + en + 'f0.png')
        f2 = pygame.image.load(image_path + en + 'f1.png')
        f3 = pygame.image.load(image_path + en + 'f2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        front.append(f1)
        front.append(f2)
        front.append(f3)

        r1 = pygame.image.load(image_path + en + 'r0.png')
        r2 = pygame.image.load(image_path + en + 'r1.png')
        r3 = pygame.image.load(image_path + en + 'r2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        right.append(r1)
        right.append(r2)
        right.append(r3)

        b1 = pygame.image.load(image_path + en + 'b0.png')
        b2 = pygame.image.load(image_path + en + 'b1.png')
        b3 = pygame.image.load(image_path + en + 'b2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        back.append(b1)
        back.append(b2)
        back.append(b3)

        l1 = pygame.image.load(image_path + en + 'l0.png')
        l2 = pygame.image.load(image_path + en + 'l1.png')
        l3 = pygame.image.load(image_path + en + 'l2.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))

        left.append(l1)
        left.append(l2)
        left.append(l3)

        self.animation.append(front)
        self.animation.append(right)
        self.animation.append(back)
        self.animation.append(left)