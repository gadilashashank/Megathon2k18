from pygame import *
from time import time as Time
from random import randint

init()
black=(0,0,0)
white=(255,255,255)
y_size=600
x_size=800
gameDisplay=display.set_mode((x_size,y_size))
clock=time.Clock()
blockwidth=100
blockheight=10
blockx=x_size/2
blocky=y_size-20
x_change=0
Level=0
gameExit=False

class Ball():
	def __init__(self,x,y,x_speed,y_speed):
		self.x=x
		self.y=y
		self.x_speed=x_speed
		self.y_speed=y_speed

	def printball(self):
		draw.circle(gameDisplay,black,(int(self.x),int(self.y)),10)

	def increasespeed(self):
		if self.x_speed>0:
			self.x_speed+=1
		else:
			self.x_speed-=1
		if self.y_speed>0:
			self.y_speed+=1
		else:
			self.y_speed-=1

	def newpos(self):
		self.x+=self.x_speed
		self.y+=self.y_speed


def drawGameArea():
	draw.rect(gameDisplay,(207,181,59),Rect(0,0,x_size,10))
	draw.rect(gameDisplay,(207,181,59),Rect(0,0,10,y_size))
	draw.rect(gameDisplay,(207,181,59),Rect(x_size-10,0,10,y_size))

def displayblock(x,y):
	draw.rect(gameDisplay,(255,223,0),Rect(x,y,blockwidth,blockheight))

def collisiondetector(ball,blockx,blocky,blockwidth):
	ballbottom=ball.y+10
	if ballbottom>=blocky and ball.x>=blockx and ball.x<=blockx+blockwidth:
		ball.y_speed=-ball.y_speed
	if ball.x>=x_size-20 or ball.x<=10:
		ball.x_speed=-ball.x_speed
	if ball.y-10<=0:
		ball.y_speed=-ball.y_speed

ball=Ball(randint(x_size/5,0.8*(x_size)),randint(y_size/5,0.8*y_size),3,3)
InitTime=Time()
while not gameExit:
	for i in event.get():
		print(i)
		if i.type==QUIT:
			gameExit=True
		if i.type==KEYDOWN:
			if i.unicode=='q':
				gameExit=True
			if i.key==275:
				x_change+=5
			if i.key==276:
				x_change-=5
		if i.type==KEYUP:
			if i.key==275 or i.key==276:
				x_change=0
	blockx+=x_change
	if blockx>x_size-110 or blockx<10:
		blockx-=x_change
	gameDisplay.fill(white)
	drawGameArea()
	ball.newpos()
	collisiondetector(ball,blockx,blocky,blockwidth)
	ball.printball()
	if ball.y>blocky+10:
		gameExit=True
	if Time()>InitTime+10:
		ball.increasespeed()
		InitTime=Time()
		Level+=1
	displayblock(blockx,blocky)
	display.update()
	clock.tick(60)

print(Level)
quit()
exit()
