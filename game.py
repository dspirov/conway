class Game:
    rule_survive = [2, 3]
    rule_reproduce = [3]

    def __init__(self, grid):
        self.grid = grid

    def step(self):
        new_grid = self.grid.empty_copy()
        cells_to_check = self.grid.get_live_cells()
        for cell in self.grid.get_live_cells():
            cells_to_check = cells_to_check.union(self.grid.get_neighbors(cell))

        for cell in cells_to_check:
            count = self.grid.count_live_neighbors(cell)
            if self.grid.is_alive(cell):
                if count in self.rule_survive:
                    new_grid.live(cell)
            else:
                if count in self.rule_reproduce:
                    new_grid.live(cell)

        self.grid = new_grid

    def get_region(self, x_offset, y_offset, x_len, y_len):
        return [[self.grid.is_alive((x, y)) for x in range(x_offset, x_len)]
                for y in range(y_offset, y_len)]
