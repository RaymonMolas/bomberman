import unittest

# Importación de módulos y clases del juego
import game
from bomb import Bomb
from enemy import Enemy
from player import Player
from enums.algorithm import Algorithm

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada prueba
        game.enemy_list.append(Enemy(11, 11, Algorithm.DFS))  # Agrega un enemigo a la lista
        game.player = Player()  # Crea un jugador

    def test_plant(self):
        # Prueba para la función de plantar bomba del jugador
        bomb = game.player.plant_bomb(game.GRID_BASE)

        # Verifica las coordenadas y el rango de la bomba plantada
        self.assertEqual(1, bomb.pos_x)
        self.assertEqual(1, bomb.pos_y)
        self.assertEqual(3, bomb.range)

    def test_get_range(self):
        # Prueba para verificar los sectores alcanzados por la bomba

        bomb = game.player.plant_bomb(game.GRID_BASE)  # Plantar una bomba para la prueba

        # Verifica si los sectores esperados están en la lista de sectores
        self.assertEqual(5, len(bomb.sectors))
        self.assertEqual(True, [1, 1] in bomb.sectors)
        self.assertEqual(True, [1, 2] in bomb.sectors)
        self.assertEqual(True, [2, 1] in bomb.sectors)
        self.assertEqual(True, [1, 3] in bomb.sectors)
        self.assertEqual(True, [3, 1] in bomb.sectors)

        # Verifica que los sectores no esperados no estén en la lista
        self.assertEqual(False, [1, 0] in bomb.sectors)
        self.assertEqual(False, [0, 1] in bomb.sectors)

    def test_bomb_explode(self):
        # Prueba para verificar la explosión de una bomba

        temp_bomb = Bomb(3, 11, 11, game.GRID_BASE, game.enemy_list[0])  # Crea una bomba temporal
        game.bombs.append(temp_bomb)  # Agrega la bomba a la lista de bombas del juego

        game.update_bombs(game.GRID_BASE, 2980)  # Actualiza las bombas con un tiempo alto

        # Verifica que la bomba aún esté presente y su tiempo restante
        self.assertEqual(1, len(game.bombs))
        self.assertEqual(20, temp_bomb.time)

        game.update_bombs(game.GRID_BASE, 50)  # Actualiza las bombas con un tiempo bajo

        # Verifica que la bomba haya explotado y que haya una explosión registrada
        self.assertEqual(0, len(game.bombs))
        self.assertEqual(1, len(game.explosions))

if __name__ == '__main__':
    unittest.main()
