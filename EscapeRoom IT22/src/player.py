from position import Position
from directions import Direction
from key import Key
from coin import Coin
from random import Random


class Player(object):
    def __init__(self):
        self.position = Position(0, 0)
        self.current_direction = Direction.UP
        self.room = None
        self.items = []

    def put_in_place(self, room):
        r = Random()

        self.position.x = r.randint(1, room.room_width)
        self.position.y = r.randint(1, room.room_length)

        self.room = room

    def turn_right(self):
        if self.current_direction == Direction.UP:
            self.current_direction = Direction.RIGHT
        elif self.current_direction == Direction.RIGHT:
            self.current_direction = Direction.DOWN
        elif self.current_direction == Direction.DOWN:
            self.current_direction = Direction.LEFT
        else:
            self.current_direction = Direction.UP

        print(f'I\'m going {self.current_direction} now.')

    def turn_left(self):
        if self.current_direction == Direction.UP:
            self.current_direction = Direction.LEFT
        elif self.current_direction == Direction.LEFT:
            self.current_direction = Direction.DOWN
        elif self.current_direction == Direction.DOWN:
            self.current_direction = Direction.RIGHT
        else:
            self.current_direction = Direction.UP

        print(f'I\'m going {self.current_direction} now.')

    def add_item(self, item):
        if type(item) == Key:
            print('Added key to my items.')
            self.room.remove_item(item)
        elif type(item) == Coin:
            print('Added coin to my items.')
            self.room.remove_item(item)
        else:
            print('Added something to my items.')
            self.room.remove_item(item)

        self.items.append(item)

    def move(self, steps):
        proceed_game = True

        if self.current_direction == Direction.UP:
            self.position.y -= steps

            if self.room.compare_door_positions(self.position) and self.room.get_door_at_position(
                    self.position).key in self.items:
                print('Player has left the room through the door.')
                proceed_game = False
            elif self.room.compare_door_positions(self.position) and not (
                    self.room.get_door_at_position(self.position).key in self.items):
                print('Player has reached the door, but doesn\'t have the key.')
                self.position.y = 1
            elif self.position.y <= 0:
                print('Ouch, hit upper wall.')
                self.position.y = 1

            self.key_radar()
            self.check_and_get_keys()
            self.coin_radar()
            self.check_and_get_coins()

        elif self.current_direction == Direction.RIGHT:
            self.position.x += steps

            if self.room.compare_door_positions(self.position) and self.room.get_door_at_position(
                    self.position).key in self.items:
                print('Player has left the room through the door.')
                proceed_game = False
            elif self.room.compare_door_positions(self.position) and not (
                    self.room.get_door_at_position(self.position).key in  self.items):
                print('Player has reached the door, but doesn\'t have the key.')
                self.position.x = self.room.room_width - 1
            elif self.position.x >= self.room.room_width:
                print('Ouch, hit right wall.')
                self.position.x = self.room.room_width - 1

            self.key_radar()
            self.check_and_get_keys()
            self.coin_radar()
            self.check_and_get_coins()

        elif self.current_direction == Direction.DOWN:
            self.position.y += steps

            if self.room.compare_door_positions(self.position) and self.room.get_door_at_position(
                    self.position).key in self.items:
                print('Player has left the room through the door.')
                proceed_game = False
            elif self.room.compare_door_positions(self.position) and not (
                    self.room.get_door_at_position(self.position).key in self.items):
                print('Player has reached the door, but doesn\'t have the key.')
                self.position.y = self.room.room_length - 1
            elif self.position.y >= self.room.room_length:
                print('Ouch, hit lower wall.')
                self.position.y = self.room.room_length - 1

            self.key_radar()
            self.check_and_get_keys()
            self.coin_radar()
            self.check_and_get_coins()
        else:
            self.position.x -= steps

            if self.room.compare_door_positions(self.position) and self.room.get_door_at_position(
                    self.position).key in self.items:
                print('Player has left the room through the door.')
                proceed_game = False
            elif self.room.compare_door_positions(self.position) and not (
                    self.room.get_door_at_position(self.position).key in self.items):
                print('Player has reached the door, but doesn\'t have the key.')
                self.position.x = 1
            elif self.position.x <= 0:
                print('Ouch, hit left wall.')
                self.position.x = 1

            self.key_radar()
            self.check_and_get_keys()
            self.coin_radar()
            self.check_and_get_coins()

        if proceed_game:
            print(f'I\'m going {self.current_direction}.')
            print(f'My current position is x:{self.position.x} y:{self.position.y}.')

        return proceed_game

    def check_and_get_keys(self):
        for key in self.room.get_keys():
            if self.position.x == key.position.x and self.position.y == key.position.y:
                self.add_item(key)

    def key_radar(self):
        key_area = []

        for key in self.room.get_keys():
            key_area += key.key_area()

        for pos in key_area:
            if self.position.x == pos.x and self.position.y == pos.y:
                print('Key nearby.')

    def check_and_get_coins(self):
        for coin in self.room.get_coins():
            if self.position.x == coin.position.x and self.position.y == coin.position.y:
                self.add_item(coin)

    def coin_radar(self):
        coin_area = []

        for coin in self.room.get_coins():
            coin_area += coin.coin_area()

        for pos in coin_area:
            if self.position.x == pos.x and self.position.y == pos.y:
                print('Coin nearby.')
