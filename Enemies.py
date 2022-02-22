# Классы, реализующие разные виды противников
# SimpleEnemy наносят 5 урона базе, могут пережить 2 попадания и движутся со коростью 5
# HardEnemy наносят 10 урона базе, могут пережить 5 попаданий и движутся со скоростью 2
# FastEnemy наносят 1 урон базе, могут пережить только 1 попадание и движутся со скоростью 7

import random
from pygame import *


class SimpleEnemy:
    def __init__(self, width, height, base_height, ):
        temp = image.load('images/simple_enemy.png')
        self.image = transform.scale(temp, (40, 60))
        self.x = width
        self.y = random.randint(base_height, height - base_height)
        self.speed = 5
        self.health = 2
        self.damage = 5

    def shot(self):
        self.health -= 1

    def move(self):
        self.x -= self.speed

    def get_coords(self):
        return self.x, self.y


class HardEnemy:
    def __init__(self, width, height, base_height):
        temp = image.load('images/hard_enemy.jpg')
        self.image = transform.scale(temp, (50, 70))
        self.x = width
        self.y = random.randint(base_height, height - base_height)
        self.speed = 2
        self.health = 5
        self.damage = 10

    def shot(self):
        self.health -= 1

    def move(self):
        self.x -= self.speed

    def get_coords(self):
        return self.x, self.y


class FastEnemy:
    def __init__(self, width, height, base_height):
        temp = image.load('images/fast_enemy.png')
        self.image = transform.scale(temp, (40, 60))
        self.x = width
        self.y = random.randint(base_height, height - base_height)
        self.speed = 7
        self.health = 1
        self.damage = 3

    def shot(self):
        self.health -= 1

    def move(self):
        self.x -= self.speed

    def get_coords(self):
        return self.x, self.y
