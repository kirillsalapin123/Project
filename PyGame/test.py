import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1280, 720
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)

# Загрузка изображения
image = pygame.image.load("images/nature-wallpapers-1280x720-0007-359101127.jpg").convert_alpha()

# Основной игровой цикл
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((0, 0, 0))  # Очистка экрана
    screen.blit(image, (0, 0))  # Отрисовка изображения

    pygame.display.flip()  # Обновление экрана

pygame.quit()
