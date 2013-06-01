from grid import Grid


class Game:
    rule_lonely = 2
    rule_crowded = 3
    rule_reproduce = 3

    def __init__(self):
        self.grid = Grid()

    def step(self):
        new_grid = Grid()
        cells_to_check = self.grid.live_cells
        for cell in self.grid.live_cells:
            cells_to_check = cells_to_check.union(self.grid.get_neighbors(cell))

        for cell in cells_to_check:
            count = self.grid.count_live_neighbors(cell)
            if self.grid.is_alive(cell):
                if count >= self.rule_lonely and count <= self.rule_crowded:
                    new_grid.live(cell)
            else:
                if count == self.rule_reproduce:
                    new_grid.live(cell)

        self.grid = new_grid

    def get_region(self, x_offset, y_offset, x_len, y_len):
        return [[self.grid.is_alive((x, y)) for x in range(x_offset, x_len)]
                for y in range(y_offset, y_len)]

import time
if __name__ == "__main__":
    g = Game()
    g.grid.live((2, 2))
    g.grid.live((2, 4))
    g.grid.live((3, 3))
    g.grid.live((3, 4))
    g.grid.live((4, 3))
    while True:
        for row in g.get_region(0, 0, 10, 10):
            print(' '.join(map(lambda c: [' ', 'x'][int(c)], row)))
        g.step()
        time.sleep(0.5)
