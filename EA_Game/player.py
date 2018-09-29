import pygame
from pygame.locals import *

screen_x = 600
screen_y = 600
screen_background = (255, 255, 255)
player_color = (0, 0, 255)
player_len = 50
player_width = 50
pygame.init()


class player():
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

test = player(100, 100)
test.draw_player()
x_change = 0
y_change = 0
while True:
    for i in pygame.event.get():
        if i.type == QUIT:
            pygame.quit()
            quit()
        elif i.type == KEYDOWN:
            if i.unicode == 'a':
                print("left movement")
                if test.x > 5:
                    test.x -= 5
                    test.draw_player()
            elif i.unicode == 'd':
                print("right movement")
                if test.x < screen_x - 50:
                    test.x += 5
                    test.draw_player()
            elif i.unicode == 's':
                print("down movement")
                test.y += 5
                test.draw_player()
            elif i.unicode == 'w':
                print("up movement")
                test.y -= 5
                test.draw_player()
        pygame.display.update()
