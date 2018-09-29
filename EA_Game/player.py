import pygame
from pygame.locals import *

class Player():
    # init method. Sets initial position
    def __init__(self, init_x, init_y):
        self.x = init_x
        self.y = init_y
    # All move actions.
    # direction = 1 for y-direction movement
    # direction = 0 for x-direction movement
    # value for units to move.
    # NOT USED BELOW
    def move(self, direction, value):
        if direction:
            self.y += value
        else:
            self.x += value

    def draw_player(self):
        screen = pygame.display.set_mode((screen_x, screen_y), 0, 32)
        screen.fill(screen_background)
        pygame.draw.rect(screen, player_color, (self.x, self.y, player_len, player_width))
        pygame.display.update()

if __name__ == "__main__":
    size = [x_size,y_size]
    screen = pygame.display.set_mode(size)

    player1=Player(x_size/2,y_size/2)
    while 1:
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.KEYDOWN:
                if i.unicode=='q':
                    exit()
            if i.type==pygame.KEYDOWN:
                if i.key==2

        screen.fill(white)
        pygame.display.flip()
        pygame.display.update()
