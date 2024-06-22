class GameLogic:
    def __init__(self):
        self.game_state = {}

    def update_game_state(self, new_state):
        self.game_state = new_state

    def get_game_state(self):
        return self.game_state