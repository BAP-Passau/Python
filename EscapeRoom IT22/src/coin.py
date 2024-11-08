from item import Item
from position import Position

class Coin(Item):
    def __init__(self, position):
        self.position = position

        print(f'The coin is at position x:{self.position.x} y:{self.position.y}.')

    def coin_area(self):
        coin_area = []

        coin_x_pos = self.position.x
        coin_y_pos = self.position.y

        for x in range(coin_x_pos - 2, coin_x_pos + 3):
            for y in range(coin_y_pos - 2, coin_y_pos + 3):
                coin_area.append(Position(x, y))

        return coin_area
