#!/usr/bin/python3
import pygame

pygame.init()     #create a pygame instance

display_width=800
display_height=600

gameDisplay=pygame.display.set_mode((display_width, display_height))    #set the screen resolution of the game
pygame.display.set_caption("Bit Racer")    #set the window title

black=(0,0,0)
white=(255,255,255)

clock=pygame.time.Clock()   #track time within the game
carImg=pygame.image.load('racecar.png')    #adds the image to the background

car_Width=73
def car(x,y):
	gameDisplay.blit(carImg, (x,y))    #blit is used to display the image on the window

def game_loop():
	x=(display_width*0.45)
	y=(display_height*0.8)
	x_change=0  #variable to position the image in the middle

	gameover=False

	while not gameover:
		for event in pygame.event.get():
			if event.type==pygame.QUIT:
				gameover=True
			#the function to handle moving the image
			if event.type==pygame.KEYDOWN:
				if event.key==pygame.K_LEFT:  #used to move the image to the left when the left arrow key is pressed
					x_change=-5
				elif event.key==pygame.K_RIGHT:   #used to move the image to the right when the right arrow key is pressed
					x_change=5
			if event.type==pygame.KEYUP:     #used to move the image to its original position when the keys are released
				if event.key==pygame.K_LEFT or event.key==pygame.K_RIGHT:
					x_change=0

			x+=x_change    #make the above changes to the game window


			gameDisplay.fill(white)      #first set the window color to white
			car(x,y)
			if x>display_width - car_Width or x<0:
				gameover=True
			pygame.display.update()    #used to update the screen
			clock.tick(30)
game_loop()
pygame.quit()
quit()