import pygame
from pygame.locals import *
from config_planes import *


class Player():
    # init method. Sets initial position
    def __init__(self, init_x, init_y, screen, length, width):
        self.x = init_x
        self.y = init_y
        self.screen = screen
        self.length = length
        self.width = width
        self.prev_x = self.x
        self.prev_y = self.y

    # All move actions.
    # direction = 1 for y-direction movement
    # direction = 0 for x-direction movement
    # value for units to move.
    def move(self, direction, value):
        if direction == "y":
            if self.y + value + self.width < y_size and self.y + value > 0:
                self.prev_y = self.y
                self.y += value
        elif direction == "x":
            if self.x + value + self.length < x_size and self.x + value > 0:
                self.prev_x = self.x
                self.x += value

    def draw_player(self):
        pygame.draw.rect(self.screen, player_color, (self.x, self.y,
                         self.length, self.width))


if __name__ == "__main__":
    size = [x_size, y_size]
    screen = pygame.display.set_mode(size)

    player1 = Player(x_size/2, y_size/2, screen, 10, 10)
    x_change = 0
    y_change = 0
    while 1:
        for i in pygame.event.get():
            print(i)
            if i.type == pygame.KEYDOWN:
                if i.unicode == 'q':
                    exit()
                if i.key == 275:
                    x_change = 1
                if i.key == 276:
                    x_change -= 1
                if i.key == 273:
                    y_change -= 1
                elif i.key == 274:
                    y_change = 1
            if i.type == pygame.KEYUP:
                if i.key == 275 or i.key == 276:
                    x_change = 0
                if i.key == 274 or i.key == 273:
                    y_change = 0

        player1.move("y", y_change)
        player1.move("x", x_change)
        screen.fill(white)
        player1.draw_player()
        pygame.display.flip()
        pygame.display.update()
