import pygame, sys

pygame.init()
win = pygame.display.set_mode((500,400))
win.fill((255,255,255))

Gulim = "C:/Windows/Fonts/HMKMMAG.TTF"	# 굴림체
Batang = "C:/Windows/Fonts/batang.ttc"

font1 = pygame.font.Font(Gulim, 40)
text1 = font1.render("한글!", True, (255,0,0))
font2 = pygame.font.Font(Gulim, 50)
font2.set_bold(True)
text2 = font2.render("안녕하세요!", True, (255,0,0))
font3 = pygame.font.Font(Batang, 60)
font3.set_italic(True)
text3 = font3.render("안녕하세요!", True, (255,0,0), (255,255,0))
win.blit(text1, (30,30))
win.blit(text2, (30,80))
win.blit(text3, (30,130))

pygame.display.update()
        
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
