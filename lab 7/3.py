import pygame
pygame.init()

WIDTH, HEIGHT = 500, 500  # Размер окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving Ball")

WHITE = (255, 255, 255)
RED = (255, 0, 0)

ball_radius = 25
ball_x, ball_y = WIDTH // 2, HEIGHT // 2  # Начальная позиция (центр экрана)
move_step = 20 

running = True
while running:
    pygame.time.delay(50)  # Небольшая задержка для плавности движения

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Управление стрелками
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and ball_x - ball_radius > 0:
        ball_x -= move_step
    if keys[pygame.K_RIGHT] and ball_x + ball_radius < WIDTH:
        ball_x += move_step
    if keys[pygame.K_UP] and ball_y - ball_radius > 0:
        ball_y -= move_step
    if keys[pygame.K_DOWN] and ball_y + ball_radius < HEIGHT:
        ball_y += move_step

    screen.fill(WHITE)

    pygame.draw.circle(screen, RED, (ball_x, ball_y), ball_radius)

    # Обновляем экран
    pygame.display.update()

pygame.quit()