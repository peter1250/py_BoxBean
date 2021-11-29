import pygame
import os
from .enemy import Enemy

imgs = []


for x in range(10):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/bird_box", "bird_box_" + add_str + ".png")).convert_alpha(),
        (64, 40)))


class bird_box(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "bird_box"
        self.money = 25
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]
        self.speed = self.speed_increase = 3.0


