import files
import unittest
import grid
import game
import os

class FilesTest(unittest.TestCase):
    def setUp(self):
        self.tmp_list = files.ListFile('tests/list_tmp.life')
        self.tmp_life = files.LifeFile('tests/life_tmp.life')
        self.glider = [(1, 1), (1, 2), (1, 3), (2, 1), (3, 2)]
        self.game = game.Game(grid.Grid())
        for coords in self.glider:
            self.game.grid.live(coords)

    def tearDown(self):
        try:
            os.remove('tests/list_tmp.life')
            os.remove('tests/life_tmp.life')
        except FileNotFoundError:
            pass

    def test_list_load(self):
        glider = files.ListFile('examples/glider.txt')
        g = glider.load()
        self.assertIsInstance(g, game.Game)
        self.assertIsInstance(g.grid, grid.Grid)
        self.assertEqual(g.grid.get_live_cells(),
                         {(2, 2), (2, 4), (3, 3), (3, 4), (4, 3)})

    def test_list_rule(self):
        file = files.ListFile('examples/rule.txt')
        g = file.load()
        self.assertEqual(g.get_rules(), ([1, 2, 3, 4], [0, 1, 2, 3, 4, 5, 7]))

    def test_list_hex(self):
        file = files.ListFile('examples/hex.txt')
        g = file.load()
        self.assertIsInstance(g.grid, grid.HexGrid)

    def test_list_save(self):
        self.tmp_list.save(self.game)
        with open(self.tmp_list.filename) as file:
            lines = file.readlines()
            self.assertEqual(lines, ['#Life 1.06\n',
                                     '#RULE B3/S23\n',
                                     '1 2\n',
                                     '3 2\n',
                                     '1 3\n',
                                     '1 1\n',
                                     '2 1\n'])

    def test_life_load(self):
        glider = files.LifeFile('examples/life1.05.LIF')
        g = glider.load()
        self.assertIsInstance(g, game.Game)
        self.assertIsInstance(g.grid, grid.Grid)
        self.assertEqual(g.grid.get_live_cells(),
                         {(1, 2), (3, 1), (2, 3), (1, 1), (2, 1)})

    def test_life_save(self):
        self.tmp_life.save(self.game)
        with open(self.tmp_life.filename) as file:
            lines = file.readlines()
            self.assertEqual(lines, ['#Life 1.05\n',
                                     '**.\n',
                                     '*.*\n',
                                     '*..\n'])