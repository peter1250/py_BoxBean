import pygame
import os
from .enemy import Enemy

imgs = []
for x in range(15):
    add_str = str(x)
    if x < 10:
        add_str = "0" + add_str
    imgs.append(pygame.transform.scale(
        pygame.image.load(os.path.join("game_assets/enemies/normal_box", "normal_box_" + add_str + ".png")).convert_alpha(),
        (64, 64)))


class normal_box(Enemy):
    def __init__(self):
        super().__init__()
        self.name = "normal_box"
        self.money = 15
        self.max_health = 1
        self.health = self.max_health
        self.imgs = imgs[:]



