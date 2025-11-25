import pygame

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)  # Fallback background color

        # Load background image
        self.bg_image = pygame.image.load('C:\\Users\\ERBECHJO\\OneDrive\\Desktop\\Programming\\PYTHON\\GAMES\\Alien_Invasion\\images\\background.jpg')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)  # White bullets
        self.bullets_allowed = 10  # Limit the number of bullets
        self.bullet_speed_factor = 3  # Adjust bullet speed

        # Alien settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed_factor = 1.0  # Reduced ship speed
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 0.3

        # Scoring
        self.alien_points = 50

        # fleet_direction of 1 represents right, -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)