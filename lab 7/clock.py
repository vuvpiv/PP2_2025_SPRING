import pygame
from datetime import datetime

# поворот изображения
def blitRotate(surf, image, pos, angle):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=pos)
    surf.blit(rotated_image, new_rect.topleft)

pygame.init()
screen = pygame.display.set_mode((500, 500))

# Загрузка изображений
bg = pygame.transform.scale(pygame.image.load("images/dial.png"), (500, 500))

left_arm = pygame.image.load("images/left-hand.png")   # секундная стрелка  
right_arm = pygame.image.load("images/right-hand.png")  # минутная

# Уменьшение размеров стрелок 
left_arm = pygame.transform.scale(left_arm, (left_arm.get_width() // 2, left_arm.get_height() // 2))
right_arm = pygame.transform.scale(right_arm, (right_arm.get_width() // 2, right_arm.get_height() // 2))

running = True
while running:
    screen.fill((255, 255, 255))
    screen.blit(bg, (0, 0))
    
    # Получаем текущее время
    now = datetime.now()
    minutes = now.minute
    seconds = now.second

    # Вычисляем углы поворота
    angle_min = -6 * minutes - 53  # -53 можно скорректировать, если нужно
    angle_sec = -6 * seconds

    # Определяем центр экрана
    pos = (screen.get_width() / 2, screen.get_height() / 2)

    # Рисуем стрелки
    blitRotate(screen, left_arm, pos, angle_sec)
    blitRotate(screen, right_arm, pos, angle_min)

    # Обновляем экран
    pygame.display.flip()

    # Обрабатываем события
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.time.delay(1000)  # Обновление каждую секунду

pygame.quit()