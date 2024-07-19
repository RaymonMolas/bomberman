import unittest
import game

from enemy import Enemy
from player import Player
from enums.algorithm import Algorithm

class MyTestCase(unittest.TestCase):

    def setUp(self):
        # Configuración inicial para cada prueba
        game.enemy_list.append(Enemy(11, 11, Algorithm.DFS))
        game.enemy_list.append(Enemy(1, 11, Algorithm.DIJKSTRA))
        game.player = Player()

    def test_explosion_sectors(self):
        # Prueba para verificar los sectores afectados por una explosión

        enemy = game.enemy_list[0]
        game.bombs.append(enemy.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 2980)
        game.update_bombs(game.GRID_BASE, 50)

        # Verificaciones de la explosión generada
        self.assertEqual(1, len(game.explosions))
        exp = game.explosions[0]

        # Verificar que los sectores afectados sean los correctos
        self.assertEqual(5, len(exp.sectors))
        self.assertTrue([11, 11] in exp.sectors)
        self.assertTrue([11, 10] in exp.sectors)
        self.assertTrue([10, 11] in exp.sectors)
        self.assertTrue([11, 9] in exp.sectors)
        self.assertTrue([9, 11] in exp.sectors)

        # Verificar que ciertos sectores no estén afectados
        self.assertFalse([11, 12] in exp.sectors)
        self.assertFalse([12, 11] in exp.sectors)

    def test_box_destroy(self):
        # Prueba para verificar la destrucción de una caja en el juego

        game.GRID_BASE[2][1] = 2
        self.assertEqual(2, game.GRID_BASE[2][1])
        game.bombs.append(game.player.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 2980)
        game.update_bombs(game.GRID_BASE, 50)

        # Verificar que la caja fue destruida correctamente
        self.assertEqual(0, game.GRID_BASE[2][1])
        self.assertTrue([2, 1] in game.explosions[0].sectors)

    def test_death(self):
        # Prueba para verificar la muerte de un enemigo por una explosión

        en = game.enemy_list[1]
        game.bombs.append(en.plant_bomb(game.GRID_BASE))
        game.update_bombs(game.GRID_BASE, 1500)

        # Verificar que el enemigo está vivo antes de la explosión
        self.assertTrue(en.life)
        self.assertEqual(0, len(game.explosions))

        game.update_bombs(game.GRID_BASE, 1501)

        # Verificar que el enemigo está muerto después de la explosión
        self.assertFalse(en.life)
        self.assertEqual(0, len(game.explosions))

if __name__ == '__main__':
    unittest.main()
