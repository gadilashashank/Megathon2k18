import pygame
from config_planes import *
pygame.init()



class Obstacle():
    '''This class renders obstacles'''
    def __init__(self,screen,length,breadth,x,y,color):
        self.color = color
        self.screen=screen
        self.dimensions = [x,y,length,breadth]

    def render_obstacle(self):
        pygame.draw.rect(self.screen,self.color,Rect(*self.dimensions))

if __name__ == "__main__":
    size = [x_size,y_size]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Example code for the draw module")
    while 1:
        for i in pygame.event.get():
            print(i)
            if i.type==pygame.KEYDOWN:
                if i.unicode=='q':
                    exit()

        a = Obstacle(screen,100,500,100,50,black)
        screen.fill(white)
        a.render_obstacle()
        pygame.display.flip()
        pygame.display.update()