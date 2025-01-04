#!/usr/bin/python3
import pygame

pygame.init()        #used  to create a pygame object

gameDisplay=pygame.display.set_mode((800,600))    #set the screen resolution of the game
pygame.display.set_caption("Bit Race")    #window title

clock=pygame.time.Clock()        #used to track time within the game

gameover=False

while not gameover:
	for event in pygame.event.get():
		print(event)     #this allows us to constantly log in events
		if event.type==pygame.QUIT:
			gameover=True
		print(event)

	pygame.display.update()     #used to update the whole screen
	clock.tick(60)     #how many frames per second

pygame.quit()
quit()       #used to end the game instance

