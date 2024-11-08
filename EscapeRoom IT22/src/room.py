from random import Random
from key import Key
from coin import Coin
from door import Door
from position import Position


class Room(object):
    def __init__(self):
        r = Random()

        self.room_width = r.randint(10, 100)
        self.room_length = r.randint(10, 100)

        self.player = None

        self.items = []
        self.doors = []

        self.valid_door_positions = []
        self.valid_room_positions = []

        for x in range(1, self.room_width - 1):
            for y in range(1, self.room_length - 1):
                self.valid_room_positions.append(Position(x, y))

        for x in range(self.room_width):
            self.valid_door_positions.append(Position(x, 0))
            self.valid_door_positions.append(Position(x, self.room_length))

        for y in range(self.room_length):
            self.valid_door_positions.append(Position(0, y))
            self.valid_door_positions.append(Position(self.room_width, y))

        keys = []
        coins = []

        for i in range(3):
            key_position = self.valid_room_positions[r.randint(0, len(self.valid_room_positions))]
            keys.append(Key(key_position))
            self.valid_room_positions.remove(key_position)

        for i in range(5):
            coin_position = self.valid_room_positions[r.randint(0, len(self.valid_room_positions))]
            coins.append(Coin(coin_position))
            self.valid_room_positions.remove(coin_position)

        for key in keys:
            door_position = self.valid_door_positions[r.randint(0, len(self.valid_door_positions))]
            door = Door(door_position, key)

            if door not in self.doors:
                self.doors.append(door)
                self.items.append(key)
                self.valid_door_positions.remove(door_position)

        for coin in coins:
            self.items.append(coin)

    def place_player(self, player):
        this = self

        player.put_in_place(this)

        self.player = player

    def remove_item(self, item):
        self.items.remove(item)

    def print(self):
        for y in range(self.room_length + 1):
            for x in range(self.room_width + 1):
                paint_pos = Position(x, y)

                if y == 0:
                    if self.doors and self.compare_door_positions(paint_pos):
                        print('D', end='')
                    else:
                        print('-', end='')

                    if x == self.room_width:
                        print()
                elif y == self.room_length:
                    if self.doors and self.compare_door_positions(paint_pos):
                        print('D', end='')
                    else:
                        print('-', end='')

                    if x == self.room_width:
                        print()
                elif x == 0:
                    if self.doors and self.compare_door_positions(paint_pos):
                        print('D', end='')
                    else:
                        print('|', end='')
                elif x == self.room_width:
                    if self.doors and self.compare_door_positions(paint_pos):
                        print('D')
                    else:
                        print('|')
                elif self.get_keys() and self.compare_key_positions(paint_pos):
                    for key in self.get_keys():
                        if paint_pos.x == key.position.x and paint_pos.y == key.position.y:
                            print('K', end='')
                elif self.get_coins() and self.compare_coin_positions(paint_pos):
                    for coin in self.get_coins():
                        if paint_pos.x == coin.position.x and paint_pos.y == coin.position.y:
                            print('€', end='')
                elif self.player.position.x == paint_pos.x and self.player.position.y == paint_pos.y:
                    print('P', end='')
                else:
                    key_nearby = False
                    coin_nearby = False

                    if self.get_keys():
                        for key in self.get_keys():
                            key_area = key.key_area()

                            if key not in self.player.items:
                                for pos in key_area:
                                    if x == pos.x and y == pos.y:
                                        key_nearby = True
                                        break

                    if self.get_coins():
                        for coin in self.get_coins():
                            coin_area = coin.coin_area()

                            if coin not in self.player.items:
                                for pos in coin_area:
                                    if x == pos.x and y == pos.y:
                                        coin_nearby = True
                                        break

                    if key_nearby or coin_nearby:
                        print('.', end='')
                    else:
                        print(' ', end='')

    def get_keys(self):
        return [i for i in self.items if type(i) == Key]

    def get_coins(self):
        return [i for i in self.items if type(i) == Coin]

    def get_door_positions(self):
        return list(map(lambda d: d.position, self.doors))

    def compare_door_positions(self, position):
        result = False

        for pos in self.get_door_positions():
            if pos.x == position.x and pos.y == position.y:
                result = True
                break

        return result

    def get_key_positions(self):
        return list(map(lambda k: k.position, self.get_keys()))

    def compare_key_positions(self, position):
        result = False

        for pos in self.get_key_positions():
            if pos.x == position.x and pos.y == position.y:
                result = True
                break

        return result

    def get_coin_positions(self):
        return list(map(lambda k: k.position, self.get_coins()))

    def compare_coin_positions(self, position):
        result = False

        for pos in self.get_coin_positions():
            if pos.x == position.x and pos.y == position.y:
                result = True
                break

        return result

    def get_door_at_position(self, position):
        door = None

        for d in self.doors:
            if d.position.x == position.x and d.position.y == position.y:
                door = d

        return door
