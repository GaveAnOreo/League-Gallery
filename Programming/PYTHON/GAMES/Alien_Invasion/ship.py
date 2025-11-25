import os
import sys
import pygame
from pygame.sprite import Sprite

class Ship(Sprite):
    def __init__(self, ai_settings, screen):
        """Initialize the ship and set its starting position."""
        super(Ship, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Print the current working directory
        print(f"Current working directory: {os.getcwd()}")

        # Load the ship image and get its rect.
        current_path = os.path.dirname(__file__)  # Get the current file path
        image_path = os.path.join(current_path, "images", "ship.png")
        print(f"Loading ship image from: {image_path}")  # Debugging info

        # Verify if the file exists
        if not os.path.exists(image_path):
            print(f"File not found: {image_path}")
            sys.exit(1)

        try:
            self.image = pygame.image.load(image_path)
            print("Ship image loaded successfully")  # Debugging info
        except pygame.error as e:
            print(f"Unable to load ship image from {image_path}: {e}")
            sys.exit(1)

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Store decimal values for the ship's center.
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)

        # Movement flags.
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def center_ship(self):
        """Center the ship on the screen."""
        self.centerx = self.screen_rect.centerx
        self.centery = self.screen_rect.bottom - (self.rect.height / 2)

    def update(self):
        """Update the ship's position, based on movement flags."""
        # Update the ship's center value, not the rect.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_up and self.rect.top > 0:
            self.centery -= self.ai_settings.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centery += self.ai_settings.ship_speed_factor

        # Update rect object from self.centerx and self.centery.
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)