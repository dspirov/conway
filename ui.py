import pygame
from vec2d import Vec2D
import game
import math


class GridDisplay:
    running = True

    def __init__(self, game):
        pygame.init()
        window_size = (640, 480)
        self.screen = pygame.display.set_mode(window_size)
        self.clock = pygame.time.Clock()
        self.square_size = 10
        self.offset = Vec2D(0, 0)
        self.window_center = Vec2D(*window_size) * 0.5

        self.fps = 30
        self.game = game
        self.next_grid_step = 0
        self.grid_freq = 2

    def main(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return

                elif event.type == pygame.MOUSEMOTION and event.dict['buttons'][0]:
                    self.offset += Vec2D(*event.dict['rel']) * (1 / self.square_size)

                elif event.type == pygame.MOUSEBUTTONUP:
                    if event.dict['button'] is 4:
                        self.square_size += 1
                    elif event.dict['button'] is 5 and self.square_size > 1:
                        self.square_size -= 1
                    elif event.dict['button'] is 3:
                        coords = Vec2D(*event.dict['pos']) - self.window_center
                        coords *= 1/self.square_size
                        coords -= self.offset
                        coords = (math.floor(coords.x), math.floor(coords.y))
                        if self.game.grid.is_alive(coords):
                            self.game.grid.kill(coords)
                        else:
                            self.game.grid.live(coords)

                elif event.type == pygame.KEYDOWN:
                    if event.dict['key'] == pygame.K_SPACE:
                        if not self.running:
                            self.next_grid_step = pygame.time.get_ticks()
                        self.running = not self.running

            self.clock.tick(self.fps)
            self.draw()
            if self.running and self.next_grid_step <= pygame.time.get_ticks():
                self.next_grid_step += 1000 / self.grid_freq
                self.game.step()

    def draw(self):
        self.screen.fill((255, 255, 255))

        for c in self.game.grid.live_cells:
            square_offset = (self.offset + Vec2D(*c)) * self.square_size + self.window_center
            coords = (square_offset.x, square_offset.y,
                      self.square_size, self.square_size)
            pygame.draw.rect(self.screen, (100, 100, 100), coords, 0)  # fill
            pygame.draw.rect(self.screen, (0, 0, 0), coords, 1)  # border

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
