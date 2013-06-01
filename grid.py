class Grid:
    def __init__(self):
        self.live_cells = set()

    def live(self, coords):
        self.live_cells.add(coords)

    def kill(self, coords):
        self.live_cells.remove(coords)

    def is_alive(self, coords):
        return coords in self.live_cells

    def get_neighbors(self, coords):
        x, y = coords
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

    def count_live_neighbors(self, coords):
        return sum(map(self.is_alive, self.get_neighbors(coords)))
