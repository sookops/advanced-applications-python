import pygame, sys

pygame.init()
W, H = 800, 600
WHITE, GRAY, RED, BLUE = (255, 255, 255), (100, 100, 100), (255, 0, 0), (0, 0, 255)

background = pygame.Surface((W, H))     # 배경 이미지
background.fill(WHITE)
pygame.draw.rect(background, GRAY, (0, H-40, W, 40))

win = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()

class Cannon(pygame.sprite.Sprite):     # 대포 스프라이트
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill(BLUE)
        self.rect = self.image.get_rect(bottomleft=(50, H-40))  # 왼쪽 하단 배치
        
class Shell(pygame.sprite.Sprite):      # 포탄 스프라이트
    def __init__(self, start_pos, mouse_pos):
        super().__init__()
        self.image = pygame.Surface((12, 12), pygame.SRCALPHA)
        pygame.draw.ellipse(self.image, RED, (0,0,12,12))
        self.rect = self.image.get_rect(center=start_pos)
        
        self.pos = pygame.math.Vector2(start_pos)   # 위치 벡터: 대포 위치
        target_pos = pygame.math.Vector2(mouse_pos) # 목표 벡터: 마우스 위치
        direction = target_pos - self.pos           # 방향 벡터
        distance = direction.length()               # 벡터의 길이(힘) 
        
        if distance > 0:    # 방향 벡터의 정규화
            direction = direction.normalize()
            
        power = min(distance * 0.05, 30)    # 포탄 발사 힘 계산, 최대 30

        self.vel = direction * power        # 초기 발사 속도
        self.gravity = 0.5                  # 중력 가속도

    def update(self):
        self.vel.y += self.gravity          # 중력 적용
        self.pos += self.vel                # 위치 벡터 갱신
        self.rect.center = self.pos         # 현재 위치 갱신
        
        # 화면 밖으로 나간 포탄 소멸 처리
        if self.rect.y > H or self.rect.x > W or self.rect.x < 0:
            self.kill()

# Main Program
cannon = Cannon()                   # 대포 생성
all_sprites = pygame.sprite.Group()
all_sprites.add(cannon)
mouse_pos = cannon.rect.center      # 마우스 위치

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()   
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:   # 1번 버튼 클릭시 포탄 발사
                new_shell = Shell(cannon.rect.center, event.pos)
                all_sprites.add(new_shell)
        elif event.type == pygame.MOUSEMOTION:
            mouse_pos = event.pos   # 마우스 위치
  
    all_sprites.update()            # 포탄 위치 갱신
    win.blit(background, (0,0))     # 배경 그리기
    pygame.draw.line(win, GRAY, cannon.rect.center, mouse_pos, 2)   # 가이드 선그리기
    all_sprites.draw(win)           # 스프라이트 그리기
    
    pygame.display.flip()
    clock.tick(60)


