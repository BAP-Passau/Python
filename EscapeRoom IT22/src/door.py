class Door(object):
    def __init__(self, position, key):

        self.key = None
        self.key = key
        self.position = position

        print(f'The door is at position x:{self.position.x} y:{self.position.y}.')