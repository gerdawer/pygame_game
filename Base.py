# Класс, реализующий работу базы
# База хранит информацию о своих координатах и текущем здоровье

class Base:
    def __init__(self, x, y, health=100):
        self.health = health
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y

    def damage(self, enemy_damage):
        self.health -= enemy_damage
