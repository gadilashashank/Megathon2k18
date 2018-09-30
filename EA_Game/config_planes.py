from pygame import *
# Colours used
black = (0, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)
gold = (255, 223, 0)
player_color = blue
font.init()

# Size of the screen
x_size = 600
y_size = 600
screen_x = x_size
screen_y = y_size
screen_background = white
player_len = 50
player_width = 50

# Game area
gameDisplay = display.set_mode((x_size, y_size))
myfont = font.SysFont('Times New Roman', 30)
textsurface = myfont.render('Some Text', False, (0, 0, 0))
