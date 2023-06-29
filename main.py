# from pygame import *
import pygame

pygame.init()

BACKGROUND = (54, 57, 64)  # цвет фона
WIDTH = 1000  # ширина игрового окна
HEIGHT = 500  # высота игрового окна
FPS = 60

loop = True
screen = pygame.display.set_mode(
    (WIDTH, HEIGHT)
)  # установка размера окна, (WIDTH, HEIGHT) - тапл
clock = pygame.time.Clock()  # для дальнейшей нормализации FPS


class GameSprite(pygame.sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, wight, height):
        super().__init__()
        self.image = transform.scale(
            image.load(player_image), (wight, height)
        )  # вместе 55,55 - параметры
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))


# игровой цикл
while loop:
    clock.tick(FPS)

    # работа с событиями
    for event in pygame.event.get():
        # проверить закрытие окна
        if event.type == pygame.QUIT:
            loop = False

    screen.fill(BACKGROUND)
    pygame.display.update()
