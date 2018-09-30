import pygame
from plane import *
from Obstacle import *
from player import *
from config_planes import *
from switch_planes import *

size = [x_size, y_size]
screen = pygame.display.set_mode(size)
player1 = Player(10, y_size - 10, screen, 10, 10)
x_change = 0
y_change = 0

plane1 = Plane(white, screen, player1, (10, 10))
plane2 = Plane(white, screen, player1, (10, 10))
plane3 = Plane(white, screen, player1, (10, 10))

plane1._obstacles.append(Obstacle(screen, int(x_size/3), 10, 0,
                                  2*int(y_size/3), black))
plane1._obstacles.append(Obstacle(screen, 10, int(y_size/3), int(x_size/3),
                                  2*int(y_size/3), black))

plane2._obstacles.append(Obstacle(screen, x_size, 10, 0,
                                  2*int(y_size/3), black))


plane3._obstacles.append(Obstacle(screen, int(x_size/3), 10, 0,
                                  2*int(y_size/3), black))
plane3._obstacles.append(Obstacle(screen, 10, y_size, int(x_size/3),
                                  0, black))

planes = [plane1, plane2, plane3]
planeNumber = 0
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

            if i.unicode == '1' or i.unicode == '2' or i.unicode == '3':
                planeNumber = switch_planes(planes, int(i.unicode)-1,
                                            planeNumber)

        if i.type == pygame.KEYUP:
            if i.key == 275 or i.key == 276:
                x_change = 0
            if i.key == 274 or i.key == 273:
                y_change = 0

    screen.fill(white)
    planes[planeNumber].render_function()
    player1.move("y", y_change)
    player1.move("x", x_change)
    planes[planeNumber].collision_detect()
    planes[planeNumber].finish_detect()
    player1.draw_player()
    pygame.display.flip()
    pygame.display.update()
