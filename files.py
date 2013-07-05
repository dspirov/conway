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
            rules = game.get_rules()
            file.write('#RULE '
                       + ('H:' if isinstance(game.grid, grid.HexGrid) else '')
                       + 'B' + ''.join(map(str, rules[0])) + '/'
                       + 'S' + ''.join(map(str, rules[1])) + '\n')
            for cell in game.grid.get_live_cells():
                file.write(str(cell[0]) + ' ' + str(cell[1]) + '\n')

    def load(self):
        with open(self.filename, mode='r') as file:
            result = game.Game(grid.Grid())
            for line in file:
                match = re.match(r'^#RULE (H:)?B(\d+)[^\d\w]?S(\d+)$', line)
                if match:
                    if match.group(1):
                        result.grid = grid.HexGrid()
                    result.set_rules(map(int, match.group(2)),
                                     map(int, match.group(3)))
                elif re.match(r'^-?\d+\s+-?\d+\s*$', line):
                    coords = map(int, line.split(' '))
                    result.grid.live(tuple(coords))
                elif not re.match(r'^#|^\s*$', line):
                    print('bad line: ' + line)
            return result


class LifeFile(GameFile):
    def save(self, game):
        with open(self.filename, mode='w') as file:
            limits = game.grid.get_limits()
            file.write('#Life 1.05\n')
            for y in range(limits['min_y'], limits['max_y'] + 1):
                for x in range(limits['min_x'], limits['max_x'] + 1):
                    file.write('*' if game.grid.is_alive((x, y)) else '.')
                file.write('\n')

    def load(self):
        with open(self.filename, mode='r') as file:
            result = game.Game(grid.Grid())
            line_number = 0
            for line in file:
                if line[0] == '#':
                    continue
                line_number += 1
                col_number = 0
                for char in line:
                    col_number += 1
                    if char == '*':
                        result.grid.live((col_number, line_number))
            return result
