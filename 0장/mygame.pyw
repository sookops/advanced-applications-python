import pygame, sys

pygame.init()		
win = pygame.display.set_mode( (400, 300) )

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
