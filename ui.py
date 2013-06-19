import pygame
from vec2d import Vec2D
import game

class GridDisplay:
    running = True
    
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((640, 480))
        self.clock = pygame.time.Clock()
        self.game = game
        self.fps = 2
        self.offset = Vec2D(320, 240)
        self.square_size = 10
    
    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                elif event.type == pygame.MOUSEMOTION and event.dict['buttons'][0]:
                    self.offset += Vec2D(*event.dict['rel'])
                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.dict['button'] == 4:
                        print('in')
                    elif event.dict['button'] == 5:
                        print('out')
            
            self.clock.tick(self.fps)
            self.draw()
            self.game.step()
    
    def draw(self):
        self.screen.fill((255, 255, 255))
        
        for c in self.game.grid.live_cells:
            pygame.draw.rect(self.screen, (100, 100, 100),
                                (self.offset.x + c[0] * self.square_size,
                                self.offset.y + c[1] * self.square_size,
                                self.square_size, self.square_size), 0)
        
        pygame.display.flip()



if __name__ == "__main__":
    g = game.Game()
    g.grid.live((2, 2))
    g.grid.live((2, 4))
    g.grid.live((3, 3))
    g.grid.live((3, 4))
    g.grid.live((4, 3))
    d = GridDisplay(g)
    d.main()