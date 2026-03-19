import pygame, sys

pygame.init()

WIDTH, HEIGHT = 500, 400
BACKGROUND_COLOR = (200,255,255)

win = pygame.display.set_mode((500,400))
clock = pygame.time.Clock()        # 클럭 객체 생성

class Ball(pygame.sprite.Sprite):  # 클래스 정의
     def __init__(self, img_file, location, speed):
          super().__init__()                      # 부모 클래스(Sprite) 초기화 
          self.image = pygame.image.load(img_file).convert_alpha() # 공 이미지 객체
          self.rect = self.image.get_rect()	  # Rect 객체
          self.rect.topleft = location		  # 기준점 설정
          self.speed = list(speed)	          # 속도 (dx, dy) – 이동 거리
          self.radius = self.rect.width//2        # 충돌 검사에서 사용함

     def update(self):              # 공 이동
          self.rect.x += self.speed[0]
          self.rect.y += self.speed[1]		    
          if self.rect.left <= 0 or self.rect.right >= WIDTH:
               self.speed[0] *= -1
          if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
               self.speed[1] *= -1

ball_group = pygame.sprite.Group()      # Sprite Group 객체 생성
ball_group.add(Ball("beach_ball.png", (100, 100), (5, 5)))    # 공 객체 생성
ball_group.add(Ball("beach_ball.png", (350, 150), (2, 5)))
ball_group.add(Ball("beach_ball.png", (200, 200), (5, 2))) 

while True:	# 메인 루프
     for event in pygame.event.get():	# 이벤트 검사
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

     win.fill(BACKGROUND_COLOR)	        # 배경 그리기
     ball_group.update()		# 공 이동
     ball_group.draw(win)               # 공 그리기

     for ball in ball_group:            # 충돌 처리
          #if len(pygame.sprite.spritecollide(ball, ball_group, False)) > 1:
          # 원으로 검사시 (sprite에 self.radius가 정의되어 있어야 함)
          if len(pygame.sprite.spritecollide(ball, ball_group, False, pygame.sprite.collide_circle)) > 1:
             ball.speed[0] *= -1
             ball.speed[1] *= -1

     pygame.display.flip()         # 그래픽 출력 갱신
     clock.tick(50)	           # 메인 루프가 1초에 50회 반복됨

