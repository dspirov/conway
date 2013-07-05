class Grid:
    def __init__(self):
        self.live_cells = set()

    def live(self, coords):
        self.live_cells.add(coords)

    def kill(self, coords):
        self.live_cells.remove(coords)

    def is_alive(self, coords):
        return coords in self.live_cells

    def get_live_cells(self):
        return self.live_cells

    def get_neighbors(self, coords):
        x, y = coords
        return [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]

    def count_live_neighbors(self, coords):
        return sum(map(self.is_alive, self.get_neighbors(coords)))

    def get_limits(self):
        xs = list(map(lambda c: c[0], self.live_cells))
        ys = list(map(lambda c: c[1], self.live_cells))
        if not self.live_cells:
            xs = [0]
            ys = [0]
        return {'min_x': min(xs),
                'max_x': max(xs),
                'min_y': min(ys),
                'max_y': max(ys)}

    def empty_copy(self):
        return Grid()


class HexGrid(Grid):
    def get_neighbors(self, coords):
        x, y = coords
        return [(x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1)]

    def empty_copy(self):
        return HexGrid()


class ToroidalGrid(Grid):
    def __init__(self, size):
        self.data = [[False for x in range(0, size[0])]
                     for y in range(0, size[1])]
        self.size = size

    def live(self, coords):
        coords = self.fix_coords(coords)
        self.data[coords[1]][coords[0]] = True

    def kill(self, coords):
        coords = self.fix_coords(coords)
        self.data[coords[1]][coords[0]] = False

    def is_alive(self, coords):
        coords = self.fix_coords(coords)
        return self.data[coords[1]][coords[0]]

    def fix_coords(self, coords):
        return (coords[0] % self.size[0], coords[1] % self.size[1])

    def get_live_cells(self):
        result = []
        for y in range(0, self.size[1]):
            for x in range(0, self.size[0]):
                if self.data[y][x]:
                    result.append((x, y))
        return set(result)

    def get_limits(self):
        return {'min_x': 0,
                'max_x': self.size[0],
                'min_y': 0,
                'max_y': self.size[1]}

    def empty_copy(self):
        return ToroidalGrid(self.size)
