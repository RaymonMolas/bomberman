import pygame
import math

from bomb import Bomb
from enums.power_up_type import PowerUpType

class Player:
    pos_x = 4  # Posición inicial en el eje x
    pos_y = 4  # Posición inicial en el eje y
    direction = 0  # Dirección inicial del jugador
    frame = 0  # Frame actual de la animación
    animation = []  # Lista de animaciones
    rango = 3  # Alcance inicial de las bombas del jugador
    bomb_limit = 1  # Límite inicial de bombas que puede plantar

    TILE_SIZE = 4  # Tamaño del tile en el mapa

    def __init__(self):
        self.life = True  # Estado de vida del jugador

    def move(self, dx, dy, grid, enemigos, power_ups):
        tempx = int(self.pos_x / Player.TILE_SIZE)
        tempy = int(self.pos_y / Player.TILE_SIZE)

        mapa = []

        # Copia el grid para evitar modificaciones no deseadas
        for i in range(len(grid)):
            mapa.append([])
            for j in range(len(grid[i])):
                mapa[i].append(grid[i][j])

        # Marca las posiciones de los enemigos en el mapa
        for enemigo in enemigos:
            if enemigo == self:
                continue
            elif not enemigo.life:
                continue
            else:
                mapa[int(enemigo.pos_x / Player.TILE_SIZE)][int(enemigo.pos_y / Player.TILE_SIZE)] = 2

        # Ajuste de posición si el jugador está entre tiles
        if self.pos_x % Player.TILE_SIZE != 0 and dx == 0:
            if self.pos_x % Player.TILE_SIZE == 1:
                self.pos_x -= 1
            elif self.pos_x % Player.TILE_SIZE == 3:
                self.pos_x += 1
            return
        if self.pos_y % Player.TILE_SIZE != 0 and dy == 0:
            if self.pos_y % Player.TILE_SIZE == 1:
                self.pos_y -= 1
            elif self.pos_y % Player.TILE_SIZE == 3:
                self.pos_y += 1
            return

        # Movimiento hacia la derecha
        if dx == 1:
            if mapa[tempx + 1][tempy] == 0:
                self.pos_x += 1
        # Movimiento hacia la izquierda
        elif dx == -1:
            tempx = math.ceil(self.pos_x / Player.TILE_SIZE)
            if mapa[tempx - 1][tempy] == 0:
                self.pos_x -= 1

        # Movimiento hacia abajo
        if dy == 1:
            if mapa[tempx][tempy + 1] == 0:
                self.pos_y += 1
        # Movimiento hacia arriba
        elif dy == -1:
            tempy = math.ceil(self.pos_y / Player.TILE_SIZE)
            if mapa[tempx][tempy - 1] == 0:
                self.pos_y -= 1

        # Verifica si el jugador consume un power-up al moverse sobre él
        for power_up in power_ups:
            if power_up.pos_x == math.ceil(self.pos_x / Player.TILE_SIZE) \
                    and power_up.pos_y == math.ceil(self.pos_y / Player.TILE_SIZE):
                self.consumir_power_up(power_up, power_ups)

    def plant_bomb(self, mapa):
        # Crea una bomba en la posición del jugador
        bomba = Bomb(self.rango, round(self.pos_x / Player.TILE_SIZE), round(self.pos_y / Player.TILE_SIZE), mapa, self)
        return bomba

    def check_death(self, explosiones):
        # Verifica si el jugador muere al estar en una posición de una explosión
        for explosion in explosiones:
            for sector in explosion.sectors:
                if int(self.pos_x / Player.TILE_SIZE) == sector[0] and int(self.pos_y / Player.TILE_SIZE) == sector[1]:
                    self.life = False

    def consumir_power_up(self, power_up, power_ups):
        # Aplica los efectos del power-up consumido por el jugador
        if power_up.type == PowerUpType.BOMB:
            self.bomb_limit += 1
        elif power_up.type == PowerUpType.FIRE:
            self.rango += 1

        # Elimina el power-up consumido de la lista
        power_ups.remove(power_up)

    def load_animations(self, escala):
        # Carga las animaciones del jugador con el tamaño especificado
        frente = []
        espalda = []
        izquierda = []
        derecha = []
        resize_width = escala
        resize_height = escala

        f1 = pygame.image.load('images/hero/pf0.png')
        f2 = pygame.image.load('images/hero/pf1.png')
        f3 = pygame.image.load('images/hero/pf2.png')

        f1 = pygame.transform.scale(f1, (resize_width, resize_height))
        f2 = pygame.transform.scale(f2, (resize_width, resize_height))
        f3 = pygame.transform.scale(f3, (resize_width, resize_height))

        frente.append(f1)
        frente.append(f2)
        frente.append(f3)

        r1 = pygame.image.load('images/hero/pr0.png')
        r2 = pygame.image.load('images/hero/pr1.png')
        r3 = pygame.image.load('images/hero/pr2.png')

        r1 = pygame.transform.scale(r1, (resize_width, resize_height))
        r2 = pygame.transform.scale(r2, (resize_width, resize_height))
        r3 = pygame.transform.scale(r3, (resize_width, resize_height))

        derecha.append(r1)
        derecha.append(r2)
        derecha.append(r3)

        b1 = pygame.image.load('images/hero/pb0.png')
        b2 = pygame.image.load('images/hero/pb1.png')
        b3 = pygame.image.load('images/hero/pb2.png')

        b1 = pygame.transform.scale(b1, (resize_width, resize_height))
        b2 = pygame.transform.scale(b2, (resize_width, resize_height))
        b3 = pygame.transform.scale(b3, (resize_width, resize_height))

        espalda.append(b1)
        espalda.append(b2)
        espalda.append(b3)

        l1 = pygame.image.load('images/hero/pl0.png')
        l2 = pygame.image.load('images/hero/pl1.png')
        l3 = pygame.image.load('images/hero/pl2.png')

        l1 = pygame.transform.scale(l1, (resize_width, resize_height))
        l2 = pygame.transform.scale(l2, (resize_width, resize_height))
        l3 = pygame.transform.scale(l3, (resize_width, resize_height))

        izquierda.append(l1)
        izquierda.append(l2)
        izquierda.append(l3)

        self.animation.append(frente)
        self.animation.append(derecha)
        self.animation.append(espalda)
        self.animation.append(izquierda)
