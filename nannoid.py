import pygame
import random
 
# O'yin o'lchamlari
WIDTH = 800
HEIGHT = 600
BLOCK_SIZE = 20
PADDLE_WIDTH = 80
PADDLE_HEIGHT = 10
BALL_RADIUS = 10
PADDLE_COLOR = (255, 255, 255)
BALL_COLOR = (255, 255, 255)
BLOCK_COLORS = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
 
# O'yin sozlamalari
ball_pos = [WIDTH // 2, HEIGHT // 2]
ball_speed = [random.choice([-5, 5]), random.choice([-5, 5])]
paddle_pos = [(WIDTH - PADDLE_WIDTH) // 2, HEIGHT - PADDLE_HEIGHT - 10]
blocks = []
for i in range(6):
    for j in range(10):
        blocks.append(pygame.Rect(j * 80 + 10, i * 30 + 10, 60, 20))
 
# Pygame yaratish
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
 
# O'yinni boshlash
while True:
    # Quti bosildi
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                quit()
 
    # Bloklarni tekshirish
    for block in blocks:
        if block.collidepoint(ball_pos):
            blocks.remove(block)
            ball_speed[1] *= -1
            break
 
    # To'pni harakatga o'tkazish
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]
 
    # To'pni qutiga tekshirish
    if ball_pos[1] < BALL_RADIUS:
        ball_speed[1] *= -1
    elif ball_pos[0] < BALL_RADIUS or ball_pos[0] > WIDTH - BALL_RADIUS:
        ball_speed[0] *= -1
    elif ball_pos[1] > HEIGHT - BALL_RADIUS - PADDLE_HEIGHT and \
            ball_pos[0] > paddle_pos[0] and ball_pos[0] < paddle_pos[0] + PADDLE_WIDTH:
        ball_speed[1] *= -1
 
    # Paddleni harakatga o'tkazish
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle_pos[0] > 0:
        paddle_pos[0] -= 5
    elif keys[pygame.K_RIGHT] and paddle_pos[0] < WIDTH - PADDLE_WIDTH:
        paddle_pos[0] += 5
 
    # Ekranga chizish
    screen.fill((0, 0, 0))
    for block, color in zip(blocks, BLOCK_COLORS):
        pygame.draw.rect(screen, color, block)
    pygame.draw.circle(screen, BALL_COLOR, ball_pos, BALL_RADIUS)
    pygame.draw.rect(screen, PADDLE_COLOR, (paddle_pos[0], paddle_pos[1], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.display.update()
 
    # Keyingi kadrlarni kutilayapmiz
    clock.tick(60)
