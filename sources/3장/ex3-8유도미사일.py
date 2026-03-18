import pygame, sys, math

W, H = 800, 600
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

pygame.init()
win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.original_image = pygame.Surface((30, 10), pygame.SRCALPHA)
        pygame.draw.polygon(self.original_image, RED, [(0, 0), (30, 5), (0, 10)])
        
        self.image = self.original_image
        self.rect = self.image.get_rect(center=(x, y))
        
        self.pos = pygame.math.Vector2(x, y)    # 위치 벡터
        self.vel = pygame.math.Vector2(0, 0)    # 속도 벡터
        self.speed = 7

    def update(self):
        mouse_pos = pygame.math.Vector2(pygame.mouse.get_pos())     # 마우스 위치(타겟) 추적
        direction = mouse_pos - self.pos    # 방향 벡터 : 목적지 - 내위치

        if direction.length() < 10:         # 미사일 명중 처리 (벡터 거리 이용)
            self.kill()
            return

        self.vel = direction.normalize() * self.speed   # 속도 벡터 갱신 - 방향 * 속력
        
        # 위치 업데이트
        self.pos += self.vel
        self.rect.center = self.pos

        # 미사일 머리 회전
        # atan2(y, x): 좌표를 각도(라디안)로 변환
        # math.degrees()로 라디안을 '도(Degree)'로 변환
        # y축 속도에 -를 붙이는 이유: Pygame의 y축은 아래가 양수(+)라서 일반 수학과 반대
        angle = math.degrees(math.atan2(-self.vel.y, self.vel.x))
        
        # 이미지 회전 (rotate는 원본 이미지를 기준으로 해야 깨지지 않음)
        self.image = pygame.transform.rotate(self.original_image, angle)
        # 회전하면 이미지 크기가 변하므로 rect 중심점 다시 잡기 (중요)
        self.rect = self.image.get_rect(center=self.rect.center)

# Main Program
all_sprites = pygame.sprite.Group()

# 플레이어 (단순한 발사대 역할)
player_rect = pygame.Rect(0, 0, 40, 40)     # rect 객체 생성
player_rect.center = (W//2, H//2)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:  # 미사일 발사
            missile = Missile(player_rect.centerx, player_rect.centery)
            all_sprites.add(missile)

    all_sprites.update()    # 스프라이트 위치 갱신
    win.fill(WHITE)         # 배경 그리기
    pygame.draw.rect(win, BLUE, player_rect)    # 발사대 그리기
    all_sprites.draw(win)   # 스프라이트 그리기
        
    pygame.display.flip()
    clock.tick(60)

