from room import Room
from player import Player
from game_state import GameState

def play():
    gamestate = GameState()
    room = None
    player = None

    if gamestate.load_game_state():
        room = gamestate.room
        player = gamestate.room.player
    else:
        room = Room()
        player = Player()
        room.place_player(player)

    print(f'The room has a length of {room.room_length} and a width of {room.room_width}.')

    gamestate.room = room

    command = ''
    steps = 0

    play = True

    while (True):
        print(f'Type "r" to turn player right, "l" to turn player left, just hit ENTER to keep current direction, "q" to quit the game: ')

        command = input().lower()

        if command == 'r':
            player.turn_right()
        elif command == 'l':
            player.turn_left()
        elif command == 'q':
            play = False
            gamestate.save_game_state()
        elif command == 'p':
            room.print()
        elif command == '':
            pass
        else:
            print(f'The player does only understand "r", "l", empty command and "q".')

        if not play:
            break

        steps = input('How many steps should the player go? ')

        try:
            steps = int(steps)
        except Exception as e:
            print(f'Invalid input')
            steps = 0

        if player.move(steps):
            gamestate.save_game_state()
            quit()

if __name__ == '__main__':
    play()