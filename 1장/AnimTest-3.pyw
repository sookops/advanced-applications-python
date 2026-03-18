import pygame, sys, random

pygame.init()
win = pygame.display.set_mode((500,500))
clock = pygame.time.Clock()        # 클럭 객체 생성

class Ball:		# 클래스 정의
     def __init__(self, img_file, location, speed):
          self.image = pygame.image.load(img_file)     # 공 이미지 객체
          self.rect = self.image.get_rect()	       # Rect 객체
          self.rect.topleft = location		       # 기준점 설정
          self.speed = list(speed)	     # 속도 (dx, dy) – 이동 거리

     def move(self):
          self.rect.move_ip(self.speed)	     # 공 이동
          if self.rect.left < 0 or self.rect.right > win.get_width():
               self.speed[0] = -self.speed[0]
          if self.rect.top < 0 or self.rect.bottom > win.get_height():
               self.speed[1] = -self.speed[1]

img_file = "beach_ball.png" 
ball_group = []		           	# 공 리스트
for y in range(0, 3):			# 9개 볼 배치
     for x in range(0, 3):
          location = (150*x + 50, 150*y + 50)
          speed = (random.choice([-2, 2]), random.choice([-2, 2]))
          ball = Ball(img_file, location, speed)
          ball_group.append(ball)

while True:	# 메인 루프
     for event in pygame.event.get():	# 이벤트 검사
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

     win.fill((200,255,255))	             # 배경 그리기
     for ball in ball_group:
          ball.move() 			     # 공 이동
          win.blit(ball.image, ball.rect)    # 공 그리기

     for ball in ball_group:		# 각 볼이 다른 볼들과 충돌하는지 검사
          if len(ball.rect.collidelistall(ball_group)) >= 2:     # 충돌한 볼 개수
               ball.speed[0] = -ball.speed[0]
               ball.speed[1] = -ball.speed[1]

     pygame.display.update()       # 그래픽 출력 갱신
     clock.tick(100)	           # 메인 루프가 1초에 50회 반복됨

