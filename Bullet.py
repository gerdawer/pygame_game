# Класс, реализующий работу выстрелов
# Каждый выстрел хранит информацию о свох координатах и угле наклона

from math import *


class Bullet:
    def __init__(self, angle, x, y, speed=10):
        self.angle = angle
        self.speed = speed
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def change_coords(self):
        self.x += cos(self.angle) * self.speed
        self.y += sin(self.angle) * self.speed
