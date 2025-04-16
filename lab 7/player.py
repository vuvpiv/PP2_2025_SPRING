import pygame
import os

pygame.init()

playlist = []
music_folder = "music"
allmusic = os.listdir(music_folder) # вытаскиваем названия песни


# Загружаем треки в плейлист
for song in allmusic:
    if song.endswith(".mp3"):
        playlist.append(os.path.join(music_folder, song)) # добавляем путь в лст плейлист

screen = pygame.display.set_mode((600, 300))  # Увеличиваем ширину окна
pygame.display.set_caption("Music Player")
clock = pygame.time.Clock() #для фпса

# Шрифт для отображения названия песни
font2 = pygame.font.SysFont(None, 30)  # Уменьшаем размер шрифта

# Фон плейера (белый)
bg = pygame.Surface((600, 300))
bg.fill((255, 255, 255))

# Функция загрузки изображений кнопок
def load_image(file_name, size):
    path = os.path.join("music_elements", file_name)
    if os.path.exists(path):
        img = pygame.image.load(path)
        return pygame.transform.smoothscale(img, size)  # Используем smoothscale для лучшего качества
    else:
        print(f"Файл кнопки не найден: {path}")
        temp_surface = pygame.Surface(size)
        temp_surface.fill((200, 200, 200))  # Серый фон, если кнопки нет
        return temp_surface

# Кнопки
playb = load_image("play.png", (70, 70))
pausb = load_image("pause.png", (70, 70))
nextb = load_image("next.png", (70, 70))
prevb = load_image("back.png", (75, 75))

index = 0
aplay = False

if playlist:
    pygame.mixer.music.load(playlist[index]) 
    pygame.mixer.music.play(1)
    aplay = True 
else:
    print("No music files found in the folder!")

run = True

while run:
    screen.blit(bg, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and playlist:
                if aplay:
                    aplay = False
                    pygame.mixer.music.pause()
                else:
                    aplay = True
                    pygame.mixer.music.unpause()
            if event.key == pygame.K_RIGHT and playlist:
                index = (index + 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
            if event.key == pygame.K_LEFT and playlist:
                index = (index - 1) % len(playlist)
                pygame.mixer.music.load(playlist[index])
                pygame.mixer.music.play()
    
    # Отображение названия текущей песни
    text2 = font2.render(os.path.basename(playlist[index]) if playlist else "No music", True, (0, 0, 0))
    text_rect = text2.get_rect(center=(300, 80))  # Центрируем текст
    
    screen.blit(text2, text_rect.topleft) #подставляем в экран
    
    if aplay: # для смены картинок паузы и плэй
        screen.blit(pausb, (265, 180)) # вставляем картинку паузы на такие координаты
    else:
        screen.blit(playb, (265, 180))  # вставляем картинку плэй на такие координаты
    
    
    screen.blit(nextb, (360, 180)) # вставляем картинку вперед
    screen.blit(prevb, (170, 180)) # вставляем картинку назад

    clock.tick(24) #fps frame per second
    pygame.display.update()