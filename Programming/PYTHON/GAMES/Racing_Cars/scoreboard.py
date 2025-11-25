import pygame.font

class Scoreboard:
    def __init__(self, screen, settings, stats):
        self.screen = screen
        self.settings = settings
        self.stats = stats
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_lives()
        self.prep_level()

    def prep_score(self):
        rounded_score = int(round(self.stats.score, -1))
        score_str = f"Score: {rounded_score}"
        self.score_image = self.font.render(score_str, True, self.text_color)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.settings.screen_width - 20
        self.score_rect.top = 20

    def prep_lives(self):
        lives_str = f"Lives: {self.stats.lives}"
        self.lives_image = self.font.render(lives_str, True, self.text_color)
        self.lives_rect = self.lives_image.get_rect()
        self.lives_rect.left = 20
        self.lives_rect.top = 20

    def prep_level(self):
        level_str = f"Level: {self.stats.level}"
        self.level_image = self.font.render(level_str, True, self.text_color)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.centerx = self.settings.screen_width // 2
        self.level_rect.top = 20

    def show_score(self):
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.lives_image, self.lives_rect)
        self.screen.blit(self.level_image, self.level_rect)