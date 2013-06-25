import unittest
import grid


class GridTest(unittest.TestCase):
    def setUp(self):
        self.grid = grid.Grid()
        self.glider = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
        for coords in self.glider:
            self.grid.live(coords)

    def test_live_cells(self):
        self.assertEqual(set(self.grid.get_live_cells()), set(self.glider))

    def test_is_alive(self):
        self.assertTrue(self.grid.is_alive((2, 1)))
        self.assertFalse(self.grid.is_alive((234, 550)))

    def test_live_kill(self):
        self.grid.kill((2, 1))
        self.assertFalse(self.grid.is_alive((2, 1)))
        self.grid.live((2, 1))
        self.assertTrue(self.grid.is_alive((2, 1)))

    def test_get_neighbors(self):
        neighbors = set([(1, 1), (1, 2), (1, 3),
                         (2, 1), (2, 3),
                         (3, 1), (3, 2), (3, 3)])
        self.assertEqual(set(self.grid.get_neighbors((2, 2))), neighbors)

    def test_count_live_neighbors(self):
        self.assertEqual(self.grid.count_live_neighbors((1, 1)), 2)
        self.assertEqual(self.grid.count_live_neighbors((4, 4)), 0)


class ToroidalGridTest(GridTest):
    def setUp(self):
        self.grid = grid.ToroidalGrid((10, 5))
        self.glider = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
        for coords in self.glider:
            self.grid.live(coords)

    def test_fix_coords(self):
        self.assertEqual(self.grid.fix_coords((10, 5)), (0, 0))
        self.assertEqual(self.grid.fix_coords((12, 4)), (2, 4))
    
    def test_loop(self):
        self.assertTrue(self.grid.is_alive((11, 6)))
        self.assertFalse(self.grid.is_alive((4, -1)))


class TestHexGrid(GridTest):
    def setUp(self):
        self.grid = grid.HexGrid()
        self.glider = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
        for coords in self.glider:
            self.grid.live(coords)

    def test_get_neighbors(self):
        neighbors = set([(1, 2), (1, 3),
                         (2, 1), (2, 3),
                         (3, 1), (3, 2)])
        self.assertEqual(set(self.grid.get_neighbors((2, 2))), neighbors)
