import pygame, sys, random

pygame.init()

W, H = 800, 600
BLACK = (0,0,0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0,255,0)
BLUE = (0, 0, 255)

win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

# 텍스트 폰트
score_font = pygame.font.Font(None, 30)
game_over_font = pygame.font.Font(None, 60)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50, 40), pygame.SRCALPHA)
        pygame.draw.polygon(self.image, GREEN, [(25, 0), (50, 40), (0, 40)])
        self.rect = self.image.get_rect(center=(W//2, H-50))
        self.speed = 8

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < W:
            self.rect.x += self.speed

    def shoot(self, all_sprites, bullets):
        # -30도, -15도, 0도, +15도, +30도 5 방향으로 발사
        angles = [-30, -15, 0, 15, 30] 
        
        for angle in angles:
            bullet = Bullet(self.rect.centerx, self.rect.top, angle)
            all_sprites.add(bullet)
            bullets.add(bullet)
                
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((30, 30))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect()
        self.rect.center=(random.randint(20, W-20), random.randint(-100, -20))
        self.speed_y = random.randint(3, 8)

    def update(self):
        self.rect.y += self.speed_y
        if self.rect.top > H:
            self.rect.y = random.randint(-100, -20)
            self.rect.x = random.randint(20, W-20)
            self.speed_y = random.randint(3, 8)

class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y, angle):
        super().__init__()
        self.image = pygame.Surface((5, 10))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect(center=(x, y))
        #self.speed = -15

        self.vel = pygame.math.Vector2(0, -15)
        self.vel = self.vel.rotate(angle)

    def update(self):
        self.rect.x += self.vel.x
        self.rect.y += self.vel.y
        if self.rect.bottom < 0:
            self.kill() 

# Main Program
all_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

player = Player()
all_sprites.add(player)

for _ in range(8):
    e = Enemy()
    all_sprites.add(e)
    enemies.add(e)

score = 0
game_over = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN and not game_over:
            if event.key == pygame.K_SPACE:
                player.shoot(all_sprites, bullets) # 발사

    if not game_over:
        all_sprites.update()
        hit_dict = pygame.sprite.groupcollide(enemies, bullets, True, True)
        for _ in hit_dict:      # 파괴된 적의 수만큼 새로운 적 생성
            score += 10         # 점수 증가
            e = Enemy()
            all_sprites.add(e)
            enemies.add(e)

        # 충돌 체크: 플레이어 vs 적
        if pygame.sprite.spritecollide(player, enemies, False):
            game_over = True

    win.fill(WHITE)
    all_sprites.draw(win)

    # 점수 표시
    score_surf = score_font.render(f"SCORE: {score}", True, BLACK)
    win.blit(score_surf, (10, 10))

    # 게임 오버 텍스트 표시
    if game_over:
        over_surf = game_over_font.render("GAME OVER", True, RED)
        # 화면 중앙 정렬을 위한 Rect 활용
        over_rect = over_surf.get_rect(center=(W//2, H//2))
        win.blit(over_surf, over_rect)

    pygame.display.flip()
    clock.tick(60)

