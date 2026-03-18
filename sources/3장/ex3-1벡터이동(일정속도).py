import pygame, sys

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
        self.pos = pygame.math.Vector2(W//2, H//2)  # 위치 벡터 생성 (1)
        self.speed = 5                          # 이동 속력 (고정값)

    def update(self):
        direction = pygame.math.Vector2(0, 0)	# 방향 벡터 생성 (2)

        # 방향 벡터 설정 (3)
        keys = pygame.key.get_pressed()		# 키 입력 확인
        if keys[pygame.K_LEFT]:
            direction.x = -1		        # 왼쪽으로 이동
        if keys[pygame.K_RIGHT]:
            direction.x = 1		        # 오른쪽으로 이동
        if keys[pygame.K_UP]:
            direction.y = -1		        # 위로 이동
        if keys[pygame.K_DOWN]:
            direction.y = 1	                # 아래로 이동

        if direction.length() > 0:	        # 방향 벡터 정규화 (4)
            direction = direction.normalize()

        self.pos += direction * self.speed      # 위치 벡터 갱신 (5)
        self.rect.center = self.pos	        # 현재 위치 갱신 (6)

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

