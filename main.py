import sys
import files
import game
import grid
import ui

if len(sys.argv) > 1:
    file = files.ListFile(sys.argv[1])
    g = file.load()
else:
    g = game.Game(grid.Grid())
    g.grid.live((2, 2))
    g.grid.live((2, 4))
    g.grid.live((3, 3))
    g.grid.live((3, 4))
    g.grid.live((4, 3))

display = ui.GridDisplay(g)
display.main()
