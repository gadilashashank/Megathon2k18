import pygame
pygame.init()

class Obstacle():
    '''This class renders obstacles'''
    def __init__(self,screen,length,breadth,x,y,color):
        self.color = color
        self.dimensions = [x,y,length,breadth]

    def render_obstacle(self):
        pygame.draw.rect(self.screen,self.color,self.dimensions, 0)

if __name__ == "__main__":
    size = [400, 300]
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Example code for the draw module")
while 1:
    for i in pygame.event.get():
        print(i)
        if i.type==pygame.KEYDOWN:
            if i.unicode=='q':
                exit()

    a = Obstacle(screen,10,100,0,0)
    a.render_obstacle()
    pygame.display.flip()
