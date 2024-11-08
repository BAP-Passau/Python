import pickle

class GameState(object):
    game_state = None

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(GameState, cls).__new__(cls)
            cls.instance.room = None

        return cls.instance

    def __init__(self):
        pass

    def load_game_state(self, *args, **kwargs):
        restored_game_state = self
        saved_game_state = None

        try:
            saved_game_state = open('gamestate.bin', 'rb')
        except Exception as e:
            pass

        if saved_game_state:
            game_state_json = None

            try:
                restored_game_state = pickle.loads(saved_game_state.read())
                return True
            except Exception as e:
                print('Invalid game state!')
                quit()

    def save_game_state(self):
        with open('gamestate.bin', 'wb') as saved_game_state:
            game_state = self

            saved_game_state.write(pickle.dumps(game_state))
