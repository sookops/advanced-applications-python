import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 500, 600
WHITE, BLACK, RED, GREEN = ((255,255,255), (0,0,0), (255,0,0), (0,255,0))

win = pygame.display.set_mode((WIDTH, HEIGHT))    # 파이게임창 생성
clock = pygame.time.Clock()                       # 클럭 객체 생성

# 공 클래스
class Ball(pygame.sprite.Sprite):
     def __init__(self, color, size, pos=(0,0), speed=(0,0)):
          super().__init__()            # 부모 클래스(Sprite) 초기화
          self.image = pygame.Surface(size, pygame.SRCALPHA)     # 서피스 생성
          pygame.draw.ellipse(self.image, color, (0,0)+size, 0)  # 공 이미지
          self.rect = self.image.get_rect()                      # Rect 객체
          self.rect.center = pos        # 공의 초기 위치 
          self.speed = list(speed)      # 방향과 속력 (dx, dy) – 이동 거리

     def update(self):                  # 공 이동
          global points, game_over
          self.rect.x += self.speed[0]
          self.rect.y += self.speed[1]   
          if self.rect.left <= 0 or self.rect.right >= WIDTH:
               self.speed[0] *= -1      # 수평 방향 반대로 전환
          if self.rect.top <= 0:
               points += 1
               self.speed[1] *= -1      # 수직 방향 반대로 전환
          if self.rect.top > HEIGHT:
               game_over = True         # 게임 종료

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
     def __init__(self, color, size, ypos=10):
          super().__init__()                 # 부모 클래스(Sprite) 초기화
          self.image = pygame.Surface(size)  # 서피스 생성
          pygame.draw.rect(self.image, color, (0,0)+size, 0)   # 패들 이미지
          self.rect = self.image.get_rect()  # Rect 객체
          self.rect.bottom = HEIGHT-ypos     # 패들의 초기 위치
          
# 점수 클래스
class Score(pygame.sprite.Sprite):
     def __init__(self, color, pos=(10,10)):
          super().__init__()
          self.score_font = pygame.font.Font(None, 50)      # 폰트 객체 생성
          self.image = self.score_font.render('0', True, BLACK)
          self.rect = self.image.get_rect()
          self.rect.topleft = pos

     def update(self):
          self.image = self.score_font.render(str(points), True, BLACK)
          self.rect = self.image.get_rect()
                    
# 게임 초기화
def init_game():
     global game_over, points
     ball.rect.center = (250,300)
     ball.speed = [random.randint(3,6)*random.choice([-1,1]), -random.randint(3,6)]
     paddle.rect.centerx = 250
     points = 0          # 점수
     game_over = False   # 게임 진행 변수

# 게임 종료 메시지
def game_over_message():
     font1 = pygame.font.Font(None, 70)
     font2 = pygame.font.Font(None, 50)
     text1 = "Game Over"
     text2 = "Your score is " + str(points)
     text1_img = font1.render(text1, True, RED)
     text2_img = font2.render(text2, True, BLACK)
     pos1 = (WIDTH-text1_img.get_width())/2
     pos2 = (WIDTH-text2_img.get_width())/2
     win.blit(text1_img, [pos1,150])
     win.blit(text2_img, [pos2,250])

# Main Program
ball = Ball(RED, (20,20))               # 공 객체 생성(color, size)
paddle = Paddle(GREEN, (100,10))        # 패들 객체 생성(color, size)
score = Score(BLACK)                    # 점수 객체 생성(color)
sprite_group = pygame.sprite.Group()    # 스트라이트 그룹 생성
sprite_group.add(ball, paddle, score)   # 모든 게임 객체 포함
init_game()                             # 게임 초기화

# Main Loop
while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()
          elif event.type == pygame.MOUSEMOTION:
               paddle.rect.centerx = event.pos[0]
          elif event.type == pygame.KEYDOWN:
               if event.key == pygame.K_SPACE and game_over:
                    init_game()    # 초기화 작업
               
     if not game_over:             # 게임 진행
          win.fill(WHITE)          # 배경 그리기
          ball.update()            # 공 위치 갱신
          score.update()           # 점수 갱신
          sprite_group.draw(win)   # 모든 스트라이프 그리기
          
          if paddle in pygame.sprite.spritecollide(ball, sprite_group, False):
               ball.speed[1] *= -1
     else:                         # 게임 종료
          game_over_message()      # 게임 종료 메시지 출력

     pygame.display.flip()         # 그리기 갱신
     clock.tick(80)                # 게임 진행 속도 설정
    
