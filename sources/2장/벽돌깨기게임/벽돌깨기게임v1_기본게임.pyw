import pygame, sys, random

pygame.init()
WIDTH, HEIGHT = 500, 600
WHITE, BLACK, RED, GREEN, BLUE = (255,255,255), (0,0,0), (255,0,0), (0,255,0), (0,0,255)
COLOR = ((255,165,0), (242,242,0), (0,128,0), (128,0,128), (0,0,250), (0,128,128))

win = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
pygame.time.set_timer(pygame.USEREVENT, 1000)    # 타이머 설정

# 공 클래스
class Ball(pygame.sprite.Sprite):
     def __init__(self, color, size, pos=(0,0), speed=(0,0)):
          super().__init__()            # 부모 클래스(Sprite) 초기화
          self.image = pygame.Surface(size, pygame.SRCALPHA)     # 서피스 생성
          pygame.draw.ellipse(self.image, color, (0,0)+size, 0)  # 공 이미지
          self.rect = self.image.get_rect()                      # Rect 객체
          self.rect.center = pos        # 공의 초기 위치 
          self.speed = list(speed)      # 방향과 속력 (dx, dy) – 이동 거리

     def update(self):
          self.rect.x += self.speed[0]
          self.rect.y += self.speed[1]   
          if self.rect.left <= 0 or self.rect.right >= WIDTH:
               self.speed[0] *= -1          # 수평 방향 반대로 전환
          if self.rect.top <= 0:
               self.speed[1] *= -1          # 수직 방향 반대로 전환
          if self.rect.top > HEIGHT:
               self.kill()         # 공 객체 소멸

# 패들 클래스
class Paddle(pygame.sprite.Sprite):
     def __init__(self, color, size, ypos=10):
          super().__init__()                 # 부모 클래스(Sprite) 초기화
          self.image = pygame.Surface(size)  # 서피스 생성
          pygame.draw.rect(self.image, color, (0,0)+size, 0)   # 패들 이미지
          self.rect = self.image.get_rect()  # Rect 객체
          self.rect.bottom = HEIGHT-ypos     # 패들의 초기 위치

# 벽돌 클래스
class Block(pygame.sprite.Sprite):
     def __init__(self, color, size,  pos):
          super().__init__()            # 부모 클래스(Sprite) 초기화
          self.image = pygame.Surface(size)
          pygame.draw.rect(self.image, color, (0,0)+size, 0)     # 벽돌 이미지
          self.rect = self.image.get_rect()                      # Rect 객체
          self.rect.topleft = pos
     
# 게임 초기화
def init_game():
     global game_over, game_speed
     ball_group.empty()
     block_group.empty()
     all_sprite_group.empty()
     for i in range(3):
          speed = (random.randint(3,6)*random.choice([-1,1]), -random.randint(3,6))
          ball_group.add(Ball(RED, (10,10), (250,300), speed))
     ypos = 0
     for color in COLOR:      # 벽돌 배치
          for xpos in range(7):
               block_group.add(Block(color, (55, 25), (xpos*60+40, ypos*30+20)))
          ypos += 1
     game_over = False   # 게임 진행 변수
     game_speed = 60     # 게임 속도
     all_sprite_group.add(paddle, ball_group, block_group)

# 게임 종료 메시지
def game_over_message():
     font1 = pygame.font.Font(None, 70)
     font2 = pygame.font.Font(None, 50)
     font3 = pygame.font.Font(None, 30)
     text1 = "Game over"
     if len(block_group) > 0:
          text2 = "You lose!"
     else:
          text2 = " You win!"
     text3 = "Press the space key to play again"
     text1_img = font1.render(text1, True, RED)
     text2_img = font2.render(text2, True, BLACK)
     text3_img = font3.render(text3, True, BLACK)
     pos1 = (win.get_width()-text1_img.get_width())/2
     pos2 = (win.get_width()-text2_img.get_width())/2
     pos3 = (win.get_width()-text3_img.get_width())/2
     win.blit(text1_img, (pos1, 150))
     win.blit(text2_img, (pos2, 250))
     win.blit(text3_img, (pos3, 350))

# Main Program
ball_group = pygame.sprite.Group()           # 공 스프라이트 그룹
block_group = pygame.sprite.Group()          # 벽돌 스프라이트 그룹
all_sprite_group = pygame.sprite.Group()     # 모든 스프라이트 그룹 생성
paddle = Paddle(GREEN, (100,10))             # 패들 객체 생성
init_game()                                  # 게임 초기화

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
                    all_sprite_group.add(ball_group, block_group)
          elif event.type == pygame.USEREVENT:
               game_speed += 1

     if not game_over:             # 게임 진행
          win.fill(WHITE)          # 배경 그리기
          ball_group.update()      # 공 위치 갱신
          all_sprite_group.draw(win)   # 모든 스프라이트 그리기
          
          for ball in ball_group:
               if pygame.sprite.spritecollide(ball, block_group, True):
                    ball.speed[1] *= -1
               if pygame.sprite.collide_rect(ball, paddle): # 두 스프라이트 사이의 충돌 검사
                    ball.speed[1] *= -1
          if len(block_group) == 0 or len(ball_group) == 0: # 벽돌 또는 공이 없으면 게임 종료
               game_over = True          

     else:                         # 게임 종료 상황
          game_over_message()      # 게임 종료 메시지 출력

     pygame.display.flip()         # 그리기 갱신
     clock.tick(game_speed)        # 게임 진행 속도 설정
    
