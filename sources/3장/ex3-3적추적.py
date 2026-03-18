import pygame, sys

pygame.init()
W, H = 800, 600
WHITE, RED, BLUE = (255, 255, 255), (255, 0, 0), (0, 0, 255)

screen = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, (0,0,40,40))
        self.rect = self.image.get_rect()
        self.rect.center = [100, 100]
        self.speed = 3

    def update(self):
        keys = pygame.key.get_pressed()		# 키 입력 확인
        if keys[pygame.K_LEFT]:
            self.rect.x += -self.speed		# 왼쪽으로 이동
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed		# 오른쪽으로 이동
        if keys[pygame.K_UP]:
            self.rect.y += -self.speed		# 위로 이동
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed		# 아래로 이동

        # 화면 밖으로 나가지 못함
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > W:
            self.rect.right = W
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > H:
            self.rect.bottom = H


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player):
        super().__init__()
        self.player = player        # 추적 대상 저장
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center = [700, 500]
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 3              # 적의 이동 속도

    def update(self):
        # 방향 벡터 계산 (플레이어 위치 - 나의 위치)
        player_pos = pygame.math.Vector2(self.player.rect.center)
        direction = player_pos - self.pos
        
        # 방향 벡터 정규화
        if direction.length() > 0:
            direction = direction.normalize()
            
        # 위치 갱신
        self.pos += direction * self.speed
        self.rect.center = self.pos

# Main Program
player = Player()       # 플레이어
enemy = Enemy(player)   # 적
all_sprites = pygame.sprite.Group(player, enemy)
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if not game_over:
        all_sprites.update()
        if enemy in pygame.sprite.spritecollide(player, all_sprites, False):
            game_over = True   # 게임 종료
            
        screen.fill(WHITE)
        all_sprites.draw(screen)
        
    pygame.display.flip()
    clock.tick(60)

