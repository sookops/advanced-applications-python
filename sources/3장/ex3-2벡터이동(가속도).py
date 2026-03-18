import pygame, sys

# 1. 초기 설정
pygame.init()
W, H = 800, 600     # 게임창의 너비와 높이
WHITE, RED = (255, 255, 255), (255, 0, 0)   # 색상 정의

win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, (0,0,40,40))
        self.rect = self.image.get_rect()

        # 벡터 설정 (1)
        self.pos = pygame.math.Vector2(W//2, H//2)  # 위치 벡터
        self.vel = pygame.math.Vector2(0, 0)        # 속도 벡터
        
        # 물리 상수 설정 (2)
        self.MAX_SPEED = 9      # 최대 속도
        self.ACCEL = 0.7        # 가속의 세기
        self.FRICTION = 0.9     # 마찰력 (값이 작을수록 빨리 멈춤)

    def update(self):
        acc = pygame.math.Vector2(0, 0)     # 가속도 벡터 초기화 (3)

        # 가속도 벡터 설정 (4)
        keys = pygame.key.get_pressed()	    # 키 입력 처리
        if keys[pygame.K_LEFT]:
            acc.x = -1
        if keys[pygame.K_RIGHT]:
            acc.x = 1
        if keys[pygame.K_UP]:
            acc.y = -1
        if keys[pygame.K_DOWN]:
            acc.y = 1

        if acc.length() > 0:            # 가속도 벡터 정규화 (5)
            acc = acc.normalize()

        acc *= self.ACCEL               # 가속도 벡터 힘 계산 (6)
        self.vel += acc                 # 속도 벡터에 가속도 반영 (7)
        self.vel *= self.FRICTION       # 속도 벡터에 마찰력 반영 (8)

        if self.vel.length() > self.MAX_SPEED:  # 최대 속도 제한
            self.vel.scale_to_length(self.MAX_SPEED)

        self.pos += self.vel            # 위치 벡터 갱신 (9)
        self.rect.center = self.pos     # 현재 위치 갱신 (10)
        
# Main Program
ball = Ball()
all_sprites = pygame.sprite.Group(ball)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    all_sprites.update()        # 공 위치 갱신
    win.fill(WHITE)             # 배경 그리기
    all_sprites.draw(win)       # 공 그리기
    
    pygame.display.flip()
    clock.tick(60) 
