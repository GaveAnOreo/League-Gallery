class GameStats:
    def __init__(self, settings):
        self.settings = settings
        self.reset_stats()
        self.game_active = False
        self.high_score = 0

    def reset_stats(self):
        self.score = 0  # Reset score to 0
        self.level = 1  # Reset level to 1
        self.lives = self.settings.player_lives

    def increase_level(self):
        self.level += 1
        self.settings.increase_speed()  # Increase game speed