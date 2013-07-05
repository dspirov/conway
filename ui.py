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
                        if self.is_hex():
                            coords = Vec2D(coords.x - coords.y / math.tan(math.pi / 3),
                                           coords.y / math.sin(math.pi / 3))
                            coords = (round(coords.x), round(coords.y))
                        else:
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
                    if event.dict['key'] in [pygame.K_PLUS, pygame.K_KP_PLUS]:
                        self.speedUp()
                    if event.dict['key'] in [pygame.K_MINUS, pygame.K_KP_MINUS]:
                        self.slowDown()

            self.clock.tick(self.fps)
            self.draw()
            if self.running and self.next_grid_step <= pygame.time.get_ticks():
                self.next_grid_step += 1000 / self.grid_freq
                self.game.step()

    def is_hex(self):
        return self.game.grid.__class__.__name__ is 'HexGrid'

    def draw(self):
        self.screen.fill((255, 255, 255))
        fill_color = (100, 100, 100)
        border_color = (0, 0, 0)

        if not self.is_hex():
            for c in self.game.grid.get_live_cells():
                square_offset = (self.offset + Vec2D(*c)) \
                    * self.square_size \
                    + self.window_center
                coords = (square_offset.x, square_offset.y,
                          self.square_size, self.square_size)
                pygame.draw.rect(self.screen, fill_color, coords, 0)
                pygame.draw.rect(self.screen, border_color, coords, 1)
        else:
            points = list(map(lambda i: Vec2D(math.sin(i * math.pi / 3),
                                              math.cos(i * math.pi / 3)),
                          range(0, 6)))

            for c in self.game.grid.get_live_cells():
                hex_center = Vec2D(c[0] + math.cos(math.pi/3) * c[1],
                                   math.sin(math.pi/3) * c[1])
                hex_center = (hex_center + self.offset) \
                    * self.square_size \
                    + self.window_center
                coords = []
                for p in points:
                    coords.append(tuple(p * (self.square_size / 2) + hex_center))
                pygame.draw.polygon(self.screen, fill_color, coords, 0)
                pygame.draw.polygon(self.screen, border_color, coords, 1)

        pygame.display.flip()

    def speedUp(self):
        self.grid_freq *= 1.4

    def slowDown(self):
        self.grid_freq /= 1.4
