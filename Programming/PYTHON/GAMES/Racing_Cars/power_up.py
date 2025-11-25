import pygame
from pygame.sprite import Sprite
import random

class PowerUp(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('assets/images/power_up.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(100, self.settings.screen_width - 100)
        self.rect.y = 0

    def update(self):
        """Move downward at power-up speed."""
        self.rect.y += self.settings.power_up_speed
        if self.rect.top > self.settings.screen_height:
            self.kill()

    def blitme(self):
        self.screen.blit(self.image, self.rect)