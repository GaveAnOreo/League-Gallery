import pygame
from pygame.sprite import Sprite

class PlayerCar(Sprite):
    def __init__(self, screen, settings):
        super().__init__()
        self.screen = screen
        self.settings = settings
        self.image = pygame.image.load('assets/images/player_car.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom - 20

        # Movement flags
        self.moving_left = False
        self.moving_right = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        """Update position based on movement flags."""
        if self.moving_left and self.rect.left > 100:
            self.rect.x -= self.settings.player_speed
        if self.moving_right and self.rect.right < self.settings.screen_width - 100:
            self.rect.x += self.settings.player_speed
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.player_speed
        if self.moving_down and self.rect.bottom < self.settings.screen_height:
            self.rect.y += self.settings.player_speed

    def blitme(self):
        """Draw the car at its current position."""
        self.screen.blit(self.image, self.rect)

    def center_car(self):
        """Reset car to starting position."""
        self.rect.centerx = self.screen.get_rect().centerx
        self.rect.bottom = self.screen.get_rect().bottom - 20