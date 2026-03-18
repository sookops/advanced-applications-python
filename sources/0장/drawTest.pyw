import pygame, sys, math

pygame.init()		
win = pygame.display.set_mode( (500, 500) )

win.fill( (255, 255, 255) )	# 흰색으로 설정

pygame.draw.rect(win, (0,0,255), (20,50,150,100), 1)            # 사각형 그리기
points = ((200,100), (300,50), (350,150), (280,210), (210,170)) # 점 리스트
pygame.draw.polygon(win, (0,255,255), points)                   # 다각형 그리기
pygame.draw.line(win, (0,0,0), (50,50), (100, 150), 3)          # 선 그리기
triangle = ((350, 300), (250, 450), (450, 450))                 # 삼각형 꼭지점 리스트
pygame.draw.lines(win, (0,255,0), True, triangle, 2)            # 삼각형 그리기
pygame.draw.circle(win, (255,0,255), (50,350), 50)              # 원 그리기
pygame.draw.ellipse(win, (0,255,0), (130,300,100,150), 2)       # 타원 그리기
deg = math.pi / 180			                        # 일반각 1도
pygame.draw.arc(win, (255,0,0), (350,50,100,100), 0, 270*deg, 3) # 원호 그리기
pygame.draw.arc(win, (0,0,0), (350,200,100,100), 45*deg, 180*deg, 3)

pygame.display.update()		# 설정된 내용을 화면에 표시

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
