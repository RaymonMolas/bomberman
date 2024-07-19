import unittest
import game

class MyTestCase(unittest.TestCase):
    
    def test_map_generation_corners(self):
        # Prueba para verificar la generación del mapa en las esquinas

        # Copia profunda de GRID_BASE para evitar modificar el original
        grid = [row[:] for row in game.GRID_BASE]
        
        # Genera el mapa en la copia de grid
        game.generate_map(grid)

        # Verifica que las esquinas del mapa tengan el valor esperado (0)
        l = len(grid)
        self.assertEqual(0, grid[1][1])
        self.assertEqual(0, grid[1][2])
        self.assertEqual(0, grid[2][1])
        self.assertEqual(0, grid[l - 2][1])
        self.assertEqual(0, grid[l - 2][2])
        self.assertEqual(0, grid[l - 3][1])
        self.assertEqual(0, grid[1][l - 2])
        self.assertEqual(0, grid[1][l - 3])
        self.assertEqual(0, grid[2][l - 2])
        self.assertEqual(0, grid[l - 2][l - 2])
        self.assertEqual(0, grid[l - 2][l - 3])
        self.assertEqual(0, grid[l - 3][l - 2])

if __name__ == '__main__':
    unittest.main()
