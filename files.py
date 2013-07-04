import game
import grid
import re


class GameFile:
    def __init__(self, filename):
        self.filename = filename


class ListFile(GameFile):
    def save(self, game):
        with open(self.filename, mode='w') as file:
            file.write('#Life 1.06\n')
            for cell in game.grid.get_live_cells():
                file.write(str(cell[0]) + ' ' + str(cell[1]) + '\n')

    def load(self):
        with open(self.filename, mode='r') as file:
            result = game.Game(grid.Grid())
            for line in file:
                if re.match(r'^-?\d+\s+-?\d+\s*$', line):
                    coords = map(int, line.split(' '))
                    result.grid.live(tuple(coords))
                elif not re.match(r'^#|^\s*$', line):
                    print('bad line: ' + line)
            return result
