from random import Random

from item import Item
from position import Position

class Key(Item):
    def __init__(self, position):
        r = Random()

        self.position = position
        self.price = r.randint(1, 4)
        self.coins = []

        print(f'The key is at position x:{self.position.x} y:{self.position.y}.')

    def key_area(self):
        key_area = []

        key_x_pos = self.position.x
        key_y_pos = self.position.y

        for x in range(key_x_pos - 3, key_x_pos + 4):
            for y in range(key_y_pos - 3, key_y_pos + 4):
                key_area.append(Position(x, y))

        return key_area