from pygame import *
from config_planes import *
from Obstacle import *

class Plane():
  def __init__(self,color,screen,player):
    self.x_=x_size
    self.y_=y_size
    self._obstacles=[]
    self.color=color
    self.screen=screen
    self.player=player

  def render_function(self):
    self.screen.fill(self.color)
    for obstacle in self._obstacles:
      obstacle.render_obstacle()



if __name__ == "__main__":
    init()
    clock=time.Clock()
    gameExit=False
    player=1
    plane1=Plane(white,gameDisplay,player)
    plane1._obstacles.append(Obstacle(gameDisplay,50,10,plane1.x_/2,plane1.y_/2,black))
    while not gameExit:
      for i in  event.get():
        print(i)
        if i.type==QUIT:
            gameExit=True
        if i.type==KEYDOWN:
            if i.unicode=="q":
                gameExit=True
      plane1.render_function()
      display.update()
      clock.tick(60)
