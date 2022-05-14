import pygame

pygame.init()

win=pygame.display.set_mode((1440,720))

x=50
y=50
width=40
height=60
vel=5

run=False
while not run:
	pygame.time.delay(200)

	for event in pygame.event.get():
		 if event.type==pygame.quit:
		 	run = false

	keys=pygame.key.get_pressed()

	if keys[pygame.K_RIGHT] and x<1440-width-vel:
		 	x+=vel
	if keys[pygame.K_LEFT]and x>vel :
		 	x-=vel
	if keys[pygame.K_UP] and y>vel:
		 	y-=vel
	if keys[pygame.K_DOWN] and y<720-height-vel:
		 	y+=vel
	win.fill((0,0,0))


	pygame.draw.rect(win,(255,0,0),(x,y,width,height))
	pygame.display.update()

pygame.quit()
quit()
