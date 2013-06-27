import unittest
import game
import grid

class GameTest(unittest.TestCase):
    def glider_test():
        self.grid = grid.Grid()
        self.glider = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
        for coords in self.glider:
            self.grid.live(coords)
        self.game = game.Game(self.grid)
        self.game.step()
        next_state = set([(0, 2), (1, 1), (1, 2), (3, 1), (3, 3)])
        self.assertEqual(set(self.game.grid.get_live_cells()), next_state)