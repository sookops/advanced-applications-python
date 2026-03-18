import pygame, sys

pygame.init()
win = pygame.display.set_mode((1000,450))
win.fill((255,255,255))

img = pygame.image.load("images/mario.png")
img1 = pygame.transform.rotate(img, 45) 	# 45도 회전
win.blit(img1, (0,0))
img2 = pygame.transform.rotate(img, 90) 	# 90도 회전
win.blit(img2, (150,0))	
img3 = pygame.transform.flip(img, True, False)  # 좌우 반전
win.blit(img3, (300, 0))
img5 = pygame.transform.rotozoom(img, -30, 1.5) # 회전후 확대
win.blit(img5, (450, 0))
img4 = pygame.transform.scale(img, (80, 80))    # 크기 설정
win.blit(img4, (600, 0))

pygame.display.update()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
