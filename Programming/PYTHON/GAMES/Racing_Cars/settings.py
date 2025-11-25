import pygame
import os

class Settings:
    def __init__(self):
        # Set the working directory to the script's directory
        os.chdir(os.path.dirname(os.path.abspath(__file__)))

        # Screen settings
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)

        # Load background image
        bg_path = os.path.join('assets', 'images', 'background.jpg')
        if not os.path.exists(bg_path):
            raise FileNotFoundError(f"Background image not found at: {bg_path}")
        self.bg_image = pygame.image.load(bg_path)
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_height))

        # Player car settings
        self.player_speed = 5
        self.player_lives = 3

        # AI car settings
        self.ai_speed = 3
        self.ai_spawn_delay = 1000  # Milliseconds between AI spawns
        self.last_ai_spawn = 0

        # Power-up settings
        self.power_up_speed = 3
        self.power_up_spawn_delay = 5000
        self.last_power_up_spawn = 0

        # Obstacle settings
        self.obstacle_speed = 3
        self.obstacle_spawn_delay = 3000
        self.last_obstacle_spawn = 0

        # Scoring
        self.power_up_points = 10  # Power-ups give 10 points each
        self.crash_penalty = 50
        self.combo_multiplier = 1

        # Game speedup
        self.speedup_scale = 1.1

        # Sound settings
        self.crash_sound_path = 'assets/sounds/crash.wav'
        self.game_over_sound_path = 'assets/sounds/game_over.wav'

    def increase_speed(self):
        """Increase game speed."""
        self.player_speed *= self.speedup_scale
        self.ai_speed *= self.speedup_scale
        self.power_up_speed *= self.speedup_scale
        self.obstacle_speed *= self.speedup_scale
        self.ai_spawn_delay = max(500, self.ai_spawn_delay - 100)  # Reduce AI spawn delay
        self.power_up_spawn_delay = max(3000, self.power_up_spawn_delay - 500)  # Reduce power-up spawn delay
        self.obstacle_spawn_delay = max(2000, self.obstacle_spawn_delay - 300)  # Reduce obstacle spawn delay