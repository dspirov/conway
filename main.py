import sys
import files
import game
import grid
import ui
import re

g = None
if len(sys.argv) > 1:
    if sys.argv[1] is 'open':
        if sys.argv[2] in ['list', 'life1.06']:
            file = files.ListFile(sys.argv[1])
        elif sys.argv[2] in ['life', 'life1.05']:
            file = files.LifeFile(sys.argv[1])
        else:
            print('Please specify file type!')
        g = file.load()
    elif sys.argv[1] == 'new':
        match = re.match(r'^(H:)?B(\d+)[^\d\w]?S(\d+)$', sys.argv[2])
        if match:
            g = game.Game(grid.HexGrid() if match.group(1) else grid.Grid())
            g.set_rules(map(int, match.group(2)), map(int, match.group(3)))
        elif sys.argv[2] == 'hex':
            g = game.Game(grid.HexGrid())
            g.set_rules([2], [3, 4])
        else:
            g = game.Game(grid.Grid())
else:
    g = game.Game(grid.Grid())

if g:
    display = ui.GridDisplay(g)
    display.main()
