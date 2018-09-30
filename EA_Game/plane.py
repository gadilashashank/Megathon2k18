from pygame import *
from config_planes import *
from Obstacle import *


class Plane():
    def __init__(self, color, screen, player, final_coods):
        self.x_ = x_size
        self.y_ = y_size
        self._obstacles = []
        self.color = color
        self.screen = screen
        self.player = player
        self.destination_x = final_coods[0]
        self.destination_y = final_coods[1]
        self.keyTaken=False

    def render_function(self):
        self.screen.fill(self.color)
        for obstacle in self._obstacles:
            obstacle.render_obstacle()
        if(not self.keyTaken):
            draw.circle(self.screen, red, (self.destination_x,
                                            self.destination_y), 10)

    def collision_detect(self):
        for obstacle in self._obstacles:
            if(self.player.x in range(obstacle.x - 10, obstacle.x + obstacle.length + 1)
               and self.player.y in range(obstacle.y - 10,
                                          obstacle.y + obstacle.breadth + 1)):
                    self.player.x = self.player.prev_x
                    self.player.y = self.player.prev_y
                    return True

    def finish_detect(self):
        if((self.player.x-self.destination_x)**2+(self.player.y-self.destination_y)**2<100) and not self.keyTaken:
            self.keyTaken=True
            return 1
        else:
            return 0


if __name__ == "__main__":
    init()
    clock = time.Clock()
    gameExit = False
    player = 1
    plane1 = Plane(white, gameDisplay, player)
    plane1._obstacles.append(Obstacle(gameDisplay, 50, 10, plane1.x_/2,
                                      plane1.y_/2, black))
    while not gameExit:
        for i in event.get():
            # print(i)
            if i.type == QUIT:
                gameExit = True
                if i.type == KEYDOWN:
                    if i.unicode == "q":
                        gameExit = True
        plane1.render_function()
        display.update()
        clock.tick(60)
