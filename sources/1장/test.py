import pygame
import sys

pygame.init()

# 화면 설정
WIDTH, HEIGHT = 800, 400
TABLE_COLOR = (0, 100, 0)
BALL_COLOR = (255, 255, 255)
BALL_RADIUS = 15

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Ball Demo")
clock = pygame.time.Clock()


class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y, vx, vy):
        super().__init__()

        # 이미지(Surface) 생성 및 투명색 설정
        size = BALL_RADIUS * 2
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, BALL_COLOR, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)

        # 위치(rect) 설정
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        # 속도
        self.vx = vx
        self.vy = vy

    def update(self):
        # 위치 업데이트
        self.rect.x += self.vx
        self.rect.y += self.vy

        # 벽 충돌 처리 (창 경계 기준)
        if self.rect.left <= 0 or self.rect.right >= WIDTH:
            self.vx *= -1
        if self.rect.top <= 0 or self.rect.bottom >= HEIGHT:
            self.vy *= -1


# 스프라이트 그룹 생성
all_sprites = pygame.sprite.Group()

# 공 하나 생성해서 그룹에 추가
ball = Ball(WIDTH // 2, HEIGHT // 2, 5, 3)
all_sprites.add(ball)

running = True
while running:
    # 이벤트 처리
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            print(pygame.mouse.get_pos())
            print(pygame.mouse.get_pressed()[1])

    # 스프라이트 업데이트
    all_sprites.update()

    # 그리기
    screen.fill(TABLE_COLOR)
    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
