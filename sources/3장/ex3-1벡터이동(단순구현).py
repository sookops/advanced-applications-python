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
        self.rect.center = [W//2, H//2]     # 초기 위치
        self.speed = 5                      # 이동 속력 (고정값)

    def update(self):
        keys = pygame.key.get_pressed()     # 키 입력 확인
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed

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

