import pygame, sys

pygame.init()
W, H = 800, 600
WHITE, RED, GRAY = (255, 255, 255), (255, 0, 0), (100, 100, 100)

background = pygame.Surface((W, H))
background.fill(WHITE)
pygame.draw.rect(background, GRAY, (0, H-40, W, 40))

win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, (0,0,40,40))
        self.rect = self.image.get_rect()

        self.pos = pygame.math.Vector2(W//2, H-40)  # 위치 벡터
        self.xspeed = 5         # 수평 이동 속도
        self.yspeed = 0         # 상승/하강 속도
        self.GRAVITY = 0.8      # 중력 가속도
              
        # 점프 힘 조절
        self.MAX_JUMP_POWER = -25   # 최대 점프 힘 (상승 속도)
        self.MIN_JUMP_CUT = -5      # 키를 놓았을 때 남겨둘 속도
        self.jumping = False        # 점프 중인 상태 판별

    def jump(self):
        if self.rect.bottom >= H-40:    # 바닥에 닿아있을 때만 점프 
            self.yspeed = self.MAX_JUMP_POWER
            self.jumping = True

    def jump_cut(self):
        if self.jumping:    # 점핑 중단시킴
            if self.yspeed < self.MIN_JUMP_CUT:
                self.yspeed = self.MIN_JUMP_CUT
                
    def update(self):
        self.yspeed += self.GRAVITY     # 상승/하강 속도에 중력 적용
        
        # 키 입력에 따른 좌우 이동 및 이미지 반전
        direction = 0      # 0: 멈춤, -1: 왼쪽 방향, 1: 오른쪽 방향
        
        keys = pygame.key.get_pressed() # 키 입력 상태 확인
        if keys[pygame.K_LEFT]:
            direction = -1      
        elif keys[pygame.K_RIGHT]:
            direction = 1

        # 위치 벡터 갱신
        self.pos.x += direction*self.xspeed     # 수평 이동
        self.pos.y += self.yspeed               # 수직 이동

        # 화면 벗어나면 반대 방향에 나타남 
        if self.pos.x > W: self.pos.x = 0
        if self.pos.x < 0: self.pos.x = W
        
        # 바닥에 닿으면 점프 상태 해제
        if self.pos.y >= H-40:          # 바닥 높이 제한
            self.pos.y = H-40
            self.yspeed = 0
            self.jumping = False

        self.rect.midbottom = self.pos  # 현재 위치 갱신
        
# 객체 생성
player = Player()
all_sprites = pygame.sprite.Group(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.jump()
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                player.jump_cut()

    all_sprites.update()
    win.blit(background, (0,0))
    all_sprites.draw(win)
    
    pygame.display.flip()
    clock.tick(60)

